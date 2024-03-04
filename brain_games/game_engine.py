from prompt import string
from brain_games.scripts.cli import welcome_user

WIN_COUNT = 3

def run_game(game_module):
    gamer_name = welcome_user()
    print(game_module.MISSION)
    count = 0

    while count < WIN_COUNT:
        question, correct_answer = game_module.answer_check()
        print(f"Question: {question}")
        gamer_answer = string('Please, enter your answer ')
        print(f"Your answer: {gamer_answer}")
        if gamer_answer == correct_answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{gamer_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {gamer_name}!")
            break

        if count == 3:
            print(f"Congratulations, {gamer_name}!")
