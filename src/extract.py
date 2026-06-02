import requests
import pandas as pd

API_URL = "https://disease.sh/v3/covid-19/countries"


def extract_data():
    """
    Extract data from COVID API
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df

    raise Exception(
        f"Failed to fetch data. Status code: {response.status_code}"
    )