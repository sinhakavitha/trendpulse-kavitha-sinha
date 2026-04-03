import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/cleaned_trends.csv")

# Plot 1: Category count
df["category"].value_counts().plot(kind="bar")
plt.title("Posts per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# Plot 2: Average score
df.groupby("category")["score"].mean().plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Score")
plt.show()