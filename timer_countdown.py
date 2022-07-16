import argparse
import time
from tkintertable import *

parser = argparse.ArgumentParser(description='Count Down Timer')
parser.add_argument('--s', default=10)

args = parser.parse_args()

# Create the interface object
clockWindow = Tk()
clockWindow.attributes('-fullscreen', True)
w, h = clockWindow.winfo_screenwidth(), clockWindow.winfo_screenheight()
clockWindow.title("Countdown Timer")
clockWindow.configure(background='#606060')

# Set Default Seconds
s = args.s

# Declare variables
secondString = StringVar()

# Set Default Seconds
secondString.set(s)

# Get user input
box_size = int(w * 0.10)

# if you want to take user inpt change Label to Entry
secondTextbox = Label(clockWindow, background="#606060", borderwidth=0, font=("Calibri", box_size, ""),
                      textvariable=secondString).place(relx=0.5, rely=0.5, anchor=CENTER)

x_c = w / 2
y_c = h


def runTimer():
    try:
        clockTime = int(secondString.get())
    except:
        print("Incorrect values")

    try:
        while clockTime > -1:
            totalSeconds = clockTime

            secondString.set(totalSeconds)

            # Update the interface
            clockWindow.update()
            time.sleep(1)

            clockTime -= 1

    except:
        print("Quit")


setTimeButton = Button(clockWindow, text='Start Timer', command=runTimer)
setTimeButton.place(relx=0.5, rely=0.9, anchor="s")
Button(clockWindow, text="Quit", command=clockWindow.destroy).pack()

# Keep looping
clockWindow.mainloop()
