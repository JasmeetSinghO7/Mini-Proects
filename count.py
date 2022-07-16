# ByJasmeet Singh (16-07-2022)
from tkintertable import *

clockWindow = Tk()
clockWindow.attributes('-fullscreen', True)
w, h = clockWindow.winfo_screenwidth(), clockWindow.winfo_screenheight()
clockWindow.title("Countdown Timer")
clockWindow.configure(background='dark slate grey')
secondString = StringVar()

progress = Progressbar(clockWindow, orient=HORIZONTAL, length=100, mode='determinate')


def bar(ln):
    progress['value'] = ln
    clockWindow.update_idletasks()
    progress.pack(pady=10)


def runTimer(i):
    if i == 0:
        clockWindow.destroy()
    else:
        secondString.set(i)

        box_size = int(w * 0.15)

        Label(clockWindow, background="dark slate grey", foreground="grey7",
              font=("Arial", box_size, ""), textvariable=secondString).place(relx=0.5, rely=0.5, anchor=CENTER)

        clockTime = int(secondString.get())

        ln = 100 / int(i)
        jn = 0
        while clockTime > -1:
            totalSeconds = clockTime
            secondString.set(totalSeconds)

            bar(jn)

            clockWindow.update()
            progress.update()
            time.sleep(1)

            clockTime -= 1
            jn += ln

        else:
            pass


def main():
    inputs = sys.argv[1:]
    for i in inputs:
        runTimer(i)

    runTimer(0)
    clockWindow.mainloop()
    print("Finsh")


if __name__ == '__main__':
    main()
