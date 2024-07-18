from utilities import start, step, completion
import time

def email():
    print("\nPlease enter the message that you would like to send:")
    message = input("")
    print("\nPreparing data...")

    start("Entering phase 1: application layer -- your email is being formatted using the Simple Mail Transfer Protocol")
    completion(1)

    start("Entering phase 2: transport layer -- your email is being segmented and encapsulated with TCP headers")
    completion(2)

    start("Entering phase 3: network layer -- each segment is becoming a packet and being encapsulated in headers that includes the source and destination IP addresses")
    completion(3)

    start("Entering phase 4: data link layer -- each packet is being encapsulated in frames that include the MAC address")
    completion(4)

    start("Entering phase 5: physical layer -- each frame is being converted into radio signals to be sent over the Wi-Fi network")
    completion(5)

    start("Entering phase 6: network routing -- routers and switches are directing the frames to the destination mail server")
    completion(6)

    start("Entering phase 7: data reception -- the mail server is processing the frames, processes the packets, and reassembles the data packets")
    completion(7)

    start("Entering phase 8: data handling -- the email is being stored on the mail server")
    completion(8)

    start("Entering phase 9: display")
    step("Retrieving email from the server")
    step("Reassembling the data")
    step("Displaying email")
    completion(9)

    print("\nThe recipient has now received this message:")
    print(message)
    time.sleep(1)
