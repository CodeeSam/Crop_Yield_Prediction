# Crop Yield Prediction Using Machine Learning

This repository contains an applied machine learning project for predicting crop yield using agricultural and environmental data. The project includes a training script, dataset, saved machine learning model, and a simple application interface for making crop yield predictions.

This project was developed as an applied machine learning and agritech project and is maintained as part of my machine learning project portfolio.

## Project Overview

Crop yield prediction is an important task in agricultural planning, food security analysis, and farm decision-making. Yield can be influenced by multiple factors, including crop type, rainfall, temperature, pesticide usage, soil conditions, and other environmental or management-related variables.

Machine learning can be used to identify patterns in agricultural datasets and build predictive models that estimate expected crop yield from available input features.

In this project, a machine learning model is trained on crop yield data and saved for reuse in a simple prediction application.

## Objectives

The main objectives of this project are to:

- preprocess crop yield data
- train a machine learning model for yield prediction
- save the trained model for reuse
- build a simple application for prediction
- demonstrate an end-to-end agricultural machine learning workflow

## Repository Structure

```text
Crop_Yield_Prediction/
├── app.py
├── crop_yield_data.csv
├── crop_yield_model.pkl
├── train_model.py
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md
```

## Files Description

### `app.py`

This file contains the application code for making crop yield predictions using the saved model. It loads the trained model and provides an interface where users can input crop or environmental variables and obtain a predicted yield value.

### `crop_yield_data.csv`

This is the dataset used for training and evaluating the crop yield prediction model. It contains crop-related and/or environmental variables used as input features for model development.

### `crop_yield_model.pkl`

This is the saved trained machine learning model. It allows the application to make predictions without retraining the model every time.

### `train_model.py`

This file contains the model training workflow. It loads the dataset, preprocesses the data, trains the model, evaluates performance, and saves the trained model as a `.pkl` file.

### `requirements.txt`

This file lists the Python packages required to run the project.

### `.gitattributes`

This file may be used for repository configuration, including file tracking settings such as Git LFS handling for larger files.

## Methodology

The project follows a standard machine learning workflow.

### 1. Data Loading

The crop yield dataset is loaded and inspected for:

- feature columns
- target variable
- missing values
- data types
- basic descriptive statistics

### 2. Data Preprocessing

The dataset is prepared for model development through preprocessing steps such as:

- separating input features and target variable
- handling missing values where applicable
- encoding categorical variables where applicable
- scaling or transforming numerical variables where required
- splitting the dataset into training and testing sets

### 3. Model Training

A machine learning regression model is trained to predict crop yield based on the available input features.

The model learns relationships between agricultural/environmental variables and crop yield outcomes.

### 4. Model Saving

After training, the model is saved as:

```text
crop_yield_model.pkl
```

This allows the model to be reused by the prediction application.

### 5. Prediction Application

The application loads the saved model and allows users to provide input values. The model then returns a predicted crop yield based on the input features.

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/CodeeSam/Crop_Yield_Prediction.git
cd Crop_Yield_Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Training the Model

To train or retrain the model, run:

```bash
python train_model.py
```

After training, the model will be saved as:

```text
crop_yield_model.pkl
```

## Running the Application

To run the application, use:

```bash
python app.py
```

If the application was built with Streamlit, use:

```bash
streamlit run app.py
```

## Requirements

The main Python packages used in this project may include:

```text
pandas
numpy
scikit-learn
streamlit
pickle
```

Depending on the implementation, additional packages may also be required. See `requirements.txt` for the complete list.

## Example Workflow

```text
Crop Yield Dataset → Data Preprocessing → Model Training → Saved Model → Prediction App
```

## Project Note

This repository represents an applied machine learning project in agricultural yield prediction. It is intended to demonstrate how machine learning can be used to build a simple predictive workflow for crop yield estimation.

The project should be interpreted as a demonstration and learning-based application, not as a production-level agricultural forecasting system.

## Limitations

Some limitations of this project include:

- The model performance depends on the size and quality of the dataset.
- The dataset may not represent all crop types, countries, climates, or farming systems.
- The model may not generalize well to regions or conditions not represented in the training data.
- The project does not include large-scale external validation.
- The application is intended for demonstration and educational purposes.
- Real-world crop yield forecasting would require more detailed agronomic, climatic, soil, and management data.

## Future Improvements

Possible future improvements include:

- adding stronger exploratory data analysis
- evaluating multiple regression models
- adding cross-validation
- reporting metrics such as MAE, RMSE, and R²
- adding feature importance analysis
- improving the user interface
- deploying the app online
- adding support for more crop types and regions
- incorporating weather, soil, fertilizer, and satellite-derived features
- organizing files into `data/`, `models/`, and `src/` folders

## Applications

This type of project can be useful as a starting point for:

- agricultural data science
- crop yield forecasting
- agritech machine learning applications
- regression modeling practice
- predictive analytics projects
- simple ML application deployment


## Author

**Samson Ayorinde Oni**  
Machine Learning | Data Science | Computational Research  


## License

This repository is released under the MIT License.
