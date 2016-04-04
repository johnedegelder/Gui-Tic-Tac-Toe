import tkinter
from tkinter import*
import tkinter as tk

score=["A","A","A","A","A","A","A","A","A"]
# Counter starting at 0
global counter
counter = -1

# function that is called when the buttons are pressed
def buttonchange(btn):
       #grabs a counter variable
       global counter
       counter += 1
       # sets the button  color and text based on whos 'turn' it is
       if counter % 2 == 0:
           btn.configure(bg = "red", text="O", state="disabled")
           global score
           score[counter]=btn
       else:
           btn.configure(bg = "blue", text="X", state="disabled")
           global score
           score[counter]=btn
       print(counter)
       print(score[counter])
       return counter



# ========================= GUI =====================================================#
# create new window
window = tkinter.Tk()
# create window title
window.title("Tic-Tac-Toe")
# set window size
window.geometry("300x300")
# all 9 buttons, with the name refering to the posistion on the grid
b00 = tkinter.Button(window, command=lambda: buttonchange(b00), text="#", padx=20, pady=20)
b00.grid(row=0, column=0)
b01 = tkinter.Button(window, command=lambda: buttonchange(b01), text="#", padx=20, pady=20)
b01.grid(row=0, column=1)
b02 = tkinter.Button(window, command=lambda: buttonchange(b02), text="#", padx=20, pady=20)
b02.grid(row=0, column=2)
b10 = tkinter.Button(window, command=lambda: buttonchange(b10), text="#", padx=20, pady=20)
b10.grid(row=1, column=0)
b11 = tkinter.Button(window, command=lambda: buttonchange(b11), text="#", padx=20, pady=20)
b11.grid(row=1, column=1)
b12 = tkinter.Button(window, command=lambda: buttonchange(b12), text="#", padx=20, pady=20)
b12.grid(row=1, column=2)
b20 = tkinter.Button(window, command=lambda: buttonchange(b20), text="#", padx=20, pady=20)
b20.grid(row=2, column=0)
b21 = tkinter.Button(window, command=lambda: buttonchange(b21), text="#", padx=20, pady=20)
b21.grid(row=2, column=1)
b22 = tkinter.Button(window, command=lambda: buttonchange(b22,), text="#", padx=20, pady=20)
b22.grid(row=2, column=2)
# label at bottom of screen will show winner and important info some day
label = tkinter.Label(window, text="Im a label!!").grid(row=3, column=0, columnspan=3)
#draws window
window.mainloop()
print(counter)
print (score)

