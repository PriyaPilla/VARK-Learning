from tests.unit.webapp import client

def test_landing(client):
    landing = client.get("/")
    # html = landing.data.decode()
    
    # Check that links to `instructor` and `student` pages exist
    assert '<a href="/instructor/">Instructor</a>'
    assert '<a href="/student/">Student</a>'
    assert landing.status_code == 200
    
# def test_landing_aliases(client):
#     landing = client.get("/")
#     html = landing.data.decode()
    
#     # assert client.get("/index/").data == landing.data
#     assert client.get("/index/").data == html