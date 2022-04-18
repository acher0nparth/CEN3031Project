import gui.course_viewer as cv
import tkinter as tk
import random
from database_API import *

class flash_card_viewer(tk.Tk):
    def __init__(self, course):
        super().__init__()

        self.course = course
        # potentially adding statistics?
        self.num_answers = 0
        self.num_correct = 0

        self.title(self.course + " Flashcard Viewer")
        self.geometry("%dx%d+0+0" % (650, 300))

        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.config(menu=self.menubar)

        self.prompt_label = tk.Label(self, text="Prompt ").grid(row=0, column=0)
        self.answer_label = tk.Label(self, text="Answer ").grid(row=0, column=2)

        self.prompt_display = tk.Label(
            self,
            font=("Times New Roman", 15),
            height=10,
            width=25,
            wraplength=250,
            justify=tk.CENTER,
        )
        self.prompt_display.grid(row=0, column=1)
        self.answer_entry = tk.scrolledtext.ScrolledText(
            self, wrap=tk.WORD, font=("Times New Roman", 15), height=10, width=25
        )
        self.answer_entry.grid(row=0, column=3)

        self.exit_button = tk.Button(
            self,
            text="Exit",
            height=1,
            width=15,
            command=self.exit,
        ).grid(row=1, column=1, padx=5, pady=5)

        self.check_answer = tk.Button(
            self,
            text="Check Answer",
            height=1,
            width=15,
            command=self.check_answer,
        ).grid(row=1, column=3, padx=5, pady=5)

        # load in random card from this set

        card = self.get_random_card()
        # self.prompt = "testjklf;djaskfl;jadskl;jkdasl;jfkl;asjfkl;asjfkl;asdjkfl;jasdkfl;jasdklf;jasdkl;fjkalsd;jfklasd;fjklas;jdfkla;sdjfkl;asjdfkl;ajsdkfl;ajsdkfl;ajskdlf;jaskld;fjasdkl;fjaksdl;fjkasdl;fjkasld;fjaskdl;fj"
        # self.correct_answer = "test"
        self.correct_answer = card[1][0:-1]
        self.prompt_display.config(text=card[0][0:-1])

    def exit(self):
        course = self.course
        self.destroy()
        self = cv.course_viewer(course)

    def popup_exit(self):
        self.popup.destroy()
        self.exit()

    def check_answer(self):
        answer = self.answer_entry.get("1.0", "end")
        answer = answer[0:-1]  # sanitizes extraneous newline character
        answer = answer.lower()
        if self.correct_answer == answer:
            self.num_correct += 1
            self.num_answers += 1
            self.popup = tk.Toplevel(self)
            correct_msg = tk.Label(
                self.popup,
                text='That is correct! The answer was "' + self.correct_answer + '".',
            )
            correct_msg.pack(side=tk.TOP)
            next_card_button = tk.Button(
                self.popup, text="Next Card", command=self.next_card
            )
            next_card_button.pack(side=tk.LEFT, padx=10)
            exit_button = tk.Button(self.popup, text="Exit", command=self.popup_exit)
            exit_button.pack(side=tk.RIGHT, padx=10)
        else:
            self.num_answers += 1
            self.popup = tk.Toplevel(self)
            wrong_msg = tk.Label(
                self.popup,
                text='That is incorrect. The correct answer was "'
                + self.correct_answer
                + '".',
            )
            wrong_msg.pack(side=tk.TOP)
            next_card_button = tk.Button(
                self.popup, text="Next Card", command=self.next_card
            )
            next_card_button.pack(side=tk.LEFT, padx=10)
            exit_button = tk.Button(self.popup, text="Exit", command=self.popup_exit)
            exit_button.pack(side=tk.RIGHT, padx=10)

    def next_card(self):
        # index a new card from the set
        self.popup.destroy()
        card = self.get_random_card()
        self.correct_answer = card[1][0:-1]
        self.prompt_display.config(text = card[0][0:-1])
        self.answer_entry.delete("1.0", tk.END)


    def get_random_card(self):
        notecards = db_get_all_course_notecards(self.course)
        return random.choice(notecards)
        # print(card)
        # if notecards:
        #     self.prompt = card[0]
        #     self.correct_answer = card[1]
        #return 

