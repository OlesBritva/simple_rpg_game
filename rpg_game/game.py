import menu
import characters
import random
import json
import os

running = True
starting_menu = menu.Menu()
starting_menu_loop = True
character_selection_menu = False
battle = False
turns = 1
rounds = 1
score = 0

warrior = characters.Warrior()
wizard = characters.Wizard()
rogue = characters.Rogue()
guardian = characters.Guardian()
characters_list = [warrior, wizard, rogue, guardian]

if os.path.exists('score.json') and os.path.getsize('score.json') > 0:
    with open('score.json', 'r') as file:
        data = json.load(file)
else:
    data = dict()

if __name__ == '__main__':
    while running:
        if starting_menu_loop:
            starting_menu.startup_menu()
            user_selection = input('Enter your option to continue: ')
            starting_menu.input_validation('1', '2', '3', user_input=user_selection)
            if user_selection == '3':
                exit()
            if user_selection == '2':
                menu.Menu.print_scores(data)
                input('Press key to go back to the menu...')
            if user_selection == '1':
                starting_menu_loop = False
                character_selection_menu = True

        if character_selection_menu:
            starting_menu.character_selection_menu()
            user_selection = input('Enter your option to continue: ')
            starting_menu.input_validation('1', '2', '3', '4', user_input=user_selection)
            if user_selection == '1':
                starting_menu.print_animation(f'You have selected {warrior.__class__.__name__}')
                PLAYER = warrior
                character_selection_menu = False
                battle = True
            elif user_selection == '2':
                starting_menu.print_animation(f'You have selected {wizard.__class__.__name__}')
                PLAYER = wizard
                character_selection_menu = False
                battle = True
            elif user_selection == '3':
                starting_menu.print_animation(f'You have selected {rogue.__class__.__name__}')
                PLAYER = rogue
                character_selection_menu = False
                battle = True
            else:
                starting_menu.print_animation(f'You have selected {guardian.__class__.__name__}')
                PLAYER = guardian
                character_selection_menu = False
                battle = True

        if battle:
            starting_menu.print_animation(f'\nRound {rounds}...')
            starting_menu.print_animation('\n\nFIGHT!\n\n')
            enemy = characters.Character.enemy_factory(random.randint(1, 100))
            starting_menu.print_animation(f'Your enemy is {enemy.__class__.__name__}\n')
            while enemy.alive:
                starting_menu.print_animation(f'Your HP = {PLAYER.health}\t\t Enemy HP = {enemy.health}\n\n')
                starting_menu.print_animation('1. Attack\t 2. Block\n')
                user_selection = input('Enter your option to continue: ')
                starting_menu.input_validation('1', '2', user_input=user_selection)
                enemy_action = 'Attack' if random.randint(1, 2) == 1 else 'Block'
                if user_selection == '1':
                    characters.Character.player_action(PLAYER, enemy, enemy_action, 'Attack',
                                                       random.randint(1, 100))
                    characters.Character.enemy_action(PLAYER, enemy, 'Attack', enemy_action,
                                                      random.randint(1, 100))
                    turns += 1
                if user_selection == '2':
                    characters.Character.player_action(PLAYER, enemy, enemy_action, 'Block',
                                                       random.randint(1, 100))
                    characters.Character.enemy_action(PLAYER, enemy, 'Block', enemy_action,
                                                      random.randint(1, 100))
                    turns += 1
                if enemy.health <= 0:
                    rounds += 1
                    score += 10
                    enemy.alive = False
                    starting_menu.print_animation(f'\n{enemy.__class__.__name__} was defeated!\n')
                    starting_menu.print_animation('Your hp was restored by 10\n')
                    PLAYER.health += 10

                if PLAYER.health <= 0:
                    starting_menu.print_animation(f'You died, game over... \t your score is {score * rounds - turns}\n',
                                                  0.3)

                    user_selection = input('Enter your Name to save your score: ')
                    if len(user_selection) > 21:
                        raise ValueError('Name can be 20 chars or less')

                    if score < 0:
                        score = 0

                    score_dict = dict(sorted({**data, user_selection: score}.items(), key=lambda item: item[1], reverse=True))

                    with open('score.json', 'w') as file:
                        json.dump(score_dict, file, indent=4)

                    starting_menu.print_animation('Your score was saved\n... bye :)')
                    quit()
