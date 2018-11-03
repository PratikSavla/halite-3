# Python 3.6
import hlt  #main halite stuff
from hlt import constants  # halite constants
from hlt.positionals import Direction, Position  # helper for moving
import random  # randomly picking a choice for now.
import logging  # logging stuff to console
import math

game = hlt.Game()  # game object
# Initializes the game
game.ready("Pratikbot")

ship_states = {}
i=0
