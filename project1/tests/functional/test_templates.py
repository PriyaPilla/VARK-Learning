from tests.unit.webapp import client
# from tests import create_app

def test_landing(client):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/' page is requested (GET)
     THEN check that the response is valid
    """
    
    #client paramter filled with fixture in conftest.py
    landing = client.get("/")
    html = landing.data.decode()
    # Spot check important text
    assert "WELCOME TO VARK LEARNING!" in html
    assert landing.status_code == 200
    
# def test_landing_aliases(client):
#     landing = client.get("/")
#     assert b'client.get("/index/").data' == b'landing.data'

def test_student_landing(client):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/' page is requested (GET)
     THEN check that the response is valid
    """
    
    #client paramter filled with fixture in conftest.py
    landing = client.get("/loginstudent")
    # html = landing.data.decode()
    
    # Spot check important text
    # assert "WELCOME TO VARK LEARNING!" in html
    # assert landing.status_code == 200
    
    # Check that links to `login` and `register` pages exist
    assert '<a href="/loginstudent/">Login as Student</a>'
    assert '<a href="/registerstudent/">Sign up as Student</a>'

