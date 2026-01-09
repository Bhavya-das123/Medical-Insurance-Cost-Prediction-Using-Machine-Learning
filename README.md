🏥 Medical Insurance Cost Prediction Using Machine Learning

 📌 Project Overview

This project focuses on predicting **medical insurance costs** for individuals using **machine learning techniques**. The model analyzes various personal, lifestyle, and insurance-related factors to estimate the insurance charges accurately. This system can assist insurance companies, healthcare analysts, and individuals in understanding cost drivers and making informed decisions.

---

## 🎯 Objectives

* To analyze factors affecting medical insurance costs
* To build and compare multiple machine learning models
* To evaluate model performance using appropriate metrics
* To deploy the best-performing model using **Streamlit**

---

## 📊 Dataset Description

The dataset includes the following features:

* **Age** – Age of the individual
* **Gender** – Male/Female
* **BMI** – Body Mass Index
* **Children** – Number of dependents
* **Smoker** – Smoking status (Yes/No)
* **Region** – Residential area
* **Diet Type** – Dietary habits
* **Insurance Plan** – Type of insurance policy
* **Medical Insurance Cost** – Target variable (charges)

---

## ⚙️ Technologies Used

* **Programming Language:** Python 🐍
* **Libraries:**

  * NumPy
  * Pandas
  * Matplotlib & Seaborn
  * Scikit-learn
  * Pickle
* **Framework:** Streamlit
* **Version Control:** Git & GitHub

---

## 🧠 Machine Learning Models Implemented

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regressor

📌 **Model Evaluation Metrics:**

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

## 🔄 Workflow

1. Data Collection
2. Data Cleaning & Preprocessing

   * Handling missing values
   * Label Encoding & One-Hot Encoding
   * Feature Scaling
3. Exploratory Data Analysis (EDA)
4. Model Training
5. Model Evaluation
6. Hyperparameter Tuning
7. Model Deployment

---

## 🚀 Deployment

The final model is deployed using **Streamlit**, providing a user-friendly web interface where users can input personal and insurance details to predict medical insurance costs.



## 📁 Project Structure

```
Medical-Insurance-Cost-Prediction-Using-Machine-Learning/
│
├── dataset/
│   └── insurance.csv
├── models/
│   ├── model.sav
│   ├── scaler.sav
│   └── label_encoder.sav
├── app.py
├── requirements.txt
└── README.md
```



## ▶️ How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/Medical-Insurance-Cost-Prediction-Using-Machine-Learning.git
   ```
2. Navigate to the project directory

   ```bash
   cd Medical-Insurance-Cost-Prediction-Using-Machine-Learning
   ```
3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app

   ```bash
   streamlit run app.py
   ```


## 📈 Results

* The tuned regression model achieved a **high R² score** on test data
* The model generalizes well without overfitting
* Smoking status and BMI were the most influential features


## 🔮 Future Enhancements

* Add deep learning models
* Improve UI/UX of the Streamlit app
* Deploy the application on cloud platforms
* Integrate real-time data


## 👤 Author

**Bhavya Das**

## ⭐ Acknowledgements

* Scikit-learn Documentation
* Streamlit Community
* Open-source datasets




