from random import choice, randint


MISSION = 'What is the result of the expression?'
OPERATOR_LIST = ('+', '-', '*')



def answer_check():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operator = choice(OPERATOR_LIST)

    question = f'{first_number} {operator} {second_number}'
    
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
        
    return question, str(correct_answer)

