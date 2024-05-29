from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question1 = Question("ABC", "True")

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
correct = 0
wrong = 0


while quiz.still_has_questions():
    quiz.nextQuestion()

print(f"\nYou've completed the quiz.\nYour final score was: {quiz.correct}/{quiz.question_number}")