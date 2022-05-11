import mysql.connector as con
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
import numpy as np
np.set_printoptions(suppress=True)

root = Tk()
root.geometry("1230x750")

data_selection_frame1 = Frame(root,
                              height=730,
                              width=530,
                              bg='grey20')
data_selection_frame1.place(x=0, y=0)

mydb = con.connect(host='localhost', user='root', password='thunderoov')
crsr = mydb.cursor(named_tuple=True)

result = list()
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


def menu_list1():
    global option11, option31, option21
    option11.clear()
    option21.clear()
    option31.clear()
    option11 = ['ALL']
    option21 = ['ALL']
    option31 = ['ALL']
    crsr.execute("SELECT subdivision, year FROM rainfall.rainfall1950")
    result1 = crsr.fetchall()

    for x in result1:
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
    x = check_var01.get()

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


menu_list1()
bl11 = Label(data_selection_frame1, text=' Subdivisions ',
             bd=4,
             bg='grey20',
             fg='SpringGreen2',
             font=('calibre', 11, 'bold')).place(x=130, y=20)
bl21 = Label(data_selection_frame1, text=' From Year ',
             bd=4,
             bg='grey20',
             fg='SpringGreen2',
             font=('calibre', 11, 'bold')).place(x=130, y=80)
bl31 = Label(data_selection_frame1, text=' To Year ',
             bd=4,
             bg='grey20',
             fg='SpringGreen2',
             font=('calibre', 11, 'bold')).place(x=130, y=140)
bl41 = Label(data_selection_frame1, text='     Months     ',
             bd=4,
             bg='grey20',
             fg='SpringGreen2',
             font=('calibre', 11, 'bold')).place(x=20, y=20)
b11 = OptionMenu(data_selection_frame1, var11, *option11)
b11.place(x=245, y=20)
b11.config(bg='grey24', fg='SpringGreen2', activeforeground='red', activebackground='grey20', font=('calibre', 9, 'bold'))
b21 = OptionMenu(data_selection_frame1, var21, *option21)
b21.place(x=245, y=80)
b21.config(bg='grey24', fg='SpringGreen2', activeforeground='red', activebackground='grey20', font=('calibre', 9, 'bold'))
b31 = OptionMenu(data_selection_frame1, var31, *option31)
b31.place(x=245, y=140)
b31.config(bg='grey24', fg='SpringGreen2', activeforeground='red', activebackground='grey20', font=('calibre', 9, 'bold'))

cb01 = Checkbutton(root, text='All Months', variable=check_var01,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='lime green',
                   font=('calibre', 10, 'bold')
                   )
cb01.place(x=20, y=60)
cb11 = Checkbutton(root, text='January    ', variable=check_var11,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                  )
cb11.place(x=20, y=90)
cb21 = Checkbutton(root, text='February   ', variable=check_var21,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                  )
cb21.place(x=20, y=120)
cb31 = Checkbutton(root, text='March       ', variable=check_var31,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb31.place(x=20, y=150)
cb41 = Checkbutton(root, text='April         ', variable=check_var41,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb41.place(x=20, y=180)
cb51 = Checkbutton(root, text='May          ', variable=check_var51,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb51.place(x=20, y=210)
cb61 = Checkbutton(root, text='June        ', variable=check_var61,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb61.place(x=20, y=240)
cb71 = Checkbutton(root, text='July        ', variable=check_var71,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb71.place(x=20, y=270)
cb81 = Checkbutton(root, text='August    ', variable=check_var81,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb81.place(x=20, y=300)
cb91 = Checkbutton(root, text='September ', variable=check_var91,
                  onvalue=1, offvalue=0,
                  bd=4,
                  bg='grey20',
                  fg='SpringGreen2',
                  font=('calibre', 10, 'bold')
                  )
cb91.place(x=20, y=330)
cb101 = Checkbutton(root, text='October     ', variable=check_var101,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                   )
cb101.place(x=20, y=360)
cb111 = Checkbutton(root, text='November  ', variable=check_var111,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                   )
cb111.place(x=20, y=390)
cb121 = Checkbutton(root, text='December  ', variable=check_var121,
                   onvalue=1, offvalue=0,
                   bd=4,
                   bg='grey20',
                   fg='SpringGreen2',
                   font=('calibre', 10, 'bold')
                   )
cb121.place(x=20, y=420)

button1 = Button(root, command=data_show_query1, text='Query',
                bd=4,
                bg='grey20',
                fg='SpringGreen2',
                font=('calibre', 11, 'bold'),
                activeforeground='red',
                activebackground='grey20'
                )
button1.place(x=20, y=480)


info_banner1 = Label(data_selection_frame1, font=('calibre', 12, 'bold'),
                     bg='grey20', fg='red',
                     text='Info:-\nRainfall Unit - millimeters\nDivision by Regions\nYear in "FROM" should be less than\n"TO".',)
info_banner1.place(y=550, x=140)


def get_data_avg():
    global result, crsr, avg_year, month_avg

    avg_year.clear()
    month_avg.clear()

    result = crsr.fetchall()

    if check_var01 != 0 or len(month_list1) != 0:

        data_matrix = np.zeros((len(result), len(result[0]) - 2))
        print(len(result), len(result[0]) - 2, data_matrix)

        for x in range(len(result)):
            for y in range(2, len(result[x])):
                data_matrix[x][y-2] = format(result[x][y], '.2f')
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
    fig = Figure(figsize=(7, 7), dpi=100)

    plot1 = fig.add_subplot(211)
    print(len(month_list1), " ", len(month_avg))
    if len(month_list1) == 0:
        print(templist)
        plot1.bar(templist, month_avg)
    else:
        plot1.bar(month_list1, month_avg)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    canvas.get_tk_widget().place(x=550, y=20)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    toolbar.place(x=550, y=700)
    insert_stat()



stat_banner = Text(master=data_selection_frame1)
stat_banner.config(height=16, width=40, font=('calibre', 11, 'bold'))
stat_banner.place(x=140, y=200)


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


root.mainloop()




