from tests.unit.webapp import client

def test_landing(client):
    #client paramter filled with fixture in conftest.py
    landing = client.get("/")
    html = landing.data.decode()
    # Spot check important text
    assert "WELCOME TO VARK LEARNING!" in html
    assert landing.status_code == 200


#from project1 import create_app
# from tests import create_app

# def test_home_page():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/' page is requested (GET)
#     THEN check that the response is valid
#     """
#     #flask_app = create_app('flask_test.cfg')
#     flask_app = create_app()

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/')
#         #assert response.status_code == 200
#         assert b"WELCOME TO VARK LEARNING!" in response.data