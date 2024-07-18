from utilities import start, step, completion
import time

def recipient() -> str | None:
    global person

    print("\nWho would you like to call? \n 1. Doctor Strange \n 2. Shang-Chi \n 3. Captain Marvel")
    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Sorry, that isn't an option. Please try again.")
        return recipient()
    choice = int(choice)

    if choice == 1:
        person = "Doctor Strange"
        return
    elif choice == 2:
        person = "Shang-chi"
        return
    elif choice == 3:
        person = "Captain Marvel"
        return
    else:
        print("Sorry, that isn't an option. Please try again.")
        recipient()

def call():
    recipient()

    phases = [
        "call initiation",
        "signal trasmission to cell tower",
        "cell tower processing",
        "MSC handling",
        "signal transmission to recipient's cell tower -- the recipient's MSC is routing the call setup request to the appropriate cell tower",
        "signal transmission to recipient's phone -- the cell tower transforms the digital setup request into radio frequency (RF) signals",
        "call notification"
    ]

    for i in range(len(phases)):
        start("Entering phase " + str(i) + phases[i])

        if i == 1:
            step("Generating a call setup request")
        elif i == 2:
            step("Converting the call setup request into radio frequency (RF) signals")
            step("Transmitting to the nearest cell tower")
        elif i == 3:
            step("Nearest cell tower receiving RF signals and converting them into digital data")
            step("Forwaring the call setup request to the nearest mobile switching center (MSC)")
        elif i == 4:
            step("MSC processing the call request")
            step("Identifying the destination number")
            step("Determining the best route to the recipient's phone")
            step("MSC sending a setup request to the recipient's nearest MSC to identify the nearest cell tower to them")
        elif i == 7:
            step("Recipient's phone receiving the RF signals")
            step("Converting back to digital data")
            step("Triggering the ringtone to notify the recipient of the incoming call")

        completion(i)

    print("\nNow calling " + person)
    time.sleep(1)
