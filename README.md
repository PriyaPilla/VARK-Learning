# VARK-Learning
Project1  
- Templates – HTML files for all the front end  
- Tests – unit and functional tests for the application  
- Application.py – Python file that has all the logical functionality for the application to work  
- Create.py – creates tables from models.py  
- Create.sql – SQL file created by create.py that has the creation for student table  
- Models.py – python classes for each table using SQLAlchemy  
- Requirements.txt – list of required modules  

Deployment and Installation Instructions.docx  
README.md  
Users and Administrator Manual.docx  



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
