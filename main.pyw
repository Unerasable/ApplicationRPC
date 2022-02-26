from calendar import c
from os import stat
from cv2 import createHanningWindow
from pypresence import Presence # The simple rich presence client in pypresence
import time
import tkinter as tk
from win32gui import GetWindowText, GetForegroundWindow
import json
import os
client_id = "947001875239145492"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop

def update():
    data = {"firefox":f"{var1.get()}", "chrome":f"{var2.get()}", "opera":f"{var3.get()}", "edge":f"{var4.get()}", "minecraft":f"{var5.get()}", "discord":f"{var6.get()}", "visual studio code":f"{var7.get()}", "notepad":f"{var8.get()}", "steam":f"{var9.get()}", "microsoft teams":f"{var10.get()}", "adobe acrobat reader":f"{var11.get()}", "photoshop":f"{var12.get()}", "blender":f"{var13.get()}", "gimp":f"{var14.get()}", "inkscape":f"{var15.get()}", "unity":f"{var16.get()}"}
    with open("./data.json", "w") as f:
        json.dump(data, f)
window = tk.Tk()
window.title('Application RPC')
window.geometry('500x500')
var1 = tk.IntVar()  
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()
var10 = tk.IntVar()
var11 = tk.IntVar()
var12 = tk.IntVar()
var13 = tk.IntVar()
var14 = tk.IntVar()
var15 = tk.IntVar()
var16 = tk.IntVar()
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()
c1 = tk.Checkbutton(window, text='Firefox', onvalue=1, offvalue=0,variable=var1)
c1.pack()
c2 = tk.Checkbutton(window, text='Chrome', onvalue=1, offvalue=0,variable=var2)
c2.pack()
c3 = tk.Checkbutton(window, text='Opera', onvalue=1, offvalue=0,variable=var3)
c3.pack()
c4 = tk.Checkbutton(window, text='Edge', onvalue=1, offvalue=0,variable=var4)
c4.pack()
c5 = tk.Checkbutton(window, text='Minecraft', onvalue=1, offvalue=0,variable=var5)
c5.pack()
c6 = tk.Checkbutton(window, text='Discord', onvalue=1, offvalue=0,variable=var6)
c6.pack()
c7 = tk.Checkbutton(window, text='Visual Studio Code', onvalue=1, offvalue=0,variable=var7)
c7.pack()
c8 = tk.Checkbutton(window, text='Notepad', onvalue=1, offvalue=0,variable=var8)
c8.pack()
c9 = tk.Checkbutton(window, text='Steam', onvalue=1, offvalue=0,variable=var9)
c9.pack()
c10 = tk.Checkbutton(window, text='Microsoft Teams', onvalue=1, offvalue=0,variable=var10)
c10.pack()
c11 = tk.Checkbutton(window, text='Adobe Acrobat Reader', onvalue=1, offvalue=0,variable=var11)
c11.pack()
c12 = tk.Checkbutton(window, text='Photoshop', onvalue=1, offvalue=0,variable=var12)
c12.pack()
c13 = tk.Checkbutton(window, text='Blender', onvalue=1, offvalue=0,variable=var13)
c13.pack()
c14 = tk.Checkbutton(window, text='GIMP', onvalue=1, offvalue=0,variable=var14)
c14.pack()
c15 = tk.Checkbutton(window, text='Inkscape', onvalue=1, offvalue=0,variable=var15)
c15.pack()
c16 = tk.Checkbutton(window, text='Unity', onvalue=1, offvalue=0,variable=var16)
c16.pack()
btn = tk.Button(window, text='Update', command=lambda: update())
btn.pack()
window.mainloop()
with open("./data.json", "r") as f:
    data = json.load(f)
while True:
    crtWin = GetWindowText(GetForegroundWindow())
    x = crtWin.split('-')
    if "Firefox" in crtWin and data["firefox"] == "1":
        RPC.update(state="Firefox", details="Using Firefox", large_image="firefox")
    elif "Chrome" in crtWin and data["chrome"] == "1":
        RPC.update(state="Chrome", details="Using Chrome", large_image="chrome")
    elif "Opera" in crtWin and data["opera"] == "1":
        RPC.update(state="Opera", details="Using Opera", large_image="opera")
    elif "Edge" in crtWin and data["edge"] == "1":
        RPC.update(state="Edge", details="Using Edge", large_image="edge")
    elif "minecraft" in crtWin.lower() and data["minecraft"] == "1":
        RPC.update(state="Minecraft", details="Playing Minecraft", large_image="minecraft")
    elif "discord" in crtWin.lower() and data["discord"] == "1":
        try:
            if x[1].lower() != " discord":
                if "discord" in x[0].lower():
                    RPC.update(state="Discord", details="Reading DMs", large_image="discord")
                else:
                    RPC.update(state="Discord", details=f"Reading {x[0]}-{x[1]}", large_image="discord")
            else:
                if "discord" in x[0].lower():
                    RPC.update(state="Discord", details="Reading DMs", large_image="discord")
                else:
                    RPC.update(state="Discord", details=f"Reading {x[0]}", large_image="discord")
        except:
            RPC.update(state="Discord", details="Reading DMs", large_image="discord")
    elif "visual studio code" in crtWin.lower() and data["visual studio code"] == "1":
        if "visual studio code" in x[0].lower():
            RPC.update(state="Visual Studio Code", details=f"Using Visual Studio Code", large_image="vscode")
        else:
            RPC.update(state="Visual Studio Code", details=f"Editing {x[0]}", large_image="vscode")
    elif "notepad" in crtWin.lower() and data["notepad"] == "1":
        if "notepad" in x[0].lower():
            RPC.update(state="Notepad", details="Using Notepad", large_image="notepad")
        else:
            RPC.update(state="Notepad", details=f"Editing {x[0]}", large_image="notepad")
    elif "steam" in crtWin.lower() and data["steam"] == "1":
        RPC.update(state="Steam", details="Playing Steam", large_image="steam")
    elif "teams" in crtWin.lower() and data["teams"] == "1":
        RPC.update(state="Teams", details="Using Teams", large_image="teams")
    elif "adobe acrobat" in crtWin.lower() and data["adobe acrobat"] == "1":
        if "adobe acrobat" in x[0].lower():
            RPC.update(state="Adobe Acrobat", details="Using Adobe Acrobat", large_image="adobeacrobat")
        else:
            RPC.update(state="Adobe Acrobat", details=f"Editing {x[0]}", large_image="adobeacrobat")
    elif "photoshop" in crtWin.lower() and data["photoshop"] == "1":
        if "photoshop" in x[0].lower():
            RPC.update(state="Photoshop", details="Using Photoshop", large_image="photoshop")
        else:
            RPC.update(state="Photoshop", details=f"Editing {x[0]}", large_image="photoshop")
    elif "blender" in crtWin.lower() and data["blender"] == "1":
        if "blender" in x[0].lower():
            RPC.update(state="Blender", details="Using Blender", large_image="blender")
        else:
            RPC.update(state="Blender", details=f"Editing {x[0]}", large_image="blender")
    elif "gimp" in crtWin.lower() and data["gimp"] == "1":
        if "gimp" in x[0].lower():
            RPC.update(state="GIMP", details="Using GIMP", large_image="gimp")
        else:
            RPC.update(state="GIMP", details=f"Editing {x[0]}", large_image="gimp")
    elif "inkscape" in crtWin.lower() and data["inkscape"] == "1":
        if "inkscape" in x[0].lower():
            RPC.update(state="Inkscape", details="Using Inkscape", large_image="inkscape")
        else:
            RPC.update(state="Inkscape", details=f"Editing {x[0]}", large_image="inkscape")
    elif "unity" in crtWin.lower() and data["unity"] == "1":
        if "unity" in x[0].lower():
            RPC.update(state="Unity", details="Using Unity", large_image="unity")
        else:
            RPC.update(state="Unity", details=f"Editing {x[0]}", large_image="unity")
    else:
        RPC.clear()