#!/usr/bin/env python3
import sys
sys.path.append('/home/anton9760/python-projects/python-project-49/brain_games')
from cli import welcome_user
from brain_even import is_even


def main():
    
    welcome_user()

    if True:
        game = input('Choose game: ')


    if game == "brain-even":
        is_even()

    
if __name__ == '__main__':
    main()  