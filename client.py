from socket import *
import threading
import json
import hashlib
import time # for testing purposes
from tkinter import messagebox




def send_to_server(vote):
    
    # threading so it doesnt block the main thread [UI]
    def communicate(): 
        
        clientsocket = socket(AF_INET, SOCK_STREAM) 
        servername = gethostbyname(gethostname())  # dynamically get the IP address
        serverport = 12000
                                                    

        try:
            clientsocket.connect((servername, serverport)) # connects lel server
            client_ip = gethostbyname(gethostname())  #the unique server
            client_id = hashlib.sha1(client_ip.encode()).hexdigest() #hashing the ip to get a unique id
           ##  print(client_id) #print for debugging purposes

            message = {"client_id": client_id, "vote": vote}
            json_message = json.dumps(message)  # convert the message to json format
            clientsocket.sendall(bytes(str(json_message), "utf-8")) 

            response = clientsocket.recv(1024).decode()
            print(response)
            messagebox.showinfo("Vote", response)
            clientsocket.close()

        except Exception as e:
            print(f"Error connecting to server {e}")
            return False
        
        
    threading.Thread(target=communicate, daemon=True).start()






