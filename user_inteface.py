from armies import Armies
import time

class User_interface(Armies):

    def __init__(self, leader=None, leadership=None, size=None, culture=None, fatigue=None):
        # Inheriting previous attributes
        super().__init__(leader, leadership, size, culture, fatigue)
        # Creating class object for methods to run
        self.battler = Armies()
        print("Welcome to a virtual battle simulator!")
        self.user_choice()

    def user_choice(self):
        x = True
        while x == True:
            user_input = input("What would you like to do: \n\n Exit E\n Run simulator R\n Continue with current armies C")
            if user_input in ["E", "R", "C"]:
                x = False
            else:
                print("\nEnter either E, R or C, try again")

            if user_input.upper() == "E":
                print("I hope you enjoyed using the simulator")
                break
            elif user_input.upper() == "R":
                print("\nRunning simulator....")
                time.sleep(5)
                self.create_armies()
                time.sleep(5)
                self.battle()
                self.user_choice()
            elif user_input.upper() == "C":
                print("\n Fighting with current armies.....")
                self.battle()


    def create_armies(self):
        # Army 1 creation
        army1_leader = input("Who leads the first army?")
        army1_leadership = input("How good are they? 0-10")
        # Use while loop here to test inputs
        self.army1 = Armies(str(army1_leader), int(army1_leadership))
        # Army 2 creation
        army2_leader = input("Who leads the second army?")
        army2_leadership = input("How good are they? 0-10")
        # Use while loop here to test inputs
        self.army2 = Armies(str(army2_leader).strip(), int(army2_leadership))
        self.army1.hunnic_army()
        time.sleep(5)
        self.army2.roman_army()

    def battle(self):
        time.sleep(5)
        self.battler.fight(self.army1, self.army2)

