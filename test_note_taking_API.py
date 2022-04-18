import sys

sys.path.append("./CEN3031Project")
from note_taking_API import *


def test_db_create_db():
    assert db_create_db() == "sprint1_rev_db"


def test_db_get_note():
    assert db_get_note(title1) == (
        "Note 1 updated",
        "testing updating my first note",
    )

def test_db_get_all_courses():
    assert db_get_all_courses() == ()