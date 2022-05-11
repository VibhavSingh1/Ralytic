from tkinter import *
import mysql.connector as con

root = Tk()
root.geometry('1230x750')
data_selection_frame = Frame(root,
                             height=730,
                             width=530,
                             bg='grey20')
data_selection_frame.place(x=0, y=0)

xscrollbar = Scrollbar(root, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
yscrollbar = Scrollbar(root, orient=VERTICAL)
yscrollbar.pack(side=RIGHT, fill=Y)


mydb = con.connect(host='localhost', user='root', password='thunderoov')
crsr = mydb.cursor(named_tuple=True)
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


txt = Text(root, height=42, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, wrap=NONE)
txt.place(x=550, y=20)
xscrollbar.config(command=txt.xview)
yscrollbar.config(command=txt.yview)


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


menu_list()
bl1 = Label(data_selection_frame, text=' Subdivisions ',
            bd=4,
            bg='grey20',
            fg='SpringGreen2',
            font=('calibre', 11, 'bold')).place(x=130, y=20)
bl2 = Label(data_selection_frame, text=' From Year ',
            bd=4,
            bg='grey20',
            fg='SpringGreen2',
            font=('calibre', 11, 'bold')).place(x=130, y=80)
bl3 = Label(data_selection_frame, text=' To Year ',
            bd=4,
            bg='grey20',
            fg='SpringGreen2',
            font=('calibre', 11, 'bold')).place(x=130, y=140)
bl4 = Label(data_selection_frame, text='     Months     ',
            bd=4,
            bg='grey20',
            fg='SpringGreen2',
            font=('calibre', 11, 'bold')).place(x=20, y=20)
b1 = OptionMenu(data_selection_frame, var1, *option1)
b1.place(x=245, y=20)
b1.config(bg='grey24', fg='SpringGreen2', activeforeground='red', activebackground='grey20', font=('calibre', 9, 'bold'))
b2 = OptionMenu(data_selection_frame, var2, *option2)
b2.place(x=245, y=80)
b2.config(bg='grey24', fg='SpringGreen2', activeforeground='red', activebackground='grey20', font=('calibre', 9, 'bold'))
b3 = OptionMenu(data_selection_frame, var3, *option3)
b3.place(x=245, y=140)
b3.config(bg='grey24', fg='SpringGreen2', activeforeground='red', activebackground='grey20', font=('calibre', 9, 'bold'))

cb0 = Checkbutton(root, text='All Months', variable=check_var0,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='lime green',
                  font=('calibre', 10, 'bold')
                  )
cb0.place(x=20, y=60)
cb1 = Checkbutton(root, text='January    ', variable=check_var1,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb1.place(x=20, y=90)
cb2 = Checkbutton(root, text='February   ', variable=check_var2,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb2.place(x=20, y=120)
cb3 = Checkbutton(root, text='March       ', variable=check_var3,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb3.place(x=20, y=150)
cb4 = Checkbutton(root, text='April         ', variable=check_var4,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb4.place(x=20, y=180)
cb5 = Checkbutton(root, text='May          ', variable=check_var5,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb5.place(x=20, y=210)
cb6 = Checkbutton(root, text='June        ', variable=check_var6,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb6.place(x=20, y=240)
cb7 = Checkbutton(root, text='July        ', variable=check_var7,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb7.place(x=20, y=270)
cb8 = Checkbutton(root, text='August    ', variable=check_var8,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb8.place(x=20, y=300)
cb9 = Checkbutton(root, text='September ', variable=check_var9,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb9.place(x=20, y=330)
cb10 = Checkbutton(root, text='October     ', variable=check_var10,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                   )
cb10.place(x=20, y=360)
cb11 = Checkbutton(root, text='November  ', variable=check_var11,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                   )
cb11.place(x=20, y=390)
cb12 = Checkbutton(root, text='December  ', variable=check_var12,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                   )
cb12.place(x=20, y=420)

button = Button(root, command=data_show_query, text='Query',
                bd=4,
                bg='grey20',
                fg='SpringGreen2',
                font=('calibre', 11, 'bold'),
                activeforeground='red',
                activebackground='grey20'
                )
button.place(x=20, y=480)


# for row in crsr:
#     print("* {:<40}: {:<10} : {:<10}".format(
#         row.subdivision,
#         row.annual,
#         row.year
#     ))

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


info_banner = Label(data_selection_frame, font=('calibre', 12, 'bold'),
                    bg='grey20', fg='red',
                    text='Info:-\nRainfall Unit - millimeters\nDivision by Regions\nYear in "FROM" should be less than\n"TO".',)
info_banner.place(y=550, x=140)


root.mainloop()







