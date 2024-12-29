from socket import *
import threading
import hashlib
import time
from tkinter import messagebox

servername = 'localhost'  ## lazm yt8yr lel other device's ip
serverport = 12000

def send_to_server(vote):
    ## putting a function inside another function for threading purposes
    # threading so it doesnt block the main thread [UI]
    def communicate(): 
        
        clientsocket = socket(AF_INET, SOCK_STREAM)  # create a socket

        try:
            clientsocket.connect((servername, serverport)) # connects lel server
            client_ip = gethostbyname(gethostname())  #the unique server
            client_id = hashlib.sha1(client_ip.encode()).hexdigest() #hashing the ip to get a unique id
           ##  print(client_id) #print for debugging purposes

            message = {"client_id": client_id, "vote": vote} # the message is in the form of a dictionary
            clientsocket.sendall(bytes(str(message), "utf-8"))

            response = clientsocket.recv(1024).decode()
            print(response)
            messagebox.showinfo("Vote", response)
            clientsocket.close()

        except Exception as e:
            print(f"Error connecting to server {e}")
            return False
        
        
    threading.Thread(target=communicate, daemon=True).start()




## here we are testing the function
send_to_server("yes")
time.sleep(1)
send_to_server("no")
time.sleep(1)
send_to_server("yes")
time.sleep(1)
send_to_server("no")
time.sleep(1)





