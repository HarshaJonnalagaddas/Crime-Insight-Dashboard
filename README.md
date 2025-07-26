# Crime Insight Dashboard  
**Analysing Socioeconomic Determinants of Crime in India using Census & NCRB Data**

This project integrates publicly available data from the Indian Census and National Crime Records Bureau (NCRB) to study how factors like unemployment, literacy, and urbanization relate to regional crime patterns. The goal is to develop insights using statistical analysis, visualization, and clustering techniques.

---

## 🔍 Objectives  
- Integrate and clean multi-source government datasets  
- Engineer meaningful indicators like per capita crime rate  
- Perform correlation analysis and statistical testing (ANOVA, Pearson)  
- Apply dimensionality reduction and clustering  
- Visualize patterns via interactive dashboards and maps  

---

## 📊 Features  
- **Preprocessing & Data Wrangling**  
  Cleaned and standardized over 25 demographic and crime-related variables.

- **Exploratory Data Analysis**  
  Correlation matrices, crime-type distributions, and demographic comparisons.

- **Statistical Testing**  
  Identified significant relationships between youth unemployment and property crimes.

- **Clustering & PCA**  
  Segmented Indian states into crime-risk categories using unsupervised learning.

- **Interactive Visualizations**  
  Geospatial plots using Plotly & Folium to visualize crime and socioeconomic data across India.

---

## 📁 Folder Structure  
├── data/ datasets (CSV/Excel)
├── preliminary_eda.ipynb
├── crime_insight_dashboard.py
├── README.md


---

## 🛠️ Tools & Libraries  
- **Python**: pandas, NumPy, seaborn, matplotlib, plotly, folium  
- **ML/Stats**: scikit-learn, PCA, KMeans, SciPy (ANOVA, Pearson)  
- **Data Sources**:  
  - [NCRB Crime Data](https://ncrb.gov.in)  
  - [Census India](https://censusindia.gov.in/)

---

## 📌 Results  
- Discovered a strong correlation (r > 0.75) between youth unemployment and property crime rates.  
- Segmented states into low-, medium-, and high-risk clusters based on socio-crime profiles.  
- Developed a prototype dashboard for public data storytelling and policy analysis.

---

## ✅ Future Enhancements  
- Add year-wise temporal trends and time-series forecasting  
- Expand dataset coverage (district-level granularity)  
- Deploy dashboard via Streamlit or Dash

---

## 📄 License  
This project is for academic and educational use. Attribution appreciated if reused.

