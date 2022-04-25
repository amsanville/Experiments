from enum import Enum, auto
import random
import math

# Monster name generating variables
descriptor = [
    'Aggressive',
    'Arrogant',
    'Boastful',
    'Bossy',
    'Boring',
    'Careless',
    'Clingy',
    'Cruel',
    'Cowardly',
    'Deceitful',
    'Dishonest',
    'Fussy',
    'Greedy',
    'Grumpy',
    'Harsh',
    'Impatient',
    'Impulsive',
    'Jealous',
    'Moody',
    'Narrow-minded',
    'Overcritical',
    'Rude',
    'Selfish',
    'Untrustworthy',
    'Unhappy'
]

species = [
    'Giant Rat',
    'Goblin',
    'Kobold',
    'Bandit',
    'Zombie',
    'Skeleton',
    'Wolf',
    'Gnoll',
    'Ghoul',
    'Orc',
    'Lizardman'
]

# Auto Generated class to enumerate basic states for the game
class State(Enum):
    MAIN_MENU = auto()
    BATTLE = auto()
    GAME_OVER = auto()
    QUIT = auto()
    SPELLBOOK = auto()
    FIRE = auto()
    WATER = auto()


# I'm transitioning a bunch of the in game mechanics to objects in order to convert the game into a more object oriented style of code.

# Hardcoded stat values - subject to change
# Base spell damage
BASE_DMG = 5

# Crit chance and damage multiplier
BASE_CRIT_CHANCE = 5
BASE_CRIT_MULTI = 2

# Item drop rates in percent
BASE_DROP_COMMON = 25
BASE_DROP_RARE = 5

# Maximum super value until fully charged
SUPER_MAX = 10000
# Charge rate on taking damage, 1 damage is equivalent to x points of super charge
BASE_SUPER_CHARGE_RATE_DMG = 10
# Charge rate on hitting an enemy, 1 damage is equivalent to x points of super charge
BASE_SUPER_CHARGE_RATE_HIT = 10

class Player():
    """
    Player

    Class for the player contains the important elements of the player character, like stats and what not.
    """
    # Character name
    name = "Hiro"
    # Amount of gold the player has
    gold = 0

    # Primary Stats
    conStat = 5
    intStat = 5
    dexStat = 5
    luckStat = 5

    # Calculated stats
    # Maximum amount of health
    maxHealth = 20 * conStat
    # Crit chance
    critChance = BASE_CRIT_CHANCE + math.floor(math.sqrt(luckStat))
    # Spell damage
    spellDamage = BASE_DMG + intStat

    # Current stats
    # Amount of health the player has currently
    currHealth = maxHealth

    # Spell Experience
    # Fire
    hasFire = True
    fireLevel = 1
    fireExp = 0
    fireDmg = 0
    fireRes = 0.5
    fireWeak = 2

    # Water
    hasWater = True
    waterLevel = 1
    waterExp = 0
    waterDmg = 0
    waterRes = 0.5
    waterWeak = 2

    # Inventory - right now I'm thinking a list of items
    # TODO: read some about programming patterns. It sounds like items in particular are a good way to

    # Equipment - this is equipped equipment
    # Python classes are pass by reference unless you deep copy
    equipHead = None
    equipChest = None
    equipLegs = None
    equipArms = None
    equipFeet = None
    equipRing1 = None
    equipRing2 = None
    equipNeck = None
    equipBracelet1 = None
    equipBracelet2 = None

    # Recalculates the stats as appropriate
    def calcStats(self):
        # Maximum amount of health
        self.maxHealth = 20 * self.conStat
        # Crit chance
        self.critChance = BASE_CRIT_CHANCE + math.floor(math.sqrt(self.luckStat))
        # Spell Damage
        self.spellDamage = BASE_DMG + intStat
        
class Item():
    """
    Class for items in game


    """



class Enemy():
    """
    """
    


class Menu():
    # Title at the top of the menu
    title = 'placeholder'
    # Text for the options
    options = ['option 1', 'option 2']
    # The resulting state after the menu
    state = [State.MAIN_MENU, State.QUIT]

    def procMenu(self):
        # Start the loop
        validPick = False
        while not validPick:
            # Print the menu
            print(self.title)
            for ind, option in enumerate(self.options):
                print(str(ind + 1) + '.) ' + option)

            # Read and validate input (check if it's a digit and if it's in the correct range)
            # BUG: could be decimal instead of integer, so not super precise. Good enough for prototype
            selected = input('Please select a # from the above.\n')
            
            if selected.isdigit() and int(selected) > 0 and int(selected) <= len(self.options):
                validPick = True
            else:
                print('Invalid option, please pick from the above.')
        return self.state[int(selected) - 1]

# Game is small enough, that I'm not going to worry about loading and unloading assets

# Build the Main Menu
mainMenuMenu = Menu()
mainMenuMenu.title = 'Main Menu:'
mainMenuMenu.options = ['New Game', 'Quit']
mainMenuMenu.state = [State.BATTLE, State.QUIT]

# Run the main menu
def mainMenu():
    return mainMenuMenu.procMenu()

# Self-Contained battle function
def battle():
    # Build Battle Menu
    battleMenu = Menu()
    battleMenu.title = 'Fight:'
    battleMenu.options = ['Cast Spell', 'Surrender']
    battleMenu.state = [State.SPELLBOOK, State.GAME_OVER]

    # Spellbook
    spellbookMenu = Menu()
    spellbookMenu.title = 'Spellbook:'
    spellbookMenu.options = ['Cast fire spell', 'Cast water spell']
    spellbookMenu.state = [State.FIRE, State.WATER]

    # Player tracker
    playerHealth = 100
    fireExp = 0
    fireLevel = 1
    waterExp = 0
    waterLevel = 1

    # Enemy tracker
    enemyLevel = 1
    enemyName = ''
    enemyHealth = 100

    # Start the main game loop
    battleOver = False
    while not battleOver:
        # Generate an enemy
        enemyName = random.choice(descriptor) + ' ' + random.choice(species)
        enemyHealth = int((5 * enemyLevel) * (1. + random.random() * 0.1))
        enemyMaxHealth = enemyHealth

        # Do the battle
        print('\nAn', enemyName, 'appears.')
        if battleMenu.procMenu() == State.GAME_OVER:
            battleOver = True
        else:
            # Loop until the enemy or the player is dead
            while enemyHealth > 0 and playerHealth > 0:
                print('Player:', playerHealth, '/', 100)
                print('Enemy:', enemyHealth, '/', enemyMaxHealth)
                spell = spellbookMenu.procMenu()

                # Generate a spell based on the player's choice
                if spell == State.FIRE:
                    # Generate a random addition problem
                    a = random.randint(fireLevel, 2 * fireLevel + 1)
                    b = random.randint(fireLevel, 2 * fireLevel + 1)
                    ans = a + b
                    damage = int(fireLevel * 10 * (1. + random.random() * 0.2))
                    print(a, ' + ', b, ' = ?')
                elif spell == State.WATER:
                    # Generate a random subtraction problem
                    a = random.randint(waterLevel, 2 * waterLevel + 1)
                    b = random.randint(waterLevel, 2 * waterLevel + 1)
                    if a > b:
                        ans = a - b
                        print(a, ' - ', b, ' = ?')
                    else:
                        ans = b - a
                        print(b, ' - ', a, ' = ?')
                    damage = int(waterLevel * 10 * (1. + random.random() * 0.2))
                # Process the answer and do damage
                # BUG: decimal thing again
                playerAns = input('Answer: ')
                if playerAns.isdigit and int(playerAns) == ans:
                    print('Correct, you do', damage, 'to the', enemyName)
                    enemyHealth -= damage
                    if spell == State.FIRE:
                        fireExp += 25
                    elif spell == State.WATER:
                        waterExp += 25
                else:
                    print('Incorrect, your spell fizzles.')
                print(enemyName, 'does 10 damage to you.')
                playerHealth -= 10

            # Battle Result
            if playerHealth <= 0:
                print('The ', enemyName, ' defeates you.')
                battleOver = True
            else:
                # You win
                print('You defeat the ', enemyName)
                enemyLevel += 1

                # Level up fire
                while fireExp > fireLevel * 100:
                    fireLevel += 1
                    fireExp -= fireLevel * 100
                    print('Your fire spell leveled up to level ', fireLevel)
                # Level up water
                while waterExp > waterLevel * 100:
                    waterLevel += 1
                    waterExp == waterLevel * 100

    return State.GAME_OVER

def gameOver():
    print('Game Over!')
    return State.MAIN_MENU

def quit():
    print('Goodbye and have a nice day!')

def errorState():
    print('Error: State not assigned correctly, error state reached.')
    return next

def main():
    # Start the game
    next = State.MAIN_MENU

    # Game state loop
    while next != State.QUIT:
        if next == State.MAIN_MENU:
            next = mainMenu()
        elif next == State.BATTLE:
            next = battle()
        elif next == State.GAME_OVER:
            next = gameOver()
        else:
            next = errorState()
    
    # Print quit message and clean up assets
    quit()

if __name__ == '__main__':
    main()