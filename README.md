# Diabetes Prediction

This project predicts the likelihood of diabetes in patients using machine learning techniques on the Pima Indians Diabetesn Dataset.

## Project Structure

- `diabetes_detect.ipynb`: Jupyter notebook containing data analysis, preprocessing, model training, evaluation, and prediction.
- `diabetes.csv`: Dataset containing patient medical information and diabetes outcomes.
- `README.md`: Project documentation.

## Dataset

The dataset (`diabetes.csv`) contains the following columns:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skinfold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function
- **Age**: Age (years)
- **Outcome**: Class variable (0: No diabetes, 1: Diabetes)

## Usage

1. Open `diabetes_detect.ipynb` in Jupyter Notebook or VS Code.
2. Run the notebook cells to:
   - Load and explore the data
   - Preprocess the dataset
   - Train and evaluate machine learning models
   - Make predictions for new patients

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install dependencies with:

```sh
pip install pandas numpy matplotlib seaborn scikit-learn# Diabetes_prediction

Example

The notebook demonstrates:

- Data exploration and visualization
- Handling missing values
- Model training (e.g., logistic regression)
- Prediction and probability output for new patient data.

License
This project is for educational purposes.