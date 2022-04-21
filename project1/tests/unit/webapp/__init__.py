#MAKES CLIENT AVAILABLE TO ALL TESTS UNDER WEBAPP DIRECTORY

# couldn't find pytest bc no import of pytest before

import pytest
#from project1 import app
# from project1.application import app
from application import app
# from . import app
# from project1.tests import app
# from instance import app

"""Initialize the testing environment

Creates an app for testing that has the configuration flag ``TESTING`` set to
``True``.

"""

@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """

    app.config['TESTING'] = True
    client = app.test_client()

    yield client