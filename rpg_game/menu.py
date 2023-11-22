import os
import time


class Menu:

    @staticmethod
    def print_animation(string, speed=0.1):
        for char in string:
            print(char, end='')
            time.sleep(speed)

    @staticmethod
    def input_validation(*args, user_input):
        if user_input not in args:
            raise ValueError('This option does not exist.')

    @staticmethod
    def startup_menu():
        Menu.print_animation('Welcome to simple RPG game!')
        time.sleep(2)
        print('\n')
        Menu.print_animation('1. New game\n')
        Menu.print_animation('2. Show scores\n')
        Menu.print_animation('3. Quit\n\n')

    @staticmethod
    def print_scores(data):
        if not data:
            Menu.print_animation('The scoreboard is currently empty\n')
            return
        for name, score in data.items():
            print(name + ' - ' + str(score))

    @staticmethod
    def character_selection_menu():
        from game import characters_list
        Menu.print_animation('Select your character... \n\n')
        for number, char in enumerate(characters_list, 1):
            Menu.print_animation(f'{number}. {char.__class__.__name__}\n')
            Menu.print_animation(f'\tHealth: {char.health}\n')
            Menu.print_animation(f'\tDamage: {char.damage}\n')
            Menu.print_animation(f'\tDefence: {char.defence}\n\n')

