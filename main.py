from armies import Armies

army1 = Armies("Attila", 9)
army2 = Armies("Aetius", 7)
obj1 = Armies()

army1.hunnic_army()
army2.roman_army()

obj1.fight(army1, army2)