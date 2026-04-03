import pandas as pd

# Load CSV
df = pd.read_csv("data/cleaned_trends.csv")

print("Total posts:", len(df))

# Posts per category
print("\nPosts per category:")
print(df["category"].value_counts())

# Average score per category
print("\nAverage score per category:")
print(df.groupby("category")["score"].mean())

# Top 5 posts by score
print("\nTop 5 posts:")
print(df.sort_values(by="score", ascending=False).head(5)[["title", "score"]])