#!/usr/local/bin/python3

import tkinter
from tkinter import ttk

import enchanting, npcgen, weathergen, alchemy

def main():
	master = tkinter.Tk()
	universal_height = 500
	nb = ttk.Notebook(master, width=700, height=500)
	enchanting.getTab(nb)
	npcgen.getTab(nb)
	weathergen.getTab(nb)
	alchemy.getTab(nb)
	nb.grid(column=0)
	master.mainloop()

if __name__ == "__main__":
	main()