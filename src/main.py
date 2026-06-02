import logging
from datetime import datetime

from extract import extract_data
from transform import transform_data
from load import load_data


LOG_FILE = "../logs/pipeline.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def run_pipeline():

    try:

        raw_df = extract_data()

        transformed_df = transform_data(raw_df)

        load_data(transformed_df)

        logging.info(
            f"STATUS=SUCCESS | ROWS={len(transformed_df)}"
        )

        print(
            f"SUCCESS: {len(transformed_df)} rows loaded"
        )

    except Exception as e:

        logging.error(
            f"STATUS=FAILED | ERROR={str(e)}"
        )

        print(
            f"FAILED: {str(e)}"
        )


if __name__ == "__main__":
    run_pipeline()