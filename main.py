import random

from questions import Question
from data import questions_data


def main():
    questions = []

    for question_data in questions_data:
        questions.append(
            Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        ))

    #print(question)
    random.shuffle(questions)
    for question in questions:
        print(question.build_question())
        user_ansver=input()
        question.user_answer =user_ansver
        if question.is_correct():
            print(question.bulit_positive_feedback())
        else:
            print(question.bulit_negative_feedback())
    correct_counter = 0
    points = 0
    for question in questions:
        if question.is_correct():
            correct_counter+=1
            points+=question.get_points()
    print('Вот и все!!!')
    print(f"Отвечено вопросов {correct_counter} из {len(questions)}")
    print(f"Набрано балов {points}!!!")

main()