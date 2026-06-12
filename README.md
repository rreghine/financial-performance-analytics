🇺🇸 **English** | [🇧🇷 Português](README.pt-BR.md)

# Financial Performance Analytics — NVIDIA vs Intel

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-orange?style=flat-square)
![KMeans](https://img.shields.io/badge/KMeans-Clustering-green?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

Comparative analysis of NVIDIA and Intel's financial performance over 15 years, combining traditional FP&A with Machine Learning — forecasting with Prophet, clustering with KMeans, and variance analysis.

---

## Preview

### Main Dashboard
![Dashboard](preview_dashboard.png)

### Comparison and Overview
![Comparison](preview_comparacao.png)

---

## Business Context

In 2009, Intel was 11x larger than NVIDIA in market cap and dominated the semiconductor industry.
By 2023, NVIDIA had reached US$ 1 trillion in market cap — while Intel remained stuck at the same US$ 109B it had in 2009.

**Core question:** What do the financial data reveal about this transformation? Which indicators anticipated the leadership reversal?

---

## Dataset

**Financial Statements of Major Companies (2009–2023) — Kaggle**

- 12 real companies — Apple, Microsoft, Google, Amazon, NVIDIA, Intel, and others
- 15 years of historical data (2009–2023)
- 23 financial indicators — Revenue, Net Income, EBITDA, ROE, ROA, ROI, Market Cap, Margins, and more
- 9 sectors — IT, Electronics, Banking, Manufacturing, Food, Logistics, FinTech

[Dataset download](https://www.kaggle.com/datasets/rish59/financial-statements-of-major-companies2009-2023)

---

## Project Structure

```
financial-performance-analytics/
│
├── images/
│   ├── nvda_analysis.png
│   ├── nvda_yoy.png
│   ├── intc_analysis.png
│   ├── intc_yoy.png
│   ├── comparacao_receita_marketcap.png
│   ├── comparacao_indicadores.png
│   ├── heatmap_empresas.png
│   ├── scatter_empresas.png
│   ├── forecast_nvidia.png
│   ├── forecast_intel.png
│   └── clusters_empresas.png
├── Financial_Statements_Analysis.ipynb
├── app_nvidia_intel.py
├── requirements.txt
├── preview_dashboard.png
├── preview_comparacao.png
└── README.md
```

---

## Project Flow

```
Raw Data → EDA → FP&A Analysis → Forecasting → Clustering → Deployment
```

### 1. Individual Analysis — NVIDIA
- Revenue, profit, and market cap evolution from 2009 to 2023
- Efficiency indicators: ROE, ROA, Net Margin
- Year-over-Year (YoY) growth with the AI boom annotated

### 2. Individual Analysis — Intel
- Same structure as NVIDIA for direct comparison
- Evidence of revenue stagnation and margin deterioration
- Sharp -20% drop in 2022

### 3. NVIDIA vs Intel Comparison
- Revenue and Market Cap side by side — 2009 to 2022
- Net Margin, ROE, and ROA evolution
- Identification of the leadership reversal point (2020)

### 4. Overview — 12 Companies
- Indicator heatmap per company (Margin, ROE, ROA)
- Scatter plot: Market Cap vs Efficiency
- KMeans clustering — segmentation by financial profile

### 5. Machine Learning — Forecast with Prophet

| Company | 2022 Revenue | 2024 Forecast | 2025 Forecast |
|---|---|---|---|
| **NVIDIA** | US$ 26.9B | US$ 23.5B | US$ 25.0B |
| **Intel** | US$ 63.0B | US$ 82.3B | US$ 85.0B |

### 6. KMeans Clustering — Financial Profile

| Cluster | Profile | Companies |
|---|---|---|
| 0 | High Efficiency | NVDA, INTC, GOOG, MCD |
| 1 | Moderate Efficiency | AAPL, MSFT, GOOG, AMZN |
| 2 | Low Efficiency | PCG, SHLDQ, AIG, BCS, PYPL |

---

## Key Insights

- **Leadership reversal:** In 2009, Intel was worth 11x more than NVIDIA. In 2020, NVIDIA surpassed Intel in market cap for the first time
- **Asymmetric growth:** NVIDIA grew +688% in revenue vs Intel's +80% over the same period
- **NVIDIA efficiency:** ROE reached 44% in 2019 and net margin hit 36% in 2022 — exceptional levels for the sector
- **Intel deterioration:** ROE fell from 28% in 2018 to 7.7% in 2022, evidencing a structural loss of competitiveness
- **Apple — highest average ROE:** 61.3% over the period — capital efficiency exceptionally above average
- **SHLDQ (Sears):** The data anticipated the bankruptcy — persistent negative margins over multiple years

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/rreghine/financial-performance-analytics.git
cd financial-performance-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the notebook to generate the charts
jupyter notebook Financial_Statements_Analysis.ipynb

# 4. Start the Streamlit app
streamlit run app_nvidia_intel.py
```

> The notebook was developed on **Google Colab**. To run locally, install the dependencies from `requirements.txt` first.

---

## Technologies Used

| Category | Tools |
|---|---|
| Language | Python 3.12 |
| Data manipulation | Pandas, NumPy |
| Forecasting | Prophet |
| Machine Learning | Scikit-learn (KMeans) |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Environment | Google Colab |

---

## Author

**Rafael Reghine Munhoz**
Data Analyst | Data Science & Analytics | MBA at USP

[![LinkedIn](https://img.shields.io/badge/LinkedIn-rafaelreghine-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/rafaelreghine)
[![GitHub](https://img.shields.io/badge/GitHub-rreghine-black?style=flat-square&logo=github)](https://github.com/rreghine)
