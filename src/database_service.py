from sqlalchemy import create_engine, select
import models as m
import pandas as pd

#MSSQL 
USERNAME = "devadmin"
PASSWORD = "Bootcamp1433!"
HOST = "de-nss-bootcamp.database.windows.net"
PORT = 1433
DATABASE = "de_bootcamp"
DRIVER = "pymssql"

#POSTGRES
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "de"

def get_student_score_info():

    engine = create_engine(
    f"mssql+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    )
    query = (
        select(m.StudentScore.student_id, m.StudentScore.score, m.StudentDepartment.home_department)
        .join(m.StudentDepartment, m.StudentScore.student_id == m.StudentDepartment.student_id)
    )
    results = pd.read_sql(query, engine)
    return results

def push_student_info(student_data):

    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    table_name = "students"
    schema_name = "silver"

    student_data.to_sql(
        table_name,
        engine,
        schema=schema_name,
        if_exists='replace',
        index=False
    )