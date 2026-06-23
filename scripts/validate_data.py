import pandas as pd

df = pd.read_csv("data/netflix_titles.csv")

# Basic expectations

assert df["show_id"].isnull().sum() == 0, "show_id contains null values"

assert df["title"].isnull().sum() == 0, "title contains null values"

assert (
    df["release_year"].between(1900, 2025).all()
), "release_year contains invalid values"

assert (
    df["type"].isin(["Movie", "TV Show"]).all()
), "type contains unexpected values"

print("All validation checks passed!")