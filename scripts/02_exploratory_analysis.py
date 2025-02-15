import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_data.csv")

# Summary statistics
summary = df.describe()
summary.to_csv("../outputs/data_summary.csv")

# Visualizations
plt.figure(figsize=(10, 6))
sns.histplot(df["Overall_Literacy_Score"], bins=20, kde=True)
plt.title("Distribution of Overall Literacy Score")
plt.savefig("../outputs/literacy_score_distribution.png")

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("../outputs/correlation_heatmap.png")
