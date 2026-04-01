# 🏠 Airbnb Dynamic Pricing Engine

## 📌 Overview

This project is an end-to-end Machine Learning system that predicts optimal Airbnb listing prices based on property features, location, and demand-related factors.

It mimics real-world dynamic pricing systems used by platforms like Uber and Airbnb.



## 🚀 Features

* 📊 Data cleaning and preprocessing of real-world Airbnb dataset
* 🧠 Feature engineering (demand signals, availability, location encoding)
* 🤖 Machine Learning model using XGBoost
* 📉 Handling outliers and skewed data using log transformation
* ⚡ FastAPI backend for real-time predictions
* 🌐 Interactive frontend using Streamlit
* ☁️ Deployment-ready architecture



## 🧱 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* FastAPI
* Streamlit



## 📊 Model Details

* Model: XGBoost Regressor
* Target: Price prediction
* Key Techniques:

  * Outlier removal
  * Log transformation of target
  * Feature encoding (one-hot encoding)



## 📈 Evaluation Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score



## ⚙️ How It Works

1. User inputs property details (location, rooms, demand signals)
2. Frontend sends request to FastAPI
3. Model processes input and predicts price
4. Result displayed instantly



## 🖥️ Run Locally

### 1. Clone the repo

```bash
git clone <your-repo-link>
cd dynamic_price_prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API

```bash
uvicorn api:app --reload
```

### 4. Run frontend

```bash
streamlit run app.py
```



## 🌍 Deployment

The project can be deployed using:

* Streamlit Cloud (for frontend)
* Render / AWS (for backend)



## 💼 Use Case

This project demonstrates how real-world pricing systems work by combining:

* Machine Learning
* Backend APIs
* Frontend applications



## 🔥 Key Learnings

* Handling real-world noisy data
* Feature importance and model interpretability
* End-to-end ML system design
* Model deployment and integration



## 📌 Future Improvements

* Add SHAP for explainability
* Use real-time streaming data
* Improve UI with React
* Hyperparameter tuning with Optuna



## 👨‍💻 Author

Your Name
