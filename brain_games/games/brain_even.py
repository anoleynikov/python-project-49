from random import randint

MISSION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def answer_check():
    question = randint(1, 100)

    if is_even(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
