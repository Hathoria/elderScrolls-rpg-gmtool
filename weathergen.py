#!/usr/local/bin/python3
import tkinter as tk
from tkinter import ttk
import random
from collections import OrderedDict

def getTab(nb):
    tab3 = ttk.Frame(nb, width=500, height=500)
    lbCountry = tk.Listbox(tab3, height=10, exportselection=False)
    lbCountry.grid(row=1,column=0, sticky=tk.N)
    lbArea = tk.Listbox(tab3, height=10, exportselection=False)
    lbArea.grid(row=1, column=1, sticky=tk.N)
    txtWeather = tk.Text(tab3, width=15, height=5)
    txtWeather.grid(row=1, column=2, sticky=tk.N)
    nb.add(tab3, text='WeatherGen')
    tk.Label(tab3, text='Country').grid(row=0, column=0)
    tk.Label(tab3, text='Area').grid(row=0, column=1)
    tk.Label(tab3, text='Weather').grid(row=0, column=0)


    """lists:
    country: the different countries of cyrodiil
    area: areas of the different countries
    weatherType: different types of weather effects"""

    country = ['Cyrodiil',
           'Morrowind']

    cyrodiil = ['Gold Coast',
            'Colovian Highlands',
            'West Weald',
            'Great Forest',
            'Jerall Mountains',
            'Heartlands',
            'Nibenay Basin',
            'Valus Mountains',
            'Nibenay Valley',
            'Blackwood']

    morrowind = ['West Gash',
             'Ashlands',
             'Red Mountain',
             'Molag Amur',
             'Grazelands',
             'Ascadian Isles',
             'Bitter Coast',
             'Azuras Coast',
             'Sheogorad']

    for itemCou in country:
        lbCountry.insert(0, itemCou)

    def selCountry(x):
        selCou = lbCountry.get(lbCountry.curselection())
        lbArea.delete(0, tk.END)
        txtWeather.delete(1.0, tk.END)
        if selCou == 'Morrowind':
            for itemAreaMor in morrowind:
                lbArea.insert(0, itemAreaMor)
        elif selCou == 'Cyrodiil':
            for itemAreaCyr in cyrodiil:
                lbArea.insert(0, itemAreaCyr)

    def selArea(x):
        txtWeather.delete(1.0, tk.END)
        selAre = lbArea.get(lbArea.curselection())
        randomNumber = random.randrange(100)

        """Cyrodiil provinces"""

        """if selected Cyrodiil province is: Colovian Highlands, West Weald, Great Forest, Heartland, Nibenay Basin or Nibenay Valley     then the output of the weather textbox is:"""
        if selAre == 'Colovian Highland' or selAre == 'West Weald' or selAre == 'Great Forest' or selAre == 'Heartlands' or 'Nibenay Basin' or selAre == 'Nibenay Valley':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 36:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 35 and randomNumber < 76:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 75 and randomNumber < 86:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 85 and randomNumber < 91:
                txtWeather.insert(1.0, 'Thunder')
            elif randomNumber > 90 and randomNumber < 96:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 95:
                txtWeather.insert(1.0, 'Rain')
        """Gold Coast"""
        if selAre == 'Gold Coast':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 31:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 30 and randomNumber < 51:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 50 and randomNumber < 71:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 70 and randomNumber < 76:
                txtWeather.insert(1.0, 'Thunder')
            elif randomNumber > 75 and randomNumber < 91:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 90:
                txtWeather.insert(1.0, 'Rain')
        """Jerall Mountains or Valus Mountains:"""
        if selAre == 'Jerall Mountains' or selAre =='Valus Mountains':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 26:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 25 and randomNumber < 51:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 50 and randomNumber < 66:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 67 and randomNumber < 91:
                txtWeather.insert(1.0, 'Snow')
            elif randomNumber > 90:
                txtWeather.insert(1.0, 'Foggy')
        """Blackwood:"""
        if selAre == 'Blackwood':
            txtWeather.delete(1.0,tk.END)
            if randomNumber < 11:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 10 and randomNumber < 21:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 20 and randomNumber < 36:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 35 and randomNumber < 56:
                txtWeather.insert(1.0, 'Thunder')
            elif randomNumber > 55 and randomNumber < 76:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 75:
                txtWeather.insert(1.0, 'Rain')

        """Morrowind Provinces"""

        """West Gash"""
        if selAre == 'West Gash':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 15:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 14 and randomNumber < 45:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 44 and randomNumber < 60:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 59 and randomNumber < 80:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 79 and randomNumber < 90:
                txtWeather.insert(1.0, 'Rain')
            elif randomNumber > 89:
                txtWeather.insert(1.0, 'Thunder')

        """Ashlands"""
        if selAre == 'Ashlands':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 10:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 9 and randomNumber < 35:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 34 and randomNumber < 45:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 44 and randomNumber < 70:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 69:
                txtWeather.insert(1.0, 'Ash')

        """Red Mountain"""
        if selAre == 'Red Mountain':
            txtWeather.delete(1.0, tk.END)
            txtWeather.insert(1.0, 'Blight')

        """"Molag Amur"""
        if selAre == 'Molag Amur':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 6:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 5 and randomNumber < 20:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 19 and randomNumber < 55:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 54 and randomNumber < 80:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 79:
                txtWeather.insert(1.0, 'Ash')

        """Grazelands"""
        if selAre == 'Grazelands':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 30:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 29 and randomNumber < 70:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 69 and randomNumber < 75:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 74 and randomNumber < 80:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 79 and randomNumber < 90:
                txtWeather.insert(1.0, 'Rain')
            elif randomNumber > 89:
                txtWeather.insert(1.0, 'Thunder')

        """Ascadian Isles"""
        if selAre == 'Ascadian Isles':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 45:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 44 and randomNumber < 90:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 89 and randomNumber < 95:
                txtWeather.insert(1.0, 'Rain')
            elif randomNumber > 94:
                txtWeather.insert(1.0, 'Thunder')

        """Bitter Coast"""
        if selAre == 'Bitter Coast':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 10:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 9 and randomNumber < 70:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 69 and randomNumber < 80:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 79 and randomNumber < 90:
                txtWeather.insert(1.0, 'Rain')
            elif randomNumber > 89:
                txtWeather.insert(1.0, 'Thunder')

        """Azuras Coast"""
        if selAre == 'Azuras Coast':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 25:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 24 and randomNumber < 70:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 69 and randomNumber < 80:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 79 and randomNumber < 90:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 89 and randomNumber < 95:
                txtWeather.insert(1.0, 'Rain')
            elif randomNumber > 94:
                txtWeather.insert(1.0, 'Thunder')

        """Sheogorad"""
        if selAre == 'Sheogorad':
            txtWeather.delete(1.0, tk.END)
            if randomNumber < 15:
                txtWeather.insert(1.0, 'Clear')
            elif randomNumber > 14 and randomNumber < 55:
                txtWeather.insert(1.0, 'Cloudy')
            elif randomNumber > 54 and randomNumber < 65:
                txtWeather.insert(1.0, 'Foggy')
            elif randomNumber > 64 and randomNumber < 80:
                txtWeather.insert(1.0, 'Overcast')
            elif randomNumber > 79 and randomNumber < 90:
                txtWeather.insert(1.0, 'Rain')
            elif randomNumber > 89:
                txtWeather.insert(1.0, 'Thunder')

    """bind listboxes and other graphical interface"""
    lbCountry.bind('<<ListboxSelect>>', selCountry)
    lbArea.bind('<<ListboxSelect>>', selArea)
    txtWeather.bind('<<ListboxSelect>>')