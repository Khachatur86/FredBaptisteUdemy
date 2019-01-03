class Warrior:
    def __init__(self):
        self.health = 50
        self.damage = 5

    @property
    def is_alive(self):
        return self.health > 0

    def info(self):
        return self.health, self.damage, self.is_alive


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.damage = 7


def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.health -= unit_1.damage

        if unit_2.health <= 0:
            # print(f"unit_1.health = {unit_1.health}, unit_2.health = {unit_2.health}")
            return unit_1.health >= unit_2.health

        unit_1.health -= unit_2.damage
        # print(f"unit_1.health = {unit_1.health}, unit_2.health = {unit_2.health}")

    return unit_1.health >= unit_2.health


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

print('fight(chuck, bruce) ', fight(chuck, bruce))  # == True
print('fight(dave, carl) ', fight(dave, carl))  # == False
print('chuck ', chuck.is_alive)  # == True
print('bruce ', bruce.is_alive, bruce.health)  # == False
print('carl ', carl.is_alive, carl.health)  # == True
print('dave ', dave.is_alive)  # == False
print('fight(carl, mark) ', fight(carl, mark))  # == False
print('carl ', carl.is_alive, carl.health)  # == False
print(0 > 0)

# khachatur = Warrior()
# senja = Knight()
# print('1',fight(khachatur, senja))
# print(senja.health, khachatur.health )
# print('2',fight(senja, khachatur))
# print()

# print('3',fight(khachatur, senja))

# print('1', khachatur.info())
# print(senja.info())
# senja = Knight()
# print('1',fight(khachatur, senja))
# print(senja.health, khachatur.health )
# print('2',fight(senja, khachatur))
# print()

# print('3',fight(khachatur, senja))

# print('1', khachatur.info())
# print(senja.info())