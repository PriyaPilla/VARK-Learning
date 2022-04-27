import pytest
from models import Student
from models import Instructor

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope='module')
def new_student():
    student = Student()
    student.id = 1
    student.username = 'Us3rn@m3'
    student.password = 'P@$$w0rd'
    student.learning_style = 'Visual'
    return student

@pytest.fixture(scope='module')
def new_student_2():
    student_2 = Student()
    student_2.id = 2
    student_2.username = 'Us3rn@m3Us3rn@m3'
    student_2.password = 'P@$$w0rdP@$$w0rd'
    student_2.learning_style = 'Kinesthetic'
    student_2.notes_timeline = 'timeline'
    student_2.notes_cause = 'cause'
    student_2.notes_end = 'end'
    student_2.notes_events = 'events'
    student_2.notes_statistics = 'stats'
    return student_2

@pytest.fixture(scope='module')
def new_instructor():
    instructor = Instructor()
    instructor.id = 2
    instructor.username = 'Us3rn@m33'
    instructor.password = 'P@$$w0rdd'
    return instructor