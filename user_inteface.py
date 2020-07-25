from armies import Armies

class User_interface(Armies):

    def __init__(self, leader=None, leadership=None, size=None, culture=None, fatigue=None):
        # Inherting previous attributes
        super().__init__(leader, leadership, size, culture, fatigue)
        # Creating class objects for methods to run
        army1 = Armies("Attila", 10)
        army2 = Armies("Aetius", 3)
        obj1 = Armies()
        print("Welcome to a virtual battle simulator!")
        self.user_choice()

    def user_choice(self):
        x = True
        while x == True:
            user_input = input("What would you like to do: \n Exit E\n Run simulator R")
            if user_input in ["E", "R"]:
                x = False
            else:
                print("\nEnter either E or R, try again")

        if user_input == "E":
            pass