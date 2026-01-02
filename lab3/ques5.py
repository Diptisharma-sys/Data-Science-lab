### 5. Menu-Driven File Operations
### ● Write data to a file
### ● Read data from a file
### ● Append data to a file
### ● Handle invalid user input and file errors using exception handling



def write_file():
    try:
        with open("data.txt", "w") as f:
            text = input("Enter text to write: ")
            f.write(text + "\n")
        print("Data written successfully")
    except Exception as e:
        print("Error:", e)


def read_file():
    try:
        with open("data.txt", "r") as f:
            print("\nFile Contents:")
            print(f.read())
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error:", e)


def append_file():
    try:
        with open("data.txt", "a") as f:
            text = input("Enter text to append: ")
            f.write(text + "\n")
        print("Data appended successfully")
    except Exception as e:
        print("Error:", e)


while True:
    print("\n--- MENU ---")
    print("1. Write to file")
    print("2. Read file")
    print("3. Append to file")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            write_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            append_file()
        elif choice == 4:
            print("Exiting program")
            break
        else:
            print("Invalid choice! Enter 1–4")

    except ValueError:
        print("Please enter a valid number")

