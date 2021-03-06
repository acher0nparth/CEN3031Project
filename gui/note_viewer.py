from tkhtmlview import HTMLLabel
import gui.gui as gui
import gui.text_editor as te
import gui.course_viewer as cv
import tkinter as tk
from database_API import *
import copy


class note_viewer(tk.Tk):
    def __init__(self, course, note):
        # add arguments so it knows what to load from database
        super().__init__()

        self.course = course
        self.note_title = note

        self.title("Flashify Note Viewer")
        self.geometry(
            "%dx%d+600+100"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )
        self.html_area = HTMLLabel(self, html="")

        # load this specific note from the database using the passed in "note" string in html form
        self.show_html()

        self.html = ""

        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Edit Notes", command=self.edit_note)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(
            label="View Other Courses", command=self.view_course_list
        )
        self.viewmenu.add_command(
            label="Return to Course Home", command=self.return_to_course
        )
        self.menubar.add_cascade(label="View", menu=self.viewmenu)

        self.config(menu=self.menubar)

    def show_html(self):
        """load html string from mySQL database ->
        display formatted html to user with HTMLLabel"""

        temp = db_get_note(self.note_title, self.course)
        self.html = temp

        new_area = HTMLLabel(self, html=self.html)
        if self.html_area.winfo_ismapped():
            self.html_area.pack_forget()
        self.html_area = new_area
        self.html_area.pack(fill=tk.BOTH, expand=True)

    def edit_note(self):
        """open current note as editable text"""
        # removed "insert_text" function
        self.destroy()
        self = te.text_editor(self.course, self.note_title)

    def view_course_list(self):
        """view courses on main page"""
        self.destroy()
        self = gui.Window()

    def return_to_course(self):
        """returns user to course page"""
        course = self.course
        self.destroy()
        self = cv.course_viewer(course)
