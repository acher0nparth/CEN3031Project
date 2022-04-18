import gui.course_viewer as cv
import tkinter as tk


class flash_card_editor(tk.Tk):
    def __init__(self, course):
        super().__init__()

        self.course = course

        self.title(self.course + " Flashcard Editor")
        self.geometry("%dx%d+0+0" % (650, 300))

        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.config(menu=self.menubar)

        self.prompt_label = tk.Label(self, text="Prompt ").grid(row=0, column=0)
        self.answer_label = tk.Label(self, text="Answer ").grid(row=0, column=2)

        self.prompt_entry = tk.scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Times New Roman", 15), height=10, width=25
        )
        self.prompt_entry.grid(row=0, column=1)
        self.answer_entry = tk.scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Times New Roman", 15), height=10, width=25
        )
        self.answer_entry.grid(row=0, column=3)

        self.exit_button = tk.Button(
            self, text="Exit without Saving", height=1, width=20, command=self.exit
        )
        self.exit_button.grid(row=1, column=1, padx=5, pady=5)

        self.save_and_exit_button = tk.Button(
            self,
            text="Save and Exit",
            height=1,
            width=20,
            command=self.save_and_exit,
        )
        self.save_and_exit_button.grid(row=1, column=3, padx=5, pady=5)

        # index the specific notecard
        prompt = "edit this"
        answer = "edit this but different"
        self.prompt_entry.insert("1.0", prompt)
        self.answer_entry.insert("1.0", answer)

    def save_flash_card(self):
        """save flash card to database, overwriting previous entry"""
        pass

    def save_and_exit(self):
        """save flashcard and return to course viewer"""
        self.save_flash_card()
        course = self.course
        self.destroy()
        self = cv.course_viewer(course)

    def exit(self):
        course = self.course
        self.destroy()
        self = cv.course_viewer(course)
