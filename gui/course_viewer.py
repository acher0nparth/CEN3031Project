import tkinter as tk
import gui.gui as gui
import gui.text_editor as te
import gui.note_viewer as nv
import gc
import gui.flash_card_creator as fcc
import gui.flash_card_viewer as fcv
import gui.flash_card_editor as fce
from database_API import *


class course_viewer(tk.Tk):
    def __init__(self, course):
        super().__init__()

        self.course = course

        self.title(self.course + " Notes and Flashcards")
        self.geometry(
            "%dx%d+600+100"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )

        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="View Courses", command=self.view_course_list)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.config(menu=self.menubar)

        for i in range(4):
            self.columnconfigure(i, weight=1)

        for i in range(30):
            self.rowconfigure(i, weight=1)

        title_label = tk.Label(
            self, text=course, font=("Times New Roman", 40, "bold italic")
        )
        title_label.grid(row=1, column=1, columnspan=2)

        self.notes_heading_label = tk.Label(
            self, text="Notes", font=("Courier New", 15, "underline")
        )
        self.notes_heading_label.grid(row=2, column=1, columnspan=2, pady=0)

        self.frame = tk.Frame(self)
        self.frame.grid(row=3, column=1, columnspan=2, pady=5)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_box = tk.Listbox(
            self.frame,
            width=50,
            yscrollcommand=self.scrollbar.set,
            font=("Courier New", 10),
        )
        self.list_box.pack(expand=True, fill=tk.Y)
        self.scrollbar.config(command=self.list_box.yview)

        # populate notes_list_box with notes from specific course in the database:
        # not sure how this works quite yet
        nts = db_get_all_course_note_titles(self.course)
        if nts:
            for nt in nts:
                self.list_box.insert(tk.END, nt[0])

        self.view_note_button = tk.Button(
            self, text="View Note", height=1, width=15, command=self.view_note
        )
        self.view_note_button.grid(row=4, column=2, pady=5)

        self.edit_note_button = tk.Button(
            self, text="Edit Note", height=1, width=15, command=self.edit_note
        )
        self.edit_note_button.grid(row=5, column=1, pady=5)

        self.create_note_button = tk.Button(
            self, text="Create New Note", height=1, width=15, command=self.create_note
        )
        self.create_note_button.grid(row=4, column=1, pady=5)

        self.delete_note_button = tk.Button(
            self, text="Delete Note", height=1, width=15, command=self.delete_note
        )
        self.delete_note_button.grid(row=5, column=2, pady=5)

        self.flashcard_heading_label = tk.Label(
            self, text="Flashcards", font=("Courier New", 15, "underline")
        )
        self.flashcard_heading_label.grid(row=6, column=1, columnspan=2, pady=0)

        self.flashcard_frame = tk.Frame(self)
        self.flashcard_frame.grid(row=7, column=1, columnspan=2, pady=5)
        self.flashcard_scrollbar = tk.Scrollbar(
            self.flashcard_frame, orient=tk.VERTICAL
        )
        self.flashcard_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.flashcard_list_box = tk.Listbox(
            self.flashcard_frame,
            width=50,
            yscrollcommand=self.flashcard_scrollbar.set,
            font=("Courier New", 10),
        )
        self.flashcard_list_box.pack(expand=True, fill=tk.Y)
        self.scrollbar.config(command=self.flashcard_list_box.yview)

        # populate notes_list_box with notes from specific course in the database:
        # not sure how this works quite yet
        flashcards = db_get_all_course_notecards_ans(self.course)
        if flashcards:
            for card in flashcards:
                self.flashcard_list_box.insert(tk.END, card[0])
        self.create_flashcard_button = tk.Button(
            self,
            text="Create Flashcards",
            height=1,
            width=15,
            command=self.create_flashcards,
        )
        self.create_flashcard_button.grid(row=8, column=1, pady=5)

        self.view_flashcard_button = tk.Button(
            self,
            text="Test On Flashcards",
            height=1,
            width=15,
            command=self.view_flashcards,
        )
        self.view_flashcard_button.grid(row=8, column=2, pady=5)

        self.edit_flashcard_button = tk.Button(
            self,
            text="Edit Flashcards",
            height=1,
            width=15,
            command=self.edit_flashcards,
        )
        self.edit_flashcard_button.grid(row=9, column=1, pady=5)

        self.delete_flashcard_button = tk.Button(
            self,
            text="Delete Flashcard",
            height=1,
            width=15,
            command=self.delete_flashcard,
        )
        self.delete_flashcard_button.grid(row=9, column=2, pady=5)

    def create_flashcards(self):
        course = self.course
        self.destroy()
        self = fcc.flash_card_creator(course)

    def edit_flashcards(self):
        course = self.course
        answer = self.flashcard_list_box.get(tk.ANCHOR)
        if answer == "":
            pass
        else:
            self.destroy()
            self = fce.flash_card_editor(course, answer)

    def view_flashcards(self):
        course = self.course
        self.destroy()
        self = fcv.flash_card_viewer(course)

    def delete_flashcard(self):
        answer = self.flashcard_list_box.get(tk.ANCHOR)
        if answer == "":
            pass
        else:
            db_delete_notecard(self.course, answer)
            self.flashcard_list_box.delete(tk.ANCHOR)

    def view_note(self):
        note = self.list_box.get(tk.ANCHOR)
        if note == "":
            pass
        else:
            self.destroy()
            self = nv.note_viewer(self.course, note)

    def edit_note(self):
        note = self.list_box.get(tk.ANCHOR)
        if note == "":
            pass
        else:
            self.destroy()
            self = te.text_editor(self.course, note)

    def create_note(self):
        """create a note"""
        self.popup = tk.Toplevel(self)
        self.popup.geometry("+700+500")
        naming_label = tk.Label(
            self.popup,
            text="Name your note: ",
        )
        naming_label.pack(side=tk.TOP)

        self.note_name = tk.Text(
            self.popup, height=1, width=20, font=("Courier New", 10)
        )
        self.note_name.pack(side=tk.TOP, pady=4)
        # add option to type note name

        create_button = tk.Button(
            self.popup,
            text="Create note",
            command=lambda: self.add_to_list(self.note_name.get(1.0, tk.END)),
        )
        # create--> add_to_list(variable)
        create_button.pack(side=tk.LEFT)
        cancel_button = tk.Button(self.popup, text="Cancel", command=self.popup.destroy)
        cancel_button.pack(side=tk.RIGHT)

    def delete_note(self):
        note_title = self.list_box.get(tk.ANCHOR)
        if note_title == "":
            pass
        else:
            db_delete_note(note_title, self.course)
            self.list_box.delete(tk.ANCHOR)

    def add_to_list(self, note_title):
        """add specified note to note list"""

        # adds empty note to database
        db_insert(note_title, self.course, "")

        # this is necessary to show newly added notes while still in window:
        self.list_box.insert(tk.END, self.note_name.get(1.0, tk.END))

        self.popup.destroy()

    def view_course_list(self):
        """view courses on main page"""
        self.destroy()
        gc.collect()
        self = gui.Window()
