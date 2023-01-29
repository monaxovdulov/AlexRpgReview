import random
import time
import os

ACTION_ATTACK = 1
ACTION_HEAL = 2

MAX_PlAYER_HP = random.randint(40, 50)
MAX_MONSTER_HP = random.randint(40, 60)

COUNT_HEAL = 2

monster_names = ('Dragon', 'Ork', 'The Dead', "Puss in boots", "Shrek")


class Creature:
    """Родительский класс сушество."""
    name = ""
    hp = 0
    power_attack = 0
    heal = 0
    count_heal = COUNT_HEAL
    max_hp = 0

    def get_action(self):
        return random.choice((ACTION_ATTACK, ACTION_HEAL))

    def attack(self, enemy):
        """Персонаж атакует."""
        print(f'Количество здоровья {enemy.name} до удара: {enemy.hp}')
        print(f"{self.name} атакует!")
        enemy.hp -= self.power_attack
        time.sleep(2)
        print(f'Количество здоровья {enemy.name} после удара: {enemy.hp}')
        time.sleep(2)
        os.system("cls")

    def healing(self):
        """Персонаж лечится."""
        if self.count_heal > 0 and self.hp != self.max_hp:
            print(f'Количество здоровья {self.name} до лечения: {self.hp}')
            print(f'{self.name} решает полечиться!')
            time.sleep(2)
            self.hp += self.heal
            print(f'Количество здоровья {self.name} после лечения: {self.hp}')
            self.count_heal -= 1
            print(f'У вас осталось лечения: {self.count_heal}')
        elif self.hp == self.max_hp:
            print(
                "Почему", self.name,
                "меня не послушали? Вы что думали что максивальное здоровье увеличится? В следующий раз будешь лучше меня слушать!")
            print(f'У вас осталось лечения: {self.count_heal}')
        else:
            print("Попытки лечения кончились! Лечиться больше нельзя!")
        time.sleep(4)
        os.system("cls")


class Hero(Creature):  # TODO: REF
    """Дочерний класс нашего героя."""

    def __init__(self, name, power_attack, heal):
        self.name = name
        self.hp = MAX_PlAYER_HP
        self.power_attack = power_attack
        self.heal = heal
        self.max_hp = MAX_PlAYER_HP

    def get_action(self):
        return random.choice((ACTION_ATTACK, ACTION_HEAL))


class Monster(Creature):  # TODO: REF

    """Дочерний класс монстра."""

    def __init__(self, name, power_attack, heal):
        self.name = name
        self.hp = MAX_MONSTER_HP
        self.power_attack = power_attack
        self.heal = heal
        self.max_hp = MAX_MONSTER_HP


name_player = input("Как тебя зовут? ")
player = Hero(name_player, power_attack=10, heal=10)
monster_name = random.choice(monster_names)
monster = Monster(monster_name, power_attack=10, heal=0)  # TODO: REF

test_player = player.hp  # TODO: REF
test_monster = monster.hp  # TODO: REF


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
                except Exception:  # TODO: REF
                    print("Введите число!")
                    choice = int(input(
                        f"Что вы хотите сделать?\t\n{ACTION_ATTACK}.Атакавать\n"
                        f"{ACTION_HEAL}.Лечиться (не стоит лечиться если у вас и так полное здоровье"
                        " и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                if choice == ACTION_ATTACK:
                    player.attack(enemy=monster)
                elif choice == ACTION_HEAL:
                    player.healing()
                else:
                    print("Варианта только два!")
                    choice = int(input(
                        f"Что вы хотите сделать?\t\n{ACTION_ATTACK}.Атакавать\n"
                        f"{ACTION_HEAL}.Лечиться (не стоит лечиться если у вас и так полное здоровье и"
                        f" ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                    if choice == ACTION_ATTACK:
                        player.attack(enemy=monster)
                    elif choice == ACTION_HEAL:
                        player.healing()
            else:
                print("Вы будете вытягивать жребий...")
                time.sleep(0.5)
                print("1...")
                time.sleep(0.5)
                print("2...")
                time.sleep(0.5)
                print("3...")
                print(f"Вы не вытянули жребий. Ход: {monster.name}")
                choice = monster.get_action()
                if choice == ACTION_ATTACK:
                    monster.attack(enemy=player)
                else:
                    monster.healing()

        chance_func()


def finish(monster, player):
    """Завершение игры."""
    if monster.hp <= 0 and player.hp <= 0:
        print("Поздравляю вы выиграли!")

    elif monster.hp <= 0:
        print("Поздравляю вы выиграли!")

    else:
        print("Вы проиграли. В следующий раз повезёт!")


asking()  # TODO: REF
game(player, monster, test_player, test_monster)  # TODO: REF
finish(monster, player)  # TODO: REF
