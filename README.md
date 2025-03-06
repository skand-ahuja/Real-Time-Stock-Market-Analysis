# **Real-Time Stock Market Analysis**

## 📌 **Project Overview**
This project performs **real-time stock market analysis** using Python, APIs, SQL, Snowflake, and AWS. It includes data collection, preprocessing, machine learning-based forecasting, and visualization using Power BI/Tableau.

## 🚀 **Key Features**
- **Real-Time Stock Data** - Fetch data using Yahoo Finance API.
- **Data Storage** - Store and query data in Snowflake / AWS RDS.
- **Machine Learning** - Apply Regression & Time-Series Forecasting (ARIMA, LSTM).
- **Visualization** - Build interactive Power BI/Tableau dashboards.
- **Cloud Deployment** - Automate data updates using AWS Lambda.

## 🛠️ **Tech Stack**
- **Programming**: Python (Pandas, NumPy, Scikit-learn, TensorFlow)
- **Database**: SQL (Snowflake, AWS RDS, PostgreSQL)
- **APIs**: Yahoo Finance API
- **Machine Learning**: Regression, ARIMA, LSTM
- **Cloud**: AWS Lambda, S3 (for automation & storage)
- **Visualization**: Power BI / Tableau

## 📂 **Folder Structure**
```
Real-Time-Stock-Market-Analysis/
│── 📂 data/                        # Raw & processed data
│   ├── raw_stock_data.csv          # Initial raw stock data
│   ├── processed_stock_data.csv     # Cleaned & processed data
│── 📂 notebooks/                    # Jupyter Notebooks for analysis
│   ├── 01_data_collection.ipynb     # Fetching real-time & historical data
│   ├── 02_data_preprocessing.ipynb  # Data cleaning & transformation
│   ├── 03_EDA.ipynb                 # Exploratory Data Analysis (EDA)
│   ├── 04_ML_Modeling.ipynb         # Regression & Time-Series Analysis
│   ├── 05_model_evaluation.ipynb    # Model evaluation & hyperparameter tuning
│── 📂 scripts/                      # Python scripts for automation
│   ├── fetch_data.py                # Automate data collection (APIs)
│   ├── preprocess_data.py           # Data cleaning and transformation
│   ├── train_model.py               # Train ML models
│   ├── predict.py                   # Make predictions using the trained model
│   ├── deploy_api.py                 # Deploy API for real-time predictions
│── 📂 reports/                      # Project reports & documentation
│   ├── stock_market_analysis.pdf    # Final report
│   ├── README.md                    # Project overview & instructions
│── 📂 dashboards/                   # Visualization files
│   ├── stock_dashboard.pbix         # Power BI dashboard
│   ├── tableau_dashboard.twbx       # Tableau dashboard
│── 📂 models/                       # Saved ML models
│   ├── lstm_model.h5                # Trained LSTM model
│   ├── arima_model.pkl              # ARIMA model file
│── 📂 deployment/                   # Deployment-related files
│   ├── fastapi_app.py               # FastAPI app for real-time predictions
│   ├── requirements.txt             # Dependencies for deployment
│   ├── Dockerfile                   # Docker config for cloud deployment
│── 📂 logs/                         # Logs for debugging
│── .gitignore                       # Ignore unnecessary files in GitHub
│── environment.yml                   # Conda environment dependencies
│── requirements.txt                   # Python dependencies
```

## 🔥 **Getting Started**
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Fetch Real-Time Stock Data
```bash
python scripts/fetch_data.py
```

### 3️⃣ Train Machine Learning Model
```bash
python scripts/train_model.py
```

### 4️⃣ Run API for Predictions (if applicable)
```bash
python deployment/fastapi_app.py
```

## 📊 **Power BI / Tableau Dashboard**
Check out the interactive stock analysis dashboard **(link to be added)**.

## 👨‍💻 **Author**
Skand Ahuja

