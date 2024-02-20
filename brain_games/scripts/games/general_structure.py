import sys
sys.path.append('/home/anton9760/python-projects/python-project-49/brain_games')
import cli
from brain_even import is_even
from brain_calc import calculate
'''from brain_even import is_even
from brain_calc import calculate'''


def main():
    game_structure()
    
   


def game_structure():
    count = 0
    
    if True:
        game = input('Choose game: ')
            
    if game == "brain-even":
        print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
        is_even()
        number, correct_answer, question = is_even()
        
    if game == "brain-calc":
        calculate()  
         
    while count < 3:
        print(f"Question: {question}")
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