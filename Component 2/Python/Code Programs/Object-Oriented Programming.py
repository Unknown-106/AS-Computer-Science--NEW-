# [Program Name]
# Azhi Amin
# 21/10/2026
# OCR AS Computer Science


# Standard Libraries
pass

# Third Party Libraries
pass

# Local Modules
pass


# Defining a Class.
class Monster():

    # Constructor
    def __init__(self, name, health):
        #attributes
        self.name = name
        self.health = health

    # Destructor
    def __del__(self):
        print(f"{self.name} has been destroyed!")

    # 1st Method
    def roar(self):
        print(f"{self.name} ROARS!")

    # 2nd Method
    def takeDamage(self, damage):
        self.health -= damage
        print(f"{self.name} now has {self.health} health.")

    # 3rd Method
    def attack(self, enemy):
        print(f"{self.name} Attacks {enemy.name}.")
        enemy.takeDamage(20)

#Creating objects: monster1, monster2, monster3
monster1 = Monster("Goblin", 100)
monster2 = Monster("Dragon", 200)
monster3 = Monster("Colossus", 1000)

print(monster1.name)
print(monster1.health)

print(monster2.name)
print(monster2.health)

print(monster3.name)
print(monster3.health)


# Main Sequence
def main():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
