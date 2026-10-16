# 🏠 House Price Prediction using Machine Learning

A Machine Learning project that predicts estimated house values using California housing data. This project covers the end-to-end ML workflow, from data analysis and model training to building and deploying a Streamlit web application.

## 🌐 Live Demo

🚀 **Try the app:** [House Price Predictor](https://house-price-prediction-tfv6pqybxm7fgta9yynr3p.streamlit.app/)

💻 **GitHub Repository:** [Anjalibhatt10/house-price-prediction](https://github.com/Anjalibhatt10/house-price-prediction)

## 📌 Project Overview

The goal of this project is to understand how Machine Learning can learn patterns from historical housing data and use them to predict house values.

This project explores data analysis, regression algorithms, model evaluation, feature importance, model saving, and web application deployment.

Users can enter housing-related details through an interactive Streamlit interface and receive an estimated house value.

## ✨ Features

- Exploratory Data Analysis (EDA)
- Data visualization and correlation analysis
- Data preprocessing and train-test splitting
- Linear Regression, Decision Tree, and Random Forest models
- Model evaluation using MAE and R²
- Cross-validation and hyperparameter experimentation
- Random Forest feature importance visualization
- Model saving and loading using Joblib
- Interactive three-screen Streamlit application
- GitHub version control and cloud deployment

## 🧠 Machine Learning Workflow

1. Load the California Housing dataset.
2. Explore the data and understand its features.
3. Analyze distributions, correlations, and potential outliers.
4. Separate input features (`X`) and target (`y`).
5. Split data into training and testing sets.
6. Train and evaluate regression models.
7. Experiment with model parameters.
8. Select a Random Forest model for the application.
9. Save the trained model using Joblib.
10. Deploy the Streamlit application.

## 🤖 Models Explored

| Model | Purpose |
|---|---|
| Linear Regression | Establish a regression baseline |
| Decision Tree Regressor | Learn nonlinear relationships and explore overfitting |
| Random Forest Regressor | Combine multiple decision trees to improve predictions |

**Current model:** Random Forest Regressor with 200 trees and a maximum depth of 20.

### 📊 Model Evaluation

Results from the current experiments:

- **Test MAE:** approximately 0.3271
- **Test R²:** approximately 0.8057
- **Five-fold cross-validation MAE:** approximately 0.3338

The target is expressed in units of $100,000. A test MAE of 0.3271 therefore corresponds to an average absolute prediction error of approximately $32,710 in the dataset's target units.

These results come from the current evaluation setup and do not guarantee accuracy for every prediction.

## 🗂️ Dataset

This project uses the **California Housing dataset** provided by scikit-learn.

It contains 20,640 observations and eight input features.

| Feature | Description |
|---|---|
| `MedInc` | Median income for a census block group |
| `HouseAge` | Median house age |
| `AveRooms` | Average rooms per household |
| `AveBedrms` | Average bedrooms per household |
| `Population` | Census block group population |
| `AveOccup` | Average household occupancy |
| `Latitude` | Geographic latitude |
| `Longitude` | Geographic longitude |

**Target:** `MedHouseVal` — median house value, in units of $100,000.

**Note:** This is California housing data, not Indian real-estate data. The current model uses regional housing statistics rather than individual-property details such as parking or bathrooms.

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook
- Streamlit
- Git and GitHub

## 📁 Project Structure

```text
house-price-prediction/
├── models/
│   └── house_price_model.pkl
├── notebooks/
│   └── house_price_analysis.ipynb
├── src/
│   └── app.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Anjalibhatt10/house-price-prediction.git
cd house-price-prediction
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run src/app.py
```

The application should open in your browser.

## 🖥️ Application Flow

The app has three screens:

1. **Welcome Screen** — introduces the House Price Predictor.
2. **House Details** — collects the eight features expected by the model.
3. **Prediction Result** — displays the estimated house value.

## 📚 Key Learnings

- Understanding supervised learning and regression
- Exploratory data analysis and visualization
- Preparing features and target variables
- Understanding overfitting and model generalization
- Comparing regression algorithms
- Evaluating models with MAE and R²
- Cross-validation and hyperparameter tuning
- Interpreting feature importance
- Saving and loading trained models
- Integrating a trained model with Streamlit
- Version control with Git and GitHub
- Deploying a web application

## 🔮 Future Improvements

- Enhance the user interface and add more visualizations.
- Improve input validation and error handling.
- Experiment with additional regression algorithms.
- Add automated tests and a reproducible training pipeline.
- Explore an appropriate Indian housing dataset.
- Incorporate individual-property features such as area, bedrooms, bathrooms, parking, and location when supported by suitable data.

## 👩‍💻 Author

**Anjali Bhatt**

Aspiring AI Engineer interested in Machine Learning, Python, data analysis, and practical AI applications.

- **GitHub:** [Anjalibhatt10](https://github.com/Anjalibhatt10)

---

*Built as a hands-on project to learn and practise the end-to-end Machine Learning workflow.*
