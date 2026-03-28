import os

print("Team Daily Status")

#Archive rute
FILE_PATH = "database.txt"

def add_blocker():
#Request and save Blocker
    blocker = input("Enter your daly blocker: ").strip()
    
    if not blocker :
        print("No blocker was entered.")
        return
    
    # Save in "Add" ('a')
    with open(FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(blocker + "\n")
    
    print(f"Blocker Saved: '{blocker}'")


def get_blocker():
   #Read and Display Saved Lockers
    # Check if the file exist
    if not os.path.exists(FILE_PATH):
        print("No blockd saved yet.")
        return
    
    print("\nStored Blockers:")
    print("-" * 40)
    
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        if not lines:
            print("There are no saved blockers yet.")
            return
        
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")
    
    print("-" * 40)


def main():
    print("=== Daly Blocker sistem Loggin ===\n")
    
    while True:
        print("\nOptions:")
        print("1. Add daly Blocker")
        print("2. Vew Blockers Saved")
        print("3. Exit")
        
        opcion = input("\nChoose one option (1-3): ").strip()
        
        if opcion == "1":
            add_blocker()
        elif opcion == "2":
            get_blocker()
        elif opcion == "3":
            print("Bye, Bye!")
            break
        else:
            print("Invalid option Please try again")

if __name__ == "__main__":
    print("=== Saly Blockers loggin system ===\n")
    main()

    #Error reports will be submitted via email to ensure prompt review by the team.

