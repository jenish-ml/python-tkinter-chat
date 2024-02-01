import socket
from tkinter import *

def send_message():
    message = entry.get()
    listbox.insert('end', "You: " + message)
    client_socket.send(message.encode("utf-8"))

def receive_message():
    message = client_socket.recv(1024).decode("utf-8")
    listbox.insert('end', "Client: " + message)

root = Tk()
root.title("Server")

entry = Entry(root, font=("Arial", 12))
entry.pack(side=BOTTOM, fill=X, padx=10, pady=10)

send_button = Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(side=RIGHT, padx=10, pady=10)

listbox = Listbox(root, font=("Arial", 12))
listbox.pack(fill=BOTH, expand=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()

receive_message_button = Button(root, text="Receive", font=("Arial", 12), command=receive_message)
receive_message_button.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
