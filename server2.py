import socket
import threading
import hashlib
import os
import json

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

# Function to process a vote (store in a simple file for now)
def process_vote(client_id, vote):
    # Simulate storing the vote (in reality, this should be handled more securely)
    vote_filename = "votes.txt"

    with open(vote_filename, "a") as file:
        file.write(f"{client_id}: {vote}\n")
    print(f"Vote recorded: {client_id} voted {vote}")
# Function to start the server and listen for incoming client connections
def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((SERVER_NAME, SERVER_PORT))
    print(f"Server started on {SERVER_NAME}:{SERVER_PORT}")

    # Start listening for incoming connections (max 5 connections in the backlog)
    server_socket.listen(5)

    # Continuously accept and handle client connections
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.daemon = True
        client_thread.start()

if __name__ == "__main__":
    if not os.path.exists("files"):
        os.makedirs("files")
    if not os.path.exists(CANDIDATE_FILE):
        with open(CANDIDATE_FILE, "w") as f:
            pass  # Create the file if it doesn't exist
    start_server()
