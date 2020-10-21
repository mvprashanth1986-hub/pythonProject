from datetime import datetime
from Old.Important import Student,get_topper
import pytest

@pytest.fixture
def dummy_student():
    return Student("James",datetime(2000,1,1), "QA", 20)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name,credits):
        return Student(name,datetime(2000,1,1),"QA",credits)
    return _make_dummy_student

# def test_student_get_age(dummy_student):
#     dummy_student_age = (datetime.now() - dummy_student.dob).days
#     assert dummy_student.get_age() == dummy_student_age

def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("James",21),
        make_dummy_student("Bond",22),
        make_dummy_student("Stalin",25)
    ]
    topper = get_topper(students)

    assert topper == students[2]