from random import randint

MISSION = 'What number is missing in the progression?'


def progression_making():
    progression_list = []
    first_member = randint(0, 10)
    difference = randint(0, 10)
    last_member = randint(8, 11)
    hidden_index = randint(0, last_member - 1)

    for i in range(last_member):
        if i == hidden_index:
            progression_list.append('..')
        else:
            progression_list.append(first_member + i * difference)
    hidden_number = first_member + hidden_index * difference
    return hidden_number, progression_list


def answer_check():
    hidden_number, progression_list = progression_making()
    question = ' '.join(map(str, progression_list))
    correct_answer = hidden_number
    return question, str(correct_answer)
