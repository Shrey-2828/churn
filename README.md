# 📉 Customer Churn Prediction

## 🚀 Project Overview

This project is a **Customer Churn Prediction System** built using the **XGBoost algorithm**.

---

## 📊 Dataset Details

* Dataset: **Churn_Modelling.csv**
* Features include:

  * Credit Score
  * Geography
  * Gender
  * Age
  * Tenure
  * Balance
  * Number of Products
  * Has Credit Card
  * Is Active Member
  * Estimated Salary

---

## 🧠 Model Details

* **Algorithm:** XGBoost Classifier
* **Type:** Gradient Boosting (Ensemble Learning)
* **Output:** Churn (1) / Not Churn (0)

---

## ⚙️ Model Configuration

* Uses decision tree boosting
* Handles non-linearity effectively
* Robust to feature interactions

---

## 📈 Model Performance

* **Accuracy:0.8575** 
* **Precision:0.7264**
* **Recall:0.5506912442396313**
* **F1-score:0.6264744429882044**

---

## 🔧 Preprocessing Steps

* Handling missing values (if any)
* Encoding categorical variables (Geography, Gender)
* Feature scaling (optional for XGBoost but used for consistency)
* Train-test split

---

## 🌐 Live Demo

🚀 Try the deployed app here:
👉 **https://customerchurn-shrey18.streamlit.app/**

---

## 🖥️ User Input Features (Planned UI)

Future UI will allow users to input:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card (0/1)
* Is Active Member (0/1)
* Estimated Salary

---

## ⚙️ Technologies & Libraries Used

| Library          | Purpose                    |
| ---------------- | -------------------------- |
| **Pandas**       | Data preprocessing         |
| **NumPy**        | Numerical operations       |
| **Scikit-learn** | Preprocessing & evaluation |
| **XGBoost**      | Model training             |
| **Streamlit**    | UI & (future) deployment   |

---

## 🔄 Workflow

1. Load dataset using Pandas
2. Perform preprocessing:

   * Encoding categorical features
   * Feature scaling
3. Split dataset into training and testing
4. Train model using **XGBoost Classifier**
5. Evaluate model performance
6. Prepare for deployment

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash id="a1b2c3"
git clone https://github.com/your-username/customer-churn-xgboost.git
cd customer-churn-xgboost
```

### 2. Install Dependencies

```bash id="d4e5f6"
pip install -r requirements.txt
```

### 3. Run the Model

```bash id="g7h8i9"
python train.py
```

---

## 📁 Project Structure

```id="j1k2l3"
customer-churn-xgboost/
│
├── Churn_Modelling.csv
├── model.pkl
├── encoder.pkl
├── scaler.pkl
├── train.py / notebook.ipynb
├── requirements.txt
└── README.md
```

---

## 📌 Features

* Powerful ensemble learning model
* Handles complex patterns in data
* Works well with structured datasets
* Ready for UI integration

---

## 📈 Future Improvements

* ✅ Build full **Streamlit UI**
* Deploy application online
* Hyperparameter tuning for better performance
* Compare with ANN & other models

---

## 📈 Key Takeaway

> XGBoost is a **high-performance ensemble algorithm**
> that often delivers **better accuracy on tabular data** compared to traditional models.

---

## 🤝 Contributing

This is an experimental project, but improvements are welcome!

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Developed by **Shrey Patel**

---

⭐ If you found this project useful, consider giving it a star!
