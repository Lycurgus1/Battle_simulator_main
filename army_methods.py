class Army_methods:

    def __init__(self, size=None, culture=None, fatigue=None):
        self.size = size
        self.culture = culture
        self.fatigue = fatigue

    def recruit(self):
        increase = int(input("How big is the army increase?"))
        self.size = self.size + increase
        return "Your army is now", self.size, "k strong"

    def rest(self):
        self.fatigue = False
        print("Your army has been rested and is no longer refreshed")

    def battle(self):
        self.fatigue = True
        print("You fight and tire your army out")


# nash = Armies(10, "celtic", False)
# print(nash.battle())
# print((nash.rest()))
# print(nash.recruit())