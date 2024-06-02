from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        checkmark_image = PhotoImage(file="images/true.png")
        self.checkmark = Button(image=checkmark_image, highlightthickness=0,
                                borderwidth=0, command=self.true_pressed)
        self.checkmark.grid(row=2, column=0, padx=2, pady=20)

        cross_image = PhotoImage(file="images/false.png")
        self.cross = Button(image=cross_image, highlightthickness=0,
                            borderwidth=0, command=self.false_pressed)
        self.cross.grid(row=2, column=1)

        self.score_label = Label(text="Score:", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="End of game")
            self.checkmark.config(state="disabled")
            self.cross.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
