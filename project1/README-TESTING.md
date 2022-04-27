# VARK-Learning

For tests to run in Visual Studio Code, create a .vscode/settings.json file using testing -> configure tests.

A file will be created. Erase what's in there. 

The contents that work used are below:

{

    "python.testing.pytestArgs": [
        "project1"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true

}

If you do not have Visual Studio Code, just make sure you have pytest imported from the command line before running tests. 
