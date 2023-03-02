import socket
import tkinter as tk
import os
from tkinter import messagebox
import time
import pickle
root = tk.Tk()
launched = True
iAmStopsPlayer = False

"""functions"""
def on_closing():
	global launched, root
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
		launched = False

def stopRound():
    global active_round, panstwo_entry_r1
    if active_round==1:
        panstwo_entry_r1.config(state=tk.DISABLED)
        miasto_entry_r1.config(state=tk.DISABLED)
        zwierze_entry_r1.config(state=tk.DISABLED)
        roslina_entry_r1.config(state=tk.DISABLED)
        imie_entry_r1.config(state=tk.DISABLED)
        gotownosc_r1_button.config(state=tk.DISABLED)
        active_round=2
        round_label.config(text=f"Round - {active_round}")
        count()
        sendMessager1 = {
            "round": str(active_round-1),
            "panstwo" : panstwo_entry_r1.get(),
            "miasto" : miasto_entry_r1.get(),
            "zwierze" : zwierze_entry_r1.get(),
            "roslina" : roslina_entry_r1.get(),
            "imie" : imie_entry_r1.get()
        }
        sendmessageBr1 = pickle.dumps(sendMessager1)
        sock.send(sendmessageBr1)
        print(f"Sent data: {sendMessager1}")
        point_r1_label.config(text=str(int(panstwo_point_r1_label.cget("text"))+int(miasto_point_r1_label.cget("text"))+int(zwierze_point_r1_label.cget("text"))+int(roslina_point_r1_label.cget("text"))+int(imie_point_r1_label.cget("text"))))
    elif active_round==2:
        panstwo_entry_r2.config(state=tk.DISABLED)
        miasto_entry_r2.config(state=tk.DISABLED)
        zwierze_entry_r2.config(state=tk.DISABLED)
        roslina_entry_r2.config(state=tk.DISABLED)
        imie_entry_r2.config(state=tk.DISABLED)
        gotownosc_r2_button.config(state=tk.DISABLED)
        active_round=3
        round_label.config(text=f"Round - {active_round}")
        count()

        sendMessager2 = {
            "round": str(active_round-1),
            "panstwo" : panstwo_entry_r2.get(),
            "miasto" : miasto_entry_r2.get(),
            "zwierze" : zwierze_entry_r2.get(),
            "roslina" : roslina_entry_r2.get(),
            "imie" : imie_entry_r2.get()
        }
        sendmessageBr2 = pickle.dumps(sendMessager2)
        sock.send(sendmessageBr2)
        print(f"Sent data: {sendMessager2}")
        point_r2_label.config(text=str(int(panstwo_point_r2_label.cget("text")) + int(miasto_point_r2_label.cget("text")) + int(zwierze_point_r2_label.cget("text")) + int(roslina_point_r2_label.cget("text")) + int(imie_point_r2_label.cget("text"))))
    elif active_round==3:
        panstwo_entry_r3.config(state=tk.DISABLED)
        miasto_entry_r3.config(state=tk.DISABLED)
        zwierze_entry_r3.config(state=tk.DISABLED)
        roslina_entry_r3.config(state=tk.DISABLED)
        imie_entry_r3.config(state=tk.DISABLED)
        gotownosc_r3_button.config(state=tk.DISABLED)
        active_round=1
        round_label.config(text=f"Round - {active_round}")
        count()
        sendMessager3 = {
            "round": str(active_round-1),
            "panstwo" : panstwo_entry_r3.get(),
            "miasto" : miasto_entry_r3.get(),
            "zwierze" : zwierze_entry_r3.get(),
            "roslina" : roslina_entry_r3.get(),
            "imie" : imie_entry_r3.get()
        }
        sendmessageBr3 = pickle.dumps(sendMessager3)
        sock.send(sendmessageBr3)
        print(f"Sent data: {sendMessager3}")
        point_r3_label.config(text=str(int(panstwo_point_r3_label.cget("text")) + int(miasto_point_r3_label.cget("text")) + int(zwierze_point_r3_label.cget("text")) + int(roslina_point_r3_label.cget("text")) + int(imie_point_r3_label.cget("text"))))
        points_summary_label.config(text="Summary: "+str(int(point_r1_label.cget("text")) + int(point_r2_label.cget("text")) + int(point_r3_label.cget("text"))))

def count():
    global counter, letters_r1_label, letters_r2_label, letters_r3_label, switch, active_round
    if active_round == 1:
        if switch:
            counter += 1
            if counter == 26:
                counter = 0
            letters_r1_label.config(text=alphabet[counter])
            letters_r1_label.after(500, count)
        else: pass
    elif active_round == 2:
        if switch2:
            # r2_stop_button.config(state=tk.NORMAL)
            counter += 1
            if counter == 26:
                counter = 0
            letters_r2_label.config(text=alphabet[counter])
            letters_r2_label.after(500, count)
    elif active_round == 3:
        if switch3:
            # r3_stop_button.config(state=tk.NORMAL)
            counter += 1
            if counter == 26:
                counter = 0
            letters_r3_label.config(text=alphabet[counter])
            letters_r3_label.after(500, count)
sw1=True
sw2=True
sw3=True
def stopletter():
    global switch, switch2, switch3, sw1, sw2, sw3
    if active_round==1:
        if iAmStopsPlayer:
            data = {"type" : "stopsPlayer",
                    "round" : active_round,
                    "ready" : True,
                    "number" : number,
                    "letter" : letters_r1_label.cget("text")
                    }
            dataB = pickle.dumps(data)
            print(data, "\n", dataB, "\n")
            sock.send(dataB)
        active_r1_letter=letters_r1_label.cget("text")
        switch=False
        r1_stop_button.config(state=tk.DISABLED)
        gotownosc_r1_button.config(state=tk.NORMAL)
        panstwo_entry_r1.config(state=tk.NORMAL)
        miasto_entry_r1.config(state=tk.NORMAL)
        zwierze_entry_r1.config(state=tk.NORMAL)
        roslina_entry_r1.config(state=tk.NORMAL)
        imie_entry_r1.config(state=tk.NORMAL)
        sw1=False
        messagebox.showinfo("Active letter", f"Active letter is: {active_r1_letter}")
    elif active_round==2:
        active_r2_letter=letters_r2_label.cget("text")
        switch2=False
        r2_stop_button.config(state=tk.DISABLED)
        gotownosc_r2_button.config(state=tk.NORMAL)
        panstwo_entry_r2.config(state=tk.NORMAL)
        miasto_entry_r2.config(state=tk.NORMAL)
        zwierze_entry_r2.config(state=tk.NORMAL)
        roslina_entry_r2.config(state=tk.NORMAL)
        imie_entry_r2.config(state=tk.NORMAL)
        sw2=False
        messagebox.showinfo("Active letter", f"Active letter is: {active_r2_letter}")
    elif active_round==3:
        active_r3_letter=letters_r3_label.cget("text")
        switch3=False
        r3_stop_button.config(state=tk.DISABLED)
        gotownosc_r3_button.config(state=tk.NORMAL)
        panstwo_entry_r3.config(state=tk.NORMAL)
        miasto_entry_r3.config(state=tk.NORMAL)
        zwierze_entry_r3.config(state=tk.NORMAL)
        roslina_entry_r3.config(state=tk.NORMAL)
        imie_entry_r3.config(state=tk.NORMAL)
        sw3=False
        messagebox.showinfo("Active letter", f"Active letter is: {active_r3_letter}")

#other
alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
active_round=1
switch=True
switch2=True
switch3=True
counter=0
number="0"
stopsPlayer="0"
#label (topics)
round_label = tk.Label(text=f"Round - {active_round}")
panstwo_label = tk.Label(text="Państwo")
miasto_label = tk.Label(text="Miasto")
zwierze_label = tk.Label(text="Zwierzę")
roslina_label = tk.Label(text="Roślina")
imie_label = tk.Label(text="Imię")
gotownosc_label = tk.Label(text="Gotowność")
points_label = tk.Label(text="Punkty")
#label (letters)
letters_r1_label = tk.Label(text="A")
letters_r2_label = tk.Label(text="A")
letters_r3_label = tk.Label(text="A")
#label (points)
point_r1_label = tk.Label(text="0")
point_r2_label = tk.Label(text="0")
point_r3_label = tk.Label(text="0")
points_summary_label = tk.Label(text="Summary: 0")
#label (points of topic, round-1)
panstwo_point_r1_label = tk.Label(text="1")
miasto_point_r1_label = tk.Label(text="1")
zwierze_point_r1_label = tk.Label(text="1")
roslina_point_r1_label = tk.Label(text="1")
imie_point_r1_label = tk.Label(text="1")
#label (points of topic, round-2)
panstwo_point_r2_label = tk.Label(text="2")
miasto_point_r2_label = tk.Label(text="2")
zwierze_point_r2_label = tk.Label(text="2")
roslina_point_r2_label = tk.Label(text="2")
imie_point_r2_label = tk.Label(text="2")
#label (points of topic, round-3)
panstwo_point_r3_label = tk.Label(text="3")
miasto_point_r3_label = tk.Label(text="3")
zwierze_point_r3_label = tk.Label(text="3")
roslina_point_r3_label = tk.Label(text="3")
imie_point_r3_label = tk.Label(text="3")
#entry (round-1)
panstwo_entry_r1 = tk.Entry(state=tk.DISABLED)
miasto_entry_r1 = tk.Entry(state=tk.DISABLED)
zwierze_entry_r1 = tk.Entry(state=tk.DISABLED)
roslina_entry_r1 = tk.Entry(state=tk.DISABLED)
imie_entry_r1 = tk.Entry(state=tk.DISABLED)
#entry (round-2)
panstwo_entry_r2 = tk.Entry(state=tk.DISABLED)
miasto_entry_r2 = tk.Entry(state=tk.DISABLED)
zwierze_entry_r2 = tk.Entry(state=tk.DISABLED)
roslina_entry_r2 = tk.Entry(state=tk.DISABLED)
imie_entry_r2 = tk.Entry(state=tk.DISABLED)
#entry (round-1)
panstwo_entry_r3 = tk.Entry(state=tk.DISABLED)
miasto_entry_r3 = tk.Entry(state=tk.DISABLED)
zwierze_entry_r3 = tk.Entry(state=tk.DISABLED)
roslina_entry_r3 = tk.Entry(state=tk.DISABLED)
imie_entry_r3 = tk.Entry(state=tk.DISABLED)
#button (stop)

r1_stop_button = tk.Button(text="STOP", state=tk.DISABLED ,command=stopletter)
r2_stop_button = tk.Button(text="STOP", state=tk.DISABLED, command=stopletter)
r3_stop_button = tk.Button(text="STOP", state=tk.DISABLED, command=stopletter)
#button (readiness)
gotownosc_r1_button = tk.Button(text="Gotowy", state=tk.DISABLED, command=stopRound)
gotownosc_r2_button = tk.Button(text="Gotowy", state=tk.DISABLED, command=stopRound)
gotownosc_r3_button = tk.Button(text="Gotowy", state=tk.DISABLED, command=stopRound)
#other
# myNumber_label=tk.Label(root, text="Your number is: "+str(number))
# stopsPlayer_label=tk.Label(root, text="Stops player is: "+str(stopsPlayer))

"""config"""
#entry (round-1)
panstwo_entry_r1.config(width=10)
miasto_entry_r1.config(width=10)
zwierze_entry_r1.config(width=10)
roslina_entry_r1.config(width=10)
imie_entry_r1.config(width=10)
#entry (round-2)
panstwo_entry_r2.config(width=10)
miasto_entry_r2.config(width=10)
zwierze_entry_r2.config(width=10)
roslina_entry_r2.config(width=10)
imie_entry_r2.config(width=10)
#entry (round-1)
panstwo_entry_r3.config(width=10)
miasto_entry_r3.config(width=10)
zwierze_entry_r3.config(width=10)
roslina_entry_r3.config(width=10)
imie_entry_r3.config(width=10)
#label (letters)
letters_r1_label.config(width=2)
letters_r2_label.config(width=2)
letters_r3_label.config(width=2)
#label (points of topic, round-1)
panstwo_point_r1_label.config(width=2)
miasto_point_r1_label.config(width=2)
zwierze_point_r1_label.config(width=2)
roslina_point_r1_label.config(width=2)
imie_point_r1_label.config(width=2)
#label (points of topic, round-2)
panstwo_point_r2_label.config(width=2)
miasto_point_r2_label.config(width=2)
zwierze_point_r2_label.config(width=2)
roslina_point_r2_label.config(width=2)
imie_point_r2_label.config(width=2)
#label (points of topic, round-3)
panstwo_point_r3_label.config(width=2)
miasto_point_r3_label.config(width=2)
zwierze_point_r3_label.config(width=2)
roslina_point_r3_label.config(width=2)
imie_point_r3_label.config(width=2)

#button (stop)
r1_stop_button.grid(column=0, row=1)
r2_stop_button.grid(column=0, row=2)
r3_stop_button.grid(column=0, row=3)
#button (gotownosc)
gotownosc_r1_button.grid(column=12, row=1)
gotownosc_r2_button.grid(column=12, row=2)
gotownosc_r3_button.grid(column=12, row=3)
#label (topics)
round_label.grid(column=0, row=0)
panstwo_label.grid(column=2, row=0)
miasto_label.grid(column=4, row=0)
zwierze_label.grid(column=6, row=0)
roslina_label.grid(column=8, row=0)
imie_label.grid(column=10, row=0)
gotownosc_label.grid(column=12,row=0)
points_label.grid(column=13, row=0)
#label (letters)
letters_r1_label.grid(column=1, row=1)
letters_r2_label.grid(column=1, row=2)
letters_r3_label.grid(column=1, row=3)
#label (points)
point_r1_label.grid(column=13, row=1)
point_r2_label.grid(column=13, row=2)
point_r3_label.grid(column=13, row=3)
points_summary_label.grid(column=13, row=4)
#label (points of topic, round-1)
panstwo_point_r1_label.grid(column=3, row=1)
miasto_point_r1_label.grid(column=5, row=1)
zwierze_point_r1_label.grid(column=7, row=1)
roslina_point_r1_label.grid(column=9, row=1)
imie_point_r1_label.grid(column=11, row=1)
#label (points of topic, round-2)
panstwo_point_r2_label.grid(column=3, row=2)
miasto_point_r2_label.grid(column=5, row=2)
zwierze_point_r2_label.grid(column=7, row=2)
roslina_point_r2_label.grid(column=9, row=2)
imie_point_r2_label.grid(column=11, row=2)
#label (points of topic, round-3)
panstwo_point_r3_label.grid(column=3, row=3)
miasto_point_r3_label.grid(column=5, row=3)
zwierze_point_r3_label.grid(column=7, row=3)
roslina_point_r3_label.grid(column=9, row=3)
imie_point_r3_label.grid(column=11, row=3)
#entry (round-1)
panstwo_entry_r1.grid(column=2, row=1)
miasto_entry_r1.grid(column=4, row=1)
zwierze_entry_r1.grid(column=6, row=1)
roslina_entry_r1.grid(column=8, row=1)
imie_entry_r1.grid(column=10, row=1)
#entry (round-2)
panstwo_entry_r2.grid(column=2, row=2)
miasto_entry_r2.grid(column=4, row=2)
zwierze_entry_r2.grid(column=6, row=2)
roslina_entry_r2.grid(column=8, row=2)
imie_entry_r2.grid(column=10, row=2)
#entry (round-3)
panstwo_entry_r3.grid(column=2, row=3)
miasto_entry_r3.grid(column=4, row=3)
zwierze_entry_r3.grid(column=6, row=3)
roslina_entry_r3.grid(column=8, row=3)
imie_entry_r3.grid(column=10, row=3)
#other
# myNumber_label.grid(column=0, row=4)
# stopsPlayer_label.grid(column=1, row=4)
count()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(("localhost", 10000))
sw=True
root.title("Państwa Miasta")
root.protocol("WM_DELETE_WINDOW", on_closing)

while True:
    if launched:
        root.update_idletasks()
        root.update()
        # try:
        #     number=sock.recv(1024)
        #     number=number.decode()
        #     print(number)
        # except:pass
        if sw==True:
            number=sock.recv(2048)
            number=pickle.loads(number)
            print("Your number is: ",number)
            tk.Label(text="Your number is: "+str(number)).grid(column=0, row=4)
            sw=False
        try:
            data=sock.recv(2048)
            data=pickle.loads(data)
            # print(data)
            stopsPlayer=data["stopPlayer"]
        except:pass
        if int(number)==int(stopsPlayer):
            iAmStopsPlayer=True
            # print(stopsPlayer, number)
        else:
            iAmStopsPlayer=False
        if active_round == 1:
            if sw1:
                if iAmStopsPlayer:
                    r1_stop_button.config(state=tk.NORMAL)
                else:
                    r1_stop_button.config(state=tk.DISABLED)
        elif active_round == 2:
            if sw2:
                if iAmStopsPlayer:
                    r2_stop_button.config(state=tk.NORMAL)
                else:
                    r2_stop_button.config(state=tk.DISABLED)
        elif active_round == 3:
            if sw3:
                if iAmStopsPlayer:
                    r3_stop_button.config(state=tk.NORMAL)
                else:
                    r3_stop_button.config(state=tk.DISABLED)
        time.sleep(0.1)
    else:break