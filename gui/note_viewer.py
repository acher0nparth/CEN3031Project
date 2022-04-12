from tkhtmlview import HTMLLabel
import gui.gui as gui
import gui.text_editor as te
import tkinter as tk

# self.html_area = HTMLLabel(self, html=html)


class note_viewer(tk.Tk):
    def __init__(self):
        # add arguments so it knows what to load from database
        super().__init__()

        self.title("Flashify Note Viewer")
        self.geometry(
            "%dx%d+0+0"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )

        # load this in from database later
        self.html = "ha ha html goes here"

        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Edit Notes", command=self.edit_note)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="View Courses", command=self.view_course_list)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)

        self.config(menu=self.menubar)

    def show_html(self):
        """load html string from mySQL database ->
        display formatted html to user with HTMLLabel"""
        pass

    def edit_note(self):
        """open current note as editable text"""
        self.destroy()
        self = te.text_editor().insert_text(text=self.html)

    def view_course_list(self):
        """view courses on main page"""
        self.destroy()
        self = gui.Window()
