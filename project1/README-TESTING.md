# VARK-Learning

Pytest needs to be imported before running these tests.

For tests to run in Visual Studio Code, create a .vscode/settings.json file using testing -> configure tests.

A file will be created. Erase what's in there. 

The contents that work are below:

{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
    }



Sources used for setting up tets:
- https://testdriven.io/blog/flask-pytest/
- https://codethechange.stanford.edu/guides/guide_flask_unit_testing.html
