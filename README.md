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

*(Buraya `grafik_1_etkilesim.png` dosyasını sürükleyip bırakarak veya linkini ekleyerek görseli yerleştirin)*

### 2. Yayın Günü Optimizasyonu
Veriler, haftanın belirli günlerinde yüklenen videoların algoritma tarafından daha fazla desteklendiğini ve kullanıcı alışkanlıklarına daha çok hitap ettiğini göstermektedir.

*(Buraya `grafik_2_gunler.png` dosyasını sürükleyip bırakarak veya linkini ekleyerek görseli yerleştirin)*

### 3. Video Süresi ve İzlenme İlişkisi
Kısa tüketim çağında videoların uzunluğunun izleyiciyi nasıl etkilediğine dair korelasyon analizi.

*(Buraya `grafik_3_sure_izlenme.png` dosyasını sürükleyip bırakarak veya linkini ekleyerek görseli yerleştirin)*

---

## 💻 Kurulum ve Çalıştırma

Projeyi kendi lokal ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu klonlayın:
   ```bash
   git clone [https://github.com/kullaniciadiniz/youtube-veri-analizi.git](https://github.com/kullaniciadiniz/youtube-veri-analizi.git)
