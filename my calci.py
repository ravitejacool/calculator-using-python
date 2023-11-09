from tkinter import *

statement=""

def click(value):
    global statement
    statement = statement + str(value)
    equation.set(statement)

def clear():
    global statement
    statement=""
    equation.set("")

def equalto():
    try:
        global statement
        total = str(eval(statement))
        equation.set(total)
        statement = ""
    except:
        equation.set(" error ")
        statement = ""

            
window=Tk()
window.configure(background="grey")
window.title("MY CALCULATOR")
window.geometry("400x400")

equation = StringVar()
expression_area = Entry(window, textvariable=equation)
expression_area.grid(columnspan=4, ipadx=100)
button1 = Button(window, text=' 7 ', fg='black', bg='white',command=lambda: click(7), height=5, width=9)
button1.grid(row=2, column=0)
button2 = Button(window, text=' 8 ', fg='black', bg='white',command=lambda: click(8), height=5, width=9)
button2.grid(row=2, column=1)
button3 = Button(window, text=' 9 ', fg='black', bg='white',command=lambda: click(9), height=5, width=9)
button3.grid(row=2, column=2)
button4 = Button(window, text=' 4 ', fg='black', bg='white',command=lambda: click(4), height=5, width=9)
button4.grid(row=3, column=0)
button5 = Button(window, text=' 5 ', fg='black', bg='white',command=lambda: click(5), height=5, width=9)
button5.grid(row=3, column=1)
button6 = Button(window, text=' 6 ', fg='black', bg='white',command=lambda: click(6), height=5, width=9)
button6.grid(row=3, column=2)
button7 = Button(window, text=' 1 ', fg='black', bg='white',command=lambda: click(1), height=5, width=9)
button7.grid(row=4, column=0)
button8 = Button(window, text=' 2 ', fg='black', bg='white',command=lambda: click(2), height=5, width=9)
button8.grid(row=4, column=1)
button9 = Button(window, text=' 3 ', fg='black', bg='white',command=lambda: click(3), height=5, width=9)
button9.grid(row=4, column=2)
clear = Button(window, text=' clear ', fg='black', bg='white',command=clear, height=5, width=9)
clear.grid(row=5, column=0)
button0 = Button(window, text=' 0 ',fg='black', bg='white',command=lambda: click(0), height=5, width=9)
button0.grid(row=5,column=1)
equal = Button(window, text=' = ',fg='black',bg='white',command=equalto, height=5, width=9)
equal.grid(row=5,column=2)
plus = Button(window, text=' + ', fg='black', bg='white',command=lambda: click("+"), height=5, width=9)
plus.grid(row=2, column=3)
minus = Button(window, text=' - ', fg='black', bg='white',command=lambda: click("-"), height=5, width=9)
minus.grid(row=3, column=3)
multiply = Button(window, text=' * ', fg='black', bg='white',command=lambda: click("*"), height=5, width=9)
multiply.grid(row=4, column=3)
divide = Button(window, text=' / ', fg='black', bg='white',command=lambda: click("/"), height=5, width=9)
divide.grid(row=5, column=3)
window.mainloop()

 
