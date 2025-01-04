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
            # server connection
            clientsocket.connect((servername, serverport)) 

            #unique id
            client_ip = gethostbyname(gethostname())  
            client_id = hashlib.sha1(client_ip.encode()).hexdigest() 

            #sending
            message = {"client_id": client_id, "vote": vote}
            json_message = json.dumps(message)  # convert the message to json format so it can be understood by the server
            clientsocket.sendall(bytes(str(json_message), "utf-8")) 

            #response
            response = clientsocket.recv(1024).decode()
            print(response)
            messagebox.showinfo("Vote", response)
            clientsocket.close()

        except Exception as e:
            print(f"Error connecting to server {e}")
            messagebox.showerror("Error", "Server is closed, Votes haven't started yet!")
            return False
        
        
    threading.Thread(target=communicate, daemon=True).start()






