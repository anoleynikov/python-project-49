#!/usr/bin/env python3
import sys
sys.path.append('/home/anton9760/python-projects/python-project-49/brain_games')
sys.path.append('/home/anton9760/python-projects/python-project-49/brain_games/scripts/games')
from cli import welcome_user
from brain_even import is_even
from brain_calc import calculate


def main():
    
    welcome_user()

    if True:
        game = input('Choose game: ')


    if game == "brain-even":
        is_even()
        
    if game == "brain-calc":
        calculate()

    
if __name__ == '__main__':
    main()  