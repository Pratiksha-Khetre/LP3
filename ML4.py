# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print(df.head())

# Select numerical columns
data = df.select_dtypes(include=["int64", "float64"])

# Remove missing values
data = data.dropna()

# Feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(data)

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow graph
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# Apply K-Means with optimal clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

print("\nCluster Results:")
print(df["Cluster"].value_counts())

print("\nFirst 10 Records:")
print(df.head(10))