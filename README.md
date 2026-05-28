Customer Churn Prediction
A Machine Learning project to predict whether a customer will churn (leave the service) or not using classification techniques.

📌 Overview
Customer churn prediction helps businesses identify customers who are likely to leave. This project uses a Random Forest Classifier to analyze customer data and predict churn.

🧠 Features
Data Cleaning & Preprocessing

Handling Missing Values

Categorical Encoding (One-Hot Encoding)

Feature Selection

Machine Learning Model (Random Forest)

Model Evaluation (Accuracy, Confusion Matrix)

Streamlit Web App for Real-time Prediction

📊 Dataset
Telco Customer Churn Dataset

Contains customer details like:

Tenure

Monthly Charges

Contract Type

Payment Method

Internet Services

⚙️ Tech Stack
Python

Pandas

NumPy

Scikit-learn

Streamlit

Joblib

🤖 Model Used
Random Forest Classifier

Handles non-linear data well

Provides good accuracy (~80–85%)

Helps in feature importance analysis

📈 Model Performance
Accuracy: ~80–85%

Confusion Matrix used for evaluation

Focus on predicting churn customers effectively

💻 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/sahilmalviya/customer-churn-prediction.git
cd customer-churn-prediction
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the app
streamlit run app.py
📸 Application
User inputs customer details

Model predicts:

✅ Customer will stay

🚨 Customer will churn

📁 Project Structure
├── app.py
├── churn_model.pkl
├── columns.pkl
├── requirements.txt
├── README.md
🔥 Future Improvements
Add more input features in UI

Improve recall for churn prediction

Hyperparameter tuning

Deploy app online

🙌 Author
Sahil Malviya
