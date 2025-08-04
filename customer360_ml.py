# ------------------------------
# Customer360: Churn Prediction
# ------------------------------

# 1. Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
print("✅ Data loaded, shape:", df.shape)
print(df.head())

# 3. Encode categorical columns (convert text → numbers)
df_copy = df.copy()
for col in df_copy.columns:
    if df_copy[col].dtype == 'object':
        df_copy[col] = LabelEncoder().fit_transform(df_copy[col].astype(str))

print("✅ Data encoded")
print(df_copy.head())

# 4. Split data (X = inputs, y = output)
X = df_copy.drop("Churn", axis=1)   # Features (independent variables)
y = df_copy["Churn"]                # Target (dependent variable)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("✅ Train size:", X_train.shape, "Test size:", X_test.shape)

# 5. Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

print("✅ Model trained!")
print("🎯 Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# 7. Add churn probability back to original data
df["Churn_Probability"] = model.predict_proba(X)[:, 1]

print("✅ Predictions added:")
print(df[["customerID", "Churn", "Churn_Probability"]].head())

# 8. Save new dataset for Power BI
df.to_csv("Customer360_with_predictions.csv", index=False)
print("✅ File saved: Customer360_with_predictions.csv")
