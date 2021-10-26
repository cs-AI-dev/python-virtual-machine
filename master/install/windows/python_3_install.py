import os
try:
	os.system("python pip install tk -q")
except:
	print("[ERROR] Error installing TKinter for DS-PVM installation GUI.")
	exit()
	
from tkinter import *

sbg = "black"
sfg = "white"

def Font(size):
	return ("OCR A Extended", int(size))
	
master = Tk()
master.configure(bg="black")
master.title("DS Python VM Installer")

title = Label(master, text="Dragonscale Python Virtual Machine Installer", fg=sfg, bg=sbg, font=font(36))
title.grid(row=1, column=1)

subtitle_1 = Label(master, text="Welcome to the DS PVM installer. Please select a", fg=sfg, bg=sbg, font=font(14))
subtitle_1.grid(row=2, column=1)

subtitle_2 = Label(master, text="directory for your PVM to be installed at.", fg=sfg, bg=sbg, font=font(14))
subtitle_2.grid(row=2, column=1)

targetButton

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

if __name__ == "__main__":
	master.mainloop()
