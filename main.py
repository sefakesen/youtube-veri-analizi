from googleapiclient.discovery import build
import pandas as pd

# 1. API Bağlantısını Kurma
API_KEY = "API_ANAHTARI_BURAYA_GELECEK"
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 2. Analiz Edilecek Kanallar
# Not: YouTube Handle (@isim) yerine Kanal ID'si (UC... ile başlayan) kullanmalısın.
channel_ids = [
    "UCX6OQ3DkcsbYNE6H8uQQuVA",
    "UCWpk9PSGHoJW1hZT4egxTNQ",
    "UC-lHJZR3Gqxm24_Vd_AJ5Yw"  # Örn: YorukyofuVODS
]


def get_channel_info(youtube, channel_ids):
    """Kanalların Upload playlist ID'lerini alır."""
    all_data = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    for item in response['items']:
        data = {
            'channelName': item['snippet']['title'],
            'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
        }
        all_data.append(data)
    return pd.DataFrame(all_data)


def get_video_ids(youtube, playlist_id):
    """Verilen playlist'teki tüm video ID'lerini toplar."""
    video_ids = []
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])

    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        next_page_token = response.get('nextPageToken')

    return video_ids


def get_video_details(youtube, video_ids):
    """Video ID'lerini kullanarak istatistik ve detayları çeker."""
    all_video_info = []

    # API tek seferde max 50 video detayına izin verir, ID'leri 50'li gruplara bölüyoruz
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i + 50])
        )
        response = request.execute()

        for video in response['items']:
            stats = video['statistics']
            snippet = video['snippet']

            video_info = {
                'video_id': video['id'],
                'channel_title': snippet['channelTitle'],
                'title': snippet['title'],
                'published_at': snippet['publishedAt'],
                'duration': video['contentDetails']['duration'],
                'views': stats.get('viewCount', 0),
                'likes': stats.get('likeCount', 0),
                'comments': stats.get('commentCount', 0),
                'tags': snippet.get('tags', [])  # Etiketler her videoda olmayabilir
            }
            all_video_info.append(video_info)

    return pd.DataFrame(all_video_info)


# 3. Ana Çalıştırma Bloğu
if __name__ == "__main__":
    print("Kanallar bulunuyor...")
    channel_df = get_channel_info(youtube, channel_ids)

    all_videos_data = pd.DataFrame()

    for index, row in channel_df.iterrows():
        print(f"{row['channelName']} kanalının videoları çekiliyor...")
        playlist_id = row['playlistId']
        video_ids = get_video_ids(youtube, playlist_id)

        video_details_df = get_video_details(youtube, video_ids)
        all_videos_data = pd.concat([all_videos_data, video_details_df], ignore_index=True)

    # Veriyi kaydetme
    all_videos_data.to_csv('youtube_raw_data.csv', index=False, encoding='utf-8')
    print("İşlem tamam! Veriler 'youtube_raw_data.csv' dosyasına kaydedildi.")
    print(all_videos_data.head())  # İlk 5 satırı ekranda gör