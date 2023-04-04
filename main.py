from tkinter import Tk
from tkinter.ttk import Button
from tkinter.ttk import Entry
from tkinter.ttk import Label

def click_button():
    x1 = x1_entry.get()
    y1 = y1_entry.get()
    x2 = x2_entry.get()
    y2 = y2_entry.get()
    if x1 == '':
        x1_i = 0
    else:
        x1_i = int(x1)
    if y1 == '':
        y1_i = 0
    else:
        y1_i = int(y1)
    if x2 == '':
        x2_i = 0
    else:
        x2_i = int(x2)
    if y2 == '':
        y2_i = 0
    else:
        y2_i = int(y2)
    label_distanse = Label(text=f'Расстояние ={str(((x2_i-x1_i)**2 + (y2_i-y1_i)**2)**0.5)}', font=("Segoe UI", 14))
    label_distanse.grid(row=3, column=0, columnspan=4)


window = Tk()
window.title("Калькулятор растояний")
window.geometry("300x200")

x1_entry = Entry(width=10)
y1_entry = Entry(width=10)
x2_entry = Entry(width=10)
y2_entry = Entry(width=10)
button = Button(text='Рассчитать',command=click_button)

x1_entry.grid(row=1,column=0,pady=[30,0])
y1_entry.grid(row=1,column=1,pady=[30,0])
x2_entry.grid(row=1,column=2,padx=[20, 0],pady=[30,0])
y2_entry.grid(row=1,column=3,pady=[30,0])
button.grid(row=2,column=0,columnspan=4)

label_x1 = Label(text='X1', font=("Segoe UI", 14))
label_y1 = Label(text='Y1', font=("Segoe UI", 14))
label_x2 = Label(text='X2', font=("Segoe UI", 14))
label_y2 = Label(text='Y2', font=("Segoe UI", 14))


label_x1.grid(row=0,column=0,pady=[30,0])
label_y1.grid(row=0,column=1,pady=[30,0])
label_y2.grid(row=0,column=3,pady=[30,0])
label_x2.grid(row=0,column=2,padx=[20,0],pady=[30,0])

# Запуск окна
window.mainloop()