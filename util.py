from questions import Question
from data import questions_data
import random
def load_question():
    questions = []
    for question_data in questions_data:
        questions.append(
            Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        ))
        random.shuffle(questions)
    return questions


def get_stats(questions):
    correct_counter = 0
    points = 0
    for question in questions:
        if question.is_correct():
            correct_counter += 1
            points += question.get_points()
    return  correct_counter, points