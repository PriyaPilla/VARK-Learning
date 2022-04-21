# from flask import Flask

# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'hello'
#     return app



'''
TRY BELOW
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# source: https://testdriven.io/blog/flask-pytest/ 

#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()
login = LoginManager()
# login.login_view = "users.login"
login.login_view = "templates.loginstudent"
 #FIXME add instructor


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    login.init_app(app)

    # Flask-Login configuration
    from project1.models import Student
    #FIXME add instructor

    @login.student_loader
    def load_student(id):
        return Student.query.filter(Student.id == int(id)).first()


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    
    # from project.recipes import recipes_blueprint
    from project1.templates import templates_blueprint
    # from project.users import users_blueprint
    # from project1.templates import student?_blueprint

    """SINCE EVERYTHING IN TEMPLATES JUST USE TEMPLATES_BLUEPRINT??? FOR ALL?"""
    app.register_blueprint(templates_blueprint)
    # app.register_blueprint(users_blueprint)
    
