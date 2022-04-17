#classes for each table 
#delete tables before using

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Book(db.Model):
#     __tablename__ = "books"
#     id = db.Column(db.Integer, primary_key =True)
#     isbn = db.Column(db.String, nullable=False)
#     title = db.Column(db.String, nullable=False)
#     author = db.Column(db.String, nullable=False)
#     publicationyear = db.Column(db.Integer, nullable=False)

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    learning_style = db.Column(db.String, nullable=True)
    notes_timeline = db.Column(db.String, nullable=True)
    notes_cause = db.Column(db.String, nullable=True)
    notes_end = db.Column(db.String, nullable=True)
    notes_events = db.Column(db.String, nullable=True)
    notes_statistics = db.Column(db.String, nullable=True)

class Instructor(db.Model):
    __tablename__ = "instructor"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


