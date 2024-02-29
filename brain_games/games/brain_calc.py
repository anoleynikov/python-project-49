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








#первоначальная функция
def calculate_old():
    count = 0
    solution = 0
    operator_list = ['+', '-', '*']
    while count < 3:
        
        print("What is the result of the expression?")
        
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        operator = random.choice(operator_list)
        
        print(f"Question: {first_number} {operator} {second_number}")
        
        if operator == '+':
            correct_answer = first_number + second_number
            
        if operator == '-':
            correct_answer = first_number - second_number
            
        if operator == '*':
            correct_answer = first_number * second_number
            
        answer = int(input("Please, enter your answer: "))    
        
        print(f"Your answer: {answer}")
        
        if answer == correct_answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {cli.gamer_name}!")
            break
        
        if count == 3:
            print(f"Congratulations, {cli.gamer_name}!")
