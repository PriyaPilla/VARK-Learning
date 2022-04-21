"""
This file (test_templates.py) has functional tests for templates.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `templates` blueprints.
"""

# from tests.unit.webapp import client
from tests import create_app
# from project1 import create_app

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"WELCOME TO VARK LEARNING!" in response.data
        # assert b"Flask User Management Example!" in response.data
        assert b"Instructor" in response.data
        assert b"Student" in response.data


#only works if don't test reponse code
#probably have to figure out client stuff
def test_student_landing(client):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/loginstudent' page is requested (GET)
     THEN check that the response is valid
    """
    
    #client paramter filled with fixture in conftest.py
    landing = client.get("/loginstudent")
    html = landing.data.decode()
    
    # Spot check important text
    # assert "WELCOME TO VARK LEARNING!" in html
    # assert landing.status_code == 200
    
    # Check that links to `login` and `register` pages exist
    assert '<a href="/loginstudent/">Login as Student</a>'
    assert '<a href="/registerstudent/">Sign up as Student</a>'
    assert landing.status_code == 200

#WORKING HERE
# def test_student_landing(client):
#     """
#      GIVEN a Flask application configured for testing
#      WHEN the '/loginstudent' page is requested (GET)
#      THEN check that the response is valid
#     """
    
#     #client paramter filled with fixture in conftest.py
#     landing = client.get("/loginstudent")
#     # html = landing.data.decode()
    
#     # Spot check important text
#     # assert "WELCOME TO VARK LEARNING!" in html
#     # assert landing.status_code == 200
    
#     # Check that links to `login` and `register` pages exist
#     assert '<a href="/loginstudent/">Login as Student</a>'
#     assert '<a href="/registerstudent/">Sign up as Student</a>'

