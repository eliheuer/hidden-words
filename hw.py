########################
#                      #
#   The Hidden Words   #
#                      #
########################
from random import *


def headline():
    print("*      The Hidden Words      *")
    print("*          from the          *")
    print("*      Arabic & Persian      *")


def persian_01():
    print("\nO MY FRIEND\n")
    print("Thou art the day-star of the  ")
    print("heavens of My holiness, let not")
    print("the defilement of the world")
    print("eclipse thy splendor. Rend as-")
    print("under the veil of heedlesness ")
    print("that from behind the clouds") 
    print("thou mayest emerge resplendent ")
    print("and array all things with the")
    print("apparel of life. ")


def persian_02():
    print("\nFOO")
    print("Bar.")

# Main
headline()
def random_verse(*vrs):
    verses = list(vrs)
    shuffle(verses)
    rand_verse = verses[1]
    rand_verse()

random_verse(persian_01,
             persian_02)

