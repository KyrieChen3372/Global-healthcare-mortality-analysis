# 🌍 Global Health Analytics: Predictive Modeling & Resource Adequacy

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Machine-Learning](https://img.shields.io/badge/Machine--Learning-Scikit--Learn-orange)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success)]()

## 📖 Overview
This project investigates the intricate relationship between **global healthcare worker density** (physicians, pharmacists, and nurse-midwives) and various **mortality rates** (infant, chronic disease, and suicide). [cite_start]Utilizing a comprehensive UN SDG (Sustainable Development Goals) dataset covering 164 countries from 2000 to 2015 [cite: 16, 17][cite_start], the system quantifies the impact of resource maldistribution on public health outcomes[cite: 14, 15].

> [cite_start]**Core Insight:** Analysis confirms that as health worker density increases, mortality rates decrease significantly[cite: 136, 137]. [cite_start]Specifically, in any year where nurse density exceeded 150 per 10,000 population, infant mortality rates approached zero[cite: 567].

---

## 🤖 Machine Learning Implementation
I developed two distinct supervised learning models to move beyond descriptive statistics into predictive risk assessment:

### 1. Logistic Regression (Binary Classification)
* **Target:** Predicted whether a country's **Maternal Mortality Ratio** falls above or below the global median.
* **Predictor:** Pharmacist density per 10,000 population.
* **Methodology:** Implemented a 70/30 train-test split and binarized targets using median thresholding to evaluate predictive accuracy.

### 2. Naive Bayes (Risk Tier Categorization)
* **Target:** Categorized countries into **three risk tiers** (Low, Medium, High) based on mortality quantiles (`pd.qcut`).
* **Features:** Integrated multi-dimensional features, including physician density and the proportion of births attended by skilled health personnel.
* **Evaluation:** Utilized **Confusion Matrices** and **Classification Reports** to validate model performance.



---

## 📊 Statistical Insights & Visual Analytics

### 📍 Healthcare Density & Infant Survival
* [cite_start]**Inverse Relationship:** A significant negative correlation exists between health worker density and neonatal/maternal mortality rates across regions[cite: 434, 566].
* [cite_start]**Critical Thresholds:** Analysis shows that areas with almost zero nurses frequently experience infant mortality rates exceeding 40%[cite: 567].



### 📍 Gender Disparities in Mortality
* [cite_start]**Suicide Rates:** Male suicide mortality consistently exceeds female rates across all analyzed regions[cite: 365, 368].
* [cite_start]**Regional Peak:** Europe boasts the highest male suicide rate among all continents, followed by Asia[cite: 366, 367].
* [cite_start]**Infant Trends:** Median infant mortality rates are similar for boys and girls (~5%), though regional outliers show extreme localized risks[cite: 584, 586].

### 📍 Regional Trends (2000–2015)
* [cite_start]**Global Improvement:** All regions (Africa, Asia, Europe, Oceania, Americas) showed a decline in child mortality over the study period[cite: 332, 333].
* [cite_start]**The African Outlier:** Africa consistently maintains the highest maternal and child mortality rates coupled with the lowest healthcare worker density[cite: 432, 477].



---

## 🛠️ Tech Stack
* [cite_start]**Data Preprocessing:** `Pandas` (ETL, column renaming, quantile cutting, data normalization)[cite: 142, 523, 528].
* **Machine Learning:** `Scikit-Learn` (LogisticRegression, GaussianNB, train_test_split, metrics).
* [cite_start]**Visualization:** `Matplotlib`, `Seaborn` (Violin Plots, Box Plots, Scatter Plots, Bubble Charts)[cite: 144, 225, 525, 610].

---

## 💻 How to Run
1. **Clone the Repository**
   ```bash
   git clone https://github.com/KyrieChen3372/Global-Healthcare-Density-Mortality-Analysis.git
   cd Global-Healthcare-Density-Mortality-Analysis
   ```
2. **Install Dependencies**
   ```bash
   pip install pandas scikit-learn matplotlib seaborn tabulate
   ```
3. **Run Predictive Models**
  ```bash
   python src/logistic.py
python src/Naive_Bayes.py
```

## 👥 Contributors
Collaborative effort for **DATA1002** at the **University of Sydney** (Group 1002_L32_G3):
* **Zelin Chen (SID: 530333591)** - Lead Machine Learning Engineer & Data Analyst: Developed Logistic/Naive Bayes models, conducted pharmacist density research, and designed advanced bubble chart visualizations.
* **Team Members (SID: 500366554, 530649584, 520595273)** - Contributors to physician/nurse analysis, data cleaning, and final report writing.
  

