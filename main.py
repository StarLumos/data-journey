from actions.email import email
from actions.browse import browse
from actions.call import call

def choice():
    print("\n".join([
        "\nWhat would you like to do?",
        "1. Send an email",
        "2. Dial a call",
        "3. Visit a website"
    ]))
    initial = input("\nEnter the corresponding number: ")

    if not initial.isdigit():
        print("Sorry, that isn't an option. Please try again.")
        return choice()
    initial = int(initial)

    if initial == 1:
        email()
    elif initial == 2:
        call()
    elif initial == 3:
        browse()
    else:
        print("Sorry, that isn't an option. Please try again.")
        choice()

def after():
    print("\nWould you like to execute another action? (y/n)")
    next_action = input("Enter your answer: ").lower()

    if next_action == "y":
        return
    elif next_action == "n":
        print("\nThank you for operating!")
        exit()
    else:
        print("Sorry, but that's not an option. Please try again.")
        after()

def main():
    while True:
        choice()
        print("\nAction completed.")
        after()

if __name__ == "__main__":
    main()
