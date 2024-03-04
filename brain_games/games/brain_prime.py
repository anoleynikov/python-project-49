from random import randint

MISSION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):

    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def answer_check():
    question = randint(0, 100)
    correct_answer = "yes" if is_prime(question) is True else 'no'
    return question, correct_answer
