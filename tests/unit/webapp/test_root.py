from tests.unit.webapp import client

def test_landing(client):
    #client paramter filled with fixture in conftest.py
    landing = client.get("/")
    html = landing.data.decode()
    # Spot check important text
    assert "WELCOME TO VARK LEARNING!" in html
    assert landing.status_code == 200