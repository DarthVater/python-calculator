#vesion 2
# course: cmps3500
# CLASS project
# PYTHON IMPLEMENTATION OF A CUSTOM SCIENTIFIC CALCULATION
# 05/17/2020
# Author: Jake Vawter
# description: Implementation of a scientific calculator
from tkinter import *
import math
import re


expression = ""

def entry(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equals():

    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total

    except(ZeroDivisionError):
        equation.set("Can not divide by zero")
        expression = ""
    except(ValueError):
        equation.set("Value out of range")
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def sin():
    global expression
    x = math.radians(int(expression))
    sintotal = math.sin(x)
    total = str(round(sintotal, 6))
    expression = total
    equation.set(total)

def cos():
    global expression
    x = math.radians(int(expression))
    costotal = math.cos(x)
    total = str(costotal)
    expression = total
    equation.set(total)
def tan():
    global expression
    x = math.radians(int(expression))
    try :
        tantotal = math.tan(x)
        total = str(round(tantotal, 6))
        expression = total

    except:
        total ="error"
    equation.set(total)

def exp():
    global expression
    x = int(expression)
    total = str(math.exp(x))
    expression = total
    equation.set(total)
def log():
    global expression
    x = int(expression)
    try:
        total = str(math.log(x))
    except(ValueError):
        equation.set("Can not get log of negative number")
    expression = total
    equation.set(total)

def signchange():
    global expression
    exp = expression
    rep_exp = re.compile(r'(\-*[0-9]+\Z)')
    exp_group = re.search(rep_exp, exp)
    sub_grp = exp_group.group(0)
    rep_str = str(int(sub_grp) * -1)
    expression = re.sub(rep_exp, rep_str, exp)
    equation.set(expression)
"""
exponents(base) performs power of 3
and power of 2. TO use, user enters digit desired, then presses button,
this function will compute the desired operation with the given digit
"""
def exponents(power):
    global expression
    exp = int(expression)
    total = 0
    if(power == 3):
        total = 3** exp
    if(power == 2):
        total = 2** exp
    expression = str(total)
    equation.set(expression)

#Square roots and cube roots, checks for negative number and returns error if num is negative
def roots(type):
    global expression
    exp = int(expression)
    total = 0
    if (exp >= 0):
        if(type == 1):
            #Square root
            total = exp **(1/2)
        else:
            #Cubed root
            total = exp **(1/3)
        expression = str(total)
    else:
        expression = "error: negative number"
    equation.set(expression)
# Removes last digit or operation entered
def cancelLast():
    global expression
    exp = expression
    expression = exp[:-1]
    equation.set(expression)
#clears screen
def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    #Window
    window = Tk()

    window.configure(background="azure")
    window.title("Calculator")
    window.geometry("350x250")
    equation = StringVar()

    expression_entry = Entry(window, textvariable=equation)
    expression_entry.grid(columnspan=4, ipadx=70, row=0)
    equation.set('')

    #Buttons#
    button1 = Button(window, text=' 1 ', fg='black', bg='ivory', command=lambda: entry(1), height=1, width=7)
    button1.grid(row=4, column=1)
    button2 = Button(window, text=' 2 ', fg='black', bg='ivory', command=lambda: entry(2), height=1, width=7)
    button2.grid(row=4, column=2)
    button3 = Button(window, text=' 3 ', fg='black', bg='ivory', command=lambda: entry(3), height=1, width=7)
    button3.grid(row=4, column=3)
    button4 = Button(window, text=' 4 ', fg='black', bg='ivory', command=lambda: entry(4), height=1, width=7)
    button4.grid(row=3, column=1)
    button5 = Button(window, text=' 5 ', fg='black', bg='ivory', command=lambda: entry(5), height=1, width=7)
    button5.grid(row=3, column=2)
    button6 = Button(window, text=' 6 ', fg='black', bg='ivory', command=lambda: entry(6), height=1, width=7)
    button6.grid(row=3, column=3)
    button7 = Button(window, text=' 7 ', fg='black', bg='ivory', command=lambda: entry(7), height=1, width=7)
    button7.grid(row=2, column=1)
    button8 = Button(window, text=' 8 ', fg='black', bg='ivory', command=lambda: entry(8), height=1, width=7)
    button8.grid(row=2, column=2)
    button9 = Button(window, text=' 9 ', fg='black', bg='ivory', command=lambda: entry(9), height=1, width=7)
    button9.grid(row=2, column=3)
    button0 = Button(window, text=' 0 ', fg='black', bg='ivory', command=lambda: entry(0), height=1, width=7)
    button0.grid(row=5, column=1)
    plus = Button(window, text=' + ', fg='black', bg='ivory', command=lambda: entry("+"), height=1, width=7)
    plus.grid(row=5, column=4)
    minus = Button(window, text=' - ', fg='black', bg='ivory', command=lambda: entry("-"), height=1, width=7)
    minus.grid(row=4, column=4)
    multiply = Button(window, text=' * ', fg='black', bg='ivory', command=lambda: entry("*"), height=1, width=7)
    multiply.grid(row=3, column=4)
    divide = Button(window, text=' / ', fg='black', bg='ivory', command=lambda: entry("/"), height=1, width=7)
    divide.grid(row=2, column=4)
    equal = Button(window, text=' ok ', fg='black', bg='navajo white', command=equals, height=1, width=14)
    equal.grid(row=1, column=3, columnspan=2)
    clear = Button(window, text='Clear', fg='black', bg='cyan', command=clear, height=1, width=7)
    clear.grid(row=1, column=0)
    Decimal = Button(window, text=' . ', fg='black', bg='ivory', command=lambda: entry('.'), height=1, width=7)
    Decimal.grid(row=5, column=2)
    powerof3 = Button(window, text=' 3^x ', fg='black', bg='ivory', command=lambda: exponents(3), height=1, width=5)
    powerof3.grid(row=6, column=1)
    powerof2 = Button(window, text=' 2^x ', fg='black', bg='ivory', command=lambda: exponents(2), height=1, width=5)
    powerof2.grid(row=5, column=0)
    squareroot = Button(window, text=' sqrt(x) ', fg='black', bg='ivory', command=lambda: roots(1), height=1, width=5)
    squareroot.grid(row=4, column=0)
    cuberoot = Button(window, text=' sqrt3 ', fg='black', bg='ivory', command=lambda: roots(2), height=1, width=5)
    cuberoot.grid(row=6, column=0)
    sinButton = Button(window, text=' sin ', fg='black', bg='ivory', command=sin, height=1, width=7)
    sinButton.grid(row=6, column=3)
    cosButton = Button(window, text=' cos ', fg='black', bg='ivory', command=cos, height=1,width=7)
    cosButton.grid(row=6, column=2)
    tanButt = Button(window, text=' tan', fg='black', bg='ivory', command=tan, height=1, width=7)
    tanButt.grid(row=6, column=4)
    expButt = Button(window, text=' exp ', fg='black', bg='ivory', command=exp, height=1, width=7)
    expButt.grid(row=2, column=0)
    logButton = Button(window, text= 'log ', fg='black', bg='ivory', command=log, height=1, width=7)
    logButton.grid(row=3, column=0)
    signButton = Button(window, text=' +/- ', fg='black', bg='ivory', command=signchange, height=1, width=7)
    signButton.grid(row=5, column=3)
    cancelButton = Button(window, text=' cancel ', fg='black', bg='tomato', command=cancelLast, height=1, width=14)
    cancelButton.grid(row=1, column=1, columnspan=2)
    window.mainloop()
