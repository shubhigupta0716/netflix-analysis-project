import pandas as pd

def test_fill_null_director():

    df = pd.DataFrame({
        "director": [None]
    })

    df["director"] = df["director"].fillna("Unknown")

    assert df["director"][0] == "Unknown"


def test_content_age():

    release_year = 2020

    content_age = 2026 - release_year

    assert content_age == 6


def test_future_release_year():

    release_year = 2030

    content_age = 2026 - release_year

    assert content_age < 0