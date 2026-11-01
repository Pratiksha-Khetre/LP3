# Import libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("emails.csv")

print(df.head())

# Remove unnecessary column
df = df.drop(columns=["Email No."], errors="ignore")

# Remove missing values
df = df.dropna()

# Separate features and target
X = df.drop("Prediction", axis=1)
y = df["Prediction"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN Classification
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred1 = knn.predict(X_test)

# SVM Classification
svm = SVC(kernel="linear")
svm.fit(X_train, y_train)

y_pred2 = svm.predict(X_test)

# Evaluate KNN
print("\nKNN Results")
print("Accuracy:", accuracy_score(y_test, y_pred1))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred1))
print("Classification Report:\n", classification_report(y_test, y_pred1))

# Evaluate SVM
print("\nSVM Results")
print("Accuracy:", accuracy_score(y_test, y_pred2))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred2))
print("Classification Report:\n", classification_report(y_test, y_pred2))