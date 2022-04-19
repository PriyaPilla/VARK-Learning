from models import Student
from models import Instructor

def test_new_blank_student():
    """
    GIVEN a Student model
    WHEN a new Student is created
    THEN check the username, password, and learning_style fields are defined correctly
    """
    blank_student = Student()
    assert blank_student.username != 'FirstName LastName'
    assert blank_student.password != 'Password'
    assert blank_student.learning_style != 'Visual'
    
def test_new_student():
    """
    GIVEN a Student model
    WHEN a new Student is created
    THEN check the username, password, and learning_style fields are defined correctly
    """
    student = Student()
    student.username = 'FirstName LastName'
    student.password = 'Password'
    student.learning_style = 'Aural'
    
    assert student.username == 'FirstName LastName'
    assert student.password == 'Password'
    assert student.learning_style == 'Aural'

def test_new_student_with_fixture(new_student):
     """
    GIVEN a Student model
    WHEN a new Student is created
    THEN check the id, username, password, and learning_style fields are defined correctly
    """
     assert new_student.id == 1
     assert new_student.username == 'Us3rn@m3'
     assert new_student.password == 'P@$$w0rd'
     assert new_student.learning_style == 'Visual'
     
def test_new_student_with_fixture_2(new_student_2):
     """
    GIVEN a Student model
    WHEN a new Student is created
    THEN check the id, username, password, 
         learning_style, all notes fields are defined correctly
         AND
         tablename is defined correctly
    """
    
     assert new_student_2.id == 2
     assert new_student_2.username == 'Us3rn@m3Us3rn@m3'
     assert new_student_2.password == 'P@$$w0rdP@$$w0rd'
     assert new_student_2.learning_style == 'Kinesthetic'
     assert new_student_2.notes_timeline == 'timeline'
     assert new_student_2.notes_cause == 'cause'
     assert new_student_2.notes_end == 'end'
     assert new_student_2.notes_events == 'events'
     assert new_student_2.notes_statistics == 'stats'
     assert new_student_2.__tablename__ == 'student'
     
def test_new_blank_instructor():
    """
    GIVEN a Instructor model
    WHEN a new Instructor is created
    THEN check the username and password fields are defined correctly
    """
    blank_instructor = Instructor()
    assert blank_instructor.username != 'FirstName LastName'
    assert blank_instructor.password != 'Password'
    
def test_new_instructor():
    """
    GIVEN an Instructor model
    WHEN a new Instructor is created
    THEN check the id, username, password, and tablename fields are defined correctly
    """
    
    instructor = Instructor()
    instructor.id = 4
    instructor.username = 'Instructor LastName'
    instructor.password = 'Instructor1'
    
    assert instructor.id == 4
    assert instructor.username == 'Instructor LastName'
    assert instructor.password == 'Instructor1'
    assert instructor.__tablename__ == 'instructor'
    
def test_new_instructor_with_fixture(new_instructor):
     """
    GIVEN a Instructor model
    WHEN a new Instructor is created
    THEN check the id, username, password, and tablename fields are defined correctly
    """
     assert new_instructor.id == 2
     assert new_instructor.username == 'Us3rn@m33'
     assert new_instructor.password == 'P@$$w0rdd'
     assert new_instructor.__tablename__ == 'instructor'
    

    

    