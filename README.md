# Elevvo-pathway-projects
student Exam Score Prediction  

Predict students’ exam scores using **machine learning regression models** with study hours, sleep, attendance, participation, past scores, and distractions as key factors.  

## 📌 Project Overview  
This project demonstrates a full **machine learning pipeline**:  
- Data generation (synthetic but realistic)  
- Data cleaning (duplicates, missing values, outliers)  
- Exploratory Data Analysis (EDA)  
- Model training (Linear Regression & Polynomial Regression)  
- Evaluation using multiple metrics  
- Visualization of results  
- Feature engineering & experiments  

The goal is to estimate a student’s **final exam score** and explore how different features (study hours, sleep, etc.) influence performance.  

---

## 🛠️ Tech Stack  
- **Language:** Python  
- **Libraries:**  
  - [Pandas](https://pandas.pydata.org/) – data manipulation  
  - [Matplotlib](https://matplotlib.org/) – visualizations  
  - [scikit-learn](https://scikit-learn.org/stable/) – machine learning  

---
## 📂 Project Structure  
```bash
student_score_project/
│── student_scores_raw.csv        # Synthetic raw dataset (with missing values & outliers)
│── student_scores_clean.csv      # Cleaned dataset
│── model_metrics.csv             # Metrics comparison (all experiments)
│── train_model.py                # Script to retrain and evaluate models
│── README.md                     # Project documentation (this file)
│── figures/                      # Visualizations
│   ├── hist_*.png                # Histograms for each feature
│   ├── correlation_heatmap.png   # Feature correlations
│   ├── linreg_all_actual_vs_pred.png
│   ├── linreg_all_residuals_vs_fitted.png
│   ├── linreg_all_residual_hist.png
│   └── poly_deg2_actual_vs_pred.png
```

---
 Run the Training Script  
```bash
python train_model.py
```

This will:  
- Train **Linear Regression** and **Polynomial Regression (degree=2)**  
- Save metrics to `script_metrics.csv`  
- Generate prediction plots inside `figures/`  

---

## 📊 Results  

- **Linear Regression** works well but struggles with non-linear effects (like sleep).  
- **Polynomial Regression (degree=2)** captures curvatures better, often giving lower RMSE and higher R².  
- Feature experiments show that **study hours + attendance + past scores** are the strongest predictors, while sleep and distractions introduce non-linear effects.

## 🖼️ Sample Visualizations  

**Correlation Heatmap**  
![Correlation Heatmap] 

**Linear Regression – Actual vs Predicted**  
![Linear Regression] 

**Polynomial Regression – Actual vs Predicted**  
![Polynomial Regression]  

---

## 📚 Topics Covered  
- Regression (Linear & Polynomial)  
- Data Cleaning & Preprocessing  
- Evaluation Metrics (MAE, MSE, RMSE, R²)  
- Feature Engineering & Experiments  
- Data Visualization (EDA + Model performance)  

---
