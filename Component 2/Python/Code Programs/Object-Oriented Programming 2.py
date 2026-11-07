# Object-Oriented Programming 2 
# Azhi Amin
# 02/11/2026
# OCR AS Computer Science


# Standard Libraries
from inspect import cleandoc

# Third Party Libraries
pass

# Local Modules
pass


# Build-a-Class
class Student:

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(cleandoc(f"""
            Name: {self.name}
            Age: {self.age}
            Student ID: {self.student_id}
        """))

    def __del__(self):
        print(f"Goodbye {self.name}.\n")


student1 = Student("Ari", 23, 34856927)
student1.display_info()
del student1
student2 = Student("Barry", 32, 72965843)
student2.display_info()
del student2


# Inheritance
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name) # calls parent constructor
        self.breed = breed

    def fetch(self):
        print(f"{self.name} fetches the ball!")

my_dog = Dog("Rex", "Labrador")
my_dog.speak() # inherited from Animal -> Rex makes a sound.
my_dog.fetch() # defined in Dog -> Rex fetches the ball!


# Main Sequence
def main():
    try:
        pass
    except Exception as e:
        print("Error occurred:", e)


# program starts here
if __name__ == "__main__":
    main()
