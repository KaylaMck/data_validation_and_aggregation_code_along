from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class StudentScore(Base):
    __tablename__ = "StudentScores"

    student_id = Column(Integer, primary_key=True)
    score = Column(Integer)

class StudentDepartment(Base):
    __tablename__ = "StudentDepartments"

    student_id = Column(Integer, primary_key=True)
    home_department = Column(String(100))