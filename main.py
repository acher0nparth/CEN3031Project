import tkinter as tk
import markdown as md
from tkhtmlview import HTMLLabel


class textEditorWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Flashify Text Editor")
        self.geometry(
            "%dx%d+0+0"
            % (self.winfo_screenwidth() / 2.5, self.winfo_screenheight() - 300)
        )

        # text entry widget
        self.text_entry = tk.scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Times New Roman", 15)
        )
        # self.text_entry.grid(row=0,column=0)
        self.text_entry.pack(side=tk.TOP)

        # button to show HTML
        self.show_button = tk.Button(self, text="Show HTML", command=self.showHTML)
        self.show_button.pack(side=tk.BOTTOM)
        self.clear_button = tk.Button(self, text="Clear HTML", command=self.clearHTML)

        # adding a little menu on top
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.config(menu=self.menubar)

    def showHTML(self):
        # remove show button
        self.show_button.pack_forget()
        text = self.text_entry.get("1.0", "end")
        html = md.markdown(text)
        self.html_area = HTMLLabel(self, html=html)

        # pack clear button first to avoid overlap
        self.clear_button.pack(side=tk.BOTTOM)
        self.html_area.pack()

    def clearHTML(self):
        try:
            self.clear_button.pack_forget()
            self.html_area.pack_forget()
            self.show_button.pack(side=tk.BOTTOM)
        except:
            pass


window = textEditorWindow()

window.mainloop()
