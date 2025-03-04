def find_acronym():
    """Search for an acronym in the acronyms file."""
    look_up = input("🔍 Enter the software acronym to look up:\n").strip().upper()

    if not look_up:
        print("⚠️ Acronym cannot be empty.")
        return

    found = False
    try:
        with open('acronyms.txt', 'r') as file:
            for line in file:
                acronym, _, definition = line.partition(" - ")
                if acronym.strip().upper() == look_up:
                    print(f"✅ {acronym.strip()} - {definition.strip()}")
                    found = True
                    break
    except FileNotFoundError:
        print("❌ File not found. No acronyms available yet.")
        return

    if not found:
        print("❌ The acronym does not exist.")

def add_acronym():
    """Add a new acronym and its definition to the file."""
    acronym = input("➕ Enter the acronym to add:\n").strip().upper()
    if not acronym:
        print("⚠️ Acronym cannot be empty.")
        return

    definition = input(f"📝 Enter the definition for {acronym}:\n").strip()
    if not definition:
        print("⚠️ Definition cannot be empty.")
        return

    with open('acronyms.txt', 'a') as file:
        file.write(f"{acronym} - {definition}\n")

    print(f"✅ Acronym '{acronym}' added successfully!")

def main():
    """Main function to handle acronym lookup and addition."""
    while True:
        choice = input("\n📌 Do you want to Find (F) or Add (A) an acronym? (Q to Quit):\n").strip().upper()
        
        if choice == "F":
            find_acronym()
        elif choice == "A":
            add_acronym()
        elif choice == "Q":
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 'F' to find, 'A' to add, or 'Q' to quit.")

if __name__ == "__main__":
    main()
