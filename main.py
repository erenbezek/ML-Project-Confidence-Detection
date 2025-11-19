import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# veri yukleme..

df = pd.read_csv("data/confidence_features.csv")
print("Veri örneği:\n", df.head(), "\n")

# kategorik kolonlari sayisallastirma

categorical_cols = ["head_direction", "arm_position", "posture"]

df = pd.get_dummies(df, columns=categorical_cols)
print("One-hot encoding sonrasi kolonlar:\n", df.columns, "\n")

# label encoding (hedef deger confident / not confident)

label_encoder = LabelEncoder()
df["confidence_label"] = label_encoder.fit_transform(df["confidence_label"])

# x - y ayirrmasi

X = df.drop("confidence_label", axis=1)
y = df["confidence_label"]

# -------------------------------------------------------------
#!! Ek Gorsellestirme: onemli ozellikler arasi iliskiler (EDA)
# (Bu kısım da One-Hot Encoding yapilmamis orijinal veriyi kullandim)
# -------------------------------------------------------------

print("Pair Plot olusturuluyor...")
try:
    
    df_original = pd.read_csv("data/confidence_features.csv")
    
    # 3 surekli ozellik ve hedef degiskeni secimi

    features_for_pairplot = ['shoulder_span', 'wrist_distance_x', 'eye_distance_ratio', 'confidence_label']
    df_subset = df_original[features_for_pairplot]

    # Pair Plot (olusturma..)
    plt.figure() # yeni bir figur
    sns.pairplot(df_subset, hue='confidence_label', palette='viridis', diag_kind='kde')
    plt.suptitle("ozellikler arasi iliskiler (sinifa gore)", y=1.02)
    plt.savefig("pair_plot_top_features.png")
    plt.close() # kaydedildikten sonra kapanis!!
    print("-> pair_plot_top_features.png basariyla olusturuldu.")

except Exception as e:
    print(f"hata oldu, Pair Plot olusturulamadi: {e}")
# ------------------------------------------------------------------------------------------------------------------------------


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model olusturma
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# test tahminleri
y_pred = model.predict(X_test)

# accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc:.4f}")

# confusion matrix (Grafik)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=label_encoder.classes_,
            yticklabels=label_encoder.classes_)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Hata Matrisi ve Feature Importance icin:
plt.savefig("dosya_adı.png") # grafigi pencere olarak degil png olarak kaydetme icin
plt.close() 

# tahmin fonksiyonu
def predict_confidence(sample_dict):
    """
    sample_dict: 
        Ör: {
            "eye_shoulder_y_ratio": -0.49,
            "shoulder_y_diff": 0.006,
            "wrist_distance_x": 0.57,
            "wrist_shoulder_ratio": 1.24,
            "head_direction": "Looking Straight",
            "arm_position": "Partially Open",
            "posture": "Upright"
        }
    """
    temp = pd.DataFrame([sample_dict])

    # kategorik kolonlari one-hot'a cevir
    temp = pd.get_dummies(temp)

    # eksik (dummy) kolonlarini ekle (esitleme)
    for col in X.columns:
        if col not in temp.columns:
            temp[col] = 0

    temp = temp[X.columns]

    pred = model.predict(temp)[0]
    return label_encoder.inverse_transform([pred])[0]


#ornek tahmin
example = {
    "eye_shoulder_y_ratio": -0.49,
    "shoulder_y_diff": 0.006,
    "wrist_distance_x": 0.57,
    "wrist_shoulder_ratio": 1.24,
    "head_direction": "Looking Straight",
    "arm_position": "Partially Open",
    "posture": "Upright"
}

print("\nÖrnek tahmin →", predict_confidence(example))
