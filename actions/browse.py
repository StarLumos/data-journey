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

    start("Entering phase 1: Domain Name System (DNS) lookup")
    step("Checking browser cache")
    step("Checking Operating System cache")
    step("Querying the configured DNS server")
    step("Performing recursive queries to find the authoritative DNS server for the domain")
    step("Returning the IP address of the webs erver hosting the website")
    completion(1)

    start("Entering phase 2: connection establishment -- the browser is initiating a TCP connection to the web server using the resolved IP on port 80 (HTTP) or port 443 (HTTPS)")
    step("SYN - the client is sending a SYN (synchronize) packet to the server")
    step("SYN-ACK - the server is responding with a SYN-ACK (synchronize-acknowledge) packet")
    step("ACK - the client is sending an ACK (acknowledge) packet back to the server")
    completion(2)

    start("Entering phase 3: HTTP handshake sending -- the browser is sending an HTTP GET request to the server for the specified resource")
    completion(3)

    start ("Entering phase 4: server processing")
    step("Processing the HTTP request")
    step("Retrieving the requested resource (e.g. HTML file)")
    step("Preparing an HTTP response")
    completion(4)

    start("Entering phase 5: data trasmission")
    step("Server is sending the HTTP response back to the browser")
    step("Breaking down response data into smaller packets for internet transmission")
    completion(5)

    start("Entering phase 6: browser processing")
    step("Receiving the data packets and reassembling into a complete HTTP response")
    step("Parsing the HTML file and processing the document structure and elements")
    step("Identifying additional resources needed (CSS, JavaScript, images) and sending HTTP requests to the server for each of the needed resources")
    completion(6)

    start("Entering phase 7: page rendering")
    step("Processing CSS")
    step("Executing JavaScript")
    step("Constructing the Document Object Model and rendering the visual representation of the web page on the screen")
    completion(7)

    print("\nNow opening " + site)
    time.sleep(1)
