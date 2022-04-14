from project1.models import Student


def test_new_student():
    """
    GIVEN a Student model
    WHEN a new Student is created
    THEN check the username, password, and learning_style fields are defined correctly
    """
    student = Student()
    assert student.username != 'FirstName LastName'
    assert student.password != 'Password'
    # assert student.role == 'student'