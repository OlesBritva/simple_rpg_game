import menu


class Character:
    def __init__(self):
        self.health = 0
        self.damage = 0
        self.defence = 0
        self.crit_chance = 0
        self.evasion = 0
        self.alive = True
        self.riposte_chance = 45

    @staticmethod
    def enemy_factory(dice):
        if dice <= 50:
            return Zombie()
        if dice <= 75:
            return Skeleton()
        if dice <= 100:
            return Hound()

    @staticmethod
    def player_action(player, enemy, enemy_action, player_action, player_dice):
        new_enemy_hp = enemy.health
        if player_action == 'Block':
            if player_dice in range(1, player.riposte_chance) and enemy_action != 'Block':
                damage_dealt = int(player.damage * 2) - enemy.defence
                enemy.health = new_enemy_hp - damage_dealt
                menu.Menu.print_animation(f'Riposte!\t You have dealt {damage_dealt} damage\n')
                return
            menu.Menu.print_animation('You decided to block\n')
            return
        if player_dice in range(1, enemy.evasion):
            menu.Menu.print_animation('You missed :(\n')
            return
        if player_dice in range(1, player.crit_chance):
            if enemy_action == 'Block':
                damage_dealt = int(player.damage * 1.5) - enemy.defence + 2
                enemy.health = new_enemy_hp - damage_dealt
                menu.Menu.print_animation(f'{enemy.__class__.__name__} decided to {enemy_action}\n')
                menu.Menu.print_animation(f'Critical!\t You have dealt {damage_dealt} damage\n')
                return
            else:
                damage_dealt = int(player.damage * 1.5) - enemy.defence
                enemy.health = new_enemy_hp - damage_dealt
                menu.Menu.print_animation(f'{enemy.__class__.__name__} decided to {enemy_action}\n')
                menu.Menu.print_animation(f'Critical!\t You have dealt {damage_dealt} damage\n')
                return
        damage_dealt = int(player.damage) - enemy.defence
        enemy.health = new_enemy_hp - damage_dealt
        menu.Menu.print_animation(f'{enemy.__class__.__name__} decided to {enemy_action}\n')
        menu.Menu.print_animation(f'You have dealt {damage_dealt} damage\n')

    @staticmethod
    def enemy_action(player, enemy, player_action, enemy_action, enemy_dice):
        new_player_hp = player.health
        if player_action == 'Block' and enemy_action == 'Block':
            menu.Menu.print_animation(f'{enemy.__class__.__name__} also decided to block, nothing happens...\n')
            return
        if enemy_action == 'Block':
            if enemy_dice in range(1, enemy.riposte_chance) and player_action != 'Block':
                damage_dealt = int(enemy.damage * 2) - player.defence
                player.health = new_player_hp - damage_dealt
                menu.Menu.print_animation(
                    f'Riposte!\t {enemy.__class__.__name__} dealt {damage_dealt} damage to you\n')
                return
            return
        if enemy_dice in range(1, player.evasion):
            menu.Menu.print_animation(f'{enemy.__class__.__name__} missed :)\n')
            return
        if enemy_dice in range(1, enemy.crit_chance):
            if player_action == 'Block':
                damage_dealt = int(enemy.damage * 1.5) - player.defence + 2
                player.health = new_player_hp - damage_dealt
                menu.Menu.print_animation(
                    f'Critical!\t {enemy.__class__.__name__} dealt {damage_dealt} damage to you\n')
                return
            else:
                damage_dealt = int(enemy.damage * 1.5) - player.defence
                player.health = new_player_hp - damage_dealt
                menu.Menu.print_animation(
                    f'Critical!\t {enemy.__class__.__name__} dealt {damage_dealt} damage to you\n')
                return
        damage_dealt = int(enemy.damage) - player.defence
        player.health = new_player_hp - damage_dealt
        menu.Menu.print_animation(f'{enemy.__class__.__name__} dealt {damage_dealt} damage to you\n')


class Warrior(Character):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.damage = 20
        self.defence = 10
        self.crit_chance = 8
        self.evasion = 10


class Wizard(Character):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.damage = 25
        self.defence = 8
        self.crit_chance = 15
        self.evasion = 15


class Rogue(Character):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.damage = 25
        self.defence = 6
        self.crit_chance = 20
        self.evasion = 15


class Guardian(Character):
    def __init__(self):
        super().__init__()
        self.health = 120
        self.damage = 15
        self.defence = 13
        self.crit_chance = 10
        self.evasion = 5


class Zombie(Character):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.damage = 20
        self.defence = 7
        self.crit_chance = 10
        self.evasion = 20


class Skeleton(Character):
    def __init__(self):
        super().__init__()
        self.health = 65
        self.damage = 25
        self.defence = 5
        self.crit_chance = 13
        self.evasion = 15


class Hound(Character):
    def __init__(self):
        super().__init__()
        self.health = 45
        self.damage = 30
        self.defence = 4
        self.crit_chance = 15
        self.evasion = 10
