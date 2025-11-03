# predictive_resource_allocation.py
# Predict issue priority based on features (demo using breast cancer dataset as placeholder).
# We'll map the breast cancer target (0/1) into a 3-level priority artificially for demo purposes.

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import joblib

# Load dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y_binary = data.target  # 0 or 1

# For demo: convert binary to 3 classes (low/medium/high) by a derived rule:
# combine some features to create a score and bin into 3 priorities
score = X['mean radius'] + X['mean texture'] * 0.1
y = pd.cut(score, bins=3, labels=['low', 'medium', 'high'])

# Encode labels
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_enc = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Evaluate
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
print("Accuracy:", acc)
print("F1 (weighted):", f1)
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Confusion matrix plot
import seaborn as sns
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Priority Prediction")
plt.savefig("images/rf_metrics.png")
plt.show()

# Save model
joblib.dump(rf, "rf_priority_model.joblib")
