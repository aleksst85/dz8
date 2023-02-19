class Question:
    def __init__(self, question_text, question_diff, question_answer):
        self.question_text = question_text
        self.question_diff = question_diff
        self.question_answer = question_answer

        self.is_asked = False
        self.user_answer = None
        self.point = self.question_diff*10


    def get_points(self):
        return  self.point


    def is_correct(self):
        return self.question_answer == self.user_answer


    def build_question(self):
        answer = f"Вопрос: {self.question_text}\n Сложность {self.question_diff}/5"
        return answer


    def bulit_positive_feedback(self):
        answer = f"Ответ верный, получено {self.point} балов."
        return answer


    def bulit_negative_feedback(self):
        answer = f"Ответ не верный! Верный ответ - {self.question_answer}."
        return answer

    def __repr__(self):
        return f'{self.question_text} - {self.question_answer} -{self.question_diff}/5'


