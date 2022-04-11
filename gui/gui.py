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

        # add landing screen sometime

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
