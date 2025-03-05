def save_note():
    """Saves user input as a note in a text file."""
    note = input("Write your note: ")
    
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    
    print("Note saved successfully!")


def view_notes():
    """Reads and displays all saved notes."""
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\nYour Notes:")
                for idx, note in enumerate(notes, start=1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found!")
    except FileNotFoundError:
        print("No notes found!")


# Menu for user interaction
while True:
    print("\n1. Write a Note")
    print("2. View Notes")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        save_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
