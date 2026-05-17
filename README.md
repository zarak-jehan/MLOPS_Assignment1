# 📊 Diabetes Prediction MLOps Project

## 🧠 Project Overview

This project is a complete end-to-end Machine Learning and MLOps pipeline that predicts whether a patient has diabetes based on medical features. It includes:

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Machine Learning model training
- Model evaluation and comparison
- Model saving using Joblib
- FastAPI deployment with Pydantic validation
- REST API testing using cURL
- Git version control

---

## 📁 Project Structure

project/
│
├── data_model.ipynb              # Data cleaning, EDA, model training
├── app.py                        # FastAPI application
├── diabetes_model.pkl           # Trained ML model
├── training_columns.pkl         # Training feature columns
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
│
├── screenshots/                 # API and terminal outputs
└── diabetes_unclean.csv        # Dataset

---

## ⚙️ Technologies Used

- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- FastAPI
- Pydantic
- Joblib
- Uvicorn
- Git & GitHub

---

## 📊 Dataset Information

Medical attributes:
- Age, Urea, Creatinine, HbA1c, Cholesterol, TG, HDL, LDL, VLDL, BMI, Gender
- Target: Diabetes class (N / Y)

---

## 🧹 Data Preprocessing

- Dropped ID columns
- Fixed Gender inconsistencies
- Handled missing values (mean/mode)
- One-hot encoding applied
- Feature alignment ensured

---

## 📊 Exploratory Data Analysis

- Gender distribution
- Age histogram
- BMI histogram
- BMI vs HbA1c scatter
- Age vs HbA1c scatter
- Box plots

---

## 🤖 Machine Learning Models

- Logistic Regression
- SVM
- Decision Tree
- Random Forest
- KNN

---

## 📈 Model Evaluation

Metrics used:
- Accuracy
- Precision
- Recall
- F1-Score

---

## 🏆 Best Model

Best model selected based on F1-score and saved using Joblib.

---

## 🚀 FastAPI Deployment

### Endpoints:

GET /
Returns API status

POST /predict
Returns diabetes prediction

---

## 🧪 Example Output

{
  "prediction": "N"
}

N = Non-Diabetic  
Y = Diabetic

---

## ⚡ Run Project

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload

---

## 🌐 API Docs

http://127.0.0.1:8000/docs

---

## 👨‍💻 Author

MLOps Assignment Project
