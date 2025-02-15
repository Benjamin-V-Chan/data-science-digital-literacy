import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset and trained model
df = pd.read_csv("../data/processed_data.csv")
X_test = df.drop(columns=["User_ID", "Overall_Literacy_Score"])
y_test = df["Overall_Literacy_Score"]

model = joblib.load("../outputs/literacy_model.pkl")

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save evaluation results
with open("../outputs/model_performance.txt", "w") as f:
    f.write(f"Mean Absolute Error: {mae}\n")
    f.write(f"R² Score: {r2}\n")
