#import actors
import random

import time

from actors import Wizard, Creature, SmallAnimal, Dragon

def main():
    print_header()
    game_loop()


def print_header():
    print('game')


def game_loop():

    creatures =[SmallAnimal('Toad', 1),Creature('Tiger', 12),SmallAnimal('Bat', 3),Dragon('Dragon', 50, 75, True),
                Wizard('Evil Wizard', 1000)]
    #hero = actors.Wizard()

    #print(creatures)
    hero=Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)

        cmd = input('Do you want to [a]ttack, [r]unaway or [l]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print ("the wizard runs and hides to recover...")
                time.sleep(5)
                print("The wizard returns revitalized")
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print(" The wizard {} takes in the sourrondings and see: ".format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        else:
            print('ok, bye')
            break
        print()

if __name__=='__main__':
    main()