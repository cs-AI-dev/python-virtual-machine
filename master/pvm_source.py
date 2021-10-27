# Dragonscale Python Virtual Machine (for Windows)
# For limiting Python's memory and time usage

version = "0.0.1

bg = "black"
fg = "white"
red = "red"
green = "lime"
def font(size):
	return ("OCR A Extended", int(size))

# Ensure TK is installed
import os
try:
	os.system("py pip install tk -q")
except:
	try:
		os.system("python pip install tk -q")
	except:
		print("[ERROR] Could not install Tkinter for GUI")
		exit()
finally:
	from tkinter import *
	print("Tkinter GUI framework install complete, loading VM GUI ...")
	
# Construct GUI
master = Tk()
master.config(bg=bg)

title = Label(master, text=f"Dragonscale Python Virtual Machine v{version}", font=font(24), bg=bg, fg=fg)
title.grid(row=1, column=1)
