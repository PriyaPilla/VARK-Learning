#classes for each table 
#delete tables before using

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    preference = db.Column(db.String, nullable=False)


