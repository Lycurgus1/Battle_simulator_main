from army_methods import Army_methods
import random

class Armies(Army_methods):

    # Setting variables to none by defualt so they do not to need to specified when creating the class
    def __init__(self, leader=None, leadership=None, size=None, culture=None, fatigue=None):
        super().__init__(size, culture, fatigue)
        self.leader = leader
        self.leadership = leadership

    # Roman army
    def roman_army(self):
        self.size = 10
        self.culture = "Roman"
        self.fatigue = False
        print("\nA Roman army 10,000 strong, of Roman culture and rested has been created.")

    # Hunnic army
    def hunnic_army(self):
        self.size = 5
        self.culture = "Hunnic"
        self.fatigue = False
        print("\nA Hun army 5,000 strong, of Hunnic culture and rested has been created.")

    # Two armies fight
    def fight(self, classobj1, classobj2):
        army1_strength = self.strength_calculator(classobj1)
        army2_strength = self.strength_calculator(classobj2)
        # Calculating what side wins or if it is a draw
        if army1_strength > army2_strength:
            # Calling armies beaten method to calculate results of battle
            self.army_beaten(classobj1, classobj2)
        elif army2_strength > army1_strength:
            # Calling armies beaten method to calculate results of battle
            self.army_beaten(classobj2, classobj1)
        elif army2_strength == army1_strength:
            self.army_draw(classobj1, classobj2)
        else:
            print(classobj1.size)
            print(classobj2.size)
            print("An error has occured")

    # Battle strength calculator
    def strength_calculator(self, classobject):
        raw_strength = classobject.size
        # Random element generator for number between 0 and 5
        random_element = random.randint(0, 5)
        # Creating strength modifier
        strength_modifier = 1 + (classobject.leadership / 10) + random_element
        army_strength = raw_strength * strength_modifier
        return army_strength

    # Method for when an army is defeated by another
    def army_beaten(self, winner, loser):
        loser.size = loser.size - 5
        print("\n" + winner.leader + " has defeated " + loser.leader)
        if loser.size <= 0:
            self.defeated_armies(loser)
        else:
            print("\n" + loser.leader + "'s army has been severely weakened and their army is now " +
                  str(loser.size) + ",000 strong")

    # Method for draw between armies
    def army_draw(self, army1, army2):
        army1.size = army1.size - 2
        army2.size = army2.size - 2
        print("\nThe armies have clashed and the battle was inconclusive")
        # If loop to check if army is defeated
        if army1.size <= 0:
            self.defeated_armies(army1)
        else:
            print("\n" + army1.leader + "'s strength is now " + str(army1.size) + ",000 strong. ")
        # If loop to check if army is defeated
        if army2.size <= 0:
            self.defeated_armies(army2)
        else:
            print("\n" + army2.leader + "'s strength is now " + str(army2.size )+ ",000 strong. ")

    # Function to deal with defeated armies
    def defeated_armies(self, classobject):
        print("\n" +classobject.leader + "'s army was destroyed, they were valiant fighters.")