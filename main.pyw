from os import stat
from cv2 import createHanningWindow
from pypresence import Presence # The simple rich presence client in pypresence
import time
from win32gui import GetWindowText, GetForegroundWindow
time.sleep(5)

client_id = "947001875239145492"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect() # Start the handshake loop




while True:
    crtWin = GetWindowText(GetForegroundWindow())
    x = crtWin.split('-')
    if "Firefox" in crtWin:
        RPC.update(state="Firefox", details="Using Firefox", large_image="firefox")
    elif "Chrome" in crtWin:
        RPC.update(state="Chrome", details="Using Chrome", large_image="chrome")
    elif "Opera" in crtWin:
        RPC.update(state="Opera", details="Using Opera", large_image="opera")
    elif "Edge" in crtWin:
        RPC.update(state="Edge", details="Using Edge", large_image="edge")
    elif "minecraft" in crtWin.lower():
        RPC.update(state="Minecraft", details="Playing Minecraft", large_image="minecraft")
    elif "discord" in crtWin.lower():
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
    elif "visual studio code" in crtWin.lower():
        if "visual studio code" in x[0].lower():
            RPC.update(state="Visual Studio Code", details=f"Using Visual Studio Code", large_image="vscode")
        else:
            RPC.update(state="Visual Studio Code", details=f"Editing {x[0]}", large_image="vscode")
    elif "notepad" in crtWin.lower():
        if "notepad" in x[0].lower():
            RPC.update(state="Notepad", details="Using Notepad", large_image="notepad")
        else:
            RPC.update(state="Notepad", details=f"Editing {x[0]}", large_image="notepad")
    elif "steam" in crtWin.lower():
        RPC.update(state="Steam", details="Playing Steam", large_image="steam")
    elif "teams" in crtWin.lower():
        RPC.update(state="Teams", details="Using Teams", large_image="teams")
    elif "adobe acrobat" in crtWin.lower():
        if "adobe acrobat" in x[0].lower():
            RPC.update(state="Adobe Acrobat", details="Using Adobe Acrobat", large_image="adobeacrobat")
        else:
            RPC.update(state="Adobe Acrobat", details=f"Editing {x[0]}", large_image="adobeacrobat")
    elif "photoshop" in crtWin.lower():
        if "photoshop" in x[0].lower():
            RPC.update(state="Photoshop", details="Using Photoshop", large_image="photoshop")
        else:
            RPC.update(state="Photoshop", details=f"Editing {x[0]}", large_image="photoshop")
    elif "blender" in crtWin.lower():
        if "blender" in x[0].lower():
            RPC.update(state="Blender", details="Using Blender", large_image="blender")
        else:
            RPC.update(state="Blender", details=f"Editing {x[0]}", large_image="blender")
    elif "gimp" in crtWin.lower():
        if "gimp" in x[0].lower():
            RPC.update(state="GIMP", details="Using GIMP", large_image="gimp")
        else:
            RPC.update(state="GIMP", details=f"Editing {x[0]}", large_image="gimp")
    elif "inkscape" in crtWin.lower():
        if "inkscape" in x[0].lower():
            RPC.update(state="Inkscape", details="Using Inkscape", large_image="inkscape")
        else:
            RPC.update(state="Inkscape", details=f"Editing {x[0]}", large_image="inkscape")
    elif "unity" in crtWin.lower():
        if "unity" in x[0].lower():
            RPC.update(state="Unity", details="Using Unity", large_image="unity")
        else:
            RPC.update(state="Unity", details=f"Editing {x[0]}", large_image="unity")
    else:
        RPC.clear()