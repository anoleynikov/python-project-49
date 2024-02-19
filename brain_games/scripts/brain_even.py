import random
import sys
sys.path.append('/home/anton9760/python-projects/python-project-49/brain_games')
import cli

def main():
    pass


def is_even():
    count = 0   

    while count < 3:
        number = random.randint(0, 100)
        if number % 2 == 0:
            correct_answer = 'Yes'
        else:
            correct_answer = 'No'
            
        print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
        print(f"Question: {number}")
        answer = input("Please, enter your answer: ")
        print(f"Your answer: {answer}")

            
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            count +=1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {cli.gamer_name}!")
            break
        
        if count == 3:
            print(f"Congratulations, {cli.gamer_name}!")



if __name__ == '__main__':
    main()