import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_data.csv")

# Feature Engineering: Score improvement after training
df["Computer_Knowledge_Improvement"] = df["Post_Training_Basic_Computer_Knowledge_Score"] - df["Basic_Computer_Knowledge_Score"]
df["Internet_Usage_Improvement"] = df["Post_Training_Internet_Usage_Score"] - df["Internet_Usage_Score"]
df["Mobile_Literacy_Improvement"] = df["Post_Training_Mobile_Literacy_Score"] - df["Mobile_Literacy_Score"]

# Save dataset with new features
df.to_csv("../data/processed_data.csv", index=False)