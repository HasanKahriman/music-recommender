# 🎵 Müzik Öneri Motoru v2.0

114.000+ şarkılık Spotify veri seti üzerinde çalışan yapay zeka destekli müzik öneri sistemi.

## Özellikler

- **Big Data**: 114.000+ şarkı içeren gerçek Spotify veri seti ile çalışır
- **Akıllı Algoritma**: Cosine Similarity ile akustik özellik analizi
- **Hızlı Sonuç**: Vektörel arama ile saniyeler içinde öneri
- **Modern Arayüz**: CustomTkinter ile Dark Mode GUI

## Kurulum
```bash
git clone https://github.com/HasanKahriman/music-recommender.git
cd music-recommender
pip install -r requirements.txt
```

## Kullanım
```bash
python src/app_gui.py
```

1. Arama kutusuna şarkı adı yazın (örn: "Starboy")
2. "Bul ve Öner" butonuna tıklayın
3. En benzer 5 şarkıyı görün

## Teknolojiler

- **Python 3.x**
- **Pandas** - Veri analizi
- **Scikit-learn** - Makine öğrenmesi
- **CustomTkinter** - GUI

## Proje Yapısı
```
music-recommender/
├── data/
│   ├── spotify_tracks.csv    # 114K+ şarkı veri seti
│   └── songs.csv             # Şarkı verileri
├── src/
│   ├── app_gui.py
│   ├── recommender.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Nasıl Çalışır?

Sistem, şarkıların tempo, enerji, dans edilebilirlik gibi akustik özelliklerini analiz eder ve Cosine Similarity algoritması ile matematiksel benzerlik hesaplar.

**Not:** Bu proje, 114.000+ şarkılık büyük veri yapısı kullanılarak geliştirilmiştir.

## İletişim

**Hasan Kahriman**
- GitHub: [@HasanKahriman](https://github.com/HasanKahriman)