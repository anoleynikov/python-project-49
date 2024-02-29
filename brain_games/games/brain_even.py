from random import randint

MISSION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0  
    

def answer_check():
    question = randint(0, 100)
    
    if is_even(question) is True:
        correct_answer = 'yes'
    else: 
        correct_answer = 'no'
        
    return question, correct_answer












#первоначальный вид функции 


def is_even_old():
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
