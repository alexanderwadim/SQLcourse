from tkinter import *
from tkinter import messagebox

from pyodbc import Row

import mainApp
from queries import *


def addDishInMenu(EntryUserId):
    window = Tk()
    window.title('dishRestriction')
    window.geometry('170x500')
    window.resizable(False, False)
    window['background'] = 'white'

    font_header = ('Times New Roman', 10, 'bold')
    font_entry = ('Times New Roman', 12)
    label_font = ('Times New Roman', 11)
    button_font = ('Times New Roman', 10)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}

    tired = EntryUserId


    def clickedEnter():
        idDish = 0
        name = name_entry.get()
        status = status_entry.get()
        description = description_entry.get()
        price = price_entry.get()

        setDishInMenu(idDish, name, description, price, status)
        window.destroy()
        mainApp.mainApp(getUserId(tired))

    name_label = Label(window, text='Name', font=label_font, **base_padding)
    name_label['background'] = 'white'
    name_label.pack()

    # ���� ����� name
    name_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    name_entry.pack()

    description_label = Label(window, text='Description', font=label_font, **base_padding)
    description_label['background'] = 'white'
    description_label.pack()

    # ���� ����� description
    description_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    description_entry.pack()

    price_label = Label(window, text='Price', font=label_font, **base_padding)
    price_label['background'] = 'white'
    price_label.pack()

    # ���� ����� price
    price_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    price_entry.pack()

    status_label = Label(window, text='Status', font=label_font, **base_padding)
    status_label['background'] = 'white'
    status_label.pack()

    # ���� ����� status
    status_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    status_entry.pack()

    # ������ �������� �����
    send_btn = Button(window, text='Enter', command=clickedEnter, font=button_font, foreground='green')
    send_btn.pack(**base_padding)

    def clickedBack():
        window.destroy()
        mainApp.mainApp(getUserId(EntryUserId))

    menu_btn = Button(window, text='Back', command=clickedBack, font=button_font, foreground='green')
    menu_btn.pack()

    window.mainloop()