import tkinter as tk
from turtle import clear
import markdown as md
from tkhtmlview import HTMLLabel


def showHTML():
    # remove show button
    show_button.pack_forget()
    text = text_entry.get("1.0", "end")
    html = md.markdown(text)
    global html_area
    global clear_button
    html_area = HTMLLabel(window, html=html)
    html_area.pack()
    clear_button = tk.Button(window, text="Clear HTML", command=clearHTML)
    clear_button.pack(side=tk.BOTTOM)


def clearHTML():
    try:
        html_area.pack_forget()
        clear_button.pack_forget()
        show_button.pack(side=tk.BOTTOM)
    except:
        pass


# base for the GUI window
window = tk.Tk()
# setting what I think is an aesthetically pleasing initial dimension, user can resize from there
w, h = window.winfo_screenwidth() / 2.5, window.winfo_screenheight() - 300
window.geometry("%dx%d+0+0" % (w, h))
window.title("Flashify Text Editor")

# text entry widget
text_entry = tk.scrolledtext.ScrolledText(
    window, wrap=tk.WORD, font=("Times New Roman", 15)
)
text_entry.pack(side=tk.TOP)

# button to show HTML
global show_button
show_button = tk.Button(window, text="Show HTML", command=showHTML)
show_button.pack(side=tk.BOTTOM)

# adding a little menu on top
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
# filemenu.add_command(label="Show HTML", command = showHTML)
# filemenu.add_command(label="Clear HTML", command = clearHTML)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)
window.mainloop()
