from tests.unit.webapp import client

def test_landing(client):
    landing = client.get("/")
    
    # Check that links to `instructor` and `student` pages exist
    assert '<a href="/instructor/">Instructor</a>'
    assert '<a href="/student/">Student</a>'
    assert landing.status_code == 200