# python-tkinter-chat

This repository contains a basic chat application developed using Python and Tkinter library for the graphical user interface (GUI). The application utilizes socket programming to establish a client-server architecture, enabling real-time communication between users.

The repository consists of two main files:

client.py: This file contains the code for the client-side application. Users can input messages via a Tkinter entry widget and send them to the server.
server.py: This file contains the code for the server-side application. It listens for incoming connections from clients, receives messages, and broadcasts them to all connected clients.
Features:

User-friendly GUI: The Tkinter library is used to create a simple and intuitive graphical interface for sending and receiving messages.
Real-time Communication: Messages are sent and received in real-time, allowing for seamless conversations between users.
Client-Server Architecture: The application follows a client-server model, facilitating communication between multiple clients and a central server.
How to Use:

Clone the repository to your local machine.
Run the server-side application by executing python server.py in your terminal.
Run the client-side application by executing python client.py in another terminal.
Start sending and receiving messages between the client and server.
Requirements:

Python 3.x
Tkinter library (usually included with Python installations)
Contribution:
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

License:
This project is licensed under the MIT License. See the LICENSE file for details.