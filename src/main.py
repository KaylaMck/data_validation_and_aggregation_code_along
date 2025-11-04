import database_service as ds
import storage_service as ss
import data_cleaning as dc

def main():
    student_data = ds.get_student_score_info()
    student_demographics = ss.get_students()

    students = dc.combine_student_data(student_data, student_demographics)
    students_transformed = dc.process_student_data(students)

    ds.push_student_info(students_transformed)
    
if __name__ == "__main__":
    main()