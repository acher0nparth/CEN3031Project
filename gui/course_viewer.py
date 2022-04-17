import tkinter as tk
import gui.gui as gui
import gui.text_editor as te
import gui.note_viewer as nv


class course_viewer(tk.Tk):
    def __init__(self, course):
        super().__init__()

        self.course = course

        self.title(course + " Notes and Flashcards")
        self.geometry(
            "%dx%d+0+0"
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

        # populate list_box with notes from specific course in the database:
        # not sure how this works quite yet
        # "for notes in database:
        #     self.list_box.insert(tk.END, note)"

        self.view_note_button = tk.Button(
            self, text="View note", height=1, width=15, command=self.view_note
        )
        self.view_note_button.grid(row=4, column=1, pady=5)

        self.edit_note_button = tk.Button(
            self, text="Edit note", height=1, width=15, command=self.edit_note
        )
        self.edit_note_button.grid(row=4, column=2, pady=5)

        self.create_note_button = tk.Button(
            self, text="Create new note", height=1, width=15, command=self.create_note
        )
        self.create_note_button.grid(row=5, column=1, pady=5)

        self.delete_note_button = tk.Button(
            self, text="Delete note", height=1, width=15, command=self.delete_note
        )
        self.delete_note_button.grid(row=5, column=2, pady=5)

    def view_note(self):
        # will create blank page if no note is selected
        note = self.list_box.get(tk.ANCHOR)
        self.destroy()
        self = nv.note_viewer(self.course, note)

    def edit_note(self):
        # will create blank page if no note is selected
        note = self.list_box.get(tk.ANCHOR)
        self.destroy()
        self = te.text_editor(self.course, note)

    def create_note(self):
        """create a note"""
        self.popup = tk.Toplevel(self)
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
            command=self.add_to_list,
        )
        # create--> add_to_list(variable)
        create_button.pack(side=tk.LEFT)
        cancel_button = tk.Button(self.popup, text="Cancel", command=self.popup.destroy)
        cancel_button.pack(side=tk.RIGHT)

    def delete_note(self):
        self.list_box.delete(tk.ANCHOR)

    def add_to_list(self):
        """add specified note to note list"""

        # adds empty note to database

        # this is necessary to show newly added notes while still in window:
        self.list_box.insert(tk.END, self.note_name.get(1.0, tk.END))

        self.popup.destroy()

    def view_course_list(self):
        """view courses on main page"""
        self.destroy()
        self = gui.Window()
