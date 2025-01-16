# EMS Response Performance Analysis

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
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Project Overview
This project analyzes and evaluates operational metrics for an urban Emergency Medical Services (EMS) agency that handles approximately 130,000 annual 911 calls. The focus is on improving **Response Time Compliance (RTC)** to achieve the 90th percentile response time benchmark of 540 seconds (9 minutes) for emergent calls, as per **NFPA Standard 1710**.

## Objectives
- **Primary Goal**: Improve compliance with the 90th percentile response time target for emergent calls.
- **Key Research Questions**:
  1. What factors significantly influence RTC?
  2. How do staffing levels, call volumes, and other metrics affect compliance?
  3. Can predictive models accurately classify cases of compliance and non-compliance?
- **Success Criteria**:
  - Gain actionable insights from exploratory data analysis and statistical tests.
  - Build a predictive model achieving an **ROC-AUC score** of 0.8 or higher.

## Data Sources
The analysis uses data aggregated hourly from:
- **Computer-Aided Dispatch (CAD) system**: Operational metrics such as response times, call counts, and vehicle allocations.
- **OpenMeteo API**: Weather data including temperature, rainfall, and snowfall.

### Dataset Details
- **Date Range**: November 1, 2014, to November 1, 2024.
- **Key Features**:
  - Incident and response metrics (e.g., `incident_count`, `emergent_responses`).
  - Resource deployment (e.g., `total_cars`, `als_ambulances`).
  - Environmental factors (e.g., `temperature`, `weather_status`).
  - Derived metrics (e.g., `tx_per_ambulance`, `rolling_emergent_avg`).

## Methodology

### 1. Data Cleaning and Preparation
- **Missing Values**:
  - Imputed `chute_times` with a KNN-based approach.
  - Set missing transport counts to zero.
- **Outlier Handling**:
  - Dropped rows with `total_cars < 1`.
  - Capped `dist_mean` using one standard deviation above the mean.
- **Feature Engineering**:
  - Interaction terms (e.g., `resp_per_ambulance`).
  - Lagged features (e.g., `percentile_90_response_emergent_lag1`).
  - Binary flags for peak hours and system overloads.

### 2. Exploratory Data Analysis (EDA)
- Visualized relationships between compliance and operational metrics using line plots, density plots, and box plots.
- Analyzed historical trends in response times and compliance rates.

### 3. Statistical Analysis
- **Kolmogorov-Smirnov (KS) Test**: Evaluated normality of key features.
- **Mann-Whitney U Test**: Compared distributions of compliant and non-compliant cases for key metrics (e.g., `dist_mean`, `chute_times_emergent`).

### 4. Modeling
- Built a predictive pipeline using logistic regression.
- Feature selection based on correlation analysis and domain expertise.
- Optimized model parameters using **GridSearchCV**.

## Results
- **Top Influential Factors**:
  1. `dist_mean`: Average travel distance to scenes.
  2. `chute_times_emergent`: Dispatch-to-departure times.
  3. `als_resources_per_emergent_response`: Availability of ALS resources.
  4. `resp_per_ambulance`: Responses handled per ambulance.
  5. `percentile_90_response_emergent_lag1`: Lagged 90th percentile response times.

- **Model Performance**:
  - Logistic Regression achieved an **F1-Score** of 0.765.
  - Decision Tree Classifier had an F1-Score of 0.712.
  - Cross-validation demonstrated consistent ROC-AUC scores averaging 0.803.

## Recommendations
1. **Strategic Ambulance Placement**:
   - Minimize travel distances (`dist_mean`) by positioning resources in high-demand areas.
2. **Reduce Dispatch Delays**:
   - Focus on improving `chute_times_emergent` through process enhancements.
3. **Optimize Resource Allocation**:
   - Deploy BLS resources for non-emergent calls to free up ALS units.
4. **Address Resource Strain**:
   - Reassess staffing levels to ensure adequate ALS coverage during peak times.

## Future Directions
- Incorporate call-level data for granular analysis.
- Study geographic patterns of compliance to refine resource deployment.
- Model `dist_mean` as a target variable to identify factors increasing travel distances.

## File Structure
```
project/
├── data/
│   ├── ems_ops.csv
│   └── EMS_Data_Dictionary.txt
├── notebooks/
│   └── EMS_Operations_Analysis.ipynb
├── models/
│   └── logistic_regression.pkl
├── visualizations/
│   └── response_times_trends.png
└── README.md
```

## Requirements
- Python 3.8+
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - statsmodels

## Usage
1. Clone the repository and navigate to the project directory.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the analysis notebook `EMS_Operations_Analysis.ipynb`.

## Acknowledgments
- EMS agency data provided by [source].
- Weather data sourced from OpenMeteo API.
