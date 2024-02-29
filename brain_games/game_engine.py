import prompt
from brain_games.scripts.cli import welcome_user




def run_game(game_module):
    gamer_name = welcome_user()

    count = 0
         
    while count < 3:
        question, correct_answer = game_module.answer_check()
        print(f"Question: {question}")
        gamer_answer = prompt.string('Please, enter your answer ')
        print(f"Your answer: {gamer_answer}")
        if gamer_answer == correct_answer:
            print("Correct!")
            count +=1
        else:
            print(f"'{gamer_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {gamer_name}!")
            break
        
        if count == 3:
            print(f"Congratulations, {gamer_name}!") 



    
   #print("Welcome to the Brain Games!")
    #gamer_name = prompt.string('May I have your name? ')
    #print(f'Hello, {gamer_name}!')
    #print(game_module.MISSION)