class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.correct = 0

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False? ").lower()
        self.check_answer(user_answer, current_question.answer.lower())

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.correct += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.correct}/{self.question_number}")
