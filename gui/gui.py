import gui.text_editor as te
import gui.note_viewer as nv
import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Flashify")
        self.geometry(
            "%dx%d+0+0"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )

        # landing screen
        # initialize grid
        for i in range(4):
            self.columnconfigure(i, weight=1)

        for i in range(30):
            self.rowconfigure(i, weight=1)

        # add various labels
        title_label = tk.Label(
            self, text="Flashify", font=("Times New Roman", 90, "bold italic")
        )
        title_label.grid(row=2, column=1, columnspan=2)

        title_subheading_label = tk.Label(
            self,
            text="# a markdown-based study tool",
            font=("Courier New", 15, "italic"),
        )
        title_subheading_label.grid(row=3, column=1, columnspan=2, pady=8, padx=5)

        self.course_heading_label = tk.Label(
            self, text="Courses", font=("Courier New", 15, "underline")
        )
        self.course_heading_label.grid(row=6, column=1, columnspan=2, pady=4)


        # list box
        self.frame = tk.Frame(self)
        self.frame.grid(row=7, column=1, columnspan=2, pady=5)
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

        # populate list_box with courses from database:
        # not sure how this works quite yet
        # "for courses in database:
        #     self.list_box.insert(tk.END, course)"


        #list box buttons
        self.create_course_button = tk.Button(
            self,
            text="Create New Course",
            height=1,
            width=15,
            command=self.create_course,
        )
        self.create_course_button.grid(row=8, column=1, pady=5)

        self.view_course_button = tk.Button(
            self, text="View Course", height=1, width=15, command=self.view_course
        )
        self.view_course_button.grid(row=8, column=2, pady=5)
        # add functionality to select course from list

        self.course_body_label = tk.Label(
            self, text="Select from the course list above to", font=("Courier New", 15)
        )
        self.course_body_label.grid(row=15, column=1, columnspan=2)

        self.course_body_label = tk.Label(
            self, text="edit/view materials in that course", font=("Courier New", 15)
        )
        self.course_body_label.grid(row=16, column=1, columnspan=2)



        # adding a little menu on top
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.filemenu.add_command(label="Take Notes", command=self.take_notes)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="View Notes", command=self.view_notes)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.config(menu=self.menubar)


    def take_notes(self):
        self.destroy()
        self = te.text_editor()

    def view_notes(self):
        """add functionality after database api is done"""
        # add pop up window to choose course/subject
        self.destroy()
        self = nv.note_viewer()

    def create_course(self):
        """create course"""
        self.popup = tk.Toplevel(self)
        naming_label = tk.Label(
            self.popup,
            text="Name your course: ",
        )
        naming_label.pack(side=tk.TOP)

        self.course_name = tk.Text(
            self.popup, height=1, width=20, font=("Courier New", 10)
        )
        self.course_name.pack(side=tk.TOP, pady=4)
        # add option to type course name

        create_button = tk.Button(
            self.popup,
            text="Create course",
            command=self.add_to_list,
        )
        # create--> add_to_list(variable)
        create_button.pack(side=tk.LEFT)
        cancel_button = tk.Button(self.popup, text="Cancel", command=self.popup.destroy)
        cancel_button.pack(side=tk.RIGHT)

    def add_to_list(self):
        """add specified course to course list"""

        # add course to database

        # this is necessary to show newly added courses while still in window:
        self.list_box.insert(tk.END, self.course_name.get(1.0, tk.END))

        self.popup.destroy()

    def view_course(self):
        """open specified course viewer"""
        # to get selected item: self.list_box.get(tk.ANCHOR)

        # self.destroy

        # add new 'course' class to view notes and flashcards in tk.Listbox's
        # this should be a new window with that respective course's notes and flashcards
        # will have same menubar functionality

        # buttons to view/edit selected course note/flashcard
