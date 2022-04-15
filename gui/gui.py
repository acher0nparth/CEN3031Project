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

        #landing screen
        #initialize grid
        for i in range(4):
            self.columnconfigure(i, weight=1)

        for i in range(30):
            self.rowconfigure(i, weight=1)

        #add various labels
        title_label = tk.Label(
            self, text="Flashify", font=("Times New Roman", 90, "bold italic")
        )
        title_label.grid(row=2, column=2, sticky=tk.W)

        title_subheading_label = tk.Label(
            self, text="# a markdown-based study tool", font=("Courier New", 15, "italic")
        )
        title_subheading_label.grid(row=3, column=2, sticky=tk.W, pady=8, padx=5)

        note_heading_label = tk.Label(
            self, text="notes", font=("Courier New", 15, "underline")
        )
        note_heading_label.grid(row=6, column=2, sticky=tk.W, pady=4)

        note_body_label1 = tk.Label(
            self,
            text="To take notes, navigate to File >> Take Notes",
            font=("Courier New", 10),
        )
        note_body_label2 = tk.Label(
            self,
            text="To take view notes, navigate to View >> View Notes",
            font=("Courier New", 10),
        )
        note_body_label1.grid(row=7, column=2, sticky=tk.W, pady=2)
        note_body_label2.grid(row=8, column=2, sticky=tk.W, pady=5)

        flashcard_heading_label = tk.Label(
            self, text="flashcards", font=("Courier New", 15, "underline")
        )
        flashcard_heading_label.grid(row=10, column=2, sticky=tk.W, pady=4)
        flashcard_body_label1 = tk.Label(
            self,
            text="To create flashcards, navigate to File >> Create Flashcards",
            font=("Courier New", 10),
        )
        flashcard_body_label2 = tk.Label(
            self,
            text="To take view flashcards, navigate to View >> View Flashcards",
            font=("Courier New", 10),
        )
        flashcard_body_label1.grid(row=11, column=2, sticky=tk.W, pady=2)
        flashcard_body_label2.grid(row=12, column=2, sticky=tk.W, pady=5)

        # experiment with adding images (for landing screen logo (?) and adding pics to notes)
        # maybe use PIL library for adding images

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
