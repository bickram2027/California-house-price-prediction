# California House Price Prediction

## Project Overview

This project predicts the median house value using the California Housing dataset.

I trained and compared two regression models:

* Linear Regression
* Random Forest Regressor

After comparing their performance using RMSE, MAE and R² Score, Random Forest was selected as the final model because it performed better.

The final model is saved as `random_forest_model.pkl` and is used in a Streamlit web application for prediction.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## Dataset Features

The model uses the following features:

* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity

The target variable is:

* `median_house_value`

## Model Comparison

Two regression models were trained and evaluated.

| Model             |    RMSE |     MAE | R² Score |
| ----------------- | ------: | ------: | -------: |
| Linear Regression |  70,059 |  50,679 |    0.625 |
| Random Forest     | 48,941* | 31,628* |   0.78* |

* These were the results of the earlier unrestricted Random Forest model. The final deployed model uses a limited tree depth to reduce model size and make deployment easier, with an R² score of approximately 0.78.

Since Random Forest performed better than Linear Regression, it was selected as the final model.

## Model Evaluation

Because this is a regression problem, the following metrics were used:

* **RMSE (Root Mean Squared Error):** Measures the average prediction error while giving more importance to larger errors. Lower is better.
* **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted values. Lower is better.
* **R² Score:** Measures how well the model explains the variation in house prices. Higher is better.

Accuracy, precision and recall were not used because they are primarily classification metrics.

## Machine Learning Workflow

```text
Load Dataset
      ↓
Separate Features and Target
      ↓
Train-Test Split
      ↓
Data Preprocessing
      ↓
Linear Regression
      ↓
Random Forest Regressor
      ↓
Compare RMSE, MAE and R²
      ↓
Select Random Forest
      ↓
Save Model using Joblib
      ↓
Streamlit Web Application
```

## Preprocessing

The numerical features are processed using:

* Median imputation for missing values
* StandardScaler for scaling

The categorical feature `ocean_proximity` is processed using:

* Most-frequent imputation
* One-Hot Encoding

The preprocessing steps are saved together with the trained Random Forest model in `random_forest_model.pkl`.

## Streamlit Application

The Streamlit application allows the user to enter house details such as location, number of rooms, population, median income and ocean proximity.

The application then uses the trained Random Forest model to predict the estimated median house value.

## Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── train_model.py
├── House_Price_Prediction.ipynb
├── random_forest_model.pkl
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/House-Price-Prediction.git
```

### 2. Open the project folder

```bash
cd House-Price-Prediction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## Final Model

The final model is a **Random Forest Regressor**.

The trained model and preprocessing pipeline are stored in:

```text
random_forest_model.pkl
```

The model can be loaded using:

```python
import joblib

model_data = joblib.load("random_forest_model.pkl")

model = model_data["model"]
preprocessor = model_data["preprocessor"]
```

## Author

**Bickram Chowdhury**

B.Tech – Computer Science and Engineering
