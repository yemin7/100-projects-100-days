import html


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.current_question = None
        self.correct = 0

    def nextQuestion(self):
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question['question'])
        return f"{q_text}".lower()
        # user_answer = input(f"{q_text} True/False? ").lower()
        # self.check_answer(user_answer, current_question['correct_answer'].lower())

    def has_next_question(self):
        return len(self.questions_list) > self.question_number

    def check_answer(self, user_input):
        if user_input == self.current_question['correct_answer'].lower():
            self.correct += 1
            return True
        else:
            return False
