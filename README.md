# Car Sharing Demand Prediction

This project predicts car rental demand using historical and environmental data. It uses machine learning models including Linear Regression, Random Forest, and XGBoost to forecast the number of car rentals at a given time.

## Dataset

The dataset contains both temporal and weather-related features:
- `record_date`, `hour_of_day`
- `temp_celsius`, `humidity_percent`, `wind_speed_mps`, `visibility_10m`, `dew_point_celsius`
- `solar_energy_mj_m2`, `rain_mm`, `snow_cm`
- `season_label`, `is_Holiday`, `is_working_day`
- `car_rental_count` (target variable)

## Models Used

- Linear Regression
- Random Forest Regressor (with GridSearchCV)
- XGBoost Regressor (with GridSearchCV)

## Installation

Make sure you have Python 3.9 or above installed. Then, create a virtual environment and install dependencies.

```bash
# Create virtual environment
python -m venv mlenv

# Activate it
# Windows
mlenv\Scripts\activate
# Linux/macOS
source mlenv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install numpy pandas matplotlib scikit-learn xgboost jupyter

