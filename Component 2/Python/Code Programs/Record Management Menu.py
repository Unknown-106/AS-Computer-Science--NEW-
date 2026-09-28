# Record Management Menu
# Azhi Amin
# 23/09/2026
# OCR AS Computer Science

#...
def addRecord():
    try:
        print("Added a record.")
    except Exception as e:
        print("Error occurred:",e)

#...
def updateRecord():
    try:
        print("Updated a record.")
    except Exception as e:
        print("Error occurred:",e)

#...
def deleteRecord():
    try:
        print("Deleted a record.")
    except Exception as e:
        print("Error occurred:",e)

def closeMenu(state):
    try:
        confirm = "."
        confirm = input("Are you sure you want to quit? ")
        if confirm == "Y" or "Yes" or "yes":
            state = False
        else:
            print("Returning to Manage Records.")
            print("Welcome to the Record Management Menu")
    except Exception as e:
        print("Error occurred:",e)

#...
def Main_Menu():
    try:
        state = True
        option = -1
        print("Welcome to the Record Management Menu")
        while state == True:
            option = int(input("Manage Records:\n1: Add\n2: Update\n3: Delete\n\n"))
            if option == 1:
                addRecord()
            elif option == 2:
                updateRecord()
            elif option == 3:
                deleteRecord()
            elif option == 0:
                closeMenu(state)
            print("\n")
        print("Menu closed.")
    except Exception as e:
        print("Error occurred:",e)


def main():
    try:
        Main_Menu()
    except Exception as e:
        print("Error occurred:",e)
    

#program starts here
if (__name__ == "__main__"):
    main()
