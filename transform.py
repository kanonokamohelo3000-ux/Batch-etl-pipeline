import logging

import pandas as pd


def transform_data(df):
    try:
        logging.info("Starting data transformation")

        required_columns = ["first_name", "last_name", "age"]
        missing_columns = [
            column for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        initial_count = len(df)

        # Work on a copy so the original DataFrame is unchanged.
        df = df[required_columns].copy()

        # Clean names and treat empty strings as missing values.
        for column in ["first_name", "last_name"]:
            df[column] = df[column].astype("string").str.strip()
            df[column] = df[column].replace("", pd.NA)

        # Convert age to a numeric type; invalid values raise an error.
        df["age"] = pd.to_numeric(df["age"], errors="raise")

        # Remove rows missing required fields.
        df = df.dropna(subset=required_columns)

        if (df["age"] < 0).any():
            raise ValueError(
                "Negative age found. Data quality check failed."
            )

        # Standardise names.
        df["first_name"] = df["first_name"].str.upper()
        df["last_name"] = df["last_name"].str.upper()

        if df.empty:
            raise ValueError(
                "No valid rows remain after cleaning"
            )

        logging.info(
            "Transformation complete: %s -> %s rows",
            initial_count,
            len(df)
        )

        return df

    except Exception:
        logging.exception("Data transformation failed")
        raise