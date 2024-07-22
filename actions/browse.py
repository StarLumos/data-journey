from utilities import start, step, completion
import time

def website() -> str:
    print("\n".join(["\nWhich website would you like to visit?",
        "1. Gmail",
        "2. YouTube",
        "3. Spotify"]))
    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Sorry, that isn't an option. Please try again.")
        website()
    choice = int(choice)

    if choice == 1:
        return "Gmail"
    elif choice == 2:
        return "YouTube"
    elif choice == 3:
        return "Spotify"
    else:
        print("Sorry, that isn't an option. Please try again.")
        return website()

def browse():
    site = website()

    phases = [
        "Domain Name System (DNS) lookup",
        "connection establishment -- the browser is initiating a TCP connection to the web server using the resolved IP on port 80 (HTTP) or port 443 (HTTPS)",
        "HTTP handshake sending -- the browser is sending an HTTP GET request to the server for the specified resource",
        "server processing",
        "data trasmission",
        "browser processing",
        "page rendering"
    ]

    for i, phase in enumerate(phases):
        start("Entering phase " + str(i) + phase)
        steps: list[str]

        match i:
            case 1:
                steps = [
                    "Checking browser cache",
                    "Checking Operating System cache",
                    "Querying the configured DNS server",
                    "Performing recursive queries to find the authoritative DNS server for the domain",
                    "Returning the IP address of the webs erver hosting the website"
                ]
            case 2:
                steps = [
                    "SYN - the client is sending a SYN (synchronize) packet to the server",
                    "SYN-ACK - the server is responding with a SYN-ACK (synchronize-acknowledge) packet",
                    "ACK - the client is sending an ACK (acknowledge) packet back to the server"
                ]
            case 4:
                steps = [
                    "Processing the HTTP request",
                    "Retrieving the requested resource (e.g. HTML file)",
                    "Preparing an HTTP response"
                ]
            case 5:
                steps = [
                    "Server is sending the HTTP response back to the browser",
                    "Breaking down response data into smaller packets for internet transmission"
                ]
            case 6:
                steps = [
                    "Receiving the data packets and reassembling into a complete HTTP response",
                    "Parsing the HTML file and processing the document structure and elements",
                    "Identifying additional resources needed (CSS, JavaScript, images) and sending HTTP requests to the server for each of the needed resources"
                ]
            case 7:
                steps = [
                    "Processing CSS",
                    "Executing JavaScript",
                    "Constructing the Document Object Model and rendering the visual representation of the web page on the screen"
                ]
            case _:
                raise ValueError()

        for it in steps:
            step(it)
        completion(i)

    print("\nNow opening " + site)
    time.sleep(1)
