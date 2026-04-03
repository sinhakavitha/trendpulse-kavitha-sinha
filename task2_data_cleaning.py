import pandas as pd
import os
import glob

# Step 1: Find JSON file inside data folder
files = glob.glob("data/*.json")

if not files:
    print("No JSON file found. Run Task 1 first.")
    exit()

latest_file = files[0]

# Step 2: Load JSON
df = pd.read_json(latest_file)

print("Original Data:")
print(df.head())

# Step 3: Cleaning

# Remove duplicates
df = df.drop_duplicates(subset=["post_id"])

# Remove missing titles
df = df.dropna(subset=["title"])

# Convert score & comments to integer
df["score"] = df["score"].fillna(0).astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)

# Optional: Clean text (lowercase titles)
df["title"] = df["title"].str.strip()

# Step 4: Save CSV
if not os.path.exists("data"):
    os.makedirs("data")

csv_file = "data/cleaned_trends.csv"
df.to_csv(csv_file, index=False)

print(f"Cleaned data saved to {csv_file}")