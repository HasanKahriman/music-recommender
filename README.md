# 🎵 Müzik Öneri Motoru (Music Recommender)

Kullanıcının sevdiği bir şarkıya dayanarak benzer şarkıları öneren **Python** tabanlı masaüstü uygulaması.

Spotify benzeri bir algoritma mantığıyla çalışır; şarkıların **BPM (Tempo)**, **Enerji**, **Dans Edilebilirlik** ve **Tür** özelliklerini analiz ederek matematiksel benzerlik (Cosine Similarity) hesaplar.

---

## 🚀 Özellikler

- **Modern Arayüz (GUI):** `CustomTkinter` ile geliştirilmiş, göz yormayan Dark Mode tasarımı
- **Akıllı Algoritma:** `Scikit-learn` ve `Cosine Similarity` ile şarkılar arası vektörel benzerlik hesabı
- **Hızlı Veri İşleme:** `Pandas` kütüphanesi ile optimize edilmiş veri analizi
- **Hata Yönetimi:** Yanlış girişlere ve eksik dosyalara karşı korumalı yapı

---

## 🛠️ Kullanılan Teknolojiler

- [Python 3.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) - Veri Manipülasyonu
- [Scikit-learn](https://scikit-learn.org/) - Makine Öğrenmesi
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern GUI

---

## 💻 Kurulum ve Çalıştırma

### 1. Projeyi İndirin
```bash
git clone https://github.com/HasanKahriman/music-recommender.git
cd music-recommender
```

### 2. Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Başlatın
```bash
python src/app_gui.py
```

---

##  Nasıl Kullanılır?

1. Uygulama açıldığında kutucuğa sevdiğiniz bir şarkı adını yazın (Örn: **Sicko Mode**)
2. **"Önerileri Getir"** butonuna tıklayın
3. Sistem size o şarkıya en çok benzeyen **5 şarkıyı** alt alta listeleyecektir

---

## 📁 Proje Yapısı
```
music-recommender/
├── src/
│   ├── app_gui.py          # Ana GUI uygulaması
│   └── recommender.py      # Öneri algoritması
├── data/
│   └── songs.csv           # Şarkı veri seti
├── requirements.txt        # Gerekli Python paketleri
└── README.md              # Proje dokümantasyonu
```

---

## 👤 Geliştirici

**Hasan Kahriman**  
[GitHub](https://github.com/HasanKahriman) | [LinkedIn](https://linkedin.com/in/hasankahriman)

---