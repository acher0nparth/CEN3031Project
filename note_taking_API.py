from database_API import *


def get_courses():
    courses = []
    temp = db_get_all_courses()
    for course in temp:
        if course not in courses:
            courses.append(course)
    return courses


def db_delete_course(course):
    db_delete_course_notes(course)
    db_delete_course_notecards(course)