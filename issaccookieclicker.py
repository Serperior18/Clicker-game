# Cookie Clicker sort of #
from tkinter import *   # so now we have buttons yayyyyyyyyy
import time

master = Tk()

def uiPrint():
    info()
    print("")
    print(click)
    blankLine()


click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(20):
        print("")

double_cost = 50 # initial cost = 50
def purchaseDoubleClicksCommand():
    global click
    global mult         # declare global
    global double_cost
    if click < double_cost:
        print("Not enough clicks!")     # if they try to buy without enough clicks, stop them
        blankLine()
    elif click >= double_cost:
        mult = mult*2   # multiplier x2 each time double click is bought
        click = click - double_cost     # pay for the x2 click
        double_cost = double_cost*4 # more expensive after each purchase
        print("Double Clicks Purchased!")
        blankLine()


autoclickers=0 # start autoclickers user has at 0
auto_cost = 75 #initial cost is 75
def purchaseAutoClickerCommand():
    global click
    global autoclickers # declare global
    global auto_cost
    if click < auto_cost:
        print("Not enough clicks!") # if they try to buy without enough clicks, stop them
        blankLine()
    else:
        click -= auto_cost # pay for an autoclicker
        print("Auto clicker purchased!")
        autoclickers += 1 # receive an autoclicker
        auto_cost = auto_cost * 4# more expensive after each purchase

# the reason for more expensive after each purchase is so the user doesn't
# spam the buy double click button and become god

def info():
    print("Double click purchases need {} clicks!".format(double_cost))     #display cost of double click
    print("Auto clicker purchases need {} clicks!".format(auto_cost))   # display cost of auto-click

info()

def autoclick():
    global master
    global click
    global autoclickers
    click += autoclickers # get 1 click per autoclickers
    master.after(1000, autoclick) # do this again 1 second later
    if autoclickers: # shows the clicks from autoclickers
        print(click) 
autoclick() # start benefiting from all existing autoclickers


def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()

    if click == 100:    # achievement for clicking the button 100 times
        print('''Man you are bored. 
        BONUS 100 clicks!''')
        click += 100

    elif click == 400:  # achievement for clicking the button 400 times
        print ('''Step away from the computer for a while.
        BONUS 200!''')
        click += 300

    elif click == 1500:     # achievement for clicking the button 1500 times
        print ('''Have you showered?
        QUADRUPLE CLICKS!''')
        mult = mult * 4

    elif click == 3000:     # achievement for clicking the button 3000 times
        print ('''Should go get yourself checked for carpal tunnel. 
        8 TIMES THE CLICKS!''')
        mult = mult * 8

mainClickButton = Button(master, text="Click!", command = buttonCommand)
mainClickButton.pack()

purchaseDoubleClickButton = Button(master, text="Purchase Double Clicks", command = purchaseDoubleClicksCommand)
purchaseDoubleClickButton.pack()

purchaseAutoClickerButton = Button(master, text="Purchase Auto Clicker", command = purchaseAutoClickerCommand)
purchaseAutoClickerButton.pack()

master.title("Virtual Carpal Tunnel Syndrome")
master.geometry("%sx%s+%s+%s" % (200,70,512,512))
mainloop()
