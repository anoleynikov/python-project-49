import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    gamer_name = prompt.string('May I have your name? ')
    print(f'Hello, {gamer_name}!')
    return gamer_name
