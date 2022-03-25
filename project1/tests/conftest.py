# Pytest fixtures allow writing pieces of code that are reusable across tests. 
# A simple fixture returns a value, but a fixture can also do setup, yield a value, then do teardown.
# Fixtures for the application, test client, and CLI runner are shown below
# https://flask.palletsprojects.com/en/2.0.x/testing/ <-- from this website 
#               but use other link in doc for in depth explanations and how to make the tests your own


# This is just to get us going with testing and can be changed

import pytest
#FIXME
from my_project import create_app

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

#do we need this- Priya?
@pytest.fixture()
def runner(app):
    return app.test_cli_runner()