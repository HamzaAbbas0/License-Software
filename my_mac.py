from firebase import firebase
from firebase_admin import db
from getmac import get_mac_address as gma
import datetime
from tkinter import messagebox
import os
from tkinter import *



gui=Tk()
gui.overrideredirect(1)
gui.withdraw()


def guifun():
    global photo, e1
    gui = Tk()
    gui.geometry("400x220")
    gui.maxsize(400, 220)
    gui.title("Hackerspace Karachi")
    l1 = Label(gui, text="Enter your name", font=("times 12 bold"))
    l1.place(x=30, y=50)
    
    e1 = Entry(gui, relief=SUNKEN, bd=5, width=30)
    e1.place(x=180, y=50)

    btn = Button(gui, text="submit",bg="green",command=feedback)
    btn.place(x=220, y=150)

    address = gma()
    print('address', address)
    gui.mainloop()



def feedback():
    global e1, firebase;
    ex1= e1.get()

    firebase.put('requested/', str(ex1), address)


    print(ex1)
    messagebox.showinfo("showinfo", "Conguralations you are sucessfull registered! ")

def networkdialog():

    gui.overrideredirect(1)
    gui.withdraw()
    messagebox.showerror("Error", "please check your internet connection")
    gui.destroy()
    os._exit(1)

def validationcheck():
    global validationcheck

    global val_i, value

    if value == None:
        val_i = 0
        answer=messagebox.showerror("Error", "you are not registered please registered your self")
        print(answer)
        if answer=="ok":
            guifun()

        


address = gma()
print('address', address)
a = 0
current_time = datetime.datetime.now()
my_str = StringVar()
try:
    firebase = firebase.FirebaseApplication('https://stx-calculator-default-rtdb.firebaseio.com/', None)
    print('code is here')
    firebase.put('approved/', str(a), current_time)
    value = firebase.get('approved/', address)
    print(value)
    validationcheck()
    print('done with validation check')
    movetomain = 1
except:
   networkdialog()




