import logging

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_postgres


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)


def run_pipeline():
    try:
        logging.info("===== PIPELINE STARTED =====")

        df = extract_data()
        clean_df = transform_data(df)

        load_to_postgres(clean_df, "practice_table")

        logging.info("===== PIPELINE COMPLETED SUCCESSFULLY =====")

    except Exception:
        logging.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run_pipeline()