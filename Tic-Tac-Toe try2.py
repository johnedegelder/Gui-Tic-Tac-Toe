import tkinter
from tkinter import*

# global variables
counter = 0 # Counter starting at 0

# function that is called when the buttons are pressed
def buttonpressed(btn):
        #grabs a counter variable
        global counter
        counter += 1
        # sets the button  color and text based on whos 'turn' it is
        if counter % 2 == 0:
            btn.configure(bg = "red", text="O", state="disabled") # sets the button to desired display values and disables it
        else:
            btn.configure(bg = "blue", text="X", state="disabled")

        print(counter)
        return counter
# function that uses the label, eventual use for scoring
def score(self):
    global counter
    if counter == 1:
        self.configure(text="working")
    else:
        print("Counter != 5")

# puts program in function called main
def main():
    print("YAY -- Main function is working")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # create new window
    window = tkinter.Tk()
    # create window title
    window.title("Tic-Tac-Toe")
    # set window size
    window.geometry("300x300")
    # all 9 buttons, with the name refering to the posistion on the grid
    b00 = tkinter.Button(window, command=lambda: (buttonpressed(b00), score(lbl)), text="#", padx=20, pady=20)
    b00.grid(row=0, column=0) #since .grid is used, this new line in needed to allow .configure to work
    b01 = tkinter.Button(window, command=lambda: (buttonpressed(b01), score(lbl)), text="#", padx=20, pady=20)
    b01.grid(row=0, column=1)
    b02 = tkinter.Button(window, command=lambda: (buttonpressed(b02), score(lbl)), text="#", padx=20, pady=20)
    b02.grid(row=0, column=2)
    b10 = tkinter.Button(window, command=lambda: (buttonpressed(b10), score(lbl)), text="#", padx=20, pady=20)
    b10.grid(row=1, column=0)
    b11 = tkinter.Button(window, command=lambda: (buttonpressed(b11), score(lbl)), text="#", padx=20, pady=20)
    b11.grid(row=1, column=1)
    b12 = tkinter.Button(window, command=lambda: (buttonpressed(b12), score(lbl)), text="#", padx=20, pady=20)
    b12.grid(row=1, column=2)
    b20 = tkinter.Button(window, command=lambda: (buttonpressed(b20), score(lbl)), text="#", padx=20, pady=20)
    b20.grid(row=2, column=0)
    b21 = tkinter.Button(window, command=lambda: (buttonpressed(b21), score(lbl)), text="#", padx=20, pady=20)
    b21.grid(row=2, column=1)
    b22 = tkinter.Button(window, command=lambda: (buttonpressed(b22), score(lbl)), text="#", padx=20, pady=20)
    b22.grid(row=2, column=2)

    # label at bottom of screen will show winner and important info some day
    lbl = tkinter.Label(window, text="Im a label!!")
    lbl.grid(row=3, column=0, columnspan=3) #since .grid is used, this new line in needed to allow .configure to work

    # draw window and start
    window.mainloop()

main()
