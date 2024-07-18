from utilities import start, step, completion
import time

def recipient() -> str | None:
    global person

    print("\nWho would you like to call? \n 1. Doctor Strange \n 2. Shang-Chi \n 3. Captain Marvel")
    choice = int(input("\nEnter your choice: "))
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

    start("Entering phase 1: call intiation")
    step("Generating a call setup request")
    completion(1)

    start("Entering phase 2: signal trasmission to cell tower")
    step("Converting the call setup request into radio frequency (RF) signals")
    step("Transmitting to the nearest cell tower")
    completion(2)

    start("Entering phase 3: cell tower processing")
    step("Nearest cell tower receiving RF signals and converting them into digital data")
    step("Forwaring the call setup request to the nearest mobile switching center (MSC)")
    completion(3)

    start ("Entering phase 4: MSC handling")
    step("MSC processing the call request")
    step("Identifying the destination number")
    step("Determining the best route to the recipient's phone")
    step("MSC sending a setup request to the recipient's nearest MSC to identify the nearest cell tower to them")
    completion(4)

    start("Entering phase 5: signal transmission to recipient's cell tower -- the recipient's MSC is routing the call setup request to the appropriate cell tower")
    completion(5)

    start("Entering phase 6: signal transmission to recipient's phone -- the cell tower transforms the digital setup request into radio frequency (RF) signals")
    completion(6)

    start("Entering phase 7: call notification")
    step("Recipient's phone receiving the RF signals")
    step("Converting back to digital data")
    step("Triggering the ringtone to notify the recipient of the incoming call")
    completion(7)

    print("\nNow calling " + person)
    time.sleep(1)
