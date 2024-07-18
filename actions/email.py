from utilities import start, step, completion
import time

def email():
    print("\nPlease enter the message that you would like to send:")
    message = input("")
    print("\nPreparing data...")

    phases = [
        "application layer -- your email is being formatted using the Simple Mail Transfer Protocol",
        "transport layer -- your email is being segmented and encapsulated with TCP headers",
        "network layer -- each segment is becoming a packet and being encapsulated in headers that includes the source and destination IP addresses",
        "data link layer -- each packet is being encapsulated in frames that include the MAC address",
        "physical layer -- each frame is being converted into radio signals to be sent over the Wi-Fi network",
        "network routing -- routers and switches are directing the frames to the destination mail server",
        "data reception -- the mail server is processing the frames, processes the packets, and reassembles the data packets",
        "data handling -- the email is being stored on the mail server",
        "display"
    ]

    for i in range(len(phases)):
        start("Entering phase " + str(i) + phases[i])

        if phases[i] == "display":
            step("Retrieving email from the server")
            step("Reassembling the data")
            step("Displaying email")

        completion(i)

    print("\nThe recipient has now received this message:")
    print(message)
    time.sleep(1)
