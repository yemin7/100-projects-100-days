from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Trivia")
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score_label = Label(text="Score: ", font=(FONT_NAME, 14, "normal"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="Test question", fill="black",
                                                font=(FONT_NAME, 20,
                                                      "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Button
        true_image = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.true_clicked)
        self.button_true.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.false_clicked)
        self.button_false.grid(row=2, column=1)

        # while self.quiz.has_next_question():
        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        if self.quiz.has_next_question():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.correct}")
            q_text = self.quiz.nextQuestion()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, text="You've reached the end of quizs.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_clicked(self):
        self.give_feedback("true")

    def false_clicked(self):
        self.give_feedback("false")

    def give_feedback(self, button_result):
        if self.quiz.check_answer(button_result):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            print("You got wrong")
        self.screen.after(1000, self.get_next_question)
