# Enflasyon ve Makroekonomik Değişkenler Arasındaki İlişki Analizi (VAR Analizi)

## Giriş
Bu proje, enflasyon değişkeni ile diğer makroekonomik değişkenler (USD/TRY, işsizlik, para arzı, BIST 100, Brent petrol, faiz oranı) arasındaki kısa ve uzun dönemli ilişkiyi VAR modeli kullanarak analiz eden bir çalışmanın sonuçlarını sunmaktadır. Amaç, değişkenler arasındaki nedenselliği belirlemek ve enflasyon üzerindeki etkileri daha iyi anlamaktır.

## Veri ve Metodoloji
Çalışmada, belirtilen makroekonomik değişkenler için zaman serisi verileri kullanılmıştır. Veriler, enflasyon, USD/TRY, işsizlik, para arzı (M3), BIST 100, Brent petrol (USD) ve faiz oranı olmak üzere yedi değişken ve 58 gözlemden oluşmaktadır. Veri setinde eksik değer bulunmamaktadır. 

Verilerin durağanlığı ADF testi ile incelenmiş ve birinci dereceden fark alınarak durağan hale getirilmiştir. Eşbütünleşme testi olarak Johansen testi uygulanmış ve değişkenler arasında uzun dönemli bir ilişki olduğu sonucuna varılmıştır. Son olarak, VAR modeli kurularak değişkenler arasındaki kısa ve uzun dönemli nedensellik ilişkileri incelenmiştir.

## ADF Testi Sonuçları
### ADF Testi Sonuçları
- **Değişken: Enflasyon**
  - Test İstatistiği: -3.1519
  - P-değeri: 0.0229 (H1: Durağan)
  
- **Değişken: USD/TRY**
  - Test İstatistiği: -0.5352
  - P-değeri: 0.8850 (H0: Durağan değil)
  
- **Değişken: İşsizlik**
  - Test İstatistiği: 0.6344
  - P-değeri: 0.9884 (H0: Durağan değil)
  
- **Değişken: Para Arzı (M3)**
  - Test İstatistiği: 0.5578
  - P-değeri: 0.9865 (H0: Durağan değil)
  
- **Değişken: BIST 100**
  - Test İstatistiği: 0.1406
  - P-değeri: 0.9687 (H0: Durağan değil)
  
- **Değişken: Brent Petrol (USD)**
  - Test İstatistiği: -2.0009
  - P-değeri: 0.2862 (H0: Durağan değil)
  
- **Değişken: Faiz Oranı**
  - Test İstatistiği: -1.7553
  - P-değeri: 0.4029 (H0: Durağan değil)

### Sonuç
ADF testi sonuçlarına göre, enflasyon değişkeni durağan iken, diğer değişkenler birinci dereceden fark alındıktan sonra durağan hale gelmiştir. Bu durum, değişkenlerin farklı hızlarda hareket ettiğini ve uzun dönemde bir dengeye doğru yaklaştıklarını göstermektedir.

## Eşbütünleşme Testi Sonuçları
Johansen eşbütünleşme testi sonuçları, değişkenler arasında uzun dönemli bir ilişki olduğunu göstermektedir. Aşağıdaki tablo eşbütünleşme test sonuçlarını sunmaktadır:

| İz Test   | İz Test Kritik | Öz Değer  | Öz Değer Kritik |
|-----------|----------------|-----------|-----------------|
| 0         | 189.0797       | 72.0189   | 52.3069         |
| 1         | 117.0608       | 39.4765   | 45.8662         |
| 2         | 77.5843        | 33.7501   | 39.3693         |
| 3         | 43.8341        | 20.4822   | 32.7172         |
| 4         | 23.3520        | 11.3337   | 25.8650         |
| 5         | 12.0182        | 7.0880    | 18.5200         |
| 6         | 4.9302         | 4.9302    | 6.6349          |

## VAR Modeli Sonuçları

![Ekran görüntüsü 2024-10-02 174754](https://github.com/user-attachments/assets/5f9d25d5-9837-4e6f-a862-9ea27b7868c5)



### Kısa Dönem Etkileri
- **İşsizlik:** İşsizlik oranındaki artışlar, enflasyonu kısa dönemde olumlu etkilemektedir.
- **Para Arzı:** Para arzındaki artışlar, enflasyonu kısa dönemde olumlu etkilemektedir.
- **USD/TRY:** USD/TRY kurundaki değer kaybı, enflasyonu kısa dönemde olumlu etkilemektedir.

### Uzun Dönem Etkileri
Eşbütünleşme ilişkisi, değişkenlerin uzun vadede birbirlerini etkilediğini göstermektedir. Bu durum, enflasyonun diğer makroekonomik değişkenlerle birlikte hareket ettiğini ifade eder.

## Sonuç
Çalışma sonuçları, enflasyon değişkeni ile diğer makroekonomik değişkenler arasında anlamlı bir ilişki olduğunu göstermektedir. Özellikle işsizlik, para arzı ve USD/TRY değişkenlerinin enflasyon üzerinde önemli etkileri bulunmaktadır. Bu sonuçlar, enflasyonu kontrol altına almak için uygulanan politikaların bu değişkenlere odaklanması gerektiğini göstermektedir.
