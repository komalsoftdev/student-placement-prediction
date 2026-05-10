# ================================
# STUDENT PLACEMENT PREDICTION MODEL
# ================================

# Import Libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ================================
# LOAD DATASET
# ================================

df = pd.read_csv("student_placement_synthetic.csv")

# ================================
# DATA PREPROCESSING
# ================================

# Drop salary column because it contains many null values
df = df.drop('salary_package_lpa', axis=1)

# Convert categorical columns into numeric columns
df = pd.get_dummies(df, drop_first=True)

# ================================
# FEATURES & TARGET
# ================================

X = df.drop('placement_status', axis=1)

y = df['placement_status']

# ================================
# TRAIN TEST SPLIT
# ================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ================================
# FEATURE SCALING
# ================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# ================================
# TRAIN MODEL
# ================================
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# ================================
# MAKE PREDICTIONS
# ================================

y_pred = model.predict(X_test)

# ================================
# MODEL EVALUATION
# ================================

print("\n========== MODEL ACCURACY ==========")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\n========== CLASSIFICATION REPORT ==========")

print(classification_report(y_test, y_pred))

print("\n========== CONFUSION MATRIX ==========")

print(confusion_matrix(y_test, y_pred))