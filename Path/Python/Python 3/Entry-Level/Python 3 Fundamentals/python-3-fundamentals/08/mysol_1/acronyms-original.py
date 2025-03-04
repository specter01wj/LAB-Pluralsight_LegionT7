def find_acronym():
    """Search for an acronym in the acronyms file."""
    look_up = input("🔍 Enter the software acronym to look up:\n").strip().upper()

    if not look_up:
        print("⚠️ Acronym cannot be empty.")
        return

    found = False
    try:
        with open('acronyms.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # Strip spaces & hidden characters
                acronym, _, definition = line.strip().partition(" - ")
                cleaned_acronym = acronym.strip().upper()

                # Debugging print to check exact values
                print(f"DEBUG: Stored Acronym: '{cleaned_acronym}', Searching For: '{look_up}'")

                if cleaned_acronym == look_up:
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

    # Open file with UTF-8 encoding
    with open('acronyms.txt', 'a', encoding='utf-8') as file:
        file.write(f"{acronym} - {definition}\n")

    print(f"✅ Acronym '{acronym}' added successfully!")

def clean_acronym_file():
    """Removes hidden characters and extra spaces from the file."""
    try:
        with open('acronyms.txt', 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # Remove blank lines & spaces

        with open('acronyms.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + "\n")

        print("✅ File formatting fixed! Try searching again.")

    except FileNotFoundError:
        print("❌ No acronym file found. Add an acronym first.")

def main():
    """Main function to handle acronym lookup and addition."""
    while True:
        choice = input("\n📌 Do you want to Find (F), Add (A), or Clean File (C)? (Q to Quit):\n").strip().upper()
        
        if choice == "F":
            find_acronym()
        elif choice == "A":
            add_acronym()
        elif choice == "C":
            clean_acronym_file()
        elif choice == "Q":
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 'F' to find, 'A' to add, 'C' to clean, or 'Q' to quit.")

if __name__ == "__main__":
    main()
