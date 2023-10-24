import sys
import datetime
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
import csv
import datetime
import math


###############################################################################################
def raise_frame(frame_name):
    frame_name.tkraise()


###############################################################################################
# KEYPAD
def num1():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (str(Enteredpin + "1"))
    print(Enteredpin)

    PinboxDisplay.set(Enteredpin)


def num2():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (str(Enteredpin + "2"))
    PinboxDisplay.set(Enteredpin)
    print(Enteredpin)


def num3():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "3")
    PinboxDisplay.set(Enteredpin)


def num4():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "4")
    PinboxDisplay.set(Enteredpin)


def num5():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "5")
    PinboxDisplay.set(Enteredpin)


def num6():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "6")
    PinboxDisplay.set(Enteredpin)


def num7():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "7")
    PinboxDisplay.set(Enteredpin)


def num8():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "8")
    PinboxDisplay.set(Enteredpin)


def num9():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "9")
    PinboxDisplay.set(Enteredpin)


def num0():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()
    pressedtracker = (Enteredpin)
    print(pressedtracker)

    Enteredpin = (Enteredpin + "0")
    PinboxDisplay.set(Enteredpin)


def numBack():
    Enteredpin = PinboxDisplay.get()
    pressedtracker = lastentered.get()

    Enteredpin = ""
    pressedtracker = ""
    PinboxDisplay.set(Enteredpin)


def BackToMenu():
    raise_frame(Menu_frame)
    PinboxDisplay.set("")


###############################################################################################
# Entry Frame

def clear_login():
    pinbox.set("")


def numEnterEntryFrame():
    Enteredpin = PinboxDisplay.get()

    if (Enteredpin == ""):
        messagebox.showinfo("User Information", "Invalid data entered", icon="warning")
        clear_login()
    else:
        with open('Bank Accounts.txt', 'r') as csvfile:
            found = 0
            # creating a found variable to see whether or not i have found the variable
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif (Enteredpin == row[0]):
                    pintracker = Enteredpin
                    print(pintracker)
                    raise_frame(Menu_frame)
                    found = 1
                    messagebox.showinfo("User Information", "Welcome To O'Brien Banking", icon="warning")

        if found == 0:
            messagebox.showinfo("User Information", "Invalid Pin", icon="warning")
            clear_login()
        csvfile.close()
        print(found)
        PinboxDisplay.set("")
        pintracker = Enteredpin
        print(pintracker)

        with open('pintracker.txt', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([str(pintracker)])


###############################################################################################
# Main Frame
def ToWithdraw():
    pin1 = pin.get()
    Enteredpin = PinboxDisplay.get()

    with open("pintracker.txt", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if pin1 == "":
                pin1 = row[0]
                print(pin1)

    csvfile.close()

    if pin1 == "":
        raise_frame(Withdraw_frame)

    with open('Bank Accounts.txt', 'r') as csvfile:
        found = 0
        # creating a found variable to see whether or not i have found the variable
        reader = csv.reader(csvfile)
        for row in reader:
            if row == []:
                pass
            elif (pin1 == row[0]):
                amount = row[3]
                messagebox.showinfo('User Information', 'Available amount is ' + amount, icon="info")
                PinboxDisplay.set("")

                raise_frame(Withdraw_frame)


def ToCurrentBal():
    Enteredpin = PinboxDisplay.get()
    pin1 = pin.get()

    with open("pintracker.txt", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == []:
                pass
            elif pin1 == "":
                pin1 = row[0]
                print(pin1)

    csvfile.close()

    if (pin1 == ""):
        raise_frame(CurrentBal_frame)

    else:
        PinboxDisplay.set("")
        raise_frame(CurrentBal_frame)
        with open('Bank Accounts.txt', 'r') as csvfile:
            found = 0
            # creating a found variable to see whether or not i have found the variable
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif (pin1 == row[0]):
                    found = 1
                    PinboxDisplay.set(row[3])

        if found == 0:
            messagebox.showinfo("User Information", "Invalid Pin", icon="warning")
            raise_frame(CurrentBal_frame)
        csvfile.close()
        print(found)


def ToDepositMoney():
    PinboxDisplay.set("")
    raise_frame(Deposit_frame)


def Exit():
    MsgBox = messagebox.askquestion('Leaving', 'Are you sure you want to exit?', icon='warning')
    if MsgBox == 'yes':
        raise_frame(Entry_frame)
    else:
        messagebox.showinfo('Leaving', 'Ensure You Exit After Finishing')


###############################################################################################
# Withdraw Frame
def numEnterWithDraw():
    amount = newamount.get()
    Enteredpin = PinboxDisplay.get()
    pin1 = pin.get()

    bankrecords = []

    with open("pintracker.txt", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if pin1 == "":
                pin1 = row[0]
                print(pin1)

    csvfile.close()

    if (pin1 == ""):
        messagebox.showinfo("User Information", "Pin Issue, Login Again", icon="warning")
    elif (Enteredpin == ""):
        messagebox.showinfo("User Information", "Invalid Data ,Try Again", icon="warning")

    else:
        with open('Bank Accounts.txt', 'r') as csvfile:
            found = 0
            # creating a found variable to see whether or not i have found the variable
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif (pin1 == row[0]):
                    found = 1
                    new_amount = int(row[3]) - int(Enteredpin)
                    print(new_amount)
                    row[3] = new_amount
                    print(row[3])
                    PinboxDisplay.set("Amount = " + str(new_amount))
                    bankrecords.append(row)

        if found == 0:
            messagebox.showinfo("User Information", "Invalid Pin", icon="warning")
            raise_frame(CurrentBal_frame)
        csvfile.close()
        print(found)

        with open('Bank Accounts.txt', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in bankrecords:
                writer.writerow(row)

        csvfile.close()


###############################################################################################
# CurrentBal Frame
def numEnterBal():
    messagebox.showinfo("User Information", "Your Current Balence was displayed, There is nothing to enter",
                        icon="warning")

    pin1 = pin.get()

    with open("pintracker.txt", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if pin1 == "":
                pin1 = row[0]
                print(pin1)

    csvfile.close()

    if (pin1 == ""):
        raise_frame(CurrentBal_frame)

    else:
        raise_frame(CurrentBal_frame)
        with open('Bank Accounts.txt', 'r') as csvfile:
            found = 0
            # creating a found variable to see whether or not i have found the variable
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif (pin1 == row[0]):
                    found = 1
                    PinboxDisplay.set(row[3])

        if found == 0:
            messagebox.showinfo("User Information", "Invalid Pin", icon="warning")
            raise_frame(CurrentBal_frame)
        csvfile.close()
        print(found)


###############################################################################################
# Deposit Frame
def numEnterDeposit():
    amount = newamount.get()
    Enteredpin = PinboxDisplay.get()
    pin1 = pin.get()

    bankdetails_record = []

    with open("pintracker.txt", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if pin1 == "":
                pin1 = row[0]
                print(pin1)

    csvfile.close()

    if (pin1 == ""):
        messagebox.showinfo("User Information", "Pin Issue, Login Again", icon="warning")
    elif (Enteredpin == ""):
        messagebox.showinfo("User Information", "Invalid Data ,Try Again", icon="warning")

    else:
        with open('Bank Accounts.txt', 'r') as csvfile:
            found = 0
            # creating a found variable to see whether or not i have found the variable
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                elif (pin1 == row[0]):
                    found = 1
                    new_amount2 = int(row[3]) + int(Enteredpin)
                    print(new_amount2)
                    PinboxDisplay.set("New Amount = " + str(new_amount2))
                    row[3] = new_amount2
                    print(row[3])
                    bankdetails_record.append(row)
                    print(bankdetails_record)

        if found == 0:
            messagebox.showinfo("User Information", "Invalid Pin", icon="warning")
            raise_frame(CurrentBal_frame)
        csvfile.close()

        print(found)
        with open('Bank Accounts.txt', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in bankdetails_record:
                writer.writerow(row)

        csvfile.close()


###############################################################################################

# I am setting up and configuring the GUI
root = Tk()
root.geometry("680x800")
root.title("O'Brien ATM")
root.configure(background="Black")

################################################################################################

# these are my individual frames
# login frame
Entry_frame = Frame(root)
Entry_frame.config(bg="Grey")

Menu_frame = Frame(root)
Menu_frame.config(bg="Grey")

Withdraw_frame = Frame(root)
Withdraw_frame.config(bg="Grey")

CurrentBal_frame = Frame(root)
CurrentBal_frame.config(bg="Grey")

Deposit_frame = Frame(root)
Deposit_frame.config(bg="Grey")

################################################################################################
# Gridding the frames
for frame in (Entry_frame, Menu_frame, Withdraw_frame, CurrentBal_frame, Deposit_frame):
    frame.grid(row=0, column=0, sticky='news')

################################################################################################
# Variables for the program
pinbox = StringVar()
PinboxDisplay = StringVar()
lastentered = StringVar()
pintracker = StringVar()
newamount = StringVar()
pin = StringVar()

##########################################################################################################################################################
# Login Frame #1

entryF_Title_L = Label(Entry_frame, text="Enter Pin Number", bg="Grey", font=('times 30'), pady=40, padx=200,
                       relief=RAISED)
entryF_Title_L.grid(row=0, column=0, columnspan=5)

entryF_spacerL = Label(Entry_frame, text="", bg="Grey")
entryF_spacerL.grid(row=1, column=0, columnspan=5)

entryF_entrybox_L = Label(Entry_frame, textvariable=PinboxDisplay, bg="dark grey", fg="White", font=('Calibri 30'),
                          padx=300, pady=30, relief=RAISED)
entryF_entrybox_L.grid(row=2, column=0, columnspan=5)

entryF_spacerL = Label(Entry_frame, text="", bg="Grey")
entryF_spacerL.grid(row=3, column=0, columnspan=5)

##########################################################################################################################################################
# Keypad
entryF_num1 = Button(Entry_frame, text="1", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num1)
entryF_num1.grid(row=4, column=1)

entryF_num2 = Button(Entry_frame, text="4", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num4)
entryF_num2.grid(row=4, column=2)

entryF_num3 = Button(Entry_frame, text="7", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num7)
entryF_num3.grid(row=4, column=3)

entryF_num4 = Button(Entry_frame, text="2", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num2)
entryF_num4.grid(row=5, column=1)

entryF_num5 = Button(Entry_frame, text="5", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num5)
entryF_num5.grid(row=5, column=2)

entryF_num6 = Button(Entry_frame, text="8", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num8)
entryF_num6.grid(row=5, column=3)

entryF_num7 = Button(Entry_frame, text="3", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num3)
entryF_num7.grid(row=6, column=1)

entryF_num8 = Button(Entry_frame, text="6", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num6)
entryF_num8.grid(row=6, column=2)

entryF_num9 = Button(Entry_frame, text="9", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num9)
entryF_num9.grid(row=6, column=3)

entryF_num0 = Button(Entry_frame, text="0", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num0)
entryF_num0.grid(row=7, column=2)

entryFack = Button(Entry_frame, text="⟵", font=('Calibri 30'), bg="White", padx=8, pady=10, command=numBack)
entryFack.grid(row=7, column=1)

entryF_Enter = Button(Entry_frame, text="↩", font=('Calibri 30'), bg="White", padx=15, pady=10,
                      command=numEnterEntryFrame)
entryF_Enter.grid(row=7, column=3)

entryF_spacerL = Label(Entry_frame, text="", bg="White")
entryF_spacerL.grid(row=8, column=0)

##########################################################################################################################################################
# Main Frame

MenuF_Title = Label(Menu_frame, text="O'Brien ATM", bg="Light Grey", font=('times 30'), pady=60, padx=200,
                    relief=RAISED)
MenuF_Title.grid(row=0, column=0, columnspan=5)

MenuF_spacer = Label(Menu_frame, text="", bg="Grey")
MenuF_spacer.grid(row=1, column=0, columnspan=5)

MenuF_withdraw = Button(Menu_frame, text="Withdraw", bg="White", font=('Calibri 30'), pady=50, padx=50,
                        command=ToWithdraw)
MenuF_withdraw.grid(row=2, column=1)

MenuF_currentbal = Button(Menu_frame, text="Current Balance", bg="White", font=('Calibri 30'), pady=50, padx=10,
                          command=ToCurrentBal)
MenuF_currentbal.grid(row=2, column=3)

MenuF_spacer = Label(Menu_frame, text="", bg="Grey")
MenuF_spacer.grid(row=3, column=0, columnspan=5)

MenuF_deposit = Button(Menu_frame, text="Deposit Money", bg="White", font=('Calibri 30'), pady=50, padx=10,
                       command=ToDepositMoney)
MenuF_deposit.grid(row=4, column=1)

MenuF_exist = Button(Menu_frame, text="Exit", bg="White", font=('Calibri 30'), pady=50, padx=110, command=Exit)
MenuF_exist.grid(row=4, column=3)

##########################################################################################################################################################
# Withdraw frame

Withdraw_Title = Button(Withdraw_frame, text="Enter Withdrawal Amount", font=('times 30'), pady=25, padx=115,
                        relief=RAISED)
Withdraw_Title.grid(row=0, column=0, columnspan=5)

Withdraw_spacer = Label(Withdraw_frame, text="", bg="Grey")
Withdraw_spacer.grid(row=1, column=0, columnspan=5)

Withdraw_entrybox = Label(Withdraw_frame, textvariable=PinboxDisplay, bg="Grey", fg="White", font=('Calibri 30'),
                          padx=300, pady=30, relief=RAISED)
Withdraw_entrybox.grid(row=2, column=0, columnspan=5)

Withdraw_spacer = Label(Withdraw_frame, text="", bg="Grey")
Withdraw_spacer.grid(row=3, column=0, columnspan=5)

##########################################################################################################################################################
# Keypad

Withdraw_num1 = Button(Withdraw_frame, text="1", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num1)
Withdraw_num1.grid(row=4, column=1)

Withdraw_num2 = Button(Withdraw_frame, text="4", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num4)
Withdraw_num2.grid(row=4, column=2)

Withdraw_num3 = Button(Withdraw_frame, text="7", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num7)
Withdraw_num3.grid(row=4, column=3)

Withdraw_num4 = Button(Withdraw_frame, text="2", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num2)
Withdraw_num4.grid(row=5, column=1)

Withdraw_num5 = Button(Withdraw_frame, text="5", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num5)
Withdraw_num5.grid(row=5, column=2)

Withdraw_num6 = Button(Withdraw_frame, text="8", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num8)
Withdraw_num6.grid(row=5, column=3)

Withdraw_num7 = Button(Withdraw_frame, text="3", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num3)
Withdraw_num7.grid(row=6, column=1)

Withdraw_num8 = Button(Withdraw_frame, text="6", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num6)
Withdraw_num8.grid(row=6, column=2)

Withdraw_num9 = Button(Withdraw_frame, text="9", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num9)
Withdraw_num9.grid(row=6, column=3)

Withdraw_num0 = Button(Withdraw_frame, text="0", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num0)
Withdraw_num0.grid(row=7, column=2)

Withdrawack = Button(Withdraw_frame, text="⟵", font=('Calibri 30'), bg="White", padx=8, pady=10, command=numBack)
Withdrawack.grid(row=7, column=1)

Withdraw_Enter = Button(Withdraw_frame, text="↩", font=('Calibri 30'), bg="White", padx=15, pady=10,
                        command=numEnterWithDraw)
Withdraw_Enter.grid(row=7, column=3)

Withdraw_spacerL = Label(Withdraw_frame, text="", bg="Grey")
Withdraw_spacerL.grid(row=8, column=0, columnspan=5)

Withdrawack = Button(Withdraw_frame, text="Back", font=('Calibri 30'), bg="White", padx=15, pady=10, command=BackToMenu)
Withdrawack.grid(row=9, column=2)

Withdraw_spacerL = Label(Withdraw_frame, text="", bg="Grey")
Withdraw_spacerL.grid(row=10, column=2)

##########################################################################################################################################################
# Current Balance frame

Balance_Title = Button(CurrentBal_frame, text="Current Balance", font=('times 30'), pady=25, padx=200, relief=RAISED)
Balance_Title.grid(row=0, column=0, columnspan=5)

Balance_spacer = Label(CurrentBal_frame, text="", bg="Light Grey")
Balance_spacer.grid(row=1, column=0, columnspan=5)

Balance_entrybox = Label(CurrentBal_frame, textvariable=PinboxDisplay, bg="Grey", fg="White", font=('Calibri 30'),
                         padx=300, pady=30, relief=RAISED)
Balance_entrybox.grid(row=2, column=0, columnspan=5)

Balance_spacer = Label(CurrentBal_frame, text="", bg="Grey")
Balance_spacer.grid(row=3, column=0, columnspan=5)

##########################################################################################################################################################
# Current Balance Keypad

Balance_num1 = Button(CurrentBal_frame, text="1", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num1)
Balance_num1.grid(row=4, column=1)

Balance_num2 = Button(CurrentBal_frame, text="4", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num4)
Balance_num2.grid(row=4, column=2)

Balance_num3 = Button(CurrentBal_frame, text="7", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num7)
Balance_num3.grid(row=4, column=3)

Balance_num4 = Button(CurrentBal_frame, text="2", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num2)
Balance_num4.grid(row=5, column=1)

Balance_num5 = Button(CurrentBal_frame, text="5", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num5)
Balance_num5.grid(row=5, column=2)

Balance_num6 = Button(CurrentBal_frame, text="8", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num8)
Balance_num6.grid(row=5, column=3)

Balance_num7 = Button(CurrentBal_frame, text="3", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num3)
Balance_num7.grid(row=6, column=1)

Balance_num8 = Button(CurrentBal_frame, text="6", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num6)
Balance_num8.grid(row=6, column=2)

Balance_num9 = Button(CurrentBal_frame, text="9", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num9)
Balance_num9.grid(row=6, column=3)

Balance_num0 = Button(CurrentBal_frame, text="0", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num0)
Balance_num0.grid(row=7, column=2)

Balance_spacerL = Label(CurrentBal_frame, text="", bg="white")
Balance_spacerL.grid(row=8, column=0, columnspan=5)

Balanceack = Button(CurrentBal_frame, text="Back", font=('Calibri 30'), padx=15, pady=10, command=BackToMenu)
Balanceack.grid(row=9, column=2)

Balance_spacerL = Label(CurrentBal_frame, text="", bg="white")
Balance_spacerL.grid(row=10, column=2)

##########################################################################################################################################################
# Deposit Frame

Deposit_Title = Button(Deposit_frame, text="Enter Deposit Amount", bg="Grey", font=('times 30'), pady=25, padx=150,
                       relief=RAISED)
Deposit_Title.grid(row=0, column=0, columnspan=5)

Deposit_spacer = Label(Deposit_frame, text="", bg="Light Grey")
Deposit_spacer.grid(row=1, column=0, columnspan=5)

Deposit_entrybox = Label(Deposit_frame, textvariable=PinboxDisplay, bg="Grey", fg="White", font=('Calibri 30'),
                         padx=300, pady=30, relief=RAISED)
Deposit_entrybox.grid(row=2, column=0, columnspan=5)

Deposit_spacer = Label(Deposit_frame, text="", bg="Grey")
Deposit_spacer.grid(row=3, column=0, columnspan=5)

##########################################################################################################################################################
# Keypad

Deposit_num1 = Button(Deposit_frame, text="1", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num1)
Deposit_num1.grid(row=4, column=1)

Deposit_num2 = Button(Deposit_frame, text="4", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num4)
Deposit_num2.grid(row=4, column=2)

Deposit_num3 = Button(Deposit_frame, text="7", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num7)
Deposit_num3.grid(row=4, column=3)

Deposit_num4 = Button(Deposit_frame, text="2", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num2)
Deposit_num4.grid(row=5, column=1)

Deposit_num5 = Button(Deposit_frame, text="5", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num5)
Deposit_num5.grid(row=5, column=2)

Deposit_num6 = Button(Deposit_frame, text="8", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num8)
Deposit_num6.grid(row=5, column=3)

Deposit_num7 = Button(Deposit_frame, text="3", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num3)
Deposit_num7.grid(row=6, column=1)

Deposit_num8 = Button(Deposit_frame, text="6", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num6)
Deposit_num8.grid(row=6, column=2)

Deposit_num9 = Button(Deposit_frame, text="9", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num9)
Deposit_num9.grid(row=6, column=3)

Deposit_num0 = Button(Deposit_frame, text="0", font=('Calibri 30'), bg="White", padx=20, pady=10, command=num0)
Deposit_num0.grid(row=7, column=2)

Depositack = Button(Deposit_frame, text="⟵", font=('Calibri 30'), padx=8, pady=10, command=numBack)
Depositack.grid(row=7, column=1)

Deposit_Enter = Button(Deposit_frame, text="↩", font=('Calibri 30'), padx=15, pady=10, command=numEnterDeposit)
Deposit_Enter.grid(row=7, column=3)

Deposit_spacerL = Label(Deposit_frame, text="", bg="Grey")
Deposit_spacerL.grid(row=8, column=0, columnspan=5)

Depositack = Button(Deposit_frame, text="Back", font=('Calibri 30'), padx=15, pady=10, command=BackToMenu)
Depositack.grid(row=9, column=2)

Deposit_spacerL = Label(Deposit_frame, text="", bg="white")
Deposit_spacerL.grid(row=10, column=2)

##########################################################################################################################################################

raise_frame(Entry_frame)
root.mainloop()
