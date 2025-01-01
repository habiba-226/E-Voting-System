
# Define server constants
SERVER_NAME = 'localhost'  # Change this if using a remote server
SERVER_PORT = 12000
CANDIDATE_FILE = "files/candidates.txt"

# Create a lock to prevent race conditions on file access
file_lock = threading.Lock()

# Function to handle each client connection
def handle_client(client_socket, client_address):
    try:
        print(f"Connection from {client_address} established")

        # Receive and decode message from client
        message = client_socket.recv(1024).decode()
        if not message:
            return

        # Parse the message (should be a JSON string)
        try:
            data = json.loads(message)
            client_id = data.get('client_id')
            vote = data.get('vote')
        except json.JSONDecodeError:
            client_socket.sendall(b"Invalid message format")
            return

        # Process the vote (store in a file or database)
        with file_lock:
            process_vote(client_id, vote)

        # Respond to the client with a success message
        response = f"Vote for {vote} has been recorded successfully!"
        client_socket.sendall(response.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket
        client_socket.close()
