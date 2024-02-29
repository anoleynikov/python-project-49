from random import randint

MISSION = 'What number is missing in the progression?'


def progression_making():
    progression_list = []
    first_member = randint(0,10) #первый член последовательности
    difference = randint(0, 10) #разность последовательности
    last_member = randint(8, 11) #длина последовательности
    hidden_index = randint(0, last_member - 1)
    
    for i in range(last_member):
        if i == hidden_index:
            progression_list.append('...')
        else:
            progression_list.append(first_member + i * difference)
    print(f'Последовательность: {progression_list}')

    


progression_making()


#def answer_check():