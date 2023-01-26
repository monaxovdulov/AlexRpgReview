from src import *


def main():
    """Вызываем все функции из src."""
    print("Привет")
    asking()
    game(player=player, monster=monster, test_player=test_player, test_monster=test_monster)
    finish(monster=monster, player=player)


if __name__ == 'main':  # todo: FIX __main__
    main()
