from cgitb import text
from ehp import *
import tkinter as tk
import markdown as md
import gui.gui as gui
import gui.note_viewer as nv
from database_API import *
import markdownify
import gui.course_viewer as cv
from note_taking_API import *
import gui.course_viewer as cv



class text_editor(tk.Tk):
    def __init__(self, course, note):
        super().__init__()

        self.course = course
        self.note_title = note

        self.title("Flashify Text Editor")
        self.geometry(
            "%dx%d+0+0"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )

        # text entry widget
        self.text_entry = tk.scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Times New Roman", 15)
        )
        self.text_entry.pack(fill=tk.BOTH, expand=True)

        # load this specific note from the database using the passed in "note" string
        text = db_get_note(self.note_title, self.course)
        self.insert_text(markdownify.markdownify(text, heading_style="ATX"))

        # adding a little menu on top
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.filemenu.add_command(label="Save", command=self.popup_dialog_exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(
            label="View Current Note", command=self.popup_dialog_view_current
        )
        self.viewmenu.add_command(
            label="View Other Notes", command=self.popup_dialog_view_other
        )
        self.viewmenu.add_command(
            label="View Courses", command=self.popup_dialog_view_course_list
        )
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.config(menu=self.menubar)

    def insert_text(self, text):
        """fills text editor with text instead of it being empty\n
        text needs to be converted from HTML before calling"""
        self.text_entry.insert("1.0", text)

    def view_current_note(self):
        """finish with note taking api"""
        self.popup.destroy()
        self.save_note()

        # saving text as html
        # save html to database, destroy this window, initialize self as note viewer window
        self.destroy()
        self = nv.note_viewer(self.course, self.note_title)

    def view_other_note(self):
        # saving work before moving on
        self.save_note()
        # add pop up window to choose course/subject
        self.popup.destroy()
        self.destroy()
        self = cv.course_viewer(self.course)


    def view_courses(self):
        # saving work before moving on
        self.save_note()
        # add pop up window to choose course/subject
        self.popup.destroy()
        self.destroy()
        self = gui.Window()

    def popup_dialog_exit(self):
        self.popup = tk.Toplevel(self)
        warning = tk.Label(
            self.popup,
            text="You are about to exit the note taker. Please save your work.",
        )
        warning.pack(side=tk.TOP)
        save_exit = tk.Button(self.popup, text="Save and Exit", command=self.save_exit)
        save_exit.pack(side=tk.LEFT)
        continue_work = tk.Button(
            self.popup, text="Continue Working", command=self.popup.destroy
        )
        continue_work.pack(side=tk.RIGHT)

    def popup_dialog_view_current(self):
        self.popup = tk.Toplevel(self)
        warning = tk.Label(
            self.popup,
            text="You are about to exit the note taker. Please save your work.",
        )
        warning.pack(side=tk.TOP)
        save_exit = tk.Button(
            self.popup,
            text="Save and View Current Note",
            command=self.view_current_note,
        )
        save_exit.pack(side=tk.LEFT)
        continue_work = tk.Button(
            self.popup, text="Continue Working", command=self.popup.destroy
        )
        continue_work.pack(side=tk.RIGHT)

    def popup_dialog_view_other(self):
        self.popup = tk.Toplevel(self)
        warning = tk.Label(
            self.popup,
            text="You are about to exit the note taker. Please save your work.",
        )
        warning.pack(side=tk.TOP)
        save_exit = tk.Button(
            self.popup,
            text="Save Current Note and View Other Note",
            command=self.view_other_note,
        )
        save_exit.pack(side=tk.LEFT)
        continue_work = tk.Button(
            self.popup, text="Continue Working", command=self.popup.destroy
        )
        continue_work.pack(side=tk.RIGHT)

    def popup_dialog_view_course_list(self):
        self.popup = tk.Toplevel(self)
        warning = tk.Label(
            self.popup,
            text="You are about to exit the note taker. Please save your work.",
        )
        warning.pack(side=tk.TOP)
        save_exit = tk.Button(
            self.popup,
            text="Save Current Note and View Courses",
            command=self.view_courses,
        )
        save_exit.pack(side=tk.LEFT)
        continue_work = tk.Button(
            self.popup, text="Continue Working", command=self.popup.destroy
        )
        continue_work.pack(side=tk.RIGHT)

    def save_note(self):
        text = self.text_entry.get("1.0", "end")
        html = md.markdown(text)
        db_update_note(self.note_title, self.course, html)

    def save_exit(self):
        self.popup.destroy()
        self.save_note()
        course = self.course
        self = cv.course_viewer(course)
