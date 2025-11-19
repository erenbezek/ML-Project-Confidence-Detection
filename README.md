# ML-Project-Confidence-Detection

#  Makine Öğrenmesi Projesi: Beden Dili ile Güven Tespiti (Confidence Detection)

Bu proje, Kaggle veri setini kullanarak, bir kişinin duruşu ve pozisyonu üzerinden güven seviyesini (**Confident, Neutral, Low**) tahmin etmeyi amaçlayan bir **Çoklu Sınıflandırma (Multi-Class Classification)** projesidir.
---

## 1. Veri Seti ve Keşifçi Veri Analizi (EDA)

### A. İşlem Gerekçeleri ve Veri Kontrolü (İster 1)

| İşlem | Yapılma Nedeni (Gerekçesi) |
| :--- | :--- |
| **`df.info()` Kontrolü** | **Eksik (Null) değer** olup olmadığını ve veri tiplerinin modellemeye uygunluğunu kontrol etmek. |
| **Sınıf Dağılım Grafiği** | Hedef sınıflar arasındaki **veri dengesizliğini (imbalance)** kontrol etmek. Modelin başarısını gerekçelendirmek. |

* **Sınıf Dağılımı (Bar Plot):**
   <img width="700" height="500" alt="class_distribution_v2" src="https://github.com/user-attachments/assets/9c502e7f-5ba6-43ca-949e-8d07bc52fa2d" />



### B. Korelasyon Testi ve Özellik Kararları (İster 2 & 3)

| Korelasyon Test Yöntemi | Yapılma Nedeni | Kolon Çıkarma Kararı |
| :--- | :--- | :--- |
| **Box/Violin Plot** | Önemli sayısal özelliklerin sınıflar arasında ayrım gücünü **görsel olarak test etmek** (Korelasyon analizi). | İlk denemede yüksek performans elde edildiği için **düşük korelasyon nedeniyle hiçbir kolon çıkarılmamıştır**. |
| **Pair Plot** | Çoklu değişkenler arasındaki ilişkilerin sınıflara göre nasıl ayrıldığını **görsel olarak test etmek** (Hocanın örneğine en yakın görsel test). | - |
| **Feature Importance** | Bir özelliğin hedef değişkenle olan **tahmin edici gücünü** belirleyerek, en güçlü ilişkiye sahip özellikleri kanıtlamak. | - |

* **Kritik Özellik Dağılımı (Violin Plot):**
   <img width="800" height="600" alt="shoulder_span_violinplot" src="https://github.com/user-attachments/assets/1215d6e0-5652-4744-ac83-a8307ecffc5f" />



* **Özellikler Arası İlişkiler (Pair Plot):**
     (ss5)

---

## 2. Veri Ön İşleme (Preprocessing)

| İşlem | Yapılma Nedeni (Gerekçesi) |
| :--- | :--- |
| **One-Hot Encoding** | **Kategorik metin** verilerini modelin anlayacağı **sayısal (ikili)** formata dönüştürmek. |
| **Label Encoding** | Üç farklı etiketi modelin anlayacağı **0, 1, 2** gibi sayısal hedeflere dönüştürmek. |
| **Train-Test Split** | Modelin genelleme yeteneğini test etmek. |

---

## 3. Model Seçimi ve Eğitimi

### A. Modelin Uygunluğu Gerekçesi (İster 4)

| Özellik | Random Forest (Seçilen) | Linear Regression (Uygun Değil) |
| :--- | :--- | :--- |
| **Problem Tipi** | **Sınıflandırma** (Etiket Tahmini) | Regresyon (Sürekli Sayı Tahmini) |
| **Uygunluk** | Kategorik etiketler için idealdir. | Sayısal tahminler için uygundur. |

**Gerekçe:** Hedef değişkenimizin **kategorik etiketler** olması nedeniyle, **Random Forest Sınıflandırıcı** modeli tercih edilmiştir. Bu model, yüksek doğruluk ve kararlılık sunarak projenin gerekliliklerini en iyi şekilde karşılamaktadır.

---

## 4. Model Değerlendirme ve Genel Sonuç

### A. Model Performansı

| Metrik | Sonuç | Yorum |
| :--- | :--- | :--- |
| **Doğruluk (Accuracy)** | **%97.56** | Model, test verisinin neredeyse tamamını doğru sınıflandırmıştır. |

* **Hata Matrisi (Confusion Matrix):**
     (ss3)
    * **Bulgu:** Matris, modelin **üç sınıfı da** çok düşük hata oranıyla ayırt ettiğini gösterir.

### B. Özellik Önem Sıralaması

* **Feature Importance:**
     (ss4)
    * **Bulgu:** Modelin kararına en çok etki eden özellikler **`shoulder_span`**, **`wrist_distance_x`** ve **`eye_distance_ratio`** gibi **vücut oranları ve duruşla** ilgili özellikler olmuştur.

### C. Genel Sonuç (İster 5)

Bu proje, **Random Forest** modeli kullanarak beden dili verilerinden güven seviyesini tahmin etme görevinde **%97.56** gibi olağanüstü bir başarı elde etmiştir. Geliştirilen modelin analizi ve **Feature Importance** bulguları, güven seviyesinin belirlenmesinde en kritik bilginin **duruş ve vücut oranlarından** geldiğini kanıtlamıştır. Proje, tüm akademik modelleme, analiz ve gerekçelendirme adımlarını başarıyla tamamlamıştır.
