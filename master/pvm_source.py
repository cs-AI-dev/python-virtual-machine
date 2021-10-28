# Dragonscale Python Virtual Machine (for Windows)
# For limiting Python's memory and time usage

import os
import sys
from sys import argv as clInput

version = "0.0.1"

bg = "black"
fg = "white"
red = "red"
green = "lime"
def font(size):
	return ("OCR A Extended", int(size))

# Ensure TK is installed
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

# - Root and title

master = Tk()
master.config(bg=bg)

title = Label(master, text=f"Dragonscale Python Virtual Machine v{version}", font=font(24), bg=bg, fg=fg)
title.grid(row=1, column=1)

# - Root and title

# - Standard output redirecting

# IO redirector object passed to an Stdout redirector because
# for some reason the system's stdout passto in tkinter requires
# an object as an argument.
class StdoutRedirectorInternal(object):
	def __init__(self,text_area):
		self.text_area = text_area

class StdoutRedirector(StdoutRedirectorInternal):
	def write(self,str):
		self.text_area.write(str,False)
		
printOutput = Label(master, text=" [ Dragonscale PVM stdout redirect ]", font=font(12), bg=bg, fg=fg)
printOutput.config(height=20, width=30)

sys.stdout = StdoutRedirector(printOutput)

stdoutRedirecting = True

outputRedirectEnabled = True
def ToggleStdoutRedirect():
	if stdoutRedirecting == True:
		stdoutRedirecting = False
		sys.stdout = sys.__stdout__
	elif stdoutRedirecting == False:
		stdoutRedirecting = True
		sys.stdout = StdoutRedirector(printOutput)
	
def DisableStdoutRedirect():
	stdoutRedirecting = False
	sys.stdout = sys.__stdout__
	
def EnableStdoutRedirect():
	stdoutRedirecting = True
	sys.stdout = StdoutRedirector(printOutput)
	
printOutput.grid(row=2, column=1)
	
# - Standard output redirecting

# - File selection bar

fileSelectionBar = Frame(master, bg=bg)
				 
fileSelectionBarLabel = Label(fileSelectionBar, text="Select a file to execute", bg=bg, fg=fg, font=font(12))
fileSelectionBarLabel.config(width=10) # Might need changing in future
fileSelectionBarLabel.grid(row=1, column=1)

fileSelectionTextField = Text(fileSelectionBar, bg=bg, fg=fg, font=font(12), insetoff=250, inseton=100, bd=)
fileSelectionTextField.grid(row=1, column=2)

def ExecuteTargetedFile():
	with open(fileSelectionTextField.get(), "r") as targetFile:
		exec(targetFile.read()) # Not the most secure method as of right now, I'm working on it

fileSelectionButton = Button(fileSelectionBar, bg=bg, fg=fg, font=font(12), text="Execute", font=font(12), command=ExecuteTargetedFile)
fileSelectionButton.grid(row=1, column=2)

master.bind("<Return>", ExecuteTargetedFile)
				 
fileSelectionBar.grid(row=3, column=1)

# - File selection bar
