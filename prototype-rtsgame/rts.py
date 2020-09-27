from copy import deepcopy
from abc import ABC, ABCMeta, abstractmethod

from random import randint

names = ["Lane",
"Thiago",
"Melany",
"Bode",
"Tyler",
"Selene",
"Zayden",
"Audra",
"Uriah",
"Milah"]

class Prototype(ABC):
    
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def clone_with_name(self):
        pass

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "knight"
        self.name = "Anything"

        with open("./"+self.unit_type + ".dat", 'r') as f:
            lines = f.read().split("\n")
            self.hp = lines[0]
            self.atk = int(lines[1]) * level #SOME USE FOR LEVEL, COULD BE ANYTHING...
            self.weapon = lines[2]

    def clone(self):
        return deepcopy(self)

    def clone_with_name(self):
        knight = deepcopy(self)

        knight.name = names[randint(0, len(names) - 1)]

        return knight

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "archer"
        self.name = "Anything"

        with open("./"+self.unit_type + ".dat", 'r') as f:
            lines = f.read().split("\n")
            self.hp = lines[0]
            self.atk = int(lines[1]) * level
            self.weapon = lines[2]
    
    def clone(self):
        return deepcopy(self)

    def clone_with_name(self):
        archer = deepcopy(self)

        archer.name = names[randint(0, len(names) - 1)]

        return archer

class Barracks():
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2),
            },
            "archer": {
                1: Archer(1),
                2: Archer(2),
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone() #Makes a clone insted of instantiating a new one (which is 'costly') 

    def build_unit_named(self, unit_type, level):
        return self.units[unit_type][level].clone_with_name()

class Training_Grounds():
    def __init__(self):
        self.current_units = []

    def assign_unit(self, unit):
        self.current_units.append(unit) #Maybe use a dict here?
        #SET A "BLOCK" FOR THE UNIT PASSED HERE...
    
    def remove_unit(self, unit):
        #DO THIS WITH A TIME MEASURE, AFTER TIME PASSES, RELEASE THE UNIT WITH ENHANCEMENTS

        for cur_unit in self.current_units:
            if unit == cur_unit:
                unit.atk += 10
                self.current_units.remove(unit)
                return unit

if __name__ == "__main__":
    b1 = Barracks()
    
    k1 = b1.build_unit("knight", 2)
    k2 = b1.build_unit("knight", 2)

    a1 = b1.build_unit("archer", 1)
    a2 = b1.build_unit("archer", 2)

    a3 = b1.build_unit_named("archer", 2)

    print(k1)
    print(k2)
    print(a1)
    print(a2)

    print(k1.name)
    print(k2.name)
    print(a1.name)
    print(a2.name)

    print(a3.name)

    tg1 = Training_Grounds() #Something for playing

    print(k1.atk)

    tg1.assign_unit(k1)
    tg1.remove_unit(k1)

    print(k1.atk)