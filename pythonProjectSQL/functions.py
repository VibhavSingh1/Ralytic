import mysql.connector as con
import time
from widgets import *
from mysql.connector.cursor import MySQLCursor
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

np.set_printoptions(suppress=True)

mydb = con.MySQLConnection()
crsr = MySQLCursor()


def connect_base(name, pasw):
    try:
        mydb1 = con.connect(host='localhost',
                            user=name,
                            password=pasw)
    except con.Error as err:
        print(err.msg)
        return 101
    return mydb1


def sending_login_info():
    global mydb, crsr
    name = name_var.get().strip()
    pasw = pasw_var.get().strip()
    mydb = connect_base(name, pasw)
    if mydb == 101:
        name_entry.delete(0, END)
        pasw_entry.delete(0, END)
        conn_label.config(text='Wrong Username/Password')
    else:
        conn_label.config(text='Connecting...')
        time.sleep(5)
        crsr = mydb.cursor(named_tuple=True)
        connected()


def connected():
    login_frame.place(x=4000)
    place_main_page()


def place_login_page():

    login_frame.place(x=0, y=0)
    login_button.place(y=600, x=310)
    login_button.config(command=sending_login_info)
    name_label.place(y=490, x=180)
    pasw_label.place(y=540, x=180)
    name_entry.place(y=492, x=280)
    pasw_entry.place(y=542, x=280)
    login_page_deco1_frame.place(y=2, x=3)
    lg_deco_label.place(x=60, y=0)
    login_page_deco2_frame.place(y=453, x=860)
    conn_label.place(y=660, x=255)


def place_main_page():
    main_frame.place(x=0, y=0)
    clear_notepad()
    main_option_frame.place(x=20, y=350)
    main_deco_frame.place(x=9, y=8)
    mp_deco_label.place(x=0, y=0)
    main_deco_frame2.place(x=5, y=664)
    main_data_button.place(x=17, y=30)
    main_data_button.config(command=place_data_page)
    main_analysis_button.place(x=17, y=150)
    main_analysis_button.config(command=place_analytic_page)
    logout_button.place(x=440, y=30)
    logout_button.config(command=logout_base)
    main_notepad_frame.place(x=900, y=350)
    main_notepad_txt.place(x=5, y=5)
    main_notepad_label.place(x=317, y=5)
    main_notepad_clear_button.place(x=317, y=120)
    main_notepad_clear_button.config(command=clear_notepad)
    main_notepad_save_button.place(x=317, y=195)
    main_notepad_save_button.config(command=save_notepad)
    main_notepad_load()


def remove_main_page():
    main_frame.place(x=4000, y=0)
    conn_label.config(text=' ')
    name_entry.delete(0, END)
    pasw_entry.delete(0, END)


def logout_base():
    mydb.close()
    remove_main_page()
    place_login_page()


def clear_notepad():
    main_notepad_txt.delete(1.0, END)


def save_notepad():
    container = main_notepad_txt.get(1.0, END)
    main_notepad = open('note.txt', 'w')
    main_notepad.write(container)
    main_notepad.close()


def main_notepad_load():
    main_notepad = open('note.txt', 'r')
    read_data = main_notepad.read(-1)
    print(read_data)
    main_notepad_txt.insert(1.0, read_data)
    main_notepad.close()

# Data show module:


result = list()
month = str()
month_dict = dict()
all_month = "january, february, march, april, may, june, july, august, september, october, november, december"
month_list = list()

var1 = StringVar()
var1.set('ALL')
var2 = StringVar()
var2.set('ALL')
var3 = StringVar()
var3.set('ALL')

check_var0 = IntVar()
check_var0.set(0)
check_var1 = IntVar()
check_var1.set(0)
check_var2 = IntVar()
check_var2.set(0)
check_var3 = IntVar()
check_var3.set(0)
check_var4 = IntVar()
check_var4.set(0)
check_var5 = IntVar()
check_var5.set(0)
check_var6 = IntVar()
check_var6.set(0)
check_var7 = IntVar()
check_var7.set(0)
check_var8 = IntVar()
check_var8.set(0)
check_var9 = IntVar()
check_var9.set(0)
check_var10 = IntVar()
check_var10.set(0)
check_var11 = IntVar()
check_var11.set(0)
check_var12 = IntVar()
check_var12.set(0)


option1 = ['ALL']
option2 = ['ALL']
option3 = ['ALL']

cb0 = Checkbutton(data_selection_frame, text='All Months', variable=check_var0,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )
cb1 = Checkbutton(data_selection_frame, text='January    ', variable=check_var1,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )
cb2 = Checkbutton(data_selection_frame, text='February   ', variable=check_var2,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )
cb3 = Checkbutton(data_selection_frame, text='March       ', variable=check_var3,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )
cb4 = Checkbutton(data_selection_frame, text='April         ', variable=check_var4,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb5 = Checkbutton(data_selection_frame, text='May          ', variable=check_var5,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb6 = Checkbutton(data_selection_frame, text='June        ', variable=check_var6,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )
cb7 = Checkbutton(data_selection_frame, text='July        ', variable=check_var7,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb8 = Checkbutton(data_selection_frame, text='August    ', variable=check_var8,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb9 = Checkbutton(data_selection_frame, text='September ', variable=check_var9,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb10 = Checkbutton(data_selection_frame, text='October     ', variable=check_var10,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )

cb11 = Checkbutton(data_selection_frame, text='November  ', variable=check_var11,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )
cb12 = Checkbutton(data_selection_frame, text='December  ', variable=check_var12,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )


def menu_list():
    global option1, option3, option2
    option1.clear()
    option2.clear()
    option3.clear()
    option1 = ['ALL']
    option2 = ['ALL']
    option3 = ['ALL']
    crsr.execute("SELECT subdivision, year FROM rainfall.rainfall1950")
    result1 = crsr.fetchall()

    for x in result1:
        if x[0] not in option1:
            option1.append(x[0])
        if x[1] not in option2:
            option2.append(x[1])
        if x[1] not in option3:
            option3.append(x[1])


def data_show_query():
    global crsr
    x = check_var0.get()

    if var2.get() > var3.get():

        print('Choose years correctly!')

    elif var2.get() <= var3.get():

        query_string()

        if str(var1.get()) == 'ALL':
            if int(check_var0.get()) == 1:
                if var2.get() == 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'.format(all_month))

                elif var2.get() != 'ALL' and var3.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950 WHERE year={}'.format(all_month, var2.get()))

                elif var2.get() != 'ALL' and var3.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={}'.format(all_month, var2.get(), var3.get()))

            elif int(check_var0.get()) == 0 and month != '':

                if var2.get() == 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'.format(all_month))

                elif var2.get() != 'ALL' and var3.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950 WHERE year={}'.format(month.strip(','),
                                                                                                       var2.get()))

                elif var2.get() != 'ALL' and var3.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={}'.format(month.strip(','), var2.get(), var3.get()))

        elif var1.get() != 'ALL':
            if int(check_var0.get()) == 1:
                if var2.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950 '
                        'WHERE subdivision = "{}"'.format(all_month, str(var1.get())))

                elif var2.get() != 'ALL' and var3.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                        ' WHERE year={} AND subdivision = "{}"'.format(all_month, var2.get(), str(var1.get())))

                elif var2.get() != 'ALL' and var3.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={} AND subdivision = "{}"'.format(all_month, var2.get(),
                                                                                              var3.get(),
                                                                                              str(var1.get())))

            elif int(check_var0.get()) == 0 and month != '':
                print(month, "oo")

                if var2.get() == 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950 '
                                 'WHERE subdivision = "{}"'.format(month.strip(','), str(var1.get())))

                elif var2.get() != 'ALL' and var3.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                        ' WHERE year={} AND subdivision = "{}"'.format(month.strip(','), var2.get(), str(var1.get())))

                elif var2.get() != 'ALL' and var3.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={} AND subdivision = "{}"'.format(month.strip(','),
                                                                                              var2.get(),
                                                                                              var3.get(),
                                                                                              str(var1.get())))

        insert_txt()


def query_string():
    global month_dict, month, month_list
    month = ''
    month_dict.clear()
    month_list.clear()
    month_dict = {'january': check_var1.get(), 'february': check_var2.get(),
                  'march': check_var3.get(), 'april': check_var4.get(), 'may': check_var5.get(),
                  'june': check_var6.get(), 'july': check_var7.get(), 'august': check_var8.get(),
                  'september': check_var9.get(), 'october': check_var10.get(),
                  'november': check_var11.get(), 'december': check_var12.get()}

    for x in month_dict.keys():

        if month_dict[x] == 1:
            month = month + "," + str(x)
            month_list.append(str(x))

    print(month.strip(','))


def place_data_page():
    remove_main_page()
    data_show_frame.place(x=0, y=0)
    data_selection_frame.place(x=11, y=0)
    xscrollbar.pack(side=BOTTOM, fill=X)
    yscrollbar.pack(side=RIGHT, fill=Y)
    txt.place(x=580, y=10)
    xscrollbar.config(command=txt.xview)
    yscrollbar.config(command=txt.yview)
    menu_list()
    bl1.place(x=130, y=20)
    bl2.place(x=130, y=80)
    bl3.place(x=130, y=140)
    bl4.place(x=20, y=20)

    b1 = OptionMenu(data_selection_frame, var1, *option1)
    b2 = OptionMenu(data_selection_frame, var2, *option2)
    b3 = OptionMenu(data_selection_frame, var3, *option3)

    b1.place(x=245, y=20)
    b1.config(bg='grey24', fg='red2', activeforeground='red', activebackground='grey20',
              font=('calibre', 9, 'bold'))
    b2.place(x=245, y=80)
    b2.config(bg='grey24', fg='red2', activeforeground='red', activebackground='grey20',
              font=('calibre', 9, 'bold'))
    b3.place(x=245, y=140)
    b3.config(bg='grey24', fg='red2', activeforeground='red', activebackground='grey20',
              font=('calibre', 9, 'bold'))
    cb0.place(x=20, y=60)
    cb1.place(x=20, y=90)
    cb2.place(x=20, y=120)
    cb3.place(x=20, y=150)
    cb4.place(x=20, y=180)
    cb5.place(x=20, y=210)
    cb6.place(x=20, y=240)
    cb7.place(x=20, y=270)
    cb8.place(x=20, y=300)
    cb9.place(x=20, y=330)
    cb10.place(x=20, y=360)
    cb11.place(x=20, y=390)
    cb12.place(x=20, y=420)
    button.place(x=20, y=480)
    button.config(command=data_show_query)
    info_banner.place(y=550, x=140)
    back_to_main.place(x=200, y=460)
    back_to_main.config(command=remove_data_page)


def remove_data_page():
    data_show_frame.place(x=2500, y=2500)
    place_main_page()


def insert_txt():
    global crsr, txt, result, month_list, check_var0
    txt.delete(0.1, END)
    monlen = len(month_list)
    cdx = int(check_var0.get())
    print(cdx, monlen)

    if monlen == 0 and cdx == 0:
        txt.insert(0.1, 'SELECT MONTH!!')

    elif monlen == 1:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | \n".format('Subdivision:', 'Year', month_list[0]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                   x.year,
                                                                   x[2]))
    elif monlen == 2:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                        month_list[0],
                                                                        month_list[1]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                            x.year,
                                                                            x[2],
                                                                            x[3]))
    elif monlen == 3:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                 month_list[0],
                                                                                 month_list[1],
                                                                                 month_list[2]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                     x.year,
                                                                                     x[2],
                                                                                     x[3],
                                                                                     x[4]))

    elif monlen == 4:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                          month_list[0],
                                                                                          month_list[1],
                                                                                          month_list[2],
                                                                                          month_list[3]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                              x.year,
                                                                                              x[2],
                                                                                              x[3],
                                                                                              x[4],
                                                                                              x[5]))
    elif monlen == 5:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                                   month_list[0],
                                                                                                   month_list[1],
                                                                                                   month_list[2],
                                                                                                   month_list[3],
                                                                                                   month_list[4]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                       x.year,
                                                                                                       x[2],
                                                                                                       x[3],
                                                                                                       x[4],
                                                                                                       x[5],
                                                                                                       x[6]))
    elif monlen == 6:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                                            month_list[0],
                                                                                                            month_list[1],
                                                                                                            month_list[2],
                                                                                                            month_list[3],
                                                                                                            month_list[4],
                                                                                                            month_list[5]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                x.year,
                                                                                                                x[2],
                                                                                                                x[3],
                                                                                                                x[4],
                                                                                                                x[5],
                                                                                                                x[6],
                                                                                                                x[7]))
    elif monlen == 7:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                                            month_list[0],
                                                                                                            month_list[1],
                                                                                                            month_list[2],
                                                                                                            month_list[3],
                                                                                                            month_list[4],
                                                                                                            month_list[5],
                                                                                                                     month_list[6]))
        result = crsr.fetchall()

        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                        x.year,
                                                                                                                        x[2],
                                                                                                                        x[3],
                                                                                                                        x[4],
                                                                                                                        x[5],
                                                                                                                        x[6],
                                                                                                                        x[7],
                                                                                                                        x[8]))
    elif monlen == 8:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}\n".format('Subdivision:', 'Year',
                                                                                                                            month_list[0],
                                                                                                                            month_list[1],
                                                                                                                            month_list[2],
                                                                                                                            month_list[3],
                                                                                                                            month_list[4],
                                                                                                                            month_list[5],
                                                                                                                            month_list[6],
                                                                                                                            month_list[7]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                                  x.year,
                                                                                                                                  x[2],
                                                                                                                                  x[3],
                                                                                                                                  x[4],
                                                                                                                                  x[5],
                                                                                                                                  x[6],
                                                                                                                                  x[7],
                                                                                                                                  x[8],
                                                                                                                                  x[9]))

    elif monlen == 9:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10}\n".format('Subdivision:', 'Year',
                                                                                                                            month_list[0],
                                                                                                                            month_list[1],
                                                                                                                            month_list[2],
                                                                                                                            month_list[3],
                                                                                                                            month_list[4],
                                                                                                                            month_list[5],
                                                                                                                            month_list[6],
                                                                                                                            month_list[7],
                                                                                                                                     month_list[8]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                                  x.year,
                                                                                                                                  x[2],
                                                                                                                                  x[3],
                                                                                                                                  x[4],
                                                                                                                                  x[5],
                                                                                                                                  x[6],
                                                                                                                                  x[7],
                                                                                                                                  x[8],
                                                                                                                                  x[9],
                                                                                                                                           x[10]))
    elif monlen == 10:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                                                            month_list[0],
                                                                                                                            month_list[1],
                                                                                                                            month_list[2],
                                                                                                                            month_list[3],
                                                                                                                            month_list[4],
                                                                                                                            month_list[5],
                                                                                                                            month_list[6],
                                                                                                                            month_list[7],
                                                                                                                                     month_list[8],
                                                                                                                                              month_list[9]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                                  x.year,
                                                                                                                                  x[2],
                                                                                                                                  x[3],
                                                                                                                                  x[4],
                                                                                                                                  x[5],
                                                                                                                                  x[6],
                                                                                                                                  x[7],
                                                                                                                                  x[8],
                                                                                                                                  x[9],
                                                                                                                                  x[10],
                                                                                                                                  x[11]))

    elif monlen == 11:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                                                            month_list[0],
                                                                                                                            month_list[1],
                                                                                                                            month_list[2],
                                                                                                                            month_list[3],
                                                                                                                            month_list[4],
                                                                                                                            month_list[5],
                                                                                                                            month_list[6],
                                                                                                                            month_list[7],
                                                                                                                                     month_list[8],
                                                                                                                                              month_list[9],
                                                                                                                                                           month_list[10]))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                                  x.year,
                                                                                                                                  x[2],
                                                                                                                                  x[3],
                                                                                                                                  x[4],
                                                                                                                                  x[5],
                                                                                                                                  x[6],
                                                                                                                                  x[7],
                                                                                                                                  x[8],
                                                                                                                                  x[9],
                                                                                                                                  x[10],
                                                                                                                                  x[11],
                                                                                                                                  x[12]))
    elif monlen == 12 or cdx == 1:
        txt.insert(0.1, "**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n".format('Subdivision:', 'Year',
                                                                                                                            'january',
                                                                                                                            'february',
                                                                                                                            'march',
                                                                                                                            'april',
                                                                                                                            'may',
                                                                                                                            'june',
                                                                                                                            'july',
                                                                                                                            'august',
                                                                                                                            'september',
                                                                                                                            'october',
                                                                                                                            'november',
                                                                                                                            'december'))
        result = crsr.fetchall()
        for x in result:
            txt.insert(END, '**{:<35}| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |\n'.format(x.subdivision,
                                                                                                                                  x.year,
                                                                                                                                  x[2],
                                                                                                                                  x[3],
                                                                                                                                  x[4],
                                                                                                                                  x[5],
                                                                                                                                  x[6],
                                                                                                                                  x[7],
                                                                                                                                  x[8],
                                                                                                                                  x[9],
                                                                                                                                  x[10],
                                                                                                                                  x[11],
                                                                                                                                  x[12],
                                                                                                                                  x[13]))


# Analytic Page:

result11 = list()
month1 = str()
month_dict1 = dict()
all_month1 = "january, february, march, april, may, june, july, august, september, october, november, december"
month_list1 = list()

month_avg = list()
avg_year = list()

var11 = StringVar()
var11.set('ALL')
var21 = StringVar()
var21.set('ALL')
var31 = StringVar()
var31.set('ALL')

check_var01 = IntVar()
check_var01.set(0)
check_var11 = IntVar()
check_var11.set(0)
check_var21 = IntVar()
check_var21.set(0)
check_var31 = IntVar()
check_var31.set(0)
check_var41 = IntVar()
check_var41.set(0)
check_var51 = IntVar()
check_var51.set(0)
check_var61 = IntVar()
check_var61.set(0)
check_var71 = IntVar()
check_var71.set(0)
check_var81 = IntVar()
check_var81.set(0)
check_var91 = IntVar()
check_var91.set(0)
check_var101 = IntVar()
check_var101.set(0)
check_var111 = IntVar()
check_var111.set(0)
check_var121 = IntVar()
check_var121.set(0)


option11 = ['ALL']
option21 = ['ALL']
option31 = ['ALL']


cb01 = Checkbutton(data_selection_frame1, text='All Months', variable=check_var01,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )

cb110 = Checkbutton(data_selection_frame1, text='January    ', variable=check_var11,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                  )

cb21 = Checkbutton(data_selection_frame1, text='February   ', variable=check_var21,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                  )

cb31 = Checkbutton(data_selection_frame1, text='March       ', variable=check_var31,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb41 = Checkbutton(data_selection_frame1, text='April         ', variable=check_var41,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb51 = Checkbutton(data_selection_frame1, text='May          ', variable=check_var51,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb61 = Checkbutton(data_selection_frame1, text='June        ', variable=check_var61,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb71 = Checkbutton(data_selection_frame1, text='July        ', variable=check_var71,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb81 = Checkbutton(data_selection_frame1, text='August    ', variable=check_var81,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb91 = Checkbutton(data_selection_frame1, text='September ', variable=check_var91,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='red2',
                  font=('calibre', 10, 'bold')
                  )

cb101 = Checkbutton(data_selection_frame1, text='October     ', variable=check_var101,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )

cb111 = Checkbutton(data_selection_frame1, text='November  ', variable=check_var111,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )

cb121 = Checkbutton(data_selection_frame1, text='December  ', variable=check_var121,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='red2',
                   font=('calibre', 10, 'bold')
                   )


def menu_list1():
    global option11, option31, option21, result11
    option11.clear()
    option21.clear()
    option31.clear()
    option11 = ['ALL']
    option21 = ['ALL']
    option31 = ['ALL']
    crsr.execute("SELECT subdivision, year FROM rainfall.rainfall1950")
    result11 = crsr.fetchall()

    for x in result11:
        if x[0] not in option11:
            option11.append(x[0])
        if x[1] not in option21:
            option21.append(x[1])
        if x[1] not in option31:
            option31.append(x[1])


def query_string1():
    global month_dict1, month1, month_list1
    month1 = ''
    month_dict1.clear()
    month_list1.clear()
    month_dict1 = {'january': check_var11.get(), 'february': check_var21.get(),
                   'march': check_var31.get(), 'april': check_var41.get(), 'may': check_var51.get(),
                   'june': check_var61.get(), 'july': check_var71.get(), 'august': check_var81.get(),
                   'september': check_var91.get(), 'october': check_var101.get(),
                   'november': check_var111.get(), 'december': check_var121.get()}

    for x in month_dict1.keys():

        if month_dict1[x] == 1:
            month1 = month1 + "," + str(x)
            month_list1.append(str(x))

    print(month1.strip(','))


def data_show_query1():
    global crsr

    if var21.get() > var31.get():

        print('Choose years correctly!')

    elif var21.get() <= var31.get():

        query_string1()

        if str(var11.get()) == 'ALL':
            if int(check_var01.get()) == 1:
                if var21.get() == 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'.format(all_month1))

                elif var21.get() != 'ALL' and var31.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950 WHERE year={}'.format(all_month1, var21.get()))

                elif var21.get() != 'ALL' and var31.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={}'.format(all_month1, var21.get(), var31.get()))

            elif int(check_var01.get()) == 0 and month1 != '':

                if var21.get() == 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'.format(all_month1))

                elif var21.get() != 'ALL' and var31.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950 WHERE year={}'.format(month1.strip(','),
                                                                                                       var21.get()))

                elif var21.get() != 'ALL' and var31.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={}'.format(month1.strip(','), var21.get(), var31.get()))

        elif var11.get() != 'ALL':
            if int(check_var01.get()) == 1:
                if var21.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950 '
                        'WHERE subdivision = "{}"'.format(all_month1, str(var11.get())))

                elif var21.get() != 'ALL' and var31.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                        ' WHERE year={} AND subdivision = "{}"'.format(all_month1, var21.get(), str(var11.get())))

                elif var21.get() != 'ALL' and var31.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={} AND subdivision = "{}"'.format(all_month1, var21.get(),
                                                                                              var31.get(),
                                                                                              str(var11.get())))

            elif int(check_var01.get()) == 0 and month1 != '':
                print(month1, "oo")

                if var21.get() == 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950 '
                                 'WHERE subdivision = "{}"'.format(month1.strip(','), str(var11.get())))

                elif var21.get() != 'ALL' and var31.get() == 'ALL':
                    crsr.execute(
                        'SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                        ' WHERE year={} AND subdivision = "{}"'.format(month1.strip(','), var21.get(), str(var11.get())))

                elif var21.get() != 'ALL' and var31.get() != 'ALL':
                    crsr.execute('SELECT subdivision, year, {} FROM rainfall.rainfall1950'
                                 ' WHERE year>={} AND year<={} AND subdivision = "{}"'.format(month1.strip(','),
                                                                                              var21.get(),
                                                                                              var31.get(),
                                                                                              str(var11.get())))

        # insert a graph calling and average cal function here
        get_data_avg()
        plotting()
        print("sum of month: ", month_avg)
        print("sum of year: ", avg_year)


def get_data_avg():
    global result11, crsr, avg_year, month_avg

    avg_year.clear()
    month_avg.clear()

    result11 = crsr.fetchall()

    if check_var01 != 0 or len(month_list1) != 0:

        data_matrix = np.zeros((len(result11), len(result11[0]) - 2))
        print(len(result11), len(result11[0]) - 2, data_matrix)

        for x in range(len(result11)):
            for y in range(2, len(result11[x])):
                data_matrix[x][y-2] = format(result11[x][y], '.2f')
        print(data_matrix)
        for x in range(len(data_matrix)):
            sum_year = format(np.sum(data_matrix[x]), '.2f')
            avg_year.append(float(sum_year))
        for y in range(len(data_matrix[0])):
            sum_month = 0
            for x in range(len(data_matrix)):
                sum_month = sum_month + data_matrix[x][y]
            month_avg.append(float(sum_month))


def plotting():
    global month_avg, avg_year, month_list1, var21, var31, option31

    templist = all_month1.split(', ')
    fig = Figure(figsize=(8, 7), dpi=100)

    plot1 = fig.add_subplot(211)
    print(len(month_list1), " ", len(month_avg))
    if len(month_list1) == 0:
        print(templist)
        plot1.bar(templist, month_avg)
    else:
        plot1.bar(month_list1, month_avg)
    canvas = FigureCanvasTkAgg(fig, master=analytic_page_frame)
    canvas.draw()

    canvas.get_tk_widget().place(x=550, y=20)
    toolbar = NavigationToolbar2Tk(canvas, analytic_page_frame)
    toolbar.update()
    toolbar.place(x=550, y=700)
    insert_stat()


def place_analytic_page():

    remove_main_page()
    analytic_page_frame.place(x=0, y=0)
    data_selection_frame1.place(x=0, y=0)

    menu_list1()

    b11 = OptionMenu(data_selection_frame1, var11, *option11)

    b21 = OptionMenu(data_selection_frame1, var21, *option21)

    b31 = OptionMenu(data_selection_frame1, var31, *option31)

    b11.place(x=245, y=20)
    b11.config(bg='grey24', fg='red2', activeforeground='red', activebackground='grey20',
               font=('calibre', 9, 'bold'))
    b21.place(x=245, y=80)
    b21.config(bg='grey24', fg='red2', activeforeground='red', activebackground='grey20',
               font=('calibre', 9, 'bold'))
    b31.place(x=245, y=140)
    b31.config(bg='grey24', fg='red2', activeforeground='red', activebackground='grey20',
               font=('calibre', 9, 'bold'))

    cb01.place(x=20, y=60)
    cb110.place(x=20, y=90)
    cb21.place(x=20, y=120)
    cb31.place(x=20, y=150)
    cb41.place(x=20, y=180)
    cb51.place(x=20, y=210)
    cb61.place(x=20, y=240)
    cb71.place(x=20, y=270)
    cb81.place(x=20, y=300)
    cb91.place(x=20, y=330)
    cb101.place(x=20, y=360)
    cb111.place(x=20, y=390)
    cb121.place(x=20, y=420)

    bl11.place(x=130, y=20)
    bl21.place(x=130, y=80)
    bl31.place(x=130, y=140)
    bl41.place(x=20, y=20)

    button1.config(command=data_show_query1)
    button1.place(x=20, y=480)
    info_banner1.place(y=550, x=140)
    back_to_main1.config(command=remove_analytic_page)
    back_to_main1.place(x=10, y=530)
    stat_banner.config(height=16, width=40, font=('calibre', 11, 'bold'))
    stat_banner.place(x=140, y=200)


def remove_analytic_page():
    analytic_page_frame.place(x=2500, y=2500)
    place_main_page()


def insert_stat():
    global avg_year, month_avg
    stat_banner.delete(0.1, END)
    t_sum = 0
    for x in avg_year:
        t_sum = t_sum + x
    t_avg = t_sum/len(avg_year)
    stat_banner.insert(0.1, "     This Stat is for all the years selected:\n")
    stat_banner.insert(END, "Average over all the years combined:\n{}\n".format(t_avg))
    if len(month_list1) == 0 and int(check_var01.get()) == 1:
        temp_list = all_month1.split(', ')
        for x in range(len(temp_list)):
            stat_banner.insert(END, "\n{} : {}".format(temp_list[x], month_avg[x]))

    elif len(month_list1) != 0:
        for x in range(len(month_list1)):
            stat_banner.insert(END, "\n{} : {}".format(month_list1[x], month_avg[x]))





