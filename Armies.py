from army_methods import Army_methods

class Armies(Army_methods):

    # Setting variables to none by defualt so they do not to need to specified when creating the class
    def __init__(self, size=None, culture=None, fatigue=None):
        super().__init__(size, culture, fatigue)

    def roman_army(self):
        self.size = 10
        self.culture = "roman"
        self.fatigue = False

    def hunnic_army(self):
        self.size = 5
        self.culture = "hunnic"
        self.fatigue = False