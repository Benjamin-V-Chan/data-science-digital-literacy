import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../data/digital_literacy_dataset.csv")

# Handle missing values (assuming no NaN values based on initial check)
df.dropna(inplace=True)

# Encode categorical variables
categorical_cols = ["Gender", "Education_Level", "Employment_Status", "Household_Income", "Location_Type", "Engagement_Level", "Employment_Impact"]
label_encoders = {col: LabelEncoder().fit(df[col]) for col in categorical_cols}
for col, le in label_encoders.items():
    df[col] = le.transform(df[col])

# Save preprocessed dataset
df.to_csv("../data/cleaned_data.csv", index=False)