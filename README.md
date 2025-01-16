# EMS_Response_Performance_Analysis

Chat history



Phase 3

Improving RTC Factors4o
You said:
when working on my project, how could i best say that i'm looking for factors that can be altered or adjusted by the agency's administration in order to improve RTC?
ChatGPT
To articulate your focus on identifying modifiable factors, you could say:

"I aim to identify operational, environmental, or resource-related factors that the agency's administration can adjust or optimize to improve Response Time Compliance (RTC). This includes exploring variables such as resource allocation (e.g., total vehicles, BLS vs. ALS ambulances), deployment strategies (e.g., satellite stations, hospital-origin dispatches), environmental conditions (e.g., weather-related delays), and operational statuses (e.g., system overload or ED diversion). By isolating these modifiable elements, we can develop targeted interventions to enhance response efficiency and meet compliance benchmarks."

This statement clearly connects your objective with actionable areas of improvement within the administration's control.






You said:
i'm just looking for one sentence, there are factors which we can change and those we cannot, i'm looking to explain human changeable factors. how do i properly say human changeable factors?
ChatGPT said:
ChatGPT
You can describe them as "modifiable operational factors" or "administratively adjustable variables."






You said:
EMS_Operations_Analysis (6).pdf
PDF
check out my notebook, which things can i pull out of my imports code block that aren't actually used anywhere in the notebook? 
ChatGPT
After reviewing your imports, here's a list of modules or functions that are likely unused in your notebook:

Unused Modules/Functions:
matplotlib.pyplot:
While seaborn is used for visualizations, there doesn't seem to be a direct use of matplotlib.pyplot for custom plotting commands.
statsmodels.api as sm:
While regression analysis functions are present, no evidence of statsmodels usage is in the provided sections.
scipy.stats.kstest and scipy.stats.norm:
If Kolmogorov-Smirnov tests are present, this might be incorrectly flagged, but specific use cases were unclear.
GridSearchCV and Pipeline:
These seem included but don't show structured testing or usage in the bulk upstream visual functions' explanation۔
Shallow features of unsual। But I couldn >

If I crosschecked ag....

There are discrepancies i






You said:
can you start working on the raw markdown for a readme for this? 
ChatGPT said:
ChatGPT
I've drafted the initial raw markdown for your README file. Let me know if you'd like any specific sections expanded, revised, or formatted further.


2/2






You said:
can you update this is a linked table of contents?
ChatGPT said:
ChatGPT
The README now includes a linked table of contents. Let me know if







ChatGPT can make mistakes. Check important info.
?
ChatGPT is still generating a response...

Ems Operations Readme
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
# EMS Operations Analysis

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
Ask ChatGPT to edit
