import prompt


def welcome_user():
    global gamer_name
    gamer_name = ''
    print("Welcome to the Brain Games!")
    gamer_name = prompt.string('May I have your name? ')
    print(f'Hello, {gamer_name}!')


if __name__ == '__main__':
    pass