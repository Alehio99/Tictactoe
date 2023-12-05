from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi
mansLogs=Tk() # loga objekts
mansLogs.title("TicTacToe")

btn1=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn2=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn3=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn4=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn5=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn6=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn7=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn8=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))
btn9=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24))

btn1.grid(row=0,column=0) #pievieno pogas 
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus
count=0 #aizpildīto rūtiņu skaits


def btnClick(button): #padod visu pogu
    global speletajsX,count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==" "and speletajsX==True:#spēlē X spēlētājs
        button["text"]="X"#maina uz X
        speletajsX=False
        count+=1 # palielina rūtiņu skaitu

    elif button["text"]==" " and speletajsX==False: # mainās spēlētāji
         button["text"]="0"
         speletajsX=True
         count+=1
    else:
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")


command=lambda:btnClick(btn1)
command=lambda:btnClick(btn2)
command=lambda:btnClick(btn3)
command=lambda:btnClick(btn4)
command=lambda:btnClick(btn5)
command=lambda:btnClick(btn6)
command=lambda:btnClick(btn7)
command=lambda:btnClick(btn8)
command=lambda:btnClick(btn9)



def checkWinner():
    global winner
    winner=False #noteiks, ja būs neizšķirts
    if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" and btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" and btn7["text"]=="X" and btn8["text"]=="X"or btn9["text"]=="X"):
        winner=True
        messagebox.showinfo("TicTacToe","SpeletajsX ir uzvarētājs")
    elif (btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O" and btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O"  and btn7["text"]=="O" and btn8["text"]=="O"  or btn9["text"]=="O" ):
        winner=True
        messagebox.showinfo("TicTacToe","SpeletajsO ir uzvarētājs")


    elif count==9 and winner==False:
        messagebox.showinfo("TicTacToe", "Neizšķirts")




mansLogs.mainloop()
