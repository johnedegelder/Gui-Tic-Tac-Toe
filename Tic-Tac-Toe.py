import tkinter
from tkinter import*
import tkinter as tk
# to allow scoreing to happen gives all buttons a false variable to pass to the function
btn00 = False
btn01 = False
btn02 = False
btn10 = False
btn11 = False
btn12 = False
btn20 = False
btn21 = False
btn22 = False

# Counter starting at 0
counter = 0

# function that is called when the buttons are pressed
def buttonpressed(btn,tf):
       #grabs a counter variable
       global counter
       counter += 1
       # sets the button  color and text based on whos 'turn' it is
       if counter % 2 == 0:
           btn.configure(bg = "red", text="O", state="disabled")
           tf=FALSE
       else:
           btn.configure(bg = "blue", text="X", state="disabled")
           tf=TRUE
       print(counter)
       return tf,counter



# create new window
window = tkinter.Tk()
# create window title
window.title("Tic-Tac-Toe")
# set window size
window.geometry("300x300")
# all 9 buttons, with the name refering to the posistion on the grid
b00 = tkinter.Button(window, command=lambda: buttonpressed(b00, btn00), text="#", padx=20, pady=20)
b00.grid(row=0, column=0)
b01 = tkinter.Button(window, command=lambda: buttonpressed(b01, btn01), text="#", padx=20, pady=20)
b01.grid(row=0, column=1)
b02 = tkinter.Button(window, command=lambda: buttonpressed(b02, btn02), text="#", padx=20, pady=20)
b02.grid(row=0, column=2)
b10 = tkinter.Button(window, command=lambda: buttonpressed(b10, btn10), text="#", padx=20, pady=20)
b10.grid(row=1, column=0)
b11 = tkinter.Button(window, command=lambda: buttonpressed(b11, btn11), text="#", padx=20, pady=20)
b11.grid(row=1, column=1)
b12 = tkinter.Button(window, command=lambda: buttonpressed(b12, btn12), text="#", padx=20, pady=20)
b12.grid(row=1, column=2)
b20 = tkinter.Button(window, command=lambda: buttonpressed(b20, btn20), text="#", padx=20, pady=20)
b20.grid(row=2, column=0)
b21 = tkinter.Button(window, command=lambda: buttonpressed(b21, btn21), text="#", padx=20, pady=20)
b21.grid(row=2, column=1)
b22 = tkinter.Button(window, command=lambda: buttonpressed(b22, btn22), text="#", padx=20, pady=20)
b22.grid(row=2, column=2)

label = tkinter.Label(window, text="Im a label!!").grid(row=3, column=0, columnspan=3)
if b00["state"]=="disabled":
    print ("finally")

if counter == 8:
    print("Counter is working as a universal variable!!")
# draw window and start
window.mainloop()

print(btn01)