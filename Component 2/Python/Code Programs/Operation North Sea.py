# Operation North Sea
# Azhi Amin
# 21/10/2026
# OCR AS Computer Science


# Standard Libraries
import inspect

# Third Party Libraries
pass

# Local Modules
pass


#
class Warship:

    def __init__(self, name, hull, firepower):
        self.name = name
        self.hull = hull
        self.firepower = firepower

    def reportStatus(self):
        print(inspect.cleandoc(f"""
            Ship Name: {self.name}
            Hull Integrity: {self.hull}
            Firepower: {self.firepower}
        """))

    def receiveHit(self, enemy, damage):
        print(f"{self.name} took a hit from {enemy}!")
        self.hull = max(0, self.hull - damage)
        print(f"{self.name} has {self.hull} hull remaining.")

    def fireAt(self, target):
        print(f"{self.name} is firing against {target.name}.")
        target.receiveHit(self.name, self.firepower)

ship1 = Warship("HMS Resolute", 120, 25)
ship2 = Warship("HMS Vanguard", 160, 35)

# ...
def one():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# Main Sequence
def main():
    try:
        ship1 = Warship("HMS Resolute", 120, 25)
        ship2 = Warship("HMS Vanguard", 160, 35)

        ship1.reportStatus()
        ship2.reportStatus()

        ship1.fireAt(ship2)
        ship2.fireAt(ship1)
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
