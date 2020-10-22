import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
win.title("Calc")

# configure the window with one of these two ways...
# win.configure(width=300,height=300,background='blue')
# control where it displays n the screen: ...+0+0 (upper left)... +200+200 (200 right and down)
win.geometry('330x300+1200+500')

# some test code...
# label = ttk.Label(win,text="Hello World")
# button = ttk.Button(win,text="Hello")

exp = ''

text = tk.StringVar()

def press(num):
    global exp
    exp += str(num)
    text.set(exp)

def clr():
    global exp
    exp = ''
    text.set(exp)

def equal():
    global exp
    total = str(eval(exp))
    text.set(total)

# entry bar - row 0
entry = ttk.Entry(win, justify='right',textvariable=text)
entry.grid(row=0,columnspan=4,sticky='nsew')

# row 1
button7 = ttk.Button(win,text='7', command=lambda:press(7))
button7.grid(row=1,column=0)

button8 = ttk.Button(win,text='8', command=lambda:press(8))
button8.grid(row=1,column=1)

button9 = ttk.Button(win,text='9', command=lambda:press(9))
button9.grid(row=1,column=2)

buttonDiv = ttk.Button(win,text='/', command=lambda:press('/'))
buttonDiv.grid(row=1,column=3)

# row 2
button4 = ttk.Button(win,text='4', command=lambda:press(4))
button4.grid(row=2,column=0)

button5 = ttk.Button(win,text='5', command=lambda:press(5))
button5.grid(row=2,column=1)

button6 = ttk.Button(win,text='6', command=lambda:press(6))
button6.grid(row=2,column=2)

buttonMul = ttk.Button(win,text='x', command=lambda:press('*'))
buttonMul.grid(row=2,column=3)

# row 3
button1 = ttk.Button(win,text='1', command=lambda:press(1))
button1.grid(row=3,column=0)

button2 = ttk.Button(win,text='2', command=lambda:press(2))
button2.grid(row=3,column=1)

button3 = ttk.Button(win,text='3', command=lambda:press(3))
button3.grid(row=3,column=2)

buttonSub = ttk.Button(win,text='-', command=lambda:press('-'))
buttonSub.grid(row=3,column=3)

# row 4
button0 = ttk.Button(win,text='0', command=lambda:press(0))
button0.grid(row=4,column=0)

buttonDec = ttk.Button(win,text='.', command=lambda:press('.'))
buttonDec.grid(row=4,column=1)

buttonC = ttk.Button(win,text='C', command=clr)
buttonC.grid(row=4,column=2)

buttonPls = ttk.Button(win,text='+', command=lambda:press('+'))
buttonPls.grid(row=4,column=3)

# equal sign - row 5
buttonEq = ttk.Button(win,text='=', command=equal)
buttonEq.grid(row=5,columnspan=4, sticky='nsew')


# order of elemnts will be the same in the window:
# label.pack()
# button.pack()

win.mainloop()