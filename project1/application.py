
import os, requests, json
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, escape
from models import *
from sqlalchemy import exc

app = Flask(__name__)
app.secret_key = "any random string"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mfjobdlqdvmjef:6068e27eae9bd7d5ab31e8a03ff6385872ba0f1d7ea5fa07d0e5e1fac58ab814@ec2-54-236-169-55.compute-1.amazonaws.com:5432/ddvh3o0nq9l139"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mfjobdlqdvmjef:6068e27eae9bd7d5ab31e8a03ff6385872ba0f1d7ea5fa07d0e5e1fac58ab814@ec2-54-236-169-55.compute-1.amazonaws.com:5432/ddvh3o0nq9l139"
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    if "student_id" in session:
        session.pop("student_id", None)
    if "instructor_id" in session:
        session.pop("instructor_id", None)
    return render_template("index.html")


@app.route("/instructor", methods=["POST"])
def instructor():
    return render_template("instructor.html")


@app.route("/student", methods=["POST"])
def student():
    return render_template("student.html")


@app.route("/registerstudent", methods=["POST"])
def registerstudent():
    return render_template("registerstudent.html")


@app.route("/registerinstructor", methods=["POST"])
def registerinstructor():
    return render_template("registerinstructor.html")


@app.route("/registrationcompletestudent", methods=["POST"])
def registrationcompletestudent():
   
    username = request.form.get("username")
    password = request.form.get("password")

    s = Student(username = username, password = password)
    db.session.add(s)
    db.session.commit()

    return render_template("registrationcompletestudent.html")


@app.route("/registrationcompleteinstructor", methods=["POST"])
def registrationcompleteinstructor():
   
    username = request.form.get("username")
    password = request.form.get("password")

    i = Instructor(username = username, password = password)
    db.session.add(i)
    db.session.commit()

    return render_template("registrationcompleteinstructor.html")


@app.route("/loginstudent", methods=["POST"])
def loginstudent():
    
    return render_template("loginstudent.html")

@app.route("/logininstructor", methods=["POST"])
def logininstructor():
    
    return render_template("logininstructor.html")


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

@app.route("/instructorpage", methods=["POST"]) 
def instructorpage():
    if "instructor_id" not in session:
        username = request.form.get("username")
        password = request.form.get("password")

        instructor = Instructor.query.filter_by(username = username).first()
   
        if instructor == None:
            return render_template("error.html", message="Username or password does not match.")
        if instructor.password != password:
            return render_template("error.html", message="Username or password does not match.")
       
        session["instructor_id"] = instructor.id

    return render_template("instructorpage.html")


@app.route("/book", methods=["POST"])
def book():
    
    try:
        book_id = int(request.form.get("book_id"))
    except ValueError:
        return render_template("error.html", message="Invalid book.")

    book = Book.query.get(book_id)
    if book is None:
        return render_template("error.html", message="No such book.")

    title = book.title
    author = book.author
    publicationyear = book.publicationyear
    isbn = book.isbn
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "pzaPV2a2PfX3QQmrXqWeQ", "isbns": book.isbn})
    book_dict = res.json()
    book_list = book_dict.get("books")
    rating_count = book_list[0].get("ratings_count")
    average_rating = book_list[0].get("average_rating")

    global the_id
    the_id = book_id
    
    reviews = Review.query.filter_by(book_id = book.id).all()

    return render_template("book.html", average_rating=average_rating, rating_count=rating_count, reviews=reviews, book=book, title=title, author=author, publicationyear=publicationyear, isbn=isbn)


@app.route("/review", methods=["POST"])
def review():
      
    book_id = the_id 
    rating = request.form.get("rating")  
    textreview = request.form.get("review")
    
    if "user_id" in session:
        user_id = int(session["user_id"])
    
    user = User.query.filter_by(id = user_id).first() 
    
    check_user = Review.query.filter_by(user_id = user.id).filter_by(book_id = book_id).first()

    if check_user != None:
        if rating != None:
            if check_user.rating != None:
                return render_template("error.html", message="You have already rated this book.")
        if textreview != None:
            if check_user.textreview != None:
                return render_template("error.html", message="You have already reviwed this book.")

    review = Review(user_id=user_id, book_id=book_id, textreview=textreview, rating=rating, username=user.username)
    db.session.add(review)
    db.session.commit()

    return render_template ("review.html")


@app.route("/logoutstudent", methods=["POST", "GET"])
def logoutstudent():
    session.pop("student_id", None)
    return render_template("index.html")

@app.route("/logoutinstructor", methods=["POST", "GET"])
def logoutinstructor():
    session.pop("instructor_id", None)
    return render_template("index.html")


@app.route("/api/<string:book_isbn>")
def book_api(book_isbn):

    book = Book.query.filter_by(isbn = book_isbn).first()

    if book is None:
        return jsonify({"error": "Invalid book_isbn"}), 404
    
    reviews = Review.query.filter_by(book_id = book.id)

    review_count = 0

    for review in reviews:
        if review.textreview != None:
            review_count = review_count + 1

    avg_score = float(0)
    sum = float(0)
    rating_count = float(0)

    for review in reviews:
        if review.rating != None:
            sum = sum + review.rating
            rating_count = rating_count + 1
    
    avg_score = sum/rating_count

    return jsonify({
        "title": book.title,
        "author": book.author,
        "year": book.publicationyear,
        "isbn": book.isbn,
        "review_count": review_count,
        "average_score": avg_score
    })




