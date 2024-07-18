from utilities import start, step, completion
import time

def website() -> str | None:
    global site

    print("\nWhich website would you like to visit? \n 1. Gmail \n 2. YouTube \n 3. Spotify")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        site = "Gmail"
    elif choice == 2:
        site = "YouTube"
    elif choice == 3:
        site = "Spotify"
    else:
        print("Sorry, that isn't an option. Please try again.")
        website()

def browse():
    website()

    phases = [
        "Domain Name System (DNS) lookup",
        "connection establishment -- the browser is initiating a TCP connection to the web server using the resolved IP on port 80 (HTTP) or port 443 (HTTPS)",
        "HTTP handshake sending -- the browser is sending an HTTP GET request to the server for the specified resource",
        "server processing",
        "data trasmission",
        "browser processing",
        "page rendering"
    ]

    for i in range(len(phases)):
        start("Entering phase " + str(i) + phases[i])

        if i == 1:
            step("Checking browser cache")
            step("Checking Operating System cache")
            step("Querying the configured DNS server")
            step("Performing recursive queries to find the authoritative DNS server for the domain")
            step("Returning the IP address of the webs erver hosting the website")
        elif i == 2:
            step("SYN - the client is sending a SYN (synchronize) packet to the server")
            step("SYN-ACK - the server is responding with a SYN-ACK (synchronize-acknowledge) packet")
            step("ACK - the client is sending an ACK (acknowledge) packet back to the server")
        elif i == 4:
            step("Processing the HTTP request")
            step("Retrieving the requested resource (e.g. HTML file)")
            step("Preparing an HTTP response")
        elif i == 5:
            step("Server is sending the HTTP response back to the browser")
            step("Breaking down response data into smaller packets for internet transmission")
        elif i == 6:
            step("Receiving the data packets and reassembling into a complete HTTP response")
            step("Parsing the HTML file and processing the document structure and elements")
            step("Identifying additional resources needed (CSS, JavaScript, images) and sending HTTP requests to the server for each of the needed resources")
        elif i == 7:
            step("Processing CSS")
            step("Executing JavaScript")
            step("Constructing the Document Object Model and rendering the visual representation of the web page on the screen")

        completion(i)

    print("\nNow opening " + site)
    time.sleep(1)
