import random
import sys
sys.path.append('/home/anton9760/python-projects/python-project-49/brain_games')
import brain_games.scripts.cli as cli


def main():
    calculate()   


def calculate():
    solution = 0
    operator_list = ['+', '-', '*']
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    operator = random.choice(operator_list)
    question = str(first_number) + str(operator) + str(second_number)

    if operator == '+':
        correct_answer = first_number + second_number
            
    if operator == '-':
        correct_answer = first_number - second_number
            
    if operator == '*':
        correct_answer = first_number * second_number
    print("What is the result of the expression?")



'''def calculate():
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
            print(f"Congratulations, {cli.gamer_name}!") '''



if __name__ == '__main__':
    main()