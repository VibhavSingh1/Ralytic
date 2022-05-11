from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.geometry("1360x750")
root.minsize(width=1360, height=750)
root.maxsize(width=1360, height=750)

login_frame = Frame(root,
                    height=750,
                    width=1360,
                    bg='grey17')
login_button = Button(login_frame,
                      height=2,
                      width=20,
                      text='LOGIN',
                      font=('calibre', 10, 'bold'),
                      bd=3)

name_var = tk.StringVar()
pasw_var = tk.StringVar()
name_label = Label(login_frame,
                   text='NAME:',
                   width=11,
                   height=2,
                   font=('calibre', 10, 'bold'))
name_entry = Entry(login_frame,
                   textvariable=name_var,
                   font=('calibre', 16, 'bold'),
                   bd=3,
                   width=24)
pasw_label = Label(login_frame,
                   text='PASSWORD:',
                   width=11, height=2,
                   font=('calibre', 10, 'bold'))
pasw_entry = Entry(login_frame,
                   textvariable=pasw_var,
                   font=('calibre', 16, 'bold'),
                   bd=3,
                   width=24)

login_page_deco1_frame = Frame(login_frame,
                               width=1353,
                               height=440)
login_page_deco2_frame = Frame(login_frame,
                               width=488,
                               height=280,
                               bg='firebrick2')
conn_label = Label(width=35,
                   height=2,
                   font=('calibre', 10, 'bold'),
                   bg='grey17',
                   fg='white')

image1 = Image.open("STATS.jpg")
test1 = ImageTk.PhotoImage(image1)

lg_deco_label = Label(login_page_deco1_frame, image=test1)
lg_deco_label.image = test1

# Main page widgets:
main_frame = Frame(root,
                   height=750,
                   width=1360,
                   bg='grey17')
main_option_frame = Frame(main_frame,
                          height=270,
                          width=860,
                          bg='grey23')
main_data_button = Button(main_option_frame,
                          height=3,
                          width=30,
                          text='Data Browser',
                          font=('calibre', 16, 'bold'),
                          bd=4)
main_analysis_button = Button(main_option_frame,
                              height=3,
                              width=30,
                              text='Analyze',
                              font=('calibre', 16, 'bold'),
                              bd=4)
main_deco_frame = Frame(main_frame,
                        height=300,
                        width=1340)
main_deco_frame2 = Frame(main_frame,
                         height=80,
                         width=1350, bg='grey18')

image2 = Image.open("stats_header_image_1_opt.jpg")
test2 = ImageTk.PhotoImage(image2)

mp_deco_label = Label(main_deco_frame, image=test2)
mp_deco_label.image = test2

logout_button = Button(main_option_frame,
                       height=3,
                       width=30,
                       text='Logout',
                       font=('calibre', 16, 'bold'),
                       bd=4)
main_notepad_frame = Frame(main_frame,
                           height=270,
                           width=440,
                           bg='grey23')

main_notepad_txt = Text(main_notepad_frame,
                        bg='grey15',
                        fg='white',
                        bd=4,
                        height=15, width=37,
                        insertbackground='white')

main_notepad_label = Label(main_notepad_frame,
                           height=5, width=11,
                           text='NotePad',
                           font=('calibre', 12, 'bold'),
                           bg='grey20', fg='lawn green', bd=3)
main_notepad_clear_button = Button(main_notepad_frame,
                                   text='Clear',
                                   bd=4, fg='lawn green',
                                   bg='grey20',
                                   font=('calibre', 12, 'bold'),
                                   height=2, width=10)
main_notepad_save_button = Button(main_notepad_frame,
                                  text='Save',
                                  bd=4, fg='lawn green',
                                  bg='grey20',
                                  font=('calibre', 12, 'bold'),
                                  height=2, width=10)

# View data page:


data_show_frame = Frame(root, width=1360, height=750, bg='red4')

data_selection_frame = Frame(data_show_frame,
                             height=730,
                             width=530,
                             bg='grey20')

xscrollbar = Scrollbar(root, orient=HORIZONTAL)
yscrollbar = Scrollbar(root, orient=VERTICAL)


txt = Text(data_show_frame, height=42, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, wrap=NONE)

bl1 = Label(data_selection_frame, text=' Subdivisions ',
            bd=4,
            bg='grey20',
            fg='red2',
            font=('calibre', 11, 'bold'))
bl2 = Label(data_selection_frame, text=' From Year ',
            bd=4,
            bg='grey20',
            fg='red2',
            font=('calibre', 11, 'bold'))
bl3 = Label(data_selection_frame, text=' To Year ',
            bd=4,
            bg='grey20',
            fg='red2',
            font=('calibre', 11, 'bold'))
bl4 = Label(data_selection_frame, text='     Months     ',
            bd=4,
            bg='grey20',
            fg='red2',
            font=('calibre', 11, 'bold'))


button = Button(data_selection_frame, text='Query',
                bd=4,
                bg='grey20',
                fg='red2',
                font=('calibre', 11, 'bold'),
                activeforeground='red',
                activebackground='grey20'
                )
info_banner = Label(data_selection_frame, font=('calibre', 12, 'bold'),
                    bg='grey20', fg='red',
                    text='Info:-\nRainfall Unit - millimeters\nDivision by Regions\nYear in "FROM" should be less than\n"TO".',)

back_to_main = Button(data_selection_frame, text="Main Page",
                      bd=4,
                      bg='grey20',
                      fg='red2',
                      font=('calibre', 11, 'bold'),
                      activeforeground='red',
                      activebackground='grey20'
                      )

# Analytic page:

analytic_page_frame = Frame(root, width=1360, height=750, bg='red4')
data_selection_frame1 = Frame(analytic_page_frame,
                              height=730,
                              width=530,
                              bg='grey20')
data_selection_frame1.place(x=0, y=0)

bl11 = Label(data_selection_frame1, text=' Subdivisions ',
             bd=4,
             bg='grey20',
             fg='red2',
             font=('calibre', 11, 'bold'))
bl21 = Label(data_selection_frame1, text=' From Year ',
             bd=4,
             bg='grey20',
             fg='red2',
             font=('calibre', 11, 'bold'))
bl31 = Label(data_selection_frame1, text=' To Year ',
             bd=4,
             bg='grey20',
             fg='red2',
             font=('calibre', 11, 'bold'))
bl41 = Label(data_selection_frame1, text='     Months     ',
             bd=4,
             bg='grey20',
             fg='red2',
             font=('calibre', 11, 'bold'))


button1 = Button(data_selection_frame1, text='Query',
                 bd=4,
                 bg='grey20',
                 fg='red2',
                 font=('calibre', 11, 'bold'),
                 activeforeground='red',
                 activebackground='grey20'
                 )


info_banner1 = Label(data_selection_frame1, font=('calibre', 12, 'bold'),
                     bg='grey20', fg='red',
                     text='Info:-\nRainfall Unit - millimeters\nDivision by Regions\nYear in "FROM" should be less than\n"TO".',)

back_to_main1 = Button(data_selection_frame1, text="Main Page",
                       bd=4,
                       bg='grey20',
                       fg='red2',
                       font=('calibre', 11, 'bold'),
                       activeforeground='red',
                       activebackground='grey20'
                      )

stat_banner = Text(master=data_selection_frame1)
