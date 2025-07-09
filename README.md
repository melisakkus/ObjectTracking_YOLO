# Object Tracking with YOLOv8

Bu proje, YOLOv8 modelini kullanarak video dosyalarında araç ve kişi takibi yapan bir uygulamadır. OpenCV ve Ultralytics kütüphaneleri kullanılarak geliştirilmiştir.

## Özellikler

- **Araç Takibi**: Video içerisindeki araçları gerçek zamanlı olarak tespit eder ve takip eder
- **Kişi Takibi**: Video içerisindeki kişileri gerçek zamanlı olarak tespit eder ve takip eder
- **Video Kaydetme**: İşlenmiş videoları MP4 formatında kaydeder
- **Benzersiz ID'ler**: Her nesneye benzersiz bir takip ID'si atar
- **Gerçek Zamanlı Görüntüleme**: İşlenmiş videoyu ekranda gösterir

## Gereksinimler

```bash
pip install ultralytics
pip install opencv-python
pip install imutils
pip install numpy
```

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/melisakkus/ObjectTracking_YOLO.git
cd ObjectTracking
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```
veya manuel olarak:
```bash
pip install ultralytics
pip install opencv-python
pip install imutils
pip install numpy
```

3. YOLOv8 modelini indirin (kod çalıştırıldığında otomatik olarak indirilir):
```bash
# yolov8n.pt modeli otomatik olarak indirilecektir
```

## Dosya Yapısı

```
ObjectTracking/
├── .idea/                   # IDE ayarları
├── .venv/                   # Sanal ortam dosyaları
├── output_videos/           # Çıktı videoları klasörü
│   ├── output_cartracking.mp4    # Araç takibi çıktı videosu
│   └── output_persontracking.mp4 # Kişi takibi çıktı videosu
├── test_videos/             # Test videoları klasörü
│   ├── test_cartracking.mp4      # Araç takibi test videosu
│   └── test_persontracking.mp4   # Kişi takibi test videosu
├── main_cartracking_trace.py     # Kuyruk eklemeli araç takibi kodu
├── main_cartracking.py           # Araç takibi kodu 
├── main_persontracking.py       # Kişi takibi kodu
├── explainings.txt               # Açıklama dosyası
├── requirements.txt              # Gerekli kütüphaneler
├── yolov8n.pt                   # YOLOv8 modeli (otomatik indirilir)
└── README.md                    # Bu dosya
```

## Kod Açıklaması

### Temel Parametreler

- **vehicle_id = 2**: COCO veri setinde araç sınıfı ID'si
- **person_id = 0**: COCO veri setinde kişi sınıfı ID'si
- **width = 1200**: Video genişliği (performans için yeniden boyutlandırılır)

### Ana İşlem Adımları

1. Video dosyası okunur
2. Her frame YOLOv8 modeline gönderilir
3. Tespit edilen nesneler filtrelenir (araç/kişi)
4. Her nesne için bounding box ve ID çizilir
5. İşlenmiş frame kaydedilir ve gösterilir

## Kontroller

- **'q' tuşu**: Uygulamayı sonlandırır
- **Pencere kapatma**: Uygulamayı sonlandırır

## Teknik Detaylar

- **Model**: YOLOv8 Nano (yolov8n.pt)
- **Video Codec**: MP4V
- **Çıktı Formatı**: MP4

### Test Videoları

Bu proje için kullanılan test videoları:

#### Araç Takibi Test Videosu
![aractest](https://github.com/user-attachments/assets/e69d5a7a-59ec-45f1-9186-1e687b39bbc0)

#### Kişi Takibi Test Videosu  

![persontest](https://github.com/user-attachments/assets/5d18b781-6244-4bb0-83e3-9aa96dd22b0a)


### Çıktı Videoları

İşlenmiş ve takip bilgileri eklenmiş videolar:

#### Araç Takibi Sonucu
![arac_output](https://github.com/user-attachments/assets/e21aea3b-112d-40d9-a743-4623f2e6e131)

#### Kişi Takibi Sonucu
![output_persontracking](https://github.com/user-attachments/assets/22211691-26dc-4c29-a5cd-a5b50de05a0d)
