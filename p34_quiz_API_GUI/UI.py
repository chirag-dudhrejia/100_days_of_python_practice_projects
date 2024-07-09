from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH = 400
HEIGHT = 700


class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.root = Tk()
        self.root.title("Quiz App")
        X = (self.root.winfo_screenwidth() // 2) - (WIDTH // 2)
        Y = (self.root.winfo_screenheight() // 2) - (HEIGHT // 2)
        self.root.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")
        self. root.config(pady=20, padx=30, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Courier", 18), bg=THEME_COLOR, fg="white", anchor="e")
        self.score_label.grid(column=1, row=0, pady=(10, 20), columnspan=2)

        self.canvas = Canvas(width=340, height=350)
        self.quiz_question = self.canvas.create_text(170, 175, text="Question will be shown here", width=300,
                                           font=("Courier", 18))
        self.canvas.grid(column=0, row=1, columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, relief="groove",
                             command=lambda:self.get_checked("true"))
        self.true_button.grid(column=0, row=2, pady=(30, 0))

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, relief="groove",
                              command=lambda:self.get_checked("false"))
        self.false_button.grid(column=1, row=2, pady=(30, 0))

        self.show_next_question()

        self.root.mainloop()

    def show_next_question(self):
        if self.quiz.has_next_question():
            self.canvas.config(bg="white")
            q_text = self.quiz.get_next_question()
            self.canvas.itemconfig(self.quiz_question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.finish_quiz()

    def get_checked(self, bool_answer: str):
        result = self.quiz.check_answer(bool_answer)

        if result:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.canvas.update()
        self.root.after(ms=0, func=self.show_next_question())

    def finish_quiz(self):
        self.canvas.itemconfig(self.quiz_question, text=f"Thank you for taking quiz.\n\n"
                                                        f"Final Score : {self.quiz.score}")
        self.true_button.grid_forget()
        self.false_button.grid_forget()
        self.score_label.grid_forget()
        self.play_again_button = Button(text="Take Quiz", font=("Courier", 16), width=15, command=self.new_quiz)
        self.play_again_button.grid(column=0, row=2, columnspan=2, pady=(20, 0))

    def new_quiz(self):
        self.play_again_button.grid_forget()
        self.score_label.grid(column=1, row=0, pady=(10, 20), columnspan=2)
        self.true_button.grid(column=0, row=2, pady=(30, 0))
        self.false_button.grid(column=1, row=2, pady=(30, 0))