import pandas as pd


def transform_data(df):
    """
    Clean and transform data
    """

    # Handle null values
    df = df.fillna(0)

    # Normalize country names
    df["country"] = df["country"].str.upper()

    # Derived Column 1
    df["active_cases"] = (
        df["cases"]
        - df["recovered"]
        - df["deaths"]
    )

    # Derived Column 2
    df["death_rate"] = (
        df["deaths"] / df["cases"]
    ) * 100

    selected_columns = [
        "country",
        "cases",
        "deaths",
        "recovered",
        "active_cases",
        "death_rate"
    ]

    return df[selected_columns]