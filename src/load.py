import sqlite3


DATABASE_PATH = "../database/covid.db"


def load_data(df):

    conn = sqlite3.connect(DATABASE_PATH)

    df.to_sql(
        "covid_data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()