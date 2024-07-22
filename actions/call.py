from utilities import start, step, completion
import time

def recipient() -> str:
    print("\n".join(["\nWho would you like to call?",
        "1. Doctor Strange",
        "2. Shang-Chi",
        "3. Captain Marvel"]))
    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Sorry, that isn't an option. Please try again.")
        return recipient()
    choice = int(choice)

    if choice == 1:
        return "Doctor Strange"
    elif choice == 2:
        return "Shang-chi"
    elif choice == 3:
        return "Captain Marvel"
    else:
        print("Sorry, that isn't an option. Please try again.")
        return recipient()

def call():
    person = recipient()

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
        steps = []

        match i:
            case 1:
                steps = ["Generating a call setup request"]
            case 2:
                steps = [
                    "Converting the call setup request into radio frequency (RF) signals",
                    "Transmitting to the nearest cell tower"
                ]
            case 3:
                steps = [
                    "Nearest cell tower receiving RF signals and converting them into digital data",
                    "Forwaring the call setup request to the nearest mobile switching center (MSC)"
                ]
            case 4:
                steps = [
                    "MSC processing the call request",
                    "Identifying the destination number",
                    "Determining the best route to the recipient's phone",
                    "MSC sending a setup request to the recipient's nearest MSC to identify the nearest cell tower to them"
                ]
            case 7:
                steps = [
                    "Recipient's phone receiving the RF signals",
                    "Converting back to digital data",
                    "Triggering the ringtone to notify the recipient of the incoming call"
                ]
            case _:
                raise ValueError()

        for it in steps:
            step(it)

        completion(i)

    print("\nNow calling " + person)
    time.sleep(1)
