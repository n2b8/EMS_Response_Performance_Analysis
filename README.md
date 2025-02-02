# Emergency Medical Services (EMS) Response Performance Analysis

![Ambulance](images/ambulance1.jpg)

*Image source: [Envato.com](https://envato.com)*

---

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Data Sources](#data-sources)
  - [Dataset Details](#dataset-details)
- [Methodology](#methodology)
  - [1. Data Cleaning and Preparation](#1-data-cleaning-and-preparation)
  - [2. Exploratory Data Analysis (EDA)](#2-exploratory-data-analysis-eda)
  - [3. Statistical Analysis](#3-statistical-analysis)
  - [4. Modeling](#4-modeling)
- [Results](#results)
- [Recommendations](#recommendations)
- [Future Directions](#future-directions)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Acknowledgments](#acknowledgments)

---

## Project Overview
This project evaluates the operational metrics of a large urban EMS agency managing approximately 130,000 annual 911 calls. The primary focus is on achieving **Response Time Compliance (RTC)**, defined as meeting the 90th percentile response time benchmark of 540 seconds (9 minutes) for emergent calls, as per **[NFPA Standard 1710](https://www.nfpa.org/codes-and-standards/nfpa-1710-standard-development/1710)**.

---

## Objectives
- **Primary Goal**: Improve RTC compliance for emergent calls.
- **Key Research Questions**:
  1. What factors significantly influence RTC?
  2. How do staffing levels, call volumes, and other metrics impact compliance?
  3. Can predictive models accurately classify compliant and non-compliant cases?
- **Success Criteria**:
  - Generate actionable insights through EDA and statistical tests.
  - Develop predictive models achieving an **F1-Score** of at least 0.75.

---

## Data Sources
The analysis leverages the following datasets:
- **Computer-Aided Dispatch (CAD) System**:
  - Operational metrics such as response times, incident counts, and resource deployment.
- **Open-Meteo API**:
  - Historical weather data, including temperature, rainfall, and snowfall.

### Dataset Details
- **Timeframe**: November 1, 2014, to November 1, 2024.
- **Features**:
  - **Operational Metrics**: Incident counts, response times, and vehicle availability.
  - **Environmental Factors**: Temperature, precipitation, and severe weather flags.
  - **Derived Metrics**: Lagged features, interaction terms, and rolling averages.

---

## Methodology

### 1. Data Cleaning and Preparation
- **Steps Taken**:
  - Imputed missing values for `chute_times` using KNN-based methods.
  - Replaced missing transport counts with zero.
  - Dropped rows with invalid `total_cars` values (<1) and capped extreme `dist_mean` values.
- **Feature Engineering**:
  - Added interaction features (`dist_mean_is_peak`, `tx_per_ambulance_is_peak`).
  - Created lagged metrics and rolling averages for temporal dependencies.
  - Introduced binary flags for peak operational hours and system overloads.

### 2. Exploratory Data Analysis (EDA)
- Examined compliance trends using KDE plots, box plots, and time series analysis.
- Identified relationships between RTC and operational factors such as distances, chute times, and resource availability.

### 3. Statistical Analysis
- **Kolmogorov-Smirnov (KS) Test**:
  - Validated normality of key features.
- **Mann-Whitney U Test**:
  - Highlighted significant differences between compliant and non-compliant incidents for features like `dist_mean` and `chute_times_emergent`.

### 4. Modeling
- **Approach**:
  - Logistic regression pipeline with hyperparameter tuning via GridSearchCV.
  - Decision tree models for interpretability and comparison.
- **Feature Selection**:
  - Based on domain expertise, correlation analysis, and feature importance scores.

---

## Results
### Top Influential Features
1. **`dist_mean`**: Travel distance to incidents.
2. **`chute_times_emergent`**: Dispatch-to-departure times.
3. **`als_resources_per_emergent_response`**: ALS availability per emergent response.

### Model Performance
- **Logistic Regression**:
  - **F1-Score = 0.800** (at a threshold of 0.45).
  - Cross-validation: **Mean F1-Score = 0.7947** (±0.0023).
- **Decision Tree**:
  - **F1-Score = 0.780** after hyperparameter tuning.
  - Cross-validation: **Mean F1-Score = 0.7823** (±0.0040).

---

## Recommendations

Based on the analysis, the following recommendations are proposed to improve Response Time Compliance (RTC). These strategies focus on actionable factors the agency can directly influence and should be tested over a 3–6 month period, with data re-evaluated to measure their effectiveness.

1. **Reduce Travel Distance During Peak Hours**:
   - **Key Insight**: Longer travel distances during peak hours significantly reduce RTC compliance.
   - **Action**: Reevaluate and optimize resource placement to minimize travel distances, particularly during peak hours (7 AM–9 PM). Implement dynamic deployment strategies based on historical and real-time incident data, focusing on high-demand areas.

2. **Address Chute Time Delays**:
   - **Key Insight**: Delays in dispatch-to-departure times are strongly associated with non-compliance.
   - **Action**: Investigate factors contributing to delays, such as time spent at hospitals and mid-shift crew breaks. Implement policies to streamline hospital-based transitions and formalize rest periods to prevent dispatch interruptions. Engage staff to gather insights and address operational challenges affecting chute times.

3. **Optimize ALS Resource Allocation**:
   - **Key Insight**: Inconsistent ALS staffing levels during peak times and overuse of ALS units for non-emergent calls reduce availability for true emergencies.
   - **Action**: Adjust staffing ratios dynamically to ensure adequate ALS coverage during high-demand periods. Increase the use of BLS units for non-emergent calls and consider allowing BLS units to respond to certain emergent calls under specific guidelines. Reassess dispatch codes to determine if certain incidents require emergent responses.

---

By implementing these strategies and re-evaluating the results after 3–6 months, the agency can iteratively refine its operations to improve RTC compliance and overall efficiency.

---

## Future Directions
- Incorporate individual call-level data for higher-resolution analysis.
- Conduct geographical studies to tailor resource placement by district.
- Investigate traffic and routing data to better model `dist_mean` and its impact.

---

## File Structure

- **[data/](data/)**:
  - **[data/ems_ops.csv](data/ems_ops.csv)**: The raw dataset containing hourly operational metrics.
  - **[data/EMS_Data_Dictionary.txt](data/EMS_Data_Dictionary.txt)**: Data dictionary describing `ems_ops.csv` dataset columns.
  - **[data/cleaned_data.csv](data/cleaned_data.csv)**: Cleaned and prepared data in csv format.
- **[models/](models/)**:
  - **[models/logreg_model.pkl](models/logreg_model.pkl)**: Trained logistic regression model for RTC prediction.
  - **[models/dtc_model.pkl](models/dtc_model.pkl)**: Trained decision tree classifier model for RTC prediction.
- **[visualizations/](visualizations/)**:
  - **[visualizations/kde_output.ipynb](visualizations/kde_output.ipynb)**: Notebook for dynamically outputting kde plots for selected features.
  - **[visualizations/kde_dist_mean_plot.png](visualizations/kde_dist_mean_plot.png)**: KDE plot for dist_mean by compliance.
- **[index.ipynb](index.ipynb)**: The analysis notebook for data preparation, EDA, and modeling.
- **[helper.py](helper.py)**: Provides ComplianceTester class which allows for statistical comparison analysis of selected feature(s).
- **[presentation.pdf](presentation.pdf)**: A PDF version of a Keynote presentation summarizing the findings and recommendations.

---

## Requirements
- **Python 3.8+**
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - statsmodels

---

## Acknowledgments
- Data provided by the EMS agency.
- Weather data sourced from the [Open-Meteo API](https://open-meteo.com/).
- Image(s) and graphic(s) sourced from [Envato.com](https://envato.com).
