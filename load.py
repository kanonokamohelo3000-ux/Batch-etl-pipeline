import logging

from sqlalchemy import create_engine

from etl.config import DB_URL


def load_to_postgres(df, table_name):
    engine = create_engine(DB_URL)

    try:
        logging.info(
            "Loading %s rows into table '%s'",
            len(df),
            table_name
        )

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        logging.info("Successfully loaded table '%s'", table_name)

    except Exception:
        logging.exception("Data loading failed")
        raise

    finally:
        engine.dispose()