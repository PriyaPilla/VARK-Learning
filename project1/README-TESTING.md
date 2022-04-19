# VARK-Learning

For tests to run in Visual Studio Code, create a .vscode/settings.json file using testing -> configure tests
A file will be created. Erase what's in there. 
The contents I used are below:

{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
