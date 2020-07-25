from armies import Armies

army1 = Armies("Attila", 10)
army2 = Armies("Aetius", 3)
obj1 = Armies()

army1.hunnic_army()
army2.roman_army()

obj1.fight(army1, army2)