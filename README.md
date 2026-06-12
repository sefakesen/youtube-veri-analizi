# 📊 YouTube VOD Etkileşim ve Büyüme Analizi

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![YouTube API](https://img.shields.io/badge/YouTube_API-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

Bu proje, içerik üreticilerinin büyüme stratejilerini optimize etmek amacıyla YouTube Data API v3 kullanılarak sıfırdan veri toplanması, temizlenmesi ve analiz edilmesi süreçlerini içerir. Hazır bir veri seti kullanılmamış; gerçek zamanlı kanal verileri çekilerek izleyici davranışları ve etkileşim metrikleri modellenmiştir.

## 🎯 Projenin Amacı
İçerik üretimi ekosisteminde "Hangi videolar daha çok izleniyor?" sorusundan ziyade, **"Hangi tür içerikler, ne zaman yayınlandığında en yüksek sadakati ve etkileşimi yaratıyor?"** sorusuna veri odaklı cevaplar bulmak hedeflenmiştir. 

## 🛠️ Veri İşleme ve Özellik Çıkarımı (Feature Engineering)
Ham veriler API üzerinden çekildikten sonra analitik modellere uygun hale getirilmesi için aşağıdaki işlemler uygulanmıştır:
* **Zaman Çevirileri:** YouTube'un standart ISO 8601 formatındaki süre verileri (örn: `PT15M33S`), matematiksel analiz yapılabilmesi için saniye cinsine (`duration_seconds`) dönüştürüldü.
* **Tarih Ayrıştırma:** Videoların yayınlanma tarihleri üzerinden "Yükleme Günü" ve "Yükleme Saati" özellikleri türetildi.
* **Etkileşim Oranı Skoru (Engagement Rate):** Bir videonun başarısını sadece izlenme sayısıyla ölçmek yanıltıcı olacağından; `(Beğeni + Yorum) / İzlenme * 100` formülü kullanılarak her videoya özel bir kalite skoru atandı.

---

## 📈 Keşifçi Veri Analizi (EDA) ve Temel Bulgular

Aşağıdaki analizler, veri setinden elde edilen görselleştirilmiş içgörüleri sunmaktadır:

### 1. Kanallara Göre Kitle Sadakati (Etkileşim Oranı)
Sadece izlenmeye değil, izleyicinin videoya verdiği reaksiyona odaklandığımızda kanalların gerçek performansları ortaya çıkmaktadır.

*<img width="1000" height="500" alt="grafik_1_etkilesim" src="https://github.com/user-attachments/assets/0781bf8e-31e0-4381-9d2d-40b4576239e2" />*

### 2. Yayın Günü Optimizasyonu
Veriler, haftanın belirli günlerinde yüklenen videoların algoritma tarafından daha fazla desteklendiğini ve kullanıcı alışkanlıklarına daha çok hitap ettiğini göstermektedir.

*<img width="1000" height="500" alt="grafik_2_gunler" src="https://github.com/user-attachments/assets/097e6162-dc3f-4672-96c3-2bcd2786c9ab" />*

### 3. Video Süresi ve İzlenme İlişkisi
Kısa tüketim çağında videoların uzunluğunun izleyiciyi nasıl etkilediğine dair korelasyon analizi.

*<img width="1000" height="500" alt="grafik_3_sure_izlenme" src="https://github.com/user-attachments/assets/b1b6b892-54ce-44d9-b6b1-0e7e33a1e445" />*

---

## 💻 Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak ve analizi kendi hedeflediğiniz kanallar üzerinde denemek için aşağıdaki adımları izleyebilirsiniz:

### 1. Gereksinimler
Projenin çalışması için bilgisayarınızda Python 3.x ve gerekli kütüphanelerin kurulu olması gerekmektedir.

```bash
git clone [https://github.com/kullaniciadiniz/youtube-veri-analizi.git](https://github.com/kullaniciadiniz/youtube-veri-analizi.git)
cd youtube-veri-analizi
pip install google-api-python-client pandas matplotlib seaborn isodate
```

### 2. YouTube API Anahtarı Kurulumu

Projenin YouTube veri çekme scriptini (main.py) çalıştırabilmesi için bir Google Cloud API anahtarına ihtiyacınız vardır:

Google Cloud Console adresine gidin.

Yeni bir proje oluşturun veya mevcut projenizi seçin.

API'ler ve Hizmetler sekmesinden YouTube Data API v3 servisini bulun ve aktif hale getirin.

Kimlik Bilgileri (Credentials) sekmesinden yeni bir API Anahtarı (API Key) oluşturun.

main.py dosyasını açın ve en üstte yer alan API_KEY değişkenine kendi anahtarınızı yapıştırın:
