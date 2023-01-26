import random
import time
import os

ACTION_ATTACK = 1
ACTION_HEAL = 2

MAX_PlAYER_HP = random.randint(40, 50)
MAX_MONSTER_HP = random.randint(40, 60)

count_player = 0    # TODO: REF
count_monster = 0   # TODO: REF
monster_names = ('Dragon', 'Ork', 'The Dead', "Puss in boots", "Shrek")


class Creature:
    """Родительский класс сушество."""

    def __init__(self, name, hp_player, power_attack_player, heal_player):
        self.name = name
        self.hp = hp_player
        self.power_attack = power_attack_player
        self.heal = heal_player

    def attack(self, enemy, player):
        """Персонаж атакует."""
        print(f'Количество здоровья {enemy.name} до удара: {enemy.hp}')
        print(f"{player.name} атакует!")
        enemy.hp -= self.power_attack
        time.sleep(2)
        print(f'Количество здоровья {enemy.name} после удара: {enemy.hp}')
        time.sleep(2)
        os.system("cls")

    def healing(self, count, test, hero, player):
        """Персонаж лечится."""
        if count != 2 and hero.hp != test:
            print(f'Количество здоровья {hero.name} до лечения: {hero.hp}')
            if hero.name == player.name:    # TODO: REF
                print(f"Вы лечитесь!")
            else:
                print(f'{hero.name} решает полечиться!')
            time.sleep(2)
            hero.hp += 10
            print(f'Количество здоровья {hero.name} после лечения: {hero.hp}')
        elif count != 2:
            print(
                "Почему", hero.name,
                "меня не послушали? Вы что думали что максивальное здоровье увеличится? В следующий раз будешь лучше меня слушать!")
        else:
            print("Попытки лечения кончились! Лечиться больше нельзя!")
        if hero.name == player.name:
            global count_player  # TODO: REF
            if count_player <= 2:
                count_player += 1
        else:
            global count_monster    # TODO: REF
            if count_monster <= 2:
                count_monster += 1

        time.sleep(4)
        os.system("cls")


class Hero(Creature):   # TODO: REF
    """Дочерний класс нашего героя."""
    pass


class Monster(Creature):  # TODO: REF

    """Дочерний класс монстра."""
    pass


name_player = input("Как тебя зовут? ")
player = Hero(name_player, MAX_PlAYER_HP, 10, 10)
monster = Monster(monster_names[random.randint(0, len(monster_names) - 1)], MAX_MONSTER_HP, 10, 0)  # TODO: REF

test_player = player.hp  # TODO: REF
test_monster = monster.hp   # TODO: REF


def asking():
    """ Принимаем главную информацию."""
    print(f'Имя вашего героя: {player.name}')
    print(f'Имя монстра: {monster.name}')
    time.sleep(2)


def game(player, monster, test_player, test_monster):
    """Запук игры."""
    while player.hp > 0 and monster.hp > 0:
        chance = random.randint(1, 2)

        def chance_func():  # TODO: REF
            """Основная функиция игры."""
            if chance == 1:
                print("Вы будете вытягивать жребий...")
                time.sleep(0.5)
                print("1...")
                time.sleep(0.5)
                print("2...")
                time.sleep(0.5)
                print("3...")
                print("Вы вытянули жребий! Поздравляю вы играете первым!")
                try:
                    choice = int(input(
                        "Что вы хотите сделать?\t\n1.Атакавать\n"
                        "2.Лечиться (не стоит лечиться если у вас и так полное здоровье "
                        "и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                except Exception:   # TODO: REF
                    print("Введите число!")
                    choice = int(input(
                        f"Что вы хотите сделать?\t\n{ACTION_ATTACK}.Атакавать\n"
                        f"{ACTION_HEAL}.Лечиться (не стоит лечиться если у вас и так полное здоровье"
                        " и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                if choice == ACTION_ATTACK:
                    player.attack(monster, player)
                elif choice == ACTION_HEAL:
                    player.healing(count_player, test_player, player, player)
                else:
                    print("Варианта только два!")
                    choice = int(input(
                        f"Что вы хотите сделать?\t\n{ACTION_ATTACK}.Атакавать\n"
                        f"{ACTION_HEAL}.Лечиться (не стоит лечиться если у вас и так полное здоровье и"
                        f" ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                    if choice == ACTION_ATTACK:
                        player.attack(monster, player)
                    elif choice == ACTION_HEAL:
                        player.healing(count_player, test_player, player, player)
            else:
                print("Вы будете вытягивать жребий...")
                time.sleep(0.5)
                print("1...")
                time.sleep(0.5)
                print("2...")
                time.sleep(0.5)
                print("3...")
                print(f"Вы не вытянули жребий. Ход: {monster.name}")
                choice = random.choice((ACTION_ATTACK, ACTION_HEAL))
                if choice == ACTION_ATTACK:
                    monster.attack(player, monster)
                else:
                    monster.healing(count_monster, test_monster, monster, player)

        chance_func()


def finish(monster, player):
    """Завершение игры."""
    if monster.hp <= 0 and player.hp <= 0:
        print("Поздравляю вы выиграли!")

    elif monster.hp <= 0:
        print("Поздравляю вы выиграли!")

    else:
        print("Вы проиграли. В следующий раз повезёт!")


asking()    # TODO: REF
game(player, monster, test_player, test_monster)  # TODO: REF
finish(monster, player)  # TODO: REF
