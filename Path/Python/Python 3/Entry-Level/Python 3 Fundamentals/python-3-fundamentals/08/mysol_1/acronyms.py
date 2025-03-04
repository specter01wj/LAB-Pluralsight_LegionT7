def find_acronym(filename, acronym):
    """Search for an acronym in the given file."""
    acronym = acronym.strip().upper()  # Normalize input for case-insensitive search

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                stored_acronym, _, definition = line.strip().partition(" - ")
                
                if stored_acronym.upper() == acronym:  # Exact match check
                    print(f"✅ {stored_acronym} - {definition}")
                    return line.strip()

    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        return False

    print("❌ The acronym does not exist.")
    return False

def add_acronym(filename, acronym, definition):
    """Add a new acronym and its definition to the file."""
    acronym = acronym.strip().upper()
    definition = definition.strip()

    if not acronym or not definition:
        print("⚠️ Acronym and definition cannot be empty.")
        return False

    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{acronym} - {definition}\n")
        print(f"✅ Acronym '{acronym}' added successfully!")
        return True
    except OSError:
        print(f"❌ Cannot open '{filename}' for writing.")
    return False

if __name__ == "__main__":
    filename = 'software_acronyms.txt'
    
    while True:
        choice = input("\n📌 Do you want to Find (F) or Add (A) an acronym? (Q to Quit): ").strip().upper()

        if choice == 'F':
            look_up = input("🔍 What software acronym would you like to look up?\n")
            find_acronym(filename, look_up)
        elif choice == 'A':
            acronym = input("➕ What acronym do you want to add?\n")
            definition = input(f"📝 What is the definition for '{acronym}'?\n")
            add_acronym(filename, acronym, definition)
        elif choice == 'Q':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 'F' to find, 'A' to add, or 'Q' to quit.")
