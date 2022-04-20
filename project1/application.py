
import os, requests, json
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape
from models import *
from sqlalchemy import exc

app = Flask(__name__)
app.secret_key = "any random string"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mfjobdlqdvmjef:6068e27eae9bd7d5ab31e8a03ff6385872ba0f1d7ea5fa07d0e5e1fac58ab814@ec2-54-236-169-55.compute-1.amazonaws.com:5432/ddvh3o0nq9l139"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    if "student_id" in session:
        session.pop("student_id", None)
    if "instructor_id" in session:
        session.pop("instructor_id", None)
    return render_template("index.html")


@app.route("/student", methods=["POST"])
def student():
    return render_template("student.html")


@app.route("/registerstudent", methods=["POST"])
def registerstudent():
    return render_template("registerstudent.html")


@app.route("/registrationcompletestudent", methods=["POST"])
def registrationcompletestudent():
   
    username = request.form.get("username")
    password = request.form.get("password")

    s = Student(username = username, password = password)
    db.session.add(s)
    db.session.commit()

    return render_template("registrationcompletestudent.html")


@app.route("/loginstudent", methods=["POST"])
def loginstudent():
    
    return render_template("loginstudent.html")


@app.route("/quiz", methods=["POST"]) 
def quiz():
    if "student_id" not in session:
        username = request.form.get("username")
        password = request.form.get("password")

        student = Student.query.filter_by(username = username).first()
   
        if student == None:
            return render_template("error.html", message="Username or password does not match.")
        if student.password != password:
            return render_template("error.html", message="Username or password does not match.")
       
        session["student_id"] = student.id

        #if quiz already taken and learning style already exists, redict to learning style page
        if "student_id" in session:
            student_id = int(session["student_id"])
    
        student = Student.query.filter_by(id = student_id).first() 
        
        if student.learning_style == "visual":
            return render_template("visualresult.html", message="Visual selected")
        if student.learning_style == "aural":
            return render_template("auralresult.html", message="Aural selected")
        if student.learning_style == "read/write":
            return render_template("readwriteresult.html", message="Read/Write selected")
        if student.learning_style == "kinesthetic":
            return render_template("kinestheticresult.html", message="Kinesthetic selected")
        
    return render_template("quiz.html")

# create function/url that quiz form submits to. 
# this function could include if statements with matching learning styles to the student input
# where the quiz code should go after the user submits from quiz.html 
#comment for merge issues - something to add
@app.route("/quizresults", methods=["POST"])
def quizresults():

    #gets value of selected radio button
    result = request.form['learning_style']
    
    if result == "Visual":
        #database: add learning style to student table
        if "student_id" in session:
            student_id = int(session["student_id"])
    
        student = Student.query.filter_by(id = student_id).first() 
        student.learning_style = "visual"

        db.session.commit()

        return render_template("visualresult.html", message="Visual selected")

    if result == "Aural":
        #database: add learning style to student table
        if "student_id" in session:
            student_id = int(session["student_id"])
    
        student = Student.query.filter_by(id = student_id).first() 
        student.learning_style = "aural"
        
        db.session.commit()
        return render_template("auralresult.html", message="Aural selected")

    if result == "Read/Write":
        #database: add learning style to student table
        if "student_id" in session:
            student_id = int(session["student_id"])
    
        student = Student.query.filter_by(id = student_id).first() 
        student.learning_style = "read/write"
        
        db.session.commit()
        return render_template("readwriteresult.html", message="Read/Write selected")

    if result == "Kinesthetic":
        #database: add learning style to student table
        if "student_id" in session:
            student_id = int(session["student_id"])
    
        student = Student.query.filter_by(id = student_id).first() 
        student.learning_style = "kinesthetic"
        
        db.session.commit()
        return render_template("kinestheticresult.html", message="Kinesthetic selected")

    #return render_template("quizresults.html")

@app.route("/ww2visual", methods=["POST"]) 
def ww2visual():
    return render_template("ww2visual.html")

@app.route("/ww2visualtopics", methods=["POST"]) 
def ww2visualtopics():
    return render_template("ww2visualtopics.html")

@app.route("/ww2visualcauses", methods=["POST"]) 
def ww2visualcauses():
    return render_template("ww2visualcauses.html")

@app.route("/ww2visualtimeline", methods=["POST"]) 
def ww2visualtimeline():
    return render_template("ww2visualtimeline.html")

@app.route("/ww2visualevents", methods=["POST"]) 
def ww2visualevents():
    return render_template("ww2visualevents.html")

@app.route("/ww2visualend", methods=["POST"]) 
def ww2visualend():
    return render_template("ww2visualend.html")

@app.route("/ww2visualaftermath", methods=["POST"]) 
def ww2visualaftermath():
    return render_template("ww2visualaftermath.html")

@app.route("/ww2aural", methods=["POST"]) 
def ww2aural():
    return render_template("ww2aural.html")

@app.route("/ww2readwritetopics", methods=["POST"]) 
def ww2readwritetopics():
    return render_template("ww2readwritetopics.html")

@app.route("/ww2readwritecauses", methods=["POST"]) 
def ww2readwritecauses():
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()
    
    notes = student.notes_cause

    if notes is None:
        notes = ""
    return render_template("ww2readwritecauses.html", notes=notes)

@app.route("/ww2readwritetimeline", methods=["POST"]) 
def ww2readwritetimeline():

    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()
    
    notes = student.notes_timeline

    if notes is None:
        notes = ""
    return render_template("ww2readwritetimeline.html", notes=notes)

@app.route("/ww2readwriteevents", methods=["POST"]) 
def ww2readwriteevents():
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()
    
    notes = student.notes_events

    if notes is None:
        notes = ""
    return render_template("ww2readwriteevents.html", notes=notes)

@app.route("/ww2readwriteend", methods=["POST"]) 
def ww2readwriteend():
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()
    
    notes = student.notes_end

    if notes is None:
        notes = ""
    return render_template("ww2readwriteend.html", notes=notes)

@app.route("/ww2readwritestatistics", methods=["POST"]) 
def ww2readwritestatistics():
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()
    
    notes = student.notes_statistics

    if notes is None:
        notes = ""
    return render_template("ww2readwritestatistics.html", notes=notes)

@app.route("/notestimeline", methods=["POST"]) 
def notestimeline():
    #take notes value
    notes = request.form.get("notes")

    #put notes in notestimeline column in table
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()

    student.notes_timeline = notes
    db.session.commit()
    
    return render_template("ww2readwritetimeline.html", notes=notes)

@app.route("/notescauses", methods=["POST"]) 
def notescauses():
    #take notes value
    notes = request.form.get("notes")

    #put notes in notestimeline column in table
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()

    student.notes_cause = notes
    db.session.commit()
    
    return render_template("ww2readwritecauses.html", notes=notes)

@app.route("/notesend", methods=["POST"]) 
def notesend():
    #take notes value
    notes = request.form.get("notes")

    #put notes in notestimeline column in table
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()

    student.notes_end = notes
    db.session.commit()
    
    return render_template("ww2readwriteend.html", notes=notes)

@app.route("/notesevents", methods=["POST"]) 
def notesevents():
    #take notes value
    notes = request.form.get("notes")

    #put notes in notestimeline column in table
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()

    student.notes_events = notes
    db.session.commit()
    
    return render_template("ww2readwriteevents.html", notes=notes)

@app.route("/notesstatistics", methods=["POST"]) 
def notesstatistics():
    #take notes value
    notes = request.form.get("notes")

    #put notes in notestimeline column in table
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first()

    student.notes_statistics = notes
    db.session.commit()
    
    return render_template("ww2readwritestatistics.html", notes=notes)
    

@app.route("/home", methods=["POST"]) 
def home():
    if "student_id" in session:
        student_id = int(session["student_id"])
    
    student = Student.query.filter_by(id = student_id).first() 
        
    if student.learning_style == "visual":
        return render_template("visualresult.html", message="Visual selected")
    if student.learning_style == "aural":
        return render_template("auralresult.html", message="Aural selected")
    if student.learning_style == "read/write":
        return render_template("readwriteresult.html", message="Read/Write selected")
    if student.learning_style == "kinesthetic":
        return render_template("kinestheticresult.html", message="Kinesthetic selected")

@app.route("/logoutstudent", methods=["POST", "GET"])
def logoutstudent():
    session.pop("student_id", None)
    return render_template("index.html")


