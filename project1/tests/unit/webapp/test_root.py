from tests.unit.webapp import client
# from project1.tests import app

def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()
    
    assert "WELCOME TO VARK LEARNING!" in html
    # Check that links to `instructor` and `student` pages exist
    assert '<a href="/instructor/">Instructor</a>'
    assert '<a href="/student/">Student</a>'
    assert landing.status_code == 200
    
# def test_landing_aliases(client):
#     landing = client.get("/")
#     html = landing.data.decode()
    
#     # assert client.get("/index/").data == landing.data
#     assert client.get("/index/").data == html