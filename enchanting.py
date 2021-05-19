#!/usr/local/bin/python3
import tkinter as tk
from tkinter import ttk
from collections import OrderedDict

"""define variables for use as global variables"""
Eff = 0
Mag = 0
Char = 0
Tar = 0
Dur = 0
toValue = 0

def getTab(nb):
    tab1 = ttk.Frame(nb, width=500)
    lbEffect = tk.Listbox(tab1, height=15, exportselection=False)
    lbEffect.grid(row=1, column=0, sticky=tk.N)
    lbTarget = tk.Listbox(tab1, height=2, exportselection=False)
    lbTarget.grid(row=1, column=1, sticky=tk.N)
    lbMagnitude = tk.Listbox(tab1, height=10, exportselection=False)
    lbMagnitude.grid(row=1, column=2, sticky=tk.N)
    lbCharges = tk.Listbox(tab1, height=7, exportselection=False)
    lbCharges.grid(row=1, column=3, sticky=tk.N)
    lbDuration = tk.Listbox(tab1, height=7, exportselection=False)
    lbDuration.grid(row=1, column=4, sticky=tk.N)
    Total = tk.Text(tab1, width=5, height=1)
    Total.grid(row=2, column=4, sticky=tk.N)
    nb.add(tab1, text='Enchanting')
    tk.Label(tab1, text='Effect').grid(row=0, column=0)
    tk.Label(tab1, text='Target').grid(row=0, column=1)
    tk.Label(tab1, text='Magnitude').grid(row=0, column=2)
    tk.Label(tab1, text='Charges').grid(row=0, column=3)
    tk.Label(tab1, text='Duration').grid(row=0, column=4)

    """Reset button to delete all input and calculate from start again"""
    def funcReset():
        global Eff, Mag, Char, Tar, Dur
        Eff = 0
        Mag = 0
        Char = 0
        Tar = 0
        Dur = 0

    resetButton = tk.Button(tab1, text="Reset", command=funcReset)
    resetButton.grid(row=2, column=2)







    """dictionaries with all the different effects, magnitudes, charges and duration"""
    dEffect = OrderedDict([('Damage', 10), ('Heal', 5), ('Drain Life', 20), ('Shield', 30), ('Elemental Shield', 20),
                           ('Fortify Ability', 30), ('Fear', 20), ('Light', -30), ('Detect Magic', 10),
                           ('Sense Hidden', 20), ('Dispel', 50), ('Invisibility', 50), ('Soul Trap', 20),
                           ('Paralyze', 100)])
    dMagnitudeDie = OrderedDict(
            [('1', 1), ('2', 2), ('1d4', 3), ('1d6', 5), ('1d8', 7), ('1d10', 9), ('2d4', 11), ('1d10', 13),
             ('1d12', 15)])
    dMagnitudeNum = OrderedDict(
            [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)])
    dMagnitudePercent = OrderedDict([('10%', 1), ('25%', 2), ('50%', 4), ('75%', 6), ('100%', 8)])
    dCharges = OrderedDict([('2', 0), ('5', 5), ('10', 10), ('20', 15), ('30', 20), ('40', 25), ('Unlimited', 50)])
    dTarget = OrderedDict([('Self', 0), ('Touch', 5)])
    dDuration = OrderedDict(
            [('Instant', 0), ('1 turn', 5), ('2 turns', 10), ('3 turns', 15), ('4 turns', 20), ('5 turns', 30),
             ('1 scene', 40), ('Permanent', 0), ('none', 0)])
    dDebuffMagnitude = OrderedDict([('Level 1-5', 1), ('Level 6-10', 2), ('Level 7-15', 3), ('Level 16-20', 4)])

    for kEf, vEf in dEffect.items():
        lbEffect.insert(tk.END, kEf)

    """Choose an Effect and make changes to listboxes to support that choice. And return the values."""

    def EffectSel(x):
        global toValue
        global Eff
        global Mag
        global Char
        global Dur
        global Tar
        global selEfCheck

        selEfCheck = lbEffect.curselection()
        selEf = lbEffect.get(lbEffect.curselection())
        Eff = dEffect[selEf]
        toValue = 0
        """Value Calculation"""
        if selEfCheck == (7,):
            toValue = Eff + Dur + Char + Tar
        else:
            toValue = (Eff * Mag) + Dur + Char + Tar

        Total.delete(1.0, tk.END)
        Total.insert(tk.END, toValue)

        """Delete Lisboxes"""
        lbDuration.delete(0, tk.END)
        lbCharges.delete(0, tk.END)
        lbTarget.delete(0, tk.END)

        """Determine Target
		if Effect is: AC, Energy Resistance, Enhance Ability, Light, Sense Magic, Sense Hidden or Invisibility. Then there will only be Self as target"""
        if selEfCheck == (3,) or selEfCheck == (4,) or selEfCheck == (5,) or selEfCheck == (7,) or selEfCheck == (
                8,) or selEfCheck == (9,) or selEfCheck == (11,):
            lbTarget.insert(tk.END, 'Self')

            """All other Effects. Self and Touch are possible targets"""
        else:
            for kTa in dTarget:
                lbTarget.insert(tk.END, kTa)

        """Determine Magnitude and Charges
		if Effect is number 0-5 from dictionary, then delete Magnitude and check if effect is either below 3, 4 or else
		if <3 then the magnitude will be die
		if 4 then it will be percentage
		else it will be numbered"""
        if selEfCheck < (6,):
            lbMagnitude.delete(0, tk.END)
            if selEfCheck < (3,):
                lbDuration.delete(0, tk.END)
                for kDie in dMagnitudeDie:
                    lbMagnitude.insert(tk.END, kDie)
                for kCh in dCharges:
                    lbCharges.insert(tk.END, kCh)

            elif selEfCheck == (4,):
                lbMagnitude.delete(0, tk.END)
                for kPercent in dMagnitudePercent:
                    lbMagnitude.insert(tk.END, kPercent)
                for kCh in dCharges:
                    lbCharges.insert(tk.END, kCh)

            else:
                lbDuration.delete(0, tk.END)
                for kCh in dCharges:
                    lbCharges.insert(tk.END, kCh)
                for kMag in dMagnitudeNum:
                    lbMagnitude.insert(tk.END, kMag)

            """if the Effect is Fear, Dispel or Paralyze, then the magnitude will be debuffmagnitude(level based magnitude)"""
        elif selEfCheck == (6,) or selEfCheck == (10,) or selEfCheck == (13,):
            lbMagnitude.delete(0, tk.END)
            for kLevel in dDebuffMagnitude:
                lbMagnitude.insert(tk.END, kLevel)
            for kCh in dCharges:
                lbCharges.insert(tk.END, kCh)
            """else there will be no magnitude"""
        else:
            lbMagnitude.delete(0, tk.END)
            for kCh in dCharges:
                lbCharges.insert(tk.END, kCh)

    """Choose Target and return value."""

    def TargetSel(x):
        global toValue
        global Eff
        global Mag
        global Char
        global Dur
        global Tar
        selTar = lbTarget.get(lbTarget.curselection())
        if selTar == 'Touch':
            Tar = 5
        elif selTar == 'Self':
            Tar = 0
        Tar = dTarget[selTar]
        toValue = 0
        """Value Calculation"""
        if selEfCheck == (7,):
            toValue = Eff + Dur + Char + Tar
        else:
            toValue = (Eff * Mag) + Dur + Char + Tar

        Total.delete(1.0, tk.END)
        Total.insert(tk.END, toValue)

        """Choose Charges and return values. Also if Charge unlimited, make the Duration Permanent."""

    def ChargesSel(x):
        global toValue
        global Eff
        global Mag
        global Char
        global Dur
        global Tar
        selCh = lbCharges.get(lbCharges.curselection())
        Char = dCharges[selCh]
        toValue = 0
        """Value Calculation"""
        toValue = (Eff * Mag) + Dur + Char + Tar

        lbDuration.delete(0, tk.END)
        """check if Unlimited Charges has been selected and sets Duration accordingly."""
        if selEfCheck == (0,) or selEfCheck == (1,) or selEfCheck == (2,) or selEfCheck == (10,):
            lbDuration.insert(tk.END, 'none')
        elif selEfCheck == (6,) or selEfCheck == (9,) or selEfCheck == (11,) or selEfCheck == (12,) or selEfCheck == (
                13,):
            for kDur in dDuration:
                if kDur != 'Permanent' and kDur != 'none':
                    lbDuration.insert(tk.END, kDur)
        else:
            for kDur in dDuration:
                if kDur != 'Permanent' and kDur != 'none':
                    lbDuration.insert(tk.END, kDur)
            if selCh == 'Unlimited':
                lbDuration.delete(0, tk.END)
                lbDuration.insert(tk.END, 'Permanent')

        Total.delete(1.0, tk.END)
        Total.insert(tk.END, toValue)

    """Choose Magnitude and return value. Also Check what Dictionary the Magnitude is."""

    def MagnitudeSel(x):
        global toValue
        global Eff
        global Mag
        global Char
        global Dur
        global Tar
        selMag = lbMagnitude.get(lbMagnitude.curselection())
        MagCheck = lbMagnitude.get(tk.END)
        if MagCheck == '1d12':
            Mag = dMagnitudeDie[selMag]
        elif MagCheck == 'Level 16-20':
            Mag = dDebuffMagnitude[selMag]
        elif MagCheck == '100%':
            Mag = dMagnitudePercent[selMag]
        else:
            Mag = dMagnitudeNum[selMag]
        toValue = 0

        """Value Calculation"""
        if selEfCheck == (7,):
            toValue = Eff + Dur + Char + Tar
        else:
            toValue = (Eff * Mag) + Dur + Char + Tar
        Total.delete(1.0, tk.END)
        Total.insert(tk.END, toValue)

    """Choose Duration, automatically set as Permanent if Charges Permanent. Return values."""

    def DurationSel(x):
        global toValue
        global Eff
        global Mag
        global Char
        global Dur
        global Tar
        selDur = lbDuration.get(lbDuration.curselection())
        Dur = dDuration[selDur]
        toValue = 0
        """Value Calculation"""
        if selEfCheck == (7,):
            toValue = Eff + Dur + Char + Tar
        else:
            toValue = (Eff * Mag) + Dur + Char + Tar

        Total.delete(1.0, tk.END)
        Total.insert(tk.END, toValue)

    """pack and run everything"""
    Total.insert(tk.END, toValue)
    lbEffect.bind('<<ListboxSelect>>', EffectSel)
    lbTarget.bind('<<ListboxSelect>>', TargetSel)
    lbMagnitude.bind('<<ListboxSelect>>', MagnitudeSel)
    lbCharges.bind('<<ListboxSelect>>', ChargesSel)
    lbDuration.bind('<<ListboxSelect>>', DurationSel)
