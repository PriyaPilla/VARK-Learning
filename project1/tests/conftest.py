#create pytest fixtures here

import pytest
from models import Student
from models import Instructor
#from functional.test_recipes import create_app
#from test_recipes.py import create_app



'''
Fixtures should be created in tests/conftest.py.

Fixtures are defined as functions (that  have a descriptive names for their purpose).

Multiple fixtures can be run to set the initial state for a test function. 
    In fact, fixtures can even call other fixtures! 
    So, you can compose them together to create the required state.

Fixtures can be run with different scopes:
    function - run once per test function (default scope)
    class - run once per test class
    module - run once per module (e.g., a test file)
    session - run once per session
For example, if you have a fixture with module scope, 
    that fixture will run once (and only once) before the test functions in the module run.
    
Source: https://testdriven.io/blog/flask-pytest/

'''

@pytest.fixture()
def app():
     app = create_app()
     app.config.update({
         "TESTING": True,
     })

    # other setup can go here

     yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

#do we need this?
@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# unit test setup below

@pytest.fixture(scope='module')
def new_student():
    student = Student()
    student.id = 1
    student.username = 'Us3rn@m3'
    student.password = 'P@$$w0rd'
    student.learning_style = 'Visual'
    return student

@pytest.fixture(scope='module')
def new_instructor():
    instructor = Instructor()
    instructor.id = 2
    instructor.username = 'Us3rn@m33'
    instructor.password = 'P@$$w0rdd'
    return instructor

# functional test setup below

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!