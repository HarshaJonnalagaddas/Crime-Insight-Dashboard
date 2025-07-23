import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import folium
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.stats import pearsonr, f_oneway, chi2_contingency

# Placeholder: Load census and crime datasets
# census_df = pd.read_csv("data/india_census.csv")
# crime_df = pd.read_csv("data/ncrb_crime_data.csv")

# Placeholder merged DataFrame
merged_df = pd.DataFrame({
    'State': ['State A', 'State B', 'State C'],
    'Youth_Unemployment_Rate': [12.5, 18.2, 8.7],
    'Literacy_Rate': [86.1, 78.3, 91.4],
    'Urbanization_Rate': [45.2, 60.3, 38.7],
    'Property_Crimes': [1450, 2300, 890],
    'Violent_Crimes': [750, 1100, 620],
    'Population': [12000000, 15000000, 9000000]
})

# Feature Engineering: Crime rates per 1 lakh population
merged_df['Property_Crime_Rate'] = merged_df['Property_Crimes'] / merged_df['Population'] * 100000
merged_df['Violent_Crime_Rate'] = merged_df['Violent_Crimes'] / merged_df['Population'] * 100000

# Correlation Analysis
corr, _ = pearsonr(merged_df['Youth_Unemployment_Rate'], merged_df['Property_Crime_Rate'])
print(f"Correlation between youth unemployment and property crime rate: {corr:.2f}")

# PCA + Clustering (Optional Insight)
features = ['Youth_Unemployment_Rate', 'Literacy_Rate', 'Urbanization_Rate', 'Property_Crime_Rate']
X = StandardScaler().fit_transform(merged_df[features])
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
kmeans = KMeans(n_clusters=2, random_state=0).fit(X_pca)
merged_df['Cluster'] = kmeans.labels_

# Scatter Plot with Clusters
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=merged_df['Cluster'], cmap='viridis')
plt.title('State Clustering based on Crime & Demographics')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

# Choropleth Map Placeholder
# folium.Choropleth(...) # When geo-data is available

# Save to CSV for dashboard use
merged_df.to_csv("output/processed_crime_demo_data.csv", index=False)
