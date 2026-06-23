import pandas as pd

df = pd.read_csv("data/netflix_titles.csv")

print("Dataset loaded successfully")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

expected_columns = [
    "show_id",
    "type",
    "title",
    "director",
    "cast",
    "country",
    "date_added",
    "release_year",
    "rating",
    "duration",
    "listed_in",
    "description"
]

missing_columns = [
    col for col in expected_columns
    if col not in df.columns
]

if len(missing_columns) == 0:
    print("Schema validation passed")
else:
    print("Missing columns:", missing_columns)