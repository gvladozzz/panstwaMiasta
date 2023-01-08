import socket
import time
# import random
import tkinter as tk
from tkinter import messagebox
import pickle

class Player():
    def __init__(self, connection, address):
        self.connection=connection
        self.address=address
        # self.round1=round1
        # self.round2=round2
        # self.round3=round3
        # self.summaryPoints=summaryPoints
        self.errors=0
        self.stop_letter=False

def identify_stops_player():
    global stops_player
    stops_player = int(stops_player_label.cget("text"))-1
    if stops_player<0:stops_player=len(players)
    stops_player_label.config(text=str(stops_player))
    log.config(state=tk.NORMAL)
    log.insert("1.0", f"Stops player changed to {str(stops_player)};\n")
    log.config(state=tk.DISABLED)
def identify_stops_player2():
    global stops_player
    stops_player = int(stops_player_label.cget("text"))+1
    if stops_player>len(players):stops_player=0#random.randint(0, len(players))
    stops_player_label.config(text=str(stops_player))
    log.config(state=tk.NORMAL)
    log.insert("1.0", f"Stops player changed to {str(stops_player)};\n")
    log.config(state=tk.DISABLED)
    
root = tk.Tk()
launched = True

"""functions"""
def on_closing():
    global launched, root
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        launched = False

"""variables"""
#other
alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
active_round=1
switch=True
switch2=True
switch3=True
counter=0
round_label=tk.Label(root,text=f"Round - {str(active_round)}")
identify_stops_player_button = tk.Button(root, text="<---", command=identify_stops_player)
identify_stops_player_button2 = tk.Button(root, text="--->", command=identify_stops_player2)
stops_player_label=tk.Label(root, text="0")
stops_player_label2=tk.Label(root, text="Stops player is")

connection_list=tk.Text(root, state=tk.DISABLED, width=45, height=20)
log=tk.Text(root, state=tk.DISABLED, width=45, height=20)

connection_list.grid(column=0, rowspan=50)
log.grid(column=0, rowspan=50)
round_label.grid(column=1, row=0)
identify_stops_player_button.grid(column=1, row=1)
identify_stops_player_button2.grid(column=2, row=1)
stops_player_label.grid(column=2, row=2)
stops_player_label2.grid(column=1, row=2)

connection_list.config(bg="#1a1a1a", fg="white")
log.config(bg="#1a1a1a", fg="white")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
server.bind(("localhost", 10000))
server.setblocking(False)
server.listen(5)
players=[]
print("Socket created;")

root.attributes('-zoomed', True)
root.title("Państwa Miasta (server)")
root.protocol("WM_DELETE_WINDOW", on_closing)
# root.mainloop()

while True:
    if launched:
        root.update_idletasks()
        root.update()
        try:
            new_socket, address = server.accept()
            print(f"Player {address} has joined;")
            connection_list.config(state=tk.NORMAL)
            connection_list.insert("1.0", f"Player {address} has joined;\n")
            connection_list.config(state=tk.DISABLED)
            new_socket.setblocking(False)
            new_player=Player(new_socket, address)
            players.append(new_player)
            new_socket.send(pickle.dumps(str(players.index(new_player))))
            
        except:pass
            # print("No one wants to join the game")           
        for player in players:
            try:
                sendmessage = {
                    "stopPlayer": stops_player_label.cget("text")
                }
                print(sendmessage)
                sendmessageB = pickle.dumps(sendmessage)
                print(sendmessageB)
                player.connection.send(sendmessageB)
                player.errors=0
            except:
                player.errors+=1
                if player.errors<=100:
                    players.remove(player)
                    player.connection.close()
                    print(f"Player {address} disconnected;\n")
                    connection_list.config(state=tk.NORMAL)
                    connection_list.insert("1.0", f"Player {address} disconnected;\n")
                    connection_list.config(state=tk.DISABLED)
        time.sleep(0.1)
    else: break
server.close()