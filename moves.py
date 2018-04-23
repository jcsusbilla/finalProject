# BATTLE 1
import sys, os, pygame, math


class battle1Moves():
    def __init__(self, name, move1, move2):
        self.name = name
        self.move1 = move1
        self.move2 = move2

charmanderMoves = battle1Moves("charmanderMoves", "scratch", "growl")
bulbasaurMoves = battle1Moves("bublbasaurMoves", "tackle", "growl")
squirtleMoves = battle1Moves("squirtleMoves", "tackle", "leer")

# BATTLE 2
class battle2Moves():
    def __init__(self, name, move1, move2, move3, move4):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

charmeleonMoves = battle2Moves("charmeleonMoves", "ember", "scratch", "growl", "dragon rage")
ivysaurMoves = battle2Moves("ivysaurMoves", "tackle", "growl", "sleep powder", "razor leaf")
wartortleMoves = battle2Moves("wartortleMoves", "tackle", "leer", "water gun", "bite")


# BATTLE 3
class battle3Moves():
    def __init__(self, name, move1, move2, move3, move4):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

charizardMoves = battle3Moves("charizardMoves", )
venusaurMoves = battle3Moves("venusaurMoves", )
blastoiseMoves = battle3Moves("blastoiseMoves", )

# MOVES

class attackMoves():
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy

class lowerAttackStatMoves():
    def __init__(self, name, lowerAttack, accuracy):
        self.name = name
        self.lowerAttack = lowerAttack
        self.accuracy = accuracy

class lowerDefenseStatMoves():
    def __init__(self, name, lowerDefense, accuracy):
        self.name = name
        self.lowerDefense = lowerDefense
        self.accuracy = accuracy


tackle = attackMoves("tackle", 13, 95)
scratch = attackMoves("scratch", 14, 85)
razor leaf = attackMoves("razor leaf",)
dragon rage = attackMoves
ember = attackMoves
sleep powder = attackMoves