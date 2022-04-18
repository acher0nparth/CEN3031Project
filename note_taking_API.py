from database_API import *

def get_courses():
    courses = []
    temp = db_get_all_courses()
    for course in temp:
        if course not in courses:
            courses.append(course)
    return courses
