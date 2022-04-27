from tests.unit.webapp import client

def test_landing(client):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/' page is requested (GET)
     THEN check that the response is valid
    """
    landing = client.get("/")
    html = landing.data.decode()
    
    # Spot check important text
    assert "WELCOME TO VARK LEARNING!" in html
    assert landing.status_code == 200

def test_student_landing(client):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/loginstudent' page is requested (GET)
     THEN check that the response is valid
    """
    landing = client.get("/loginstudent")
    
    # Check that links to `login` and `register` pages exist
    assert '<a href="/loginstudent/">Login as Student</a>'
    assert '<a href="/registerstudent/">Sign up as Student</a>'