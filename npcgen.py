#!/usr/local/bin/python3

from tkinter import ttk
import tkinter as tk
import random

def getTab(nb):
    page2 = ttk.Frame(nb, width=500, height=500)
    racetxt = tk.Text(page2, width=20, height=2)
    racetxt.pack()
    nb.add(page2, text='NpcGen')

    """list of races, classes(concepts) and gender"""
    race = ['Argonian',
            'Khajiit',
            'Altmer',
            'Bosmer',
            'Dunmer',
            'Orismer',
            'Imperial',
            'Nord',
            'Redguard',
            'Breton']

    gender = ['Female',
            'Male']

    """what happens if you push the Random button, it generates pseudo-random numbers and puts race and the like in the textfield."""
    def randomize():
        """clear"""
        racetxt.delete(1.0,tk.END)
        """random races"""
        raceInt = random.randrange(0,len(race))
        raceRand = race[raceInt]
        racetxt.insert(tk.END, raceRand)
        """random gender"""
        sexInt = random.randrange(0,len(gender))
        genderRand = gender[sexInt]
        racetxt.insert(tk.END, ', ' + genderRand)

    randombutton = tk.Button(page2, text='Random', command=randomize)
    randombutton.pack()

