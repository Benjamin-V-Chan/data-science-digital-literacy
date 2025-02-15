# data-science-digital-literacy

# Project Overview
This project analyzes digital literacy data to assess training effectiveness and predict overall literacy scores. The workflow includes data preprocessing, exploratory analysis, feature engineering, model training, and results evaluation.

# Folder Structure
```
project-root/
├── data/
│   ├── digital_literacy_dataset.csv  # Original dataset
│   ├── cleaned_data.csv              # Preprocessed dataset
│   ├── processed_data.csv            # Dataset with new features
├── scripts/
│   ├── 01_data_preprocessing.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_feature_engineering.py
│   ├── 04_model_training.py
│   ├── 05_results_analysis.py
├── outputs/
│   ├── data_summary.csv
│   ├── literacy_score_distribution.png
│   ├── correlation_heatmap.png
│   ├── literacy_model.pkl
│   ├── model_performance.txt
```

# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

## 2. Run Data Preprocessing:
Clean and encode the dataset.
```sh
python scripts/01_data_preprocessing.py
```

## 3. Run Exploratory Analysis:
Generate descriptive statistics and visualizations.
```sh
python scripts/02_exploratory_analysis.py
```

## 4. Run Feature Engineering:
Create new features from existing data.
```sh
python scripts/03_feature_engineering.py
```

## 5. Train the Model:
Train a regression model to predict literacy scores.
```sh
python scripts/04_model_training.py
```

## 6. Analyze Results:
Evaluate the model and save the results.
```sh
python scripts/05_results_analysis.py
```

# Requirements
- Python 3.x
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

# Acknowledgments
**Dataset Name:** Digital Literacy Education Dataset  
**Dataset Author:** Ziya  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/ziya07/digital-literacy-education-dataset)