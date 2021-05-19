import sqlite3 as lite
import tkinter as tk
from collections import OrderedDict

def getTab(nb):

    """connect to database."""
    ingredientsdb = lite.connect('alchemy-ingredients.db')
    db = ingredientsdb.cursor()

    """ this code orders the table according to names. Not used, but still here if I ever need it again.
    db.execute('CREATE TABLE "ordered" ("name" TEXT NOT NULL UNIQUE, "effect1" TEXT, "effect2" TEXT, "effect3" TEXT, "effect4" TEXT )')
    db.execute('INSERT INTO ordered VALUES (1,1,1,1,1)')
    db.execute("INSERT INTO ordered (name,effect1,effect2,effect3,effect4) SELECT name,effect1,effect2,effect3,effect4 FROM ingredients ORDER BY name")
    ingredientsdb.commit()"""

    """############################################################################################################"""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
                'V', 'W']
    """clear the listbox for the names and insert names from db for the letter that is being selected in optionmenu"""
    def selectedletter(value):
        lbIngredientName.delete(0,tk.END)
        letter = value
        ingredienttoLB = db.execute("SELECT name FROM ingredients WHERE name LIKE '{0}%' ORDER BY name DESC" .format(letter))
        for ingredientName in ingredienttoLB:
            ingredientName =str(ingredientName)
            ingredientName = ingredientName.replace('(', '').replace(',', '').replace(')','').replace("'",'')
            lbIngredientName.insert(0,ingredientName)

    """find selected ingredient from listbox, turn it to string and replace unnesesary symbols."""
    def selingredientname(x):
        lbIngredientEffect.delete(0,tk.END)
        dbIngredientName = lbIngredientName.get(lbIngredientName.curselection())
        dbIngredientName = str(dbIngredientName)
        dbIngredientName = dbIngredientName.replace('(', '').replace(',', '').replace(')','').replace("'",'')


        """select all effects 1,2,3,4 from db where name is like the selected ingredient, and put them into a list."""
        ingredientEffect1 = db.execute("SELECT effect1 FROM ingredients WHERE name LIKE '{0}%'" .format(dbIngredientName))
        for effect in ingredientEffect1:
            effect1 = effect
        ingredientEffect2 = db.execute("SELECT effect2 FROM ingredients WHERE name LIKE '{0}%'" .format(dbIngredientName))
        for effect in ingredientEffect2:
            effect2 = effect
        ingredientEffect3 = db.execute("SELECT effect3 FROM ingredients WHERE name LIKE '{0}%'" .format(dbIngredientName))
        for effect in ingredientEffect3:
            effect3 = effect
        ingredientEffect4 = db.execute("SELECT effect4 FROM ingredients WHERE name LIKE '{0}%'" .format(dbIngredientName))
        for effect in ingredientEffect4:
            effect4 = effect
        #list for effects, and puts them into listbox.
        ingredientlist = [effect1,effect2,effect3,effect4]
        for k in ingredientlist:
            lbIngredientEffect.insert(tk.END,k)

    """############################################################################################################"""
    """make a list of all the different effects that are, to be put into the optionmenu for effects."""
    effectList = []
    i=0
    unique1 = db.execute("SELECT DISTINCT effect1 FROM ingredients")
    for one in unique1:
        one = str(one).replace('(', '').replace(',', '').replace(')','').replace("'",'')
        i=i+1
        effectList.insert(i,one)
    unique2 = db.execute("SELECT DISTINCT effect2 FROM ingredients")
    for one in unique2:
        one = str(one).replace('(', '').replace(',', '').replace(')', '').replace("'", '')
        i = i + 1
        effectList.insert(i, one)
    unique3 = db.execute("SELECT DISTINCT effect3 FROM ingredients")
    for one in unique3:
        one = str(one).replace('(', '').replace(',', '').replace(')', '').replace("'", '')
        i = i + 1
        effectList.insert(i, one)
    unique4 = db.execute("SELECT DISTINCT effect4 FROM ingredients")
    for one in unique4:
        one = str(one).replace('(', '').replace(',', '').replace(')', '').replace("'", '')
        i = i + 1
        effectList.insert(i, one)
    effectListUnique = sorted(set(effectList))


    """returns the ingredients according to what effect you chose."""
    def selectedeffect(value):
        lbIngredientByEffect.delete(0,tk.END)
        uniqueeffect = value
        lbIngredientByEffectToLB = db.execute("SELECT name FROM ingredients WHERE effect1 LIKE '{0}%' "
                                              "OR effect2 LIKE '{0}%' "
                                              "OR effect3 LIKE '{0}%' "
                                              "OR effect4 LIKE '{0}%' ORDER BY name DESC" .format(uniqueeffect))
        for ingredientName in lbIngredientByEffectToLB:
            lbIngredientByEffect.insert(0,ingredientName)

    """############################################################################################################"""
    """define tkinter gui"""
    tab4 = tk.Frame(nb, width=500, height=500)
    """first part of the gui where you choose ingredient and get it's effects"""
    tkvar = tk.StringVar(tab4)
    tkvar.set(alphabet[0]) #default option
    menuIngredient = tk.OptionMenu(tab4, tkvar, *alphabet,command=selectedletter)
    menuIngredient.grid(row=1, column=0, sticky=tk.N)
    LabelPickIngredient = tk.Label(tab4, text='Pick Ingredient').grid(row=0, column=1)
    lbIngredientName = tk.Listbox(tab4, height=30)
    lbIngredientName.grid(row=1, column=1, sticky=tk.N)
    LabelEffect = tk.Label(tab4, text='Effects').grid(row=0, column=2)
    lbIngredientEffect = tk.Listbox(tab4, height=5)
    lbIngredientEffect.grid(row=1, column=2, sticky=tk.N)
    """add part of gui that lets you choose an effect and find ingredients that have the effect"""
    tkvar2 = tk.StringVar(tab4)
    tkvar2.set(effectList[0]) #default option
    LabelPickEffect = tk.Label(tab4, text='Pick Effect').grid(row=0, column=3)
    menueffect = tk.OptionMenu(tab4, tkvar2, *effectListUnique,command=selectedeffect)
    menueffect.grid(row=1,column=3, sticky=tk.N)
    LabelIngredient = tk.Label(tab4, text='Ingredients').grid(row=0, column=4)
    lbIngredientByEffect = tk.Listbox(tab4, height=30)
    lbIngredientByEffect.grid(row=1, column=4, sticky=tk.N)

    nb.add(tab4, text='Alchemy') #adds all the gui to notebook


    menuIngredient.bind()
    lbIngredientName.bind('<<ListboxSelect>>', selingredientname)
    lbIngredientEffect.bind()

    """select kolonnenavn from tabel where kolonne like '%text%'"""