from random import randint

MISSION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def answer_check():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) is True else 'no'
    return question, correct_answer
