import tkinter
from tkinter import*
import tkinter as tk

counter = -1
# function that is called when the buttons are pressed
def buttonpressed(btn):
    global counter
    counter+=1
    if counter % 2 == 0:
        btn["text"]== "O"
        btn.configure(bg = "red")
    else:
        btn["text"]== "X"
        btn.configure(bg = "blue")

# create new window
window = tkinter.Tk()
# create window title
window.title("Tic-Tac-Toe")
# set window size
window.geometry("300x300")

# all 9 buttons, with the name refering to the posistion on the grid

b00 = tkinter.Button(window, command=lambda: buttonpressed(b00), text="X", padx=20, pady=20)
b00.grid(row=0, column=0)
b01 = tkinter.Button(window, command=lambda: buttonpressed(b01), text="X", padx=20, pady=20)
b01.grid(row=0, column=1)
b02 = tkinter.Button(window, command=lambda: buttonpressed(b02), text="X", padx=20, pady=20)
b02.grid(row=0, column=2)
b10 = tkinter.Button(window, command=lambda: buttonpressed(b10), text="X", padx=20, pady=20)
b10.grid(row=1, column=0)
b11 = tkinter.Button(window, command=lambda: buttonpressed(b11), text="X", padx=20, pady=20)
b11.grid(row=1, column=1)
b12 = tkinter.Button(window, command=lambda: buttonpressed(b12), text="X", padx=20, pady=20)
b12.grid(row=1, column=2)
b20 = tkinter.Button(window, command=lambda: buttonpressed(b20), text="X", padx=20, pady=20)
b20.grid(row=2, column=0)
b21 = tkinter.Button(window, command=lambda: buttonpressed(b21), text="X", padx=20, pady=20)
b21.grid(row=2, column=1)
b22 = tkinter.Button(window, command=lambda: buttonpressed(b22), text="X", padx=20, pady=20)
b22.grid(row=2, column=2)
label = tkinter.Label(window, text="Im a label!!").grid(row=3, column=0, columnspan=3)


# draw window and start
window.mainloop()