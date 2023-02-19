import random
from util import load_question, get_stats


def main():
    questions = load_question()
    random.shuffle(questions)
    for question in questions:
        print(question.build_question())
        user_ansver=input()
        question.user_answer = user_ansver
        if question.is_correct():
            print(question.bulit_positive_feedback())
        else:
            print(question.bulit_negative_feedback())

    correct_counter, points = get_stats(questions)

    print('Вот и все!!!')
    print(f"Отвечено вопросов {correct_counter} из {len(questions)}")
    print(f"Набрано балов {points}!!!")

main()