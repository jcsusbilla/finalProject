from moves import Moves
import sys, pygame, os, math

moveset = Moves()

class Pokemon():
    def __init__(self, name, pkmnType, level, hp, attack, defense, speed):
        self.name = name
        self.pkmnType = pkmnType
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moveset = moveset

# BATTLE #1
charmander = Pokemon("Charmader", "Fire", 5, 39, 52, 43, 65)
bulbasaur = Pokemon("Bulbasaur", "Grass", 5, 45, 49, 49, 45)
squirtle = Pokemon("Squirtle", "Water", 5, 44, 48, 65, 43)

# BATTLE #2
charmeleon = Pokemon("Charmeleon", "Fire", 20, 58, 64, 58, 80)
ivysaur = Pokemon("Ivysaur", "Grass", 20, 60, 62, 63, 60)
wartortle = Pokemon("Wartortle", "Water", 20, 59, 63, 80, 58)

#Battle #3
charizard = Pokemon("Charizard", "Fire" + "Flying", 45, 78, 84, 78, 100)
venusaur = Pokemon("Venusaur", "Grass" + "Poison", 45, 80, 82, 83, 80)
blastoise = Pokemon("Blastoise", "Water", 45, 79, 83, 100, 78)

