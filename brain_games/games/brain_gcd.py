from random import randint

MISSION = 'Find the greatest common divisor of given numbers.'

def finding_gcd(first, second):
    if second == 0:
        return first
    else:
        return finding_gcd(second, first % second)



def answer_check():
    number_main = randint(1, 10)
    first_multiplier = randint(2,8)
    second_multiplier = randint(2,8)
    
    number_first = number_main * first_multiplier
    number_second = number_main * second_multiplier
    question = f'{number_first} {number_second}'
    correct_answer = finding_gcd(number_first, number_second)
    return question, str(correct_answer)
    




    