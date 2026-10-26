# Batch-etl-pipeline

Batch ETL Pipeline Using Python and PostgreSQL

Project Overview

This project is a simple batch ETL pipeline built with Python. It extracts data from a CSV file, cleans and validates the data, and loads the results into a PostgreSQL database.

The purpose of this project is to practise the basic concepts of data engineering and build a repeatable data processing workflow.

Technologies Used

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- python-dotenv
- Logging

How It Works

The pipeline follows three main steps:

1. Extract: Reads data from "Practice_Table.csv" using Pandas.
2. Transform: Cleans names, converts age values to numeric data, removes rows with missing required values, and checks for negative ages.
3. Load: Loads the cleaned data into a PostgreSQL table named "practice_table".

The pipeline also uses logging to track progress and record errors.

Installation

Install the required dependencies:

pip install -r requirements.txt

Make sure Python and PostgreSQL are installed and available.

Database Configuration

Create a PostgreSQL database for the project.

Create a ".env" file in the project root directory using ".env.example" as a guide.

Add your database credentials:

DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name

Replace the example values with your actual PostgreSQL credentials.

Security: Do not upload your ".env" file or database passwords to GitHub.

Running the Pipeline

From the project root directory, run:

python main.py

The pipeline will extract the CSV data, transform it, and load the cleaned records into PostgreSQL.

Execution progress and errors are recorded in "pipeline.log".

Data Quality Checks

The transformation step performs the following checks:

- Confirms that the required columns exist.
- Removes leading and trailing spaces from names.
- Converts empty names into missing values.
- Converts age values to numeric data.
- Removes rows with missing required fields.
- Rejects negative ages.
- Checks that valid rows remain after cleaning.

Expected Result

After a successful run, the cleaned data should be available in the PostgreSQL table "practice_table".

The pipeline logs indicate whether extraction, transformation, and loading completed successfully.

Limitations

- The pipeline currently reads data from a single CSV file.
- The required database columns are limited to "first_name", "last_name", and "age".
- The loading process replaces the destination table each time the pipeline runs.
- Automated tests and scheduled execution have not yet been implemented.

What I Learned

Through this project, I practised:

- Building a basic ETL workflow in Python.
- Cleaning and validating data using Pandas.
- Connecting Python applications to PostgreSQL.
- Managing database credentials using environment variables.
- Using logging and exception handling to monitor a pipeline.

Future Improvements

- Add automated tests.
- Support multiple input files.
- Add more data quality checks.
- Implement incremental loading.
- Schedule automatic pipeline execution.