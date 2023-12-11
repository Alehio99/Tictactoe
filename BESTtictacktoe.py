from tkinter import *
from tkinter import messagebox

mansLogs = Tk()
mansLogs.title("TicTacToe")

speletajsX = True
count = 0

def btnClick(button):
    global speletajsX, count
    if button["text"] == " " and speletajsX == True:
        button["text"] = "X"
        speletajsX = False
        count += 1
        checkWinner()
    elif button["text"] == " " and speletajsX == False:
        button["text"] = "O"
        speletajsX = True
        count += 1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe", "Šeit kāds ir ieklikšķinājis!")

def checkWinner():
    global winner
    winner = False
    if (
        btn1["text"] == btn2["text"] == btn3["text"] == "X" or
        btn4["text"] == btn5["text"] == btn6["text"] == "X" or
        btn7["text"] == btn8["text"] == btn9["text"] == "X" or
        btn1["text"] == btn5["text"] == btn9["text"] == "X" or
        btn3["text"] == btn5["text"] == btn7["text"] == "X" or
        btn1["text"] == btn4["text"] == btn7["text"] == "X" or
        btn2["text"] == btn5["text"] == btn8["text"] == "X" or
        btn3["text"] == btn6["text"] == btn9["text"] == "X"
    ):
        winner = True
        disableButtons()
        messagebox.showinfo("TicTacToe", "Speletajs X ir uzvarētājs")
    elif (
        btn1["text"] == btn2["text"] == btn3["text"] == "O" or
        btn4["text"] == btn5["text"] == btn6["text"] == "O" or
        btn7["text"] == btn8["text"] == btn9["text"] == "O" or
        btn1["text"] == btn5["text"] == btn9["text"] == "O" or
        btn3["text"] == btn5["text"] == btn7["text"] == "O" or
        btn1["text"] == btn4["text"] == btn7["text"] == "O" or
        btn2["text"] == btn5["text"] == btn8["text"] == "O" or
        btn3["text"] == btn6["text"] == btn9["text"] == "O"
    ):
        winner = True
        disableButtons()
        messagebox.showinfo("TicTacToe", "Speletajs O ir uzvarētājs")
    elif count == 9:
        winner = False
        disableButtons()
        messagebox.showinfo("TicTacToe", "Neizšķirts")

def disableButtons():
    for button in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        button.config(state=DISABLED)

def enableButtons():
    for button in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        button.config(state=NORMAL)
        button["text"] = " "

btn1 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn1), bg="red")
btn2 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn2), bg="blue")
btn3 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn3), bg="red")
btn4 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn4), bg="blue")
btn5 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn5), bg="red")
btn6 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn6), bg="blue")
btn7 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn7), bg="red")
btn8 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn8), bg="blue")
btn9 = Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda: btnClick(btn9), bg="red")

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

galvenaIzvelne = Menu(mansLogs)
mansLogs.config(menu=galvenaIzvelne)
opcijas = Menu(galvenaIzvelne, tearoff=False)

galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

def reset():
    global winner, count, speletajsX
    winner = False
    count = 0
    speletajsX = True
    enableButtons()



def infoLogs():
    jaunsLogs = Toplevel()
    jaunsLogs.title('Info par programmu')
    jaunsLogs.geometry("300x300")
    apraksts = Label(jaunsLogs, text='Spēles noteikumi')
    apraksts.grid(row=0, column=0)


opcijas.add_command(label="Jauna spēle", command=reset)
opcijas.add_command(label="Iziet", command=mansLogs.quit)
opcijas.add_command(label="Par programmu", command=infoLogs)



mansLogs.mainloop()