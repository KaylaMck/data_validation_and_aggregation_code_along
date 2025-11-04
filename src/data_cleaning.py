import pandas as pd
import local_logging as ll

logger = ll.get_logger()

def combine_student_data(dataframe1, dataframe2):
    joined_data = pd.merge(
        dataframe1,
        dataframe2,
        on="student_id",
        how="inner"
    )
    return joined_data

def _remove_nulls(data):
    null_counts = data.isnull().sum().sum()

    logger.info(f"Removing {null_counts} rows due to null values.")
    return data.dropna()

def _fix_departments(data):
    mixmatches = data[data["home_department"] != data["major"]]
    logger.info(f"Overwriting homedepartment for {len(mixmatches)} rows based on major")

    data.loc[:, "home_department"] = data["major"]
    return data

def process_student_data(data):
    processed_nulls = _remove_nulls(data)
    processed_majors = _fix_departments(processed_nulls)

    return processed_majors