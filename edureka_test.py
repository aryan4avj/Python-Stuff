##def edureka1():
##    from collections import namedtuple
##
##    a=namedtuple( 'courses', 'number, name, type')
##    b=a(1,'python','lang')
##    print(b)
##
##def edureka2():
##    from collections import namedtuple
##
##    a=namedtuple( 'courses', 'number, name, type')
##    b=a.make([2,'python2','lang'])
##    print(b)
##
##def edureka3():
##    from collections import deque
##    a = deque['a','b','e','g','e','k']
##    print(a)
##
##pattern problems.
##def edureka4():
##    a=int(input("enter a no"))
##    for i in range(1,a+1):
##        print('')
##        for j in range(1,i+1):
##            print('*', end='')
##        
##def edureka5():
##    a=int(input("enter a no "))
##    for i in range(1,a+1):
##        k=a-i+1
##        while(k>0):
##            print(' ',end='')
##            k=k-1
##            if k==0:
##                for j in range(1,i+1):
##                    print('*', end='')
##        print('')
##
##def edureka6():
##    a=int(input("enter a no "))
##    for i in range(1,a+1):
##        k=a-i+1
##        while(k>0):
##            print(' ',end='')
##            k=k-1
##            if k==0:
##                for j in range(1,i+1):
##                    print('* ', end='')
##        print('')

from tkinter import *
import tkinter
from tkinter import messagebox
def proces():
    number1=Entry.get(E1)
    number2=Entry.get(E2)
    operator=Entry.get(E3)
    number1=int(number1)
    number2=int(number2)
    if operator =="+":
        answer=number1+number2
    if operator =="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    Entry.insert(E4,0,answer)
    print(answer)

top = tkinter.Tk()
L1 = Label(top, text="My calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1",).grid(row=1,column=0)
L3 = Label(top, text="Number 2",).grid(row=2,column=0)
L4 = Label(top, text="Operator",).grid(row=3,column=0)
L4 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = proces).grid(row=5,column=1,)

top.mainloop()

