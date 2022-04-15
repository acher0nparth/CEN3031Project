from tkhtmlview import HTMLLabel
import gui.text_editor as te
import tkinter as tk
from note_taking_API import *
import copy



class note_viewer(tk.Tk):
    def __init__(self):
        # add arguments so it knows what to load from database
        super().__init__()

        self.title("Flashify Note Viewer")
        self.geometry(
            "%dx%d+0+0"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )
        self.html_area = HTMLLabel(self, html='')

        # load this in from database later        
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Edit Notes", command=self.edit_note)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        
        titles = self.display_titles()
        self.notemenu = tk.Menu(self.menubar, tearoff=0)
        for title in titles:
            self.notemenu.add_command(label=title[0], command=lambda title=title: self.show_html(title[0]))

        self.menubar.add_cascade(label="Notes", menu=self.notemenu)

        self.config(menu=self.menubar)

    def display_titles(self):
        titles = db_get_all_titles(connection)
        return titles

        
    def note_to_display(self, title):
        self.show_html(self.label)

    def show_html(self, title):
        """load html string from mySQL database ->
        display formatted html to user with HTMLLabel"""
        
        temp = db_get_note_t(connection, title)
        self.html = temp[0]
    
        new_area = HTMLLabel(self, html=self.html)
        if(self.html_area.winfo_ismapped()):
            self.html_area.pack_forget()
        self.html_area = new_area
        self.html_area.pack(fill=tk.BOTH, expand=True)

    def edit_note(self):
        """open current note as editable text"""
        self.destroy()
        self = te.text_editor().insert_text(text=self.html)
