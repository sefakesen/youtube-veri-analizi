import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import isodate

# Grafikler için genel tema ayarı
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("Veri yükleniyor ve temizleniyor...")

# 1. Veriyi Yükleme
df = pd.read_csv('youtube_raw_data.csv')

# 2. Veri Temizleme ve Özellik Çıkarımı (Feature Engineering)

# Tarih formatını düzeltme ve yeni kolonlar üretme
df['published_at'] = pd.to_datetime(df['published_at'])
df['publish_day'] = df['published_at'].dt.day_name() # Hangi gün yüklendi? (Pazartesi, Salı vb.)
df['publish_hour'] = df['published_at'].dt.hour       # Saat kaçta yüklendi?

# YouTube'un tuhaf süre formatını (PT15M33S) saniyeye çevirme
df['duration_seconds'] = df['duration'].apply(lambda x: isodate.parse_duration(x).total_seconds())

# Başlık uzunluğu (Karakter sayısı)
df['title_length'] = df['title'].apply(len)

# Etkileşim Oranı (Engagement Rate) hesaplama
# (Beğeni + Yorum) / İzlenme oranını yüzde olarak buluyoruz. (İzlenmesi 0 olanları bölme hatasından koruyoruz)
df['engagement_rate'] = ((df['likes'] + df['comments']) / df['views']) * 100
df['engagement_rate'] = df['engagement_rate'].fillna(0) # Eğer NaN çıkarsa 0 yap

print("Veri temizleme tamamlandı! Analizlere geçiliyor...\n")

# ---------------------------------------------------------
# 3. KEŞİFÇİ VERİ ANALİZİ (GÖRSELLEŞTİRME)
# ---------------------------------------------------------

# Grafik 1: Hangi Kanalın Etkileşim Oranı Daha Yüksek?
plt.figure(figsize=(10, 5))
sns.barplot(x='channel_title', y='engagement_rate', data=df, estimator=lambda x: sum(x)/len(x), errorbar=None, palette="viridis")
plt.title('Kanallara Göre Ortalama Etkileşim Oranı (%)', fontsize=14)
plt.ylabel('Etkileşim Oranı (%)')
plt.xlabel('Kanal Adı')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafik_1_etkilesim.png') # Grafiği bilgisayara kaydeder
plt.show()

# Grafik 2: Haftanın Hangi Günü Daha Çok İzlenme Alınıyor?
# Günleri sıraya koyalım
gun_sirasi = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(10, 5))
sns.barplot(x='publish_day', y='views', data=df, order=gun_sirasi, errorbar=None, palette="magma")
plt.title('Günlere Göre Ortalama İzlenme Sayıları', fontsize=14)
plt.ylabel('Ortalama İzlenme')
plt.xlabel('Yayın Günü')
plt.tight_layout()
plt.savefig('grafik_2_gunler.png')
plt.show()

# Grafik 3: Video Süresi ile İzlenme Arasındaki İlişki (Dağılım Grafiği)
# Sadece 1 saatin (3600 sn) altındaki videoları baz alalım ki grafik çok sıkışmasın
kisa_videolar = df[df['duration_seconds'] < 3600]
plt.figure(figsize=(10, 5))
sns.scatterplot(x='duration_seconds', y='views', hue='channel_title', data=kisa_videolar, alpha=0.7)
plt.title('Video Süresi (Saniye) vs İzlenme Sayısı', fontsize=14)
plt.ylabel('İzlenme Sayısı')
plt.xlabel('Video Süresi (Saniye)')
plt.tight_layout()
plt.savefig('grafik_3_sure_izlenme.png')
plt.show()

# 4. En Çok İzlenen 5 Videonun Çıktısını Alma
print("--- EN ÇOK İZLENEN 5 VİDEO ---")
top_5 = df.nlargest(5, 'views')[['title', 'channel_title', 'views', 'engagement_rate']]
print(top_5.to_string(index=False))

print("\nTüm grafikler çizildi ve bilgisayarına kaydedildi!")