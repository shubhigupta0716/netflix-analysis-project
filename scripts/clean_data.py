import pandas as pd

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Standardize text columns
text_columns = [
    "title",
    "director",
    "cast",
    "country"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df["content_age"] = 2026 - df["release_year"]

print("Added content_age column")

df = df.sort_values(
    by="release_year",
    ascending=False
)

print("Data sorted by release year")

# Save cleaned dataset
df.to_csv(
    "data/clean_output.csv",
    index=False
)

print("clean_output.csv created")
