import logging
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def extract_data(file_path=None):
    if file_path is None:
        file_path = PROJECT_ROOT / "data" / "Practice_Table.csv"
    else:
        file_path = Path(file_path)

        if not file_path.is_absolute():
            file_path = PROJECT_ROOT / file_path

    try:
        logging.info("Extracting data from %s", file_path)

        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("CSV file contains no rows")

        logging.info("Extracted %s rows", len(df))
        return df

    except Exception:
        logging.exception("Data extraction failed")
        raise