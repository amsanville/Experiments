from enum import(Enum)

'''
Slot

Enumeration for gear slot/type.
'''
class Slot(Enum):
    MAINHAND = auto()
    OFFHAND = auto()
    HEAD = auto()
    CHEST = auto()
    LEGS = auto()
    HANDS = auto()
    FEET = auto()
    ACCESSORY = auto()

class Player:
    # Base Stats
    str_stat = 10
    dex_stat = 10
    con_stat = 10
    int_stat = 10
    wis_stat = 10
    cha_stat = 10
    lck_stat = 10

    # Gear Slots


    # Derived Stats
    health = 100


class Equipment:
    # Core Stat bonuses
    str_bonus = 0
    dex_bonus = 0
    con_bonus = 0
    int_bonus = 0
    wis_bonus = 0
    cha_bonus = 0
    lck_bonus = 0


def main():
    player = Player()
    print(player.health)

if __name__ == '__main__':
    main()