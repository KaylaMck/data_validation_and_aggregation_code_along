import database_service as ds
import storage_service as ss
import data_cleaning as dc
import local_logging as ll

logger = ll.get_logger()

def main():
    logger.info("Starting data pipeline")
    student_data = ds.get_student_score_info()
    logger.info(f"Retrieved {len(student_data)} rows of student score data")
    student_demographics = ss.get_students()
    logger.info(f"Retrieved {len(student_demographics)} rows of student demographic data")

    students = dc.combine_student_data(student_data, student_demographics)
    logger.info(f"Combined data has {len(students)} rows")
    students_transformed = dc.process_student_data(students)
    logger.info(f"Processed data has {len(students_transformed)} rows")

    ds.push_student_info(students_transformed)
    logger.info("Data pipeline completed successfully")

if __name__ == "__main__":
    main()