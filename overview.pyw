# © Copyright Sussex Police
#
# This software is licensed 'as-is'.  You bear the risk of using it.  In
# consideration for use of the software, you agree that you have not relied upon
# any, and we have made no, warranties, whether oral, written, or implied, to
# you in relation to the software.  To the extent permitted at law, we disclaim
# any and all warranties, whether express, implied, or statutory, including, but
# without limitation, implied warranties of non-infringement of third party
# rights, merchantability and fitness for purpose.
# 
# In no event will we be held liable to you for any loss or damage (including
# without limitation loss of profits or any indirect or consequential losses)
# arising from the use of this software.
#
# Permission is granted to LAW ENFORCEMENT ONLY to use this software free of charge
# for any purpose and to alter it and redistribute it freely, subject to the
# following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the form of
# "Copyright Sussex Police" in the product
# documentation would be appreciated but is not required.
#
# 2. Altered versions of the source code must be plainly marked as such, and
# must not be misrepresented as being the original software.
#
# 3. This copyright notice and disclaimer may not be removed from or varied in
# any copy of the software (whether in its original form or any altered version)
#
# DESCRIPTION:
# CASE
#
# Author:
# Ryan Ward - Sussex Police
#
# Contact: ryan.ward@sussex.pnn.police.uk
#
# Version: 3.0.0 - LargeScreen
#
# Tested with Word 2003, 2013
#
#/usr/bin/env python3

############################################################################################
import sqlite3
import os
import hashlib
import re
from sys import argv
import string
import secrets
import shutil
import ctypes
import glob
import time
import datetime
from datetime import date
import tempfile
from time import sleep
import threading
from random import choice, shuffle
from string import printable
from tkinter import * 
from tkinter import ttk, messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import font
import subprocess
import docx
from docx import *
from docx import Document
from docx.shared import Pt
import xlsxwriter
from PIL import ImageTk, Image, ImageGrab
import random
from random import choice
############################################################################################
assignedcasevariables=[]
overviewvariables=[]
opencasevariables=[]
closedcasevariables=[]
pindecryptvariables=[]
individualcasevariables=[]
individual_pd_casevariables=[]
new_notification_variables=[]
############################################################################################
def readopencases():
    global opencases, casecount, case_dir, template_dir, contemp_file, examiner
    sqlprolocal = ("C:\\Case Creator\\casecreator.sqlite3")
    analyst='R WARD 32533'
    try:
        conn = sqlite3.connect(sqlprolocal, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        opencases=[]
        c.execute(""" select * from cases WHERE analyst like '%'||?||'%'""", (analyst,))
        for each in c:
            opencases.append(each)
        conn.close()
        
    except:
        conn = sqlite3.connect(sqlprolocal, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        opencases=[]
        c.execute(""" select * from cases WHERE analyst like '%'||?||'%'""", (analyst,))
        for each in c:
            opencases.append(each)
            opencases_easy_view.append(each[11]+" - "+each[3])
        conn.close()
    #casecount = (len(cases))
############################################################################################
def populate_individual_case():
    global TEXT
    try:
        case_get = d1a.get()
        print('case get', case_get)
        TEXT = case_get[:7]
        get_individual_case_data()
    except:
        pass
############################################################################################
def update_scrollregion(event):
    photoCanvas1.configure(scrollregion=photoCanvas1.bbox("all"))
############################################################################################
def notepad_overview_notes1(*args):
    get=notepad_overview.get(1.0, END)
    print('in func.', get)
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    conn = sqlite3.connect(sqlprolocal, isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    c=conn.cursor()
    c.execute(""" UPDATE notepad SET notes = ? WHERE _rowid_ = 1""", (get,))
    idno=2
    c.execute(""" UPDATE notepad SET last_written = ? WHERE _rowid_ = 1""", (timestamp,))
    conn.commit()
    conn.close()
    notepad_n59b.delete(1.0,END)
    notepad_n59b.insert(INSERT, get)
############################################################################################
def gui():
    global root, open_cases, height, width, left1, right1, left_frame, right_frame, photoCanvas1, photoCanvas2
    root = Tk()

    #root.iconbitmap(iconfile)
    root.title("CASE")# - "+analyst)
    root.resizable(width=True, height=True)
    root.geometry('1800x720')
    width  = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(width)
    print(height)

    root.attributes("-fullscreen", False)
    #menu()

    #FRAME SETUP / SPACING
    tabs = ttk.Notebook(root)

    tabs.pack(fill='both', expand=Y)

    open_cases=ttk.Frame()
    #graykey=ttk.Frame()
    notepad=ttk.Frame()
    #notifications=ttk.Frame()
    #settings=ttk.Frame()
    #about=ttk.Frame()
    #triage=ttk.Frame()

    tabs.add(open_cases,text='Casework')
    #tabs.add(graykey,text='Graykey')
    tabs.add(notepad,text='Notepad')
    #tabs.add(notifications,text='Notifications')
    #tabs.add(settings,text='Settings')
    #tabs.add(about,text='About')
    #tabs.add(triage,text='Triage')

    ### Notepad tab (scroll WORKING)
    notepad_scrollbar = Scrollbar(notepad)
    #Label(notepad, text=" Results/Findings: ").grid(row=5, column=0, sticky=W, pady=0, columnspan=6)
    notepad_n59b=Text(notepad, wrap=WORD, width=width, height=50, yscrollcommand=notepad_scrollbar.set)
    notepad_n59b.grid(row=1, column=0, columnspan=1, sticky=EW, rowspan=1)
##    print('Len notepadentries:',(len(notepadentries)))
##    if (len(notepadentries))==2:
##            print('in func')
##            notepadnotes1_text = (str(notepadentries[1]))
##            notepadnotes1_text = (str.replace(notepadnotes1_text,"\\n","\n"))
##            notepad_n59b.insert(INSERT, notepadnotes1_text)
##    else:
##        pass
    notepad_n59b.grid_propagate(False)
    #notepad_n59b.bind('<KeyRelease>', notepadnotes1)
    notepad_scrollbar.config( command = notepad_n59b.yview)
    notepad_scrollbar.bind('<MouseWheel>', notepad_n59b)
    notepad_scrollbar.grid(row=1, column=1, rowspan=1,  sticky='NS')

    ############################################################################################

    left_frame = Frame(open_cases, borderwidth=1,relief=RIDGE)
    left_frame.grid(row=0, column=1, columnspan=10, sticky=E) 

    photoCanvas1 = Canvas(left_frame, width=1000, height=(height)-45) #width=width, height=(height)-45)
    photoCanvas1.grid()#sticky=NSEW)

    left1 = Frame(photoCanvas1, width=width, height=10000)
    photoCanvas1.create_window(0, 0, window=left1, anchor='nw')
    ############################################################################################

    right_frame = Frame(open_cases, borderwidth=1,relief=RIDGE)
    right_frame.grid(row=0, column=11, columnspan=10, sticky=W)

    photoCanvas2 = Canvas(right_frame, width=800, height=(height)-45) #width=width, height=(height)-45)
    photoCanvas2.grid()#sticky=NSEW)

    right1 = Frame(photoCanvas2, width=width, height=10000)
    photoCanvas2.create_window(0, 0, window=right1, anchor='nw')
    ############################################################################################

 

    ############################################################################################
    # Monitoring tab changes
    #tabs.bind('<<NotebookTabChanged>>', lambda x: ontabchangelock())
    #everyfive()
    overview()
    root.mainloop()
############################################################################################
def overview():
    global left1, right1, row, notepad_overview, Entry1a, Entry2a, Entry3a, Entry4a, Entry5a, Entry6a, entry1, Entry2a, Entry3a, Entry4a, Entry5a, Entry6a, opencasevariables, notepad_n59b_overview, photoScrollv, photoScrollh, photoCanvas1, photoCanvas2
    #readpindecryptlog()
    #readnotepad()
    readopencases()
##    for each in pindecryptvariables:
##        each.destroy()
##    for each in opencasevariables:
##        each.destroy()
##    for each in overviewvariables:
##        each.destroy()
##    for each in closedcasevariables:
##        each.destroy()
    #viewTypea.set('Overview')

    ############################################################################################
    '''
    left_frame = Frame(open_cases, borderwidth=1,relief=RIDGE)
    left_frame.grid(row=0, column=1, columnspan=10, sticky=E) 

    photoCanvas1 = Canvas(left_frame, width=1200, height=(height)-45) #width=width, height=(height)-45)
    photoCanvas1.grid()#sticky=NSEW)

    left1 = Frame(photoCanvas1, width=width, height=10000)
    photoCanvas1.create_window(0, 0, window=left1, anchor='nw')
    ############################################################################################
    right_frame = Frame(open_cases, borderwidth=1,relief=RIDGE)
    right_frame.grid(row=0, column=11, columnspan=10, sticky=W)

    photoCanvas2 = Canvas(right_frame, width=600, height=(height)-45) #width=width, height=(height)-45)
    photoCanvas2.grid()#sticky=NSEW)

    right1 = Frame(photoCanvas2, width=width, height=10000)
    photoCanvas2.create_window(0, 0, window=right1, anchor='nw')'''

    centre_frame = Frame(open_cases, borderwidth=1,relief=RIDGE)
    centre_frame.grid(row=0, column=11, columnspan=10, sticky=W)

    photoCanvas3 = Canvas(centre_frame, width=600, height=(height)-45) #width=width, height=(height)-45)
    photoCanvas3.grid()#sticky=NSEW)

    centre1 = Frame(photoCanvas3, width=width, height=10000)
    photoCanvas3.create_window(0, 0, window=centre1, anchor='center')
    #anchor must be n, ne, e, se, s, sw, w, nw, or center
    ############################################################################################
    
    ### Notepad tab (scroll WORKING)
    notepad_overview=Text(left1, wrap=WORD, width=122, height=8) #, yscrollcommand=notepad_scrollbar.set)
    notepad_overview.grid(row=1, column=1, columnspan=15, rowspan=4, sticky=W)
    #print('Len notepadentries:',(len(notepadentries)))
##    if (len(notepadentries))==2:
##            print('in func')
##            notepadnotes1_text = (str(notepadentries[1]))
##            notepadnotes1_text = (str.replace(notepadnotes1_text,"\\n","\n"))
##            notepad_overview.insert(INSERT, notepadnotes1_text)
##    else:
##        pass
    notepad_overview.grid_propagate(True)
    notepad_overview.bind('<KeyRelease>', notepad_overview_notes1)
    notepad_overview.bind('<Double-Button-1>', lambda x: tabs.select(notepad))
    notepad_overview.config(state='normal')
    overviewvariables.append(notepad_overview)
    
    row = 1
    column = 1
    Label_pin_d = Label(right1,  text='PIN Decryption(s)')
    Label_pin_d.grid(row=row, column=column, sticky=W, padx=1)
    overviewvariables.append(Label_pin_d)
    
    row+=1
    
    count=1
    Label0 = Label(right1, text=' ', width=200,  borderwidth=3, relief="groove")
    Label0.grid(row=row, column=column, columnspan=25, sticky=W, ipady=3, ipadx=20)
    overviewvariables.append(Label0)

    v0 =  StringVar()
    Label0 = Label(right1, textvariable=v0)
    Label0.grid(row=row, column=column, sticky=W, padx=1)
    v0.set('DFT  Ref')
    overviewvariables.append(Label0)
    column+=1        
    v1 =  StringVar()
    Label1 = Label(right1, textvariable=v1)
    Label1.grid(row=row, column=column, sticky=W)
    v1.set('Crime Ref')
    overviewvariables.append(Label1)
    column+=1
    v2 =  StringVar()
    Label2 = Label(right1, textvariable=v2)
    Label2.grid(row=row, column=column, sticky=W)
    v2.set('Exhibit Ref')
    overviewvariables.append(Label2)
    column+=1
    v3 =  StringVar()
    Label3 = Label(right1, textvariable=v3)
    Label3.grid(row=row, column=column, sticky=W)
    v3.set('OIC')
    overviewvariables.append(Label3)
    column+=1
    v4 =  StringVar()
    Label4 = Label(right1, textvariable=v4)
    Label4.grid(row=row, column=column, sticky=W)
    v4.set('Date started')
    overviewvariables.append(Label4)
    column+=1
    v5 =  StringVar()
    Label5 = Label(right1, textvariable=v5)
    Label5.grid(row=row, column=column, sticky=W)
    v5.set('Day running')
    overviewvariables.append(Label5)
    column+=1
    v6 =  StringVar()
    Label6 = Label(right1, textvariable=v6)
    Label6.grid(row=row, column=column, sticky=W)
    v6.set('Notes')
    overviewvariables.append(Label6)
    column+=1
    v7 =  StringVar()
    Label7 = Label(right1, textvariable=v7)
    Label7.grid(row=row, column=column, sticky=W)
    v7.set('')
    overviewvariables.append(Label7)
    column+=1    
    v8 =  StringVar()
    Label8 = Label(right1, textvariable=v8)
    Label8.grid(row=row, column=column, sticky=W)
    v8.set('')
    overviewvariables.append(Label8)
    column+=1
    v9 =  StringVar()
    Label9 = Label(right1, textvariable=v9)
    Label9.grid(row=row, column=column, sticky=W)
    v9.set('')
    overviewvariables.append(Label9)
    column+=1    
    '''edit1b.grid(row=0, column=15, columnspan=2, sticky=W)
    edit1b.config(state='normal')'''

#    launch.grid(row=0, column=13, columnspan=1, sticky=W)
    column = 1
    row=3
    try:
        for each in pindecryptlogs:

            entry1 = (str("e"+(str(count))))
            Entry1a = StringVar()
            Entry1a.set(each[1])
            dft=each[1]
            Entry1a.trace("w", lambda name, index, mode, Entry1a=Entry1a: callback(Entry1a))
            entry1 = Button(right1, text=dft, width= 10, state='normal', textvariable=Entry1a)
            entry1.bind('<Button-1>', populate_individual_pd)
            entry1.grid(row=row, column=column, sticky=EW)
            column+=1
            
            '''entry1 = (str("e"+(str(count))))
            Entry1a = StringVar()
            Entry1a.set(each[1])
            Entry1a.trace("w", lambda name, index, mode, Entry1a=Entry1a: callback(Entry1a))
            entry1 = Entry(right1, relief=SUNKEN,width=8, state='disabled', textvariable=Entry1a)
            entry1.grid(row=row, column=11, sticky=EW)'''
            pindecryptvariables.append(entry1)
            count += 1
            entry2 = (str("e"+(str(count))))
            Entry2a = StringVar()
            Entry2a.set(each[2])
            Entry2a.trace("w", lambda name, index, mode, Entry2a=Entry2a: callback(Entry2a))
            entry2 = Entry(right1, relief=SUNKEN,width=15, state='disabled', textvariable=Entry2a)
            entry2.grid(row=row, column=column, sticky=EW, ipady=3, padx=2)
            pindecryptvariables.append(entry2)
            count += 1
            column+=1
            
            entry3 = (str("e"+(str(count))))
            Entry3a = StringVar()
            Entry3a.set(each[3])
            Entry3a.trace("w", lambda name, index, mode, Entry3a=Entry3a: callback(Entry3a))
            entry3 = Entry(right1, relief=SUNKEN, width=12, state='disabled', textvariable=Entry3a)
            entry3.grid(row=row, column=column, sticky=EW, ipady=3)
            pindecryptvariables.append(entry3)
            count += 1
            column+=1
            
            entry4 = (str("e"+(str(count))))
            Entry4a = StringVar()
            Entry4a.set(each[4])
            Entry4a.trace("w", lambda name, index, mode, Entry4a=Entry4a: callback(Entry4a))
            entry4 = Entry(right1, relief=SUNKEN,width=30, state='disabled', textvariable=Entry4a)
            entry4.grid(row=row, column=column, sticky=W, ipady=3)
            pindecryptvariables.append(entry4)
            count += 1
            column+=1
            
            entry5 = (str("e"+(str(count))))
            Entry5a = StringVar()
            Entry5a.set(each[5])
            Entry5a.trace("w", lambda name, index, mode, Entry5a=Entry5a: callback(Entry5a))
            entry5 = Entry(right1, relief=SUNKEN,width=13, state='disabled', textvariable=Entry5a)
            entry5.grid(row=row, column=column, columnspan=2, sticky=W, ipady=3)
            pindecryptvariables.append(entry5)
            count += 1
            column+=1
            
            selected_month_rec = (each[5])
            start = date(int(selected_month_rec.split('-')[0]),int(selected_month_rec.split('-')[1]),int(selected_month_rec.split('-')[2]))
            today = date.today()
            res = today - start
            res.days
            entry6 = (str("e"+(str(count))))
            Entry6a = StringVar()
            Entry6a.set(res.days)
            Entry6a.trace("w", lambda name, index, mode, Entry6a=Entry6a: callback(Entry6a))
            entry6 = Entry(right1, relief=SUNKEN,width=12, state='disabled', textvariable=Entry6a)
            entry6.grid(row=row, column=column, sticky=W, ipady=3)
            pindecryptvariables.append(entry6)
            count += 1
            column+=1
            
            entry7 = (str("e"+(str(count))))
            Entry7a = StringVar()
            Entry7a.set(each[8])
            Entry7a.trace("w", lambda name, index, mode, Entry7a=Entry7a: callback(Entry7a))
            entry7 = Entry(right1, relief=SUNKEN,width=155, state='disabled', textvariable=Entry7a)
            entry7.grid(row=row, column=column, sticky=W, columnspan=50, ipady=3)
            pindecryptvariables.append(entry7)
            row += 1
            column = 1
        
    except:
        pass
    
#    edit1b.config(command=disable_edit2)
    readopencases()
    column=1
    count=1
    row=6

    Label21 = Label(left1, text=' ')
    Label21.grid(row=row, column=column, columnspan=1)
    overviewvariables.append(Label21)
    
    row += 1
    Label20 = Label(left1, textvariable=' ', width=140,  borderwidth=3, relief="groove")
    Label20.grid(row=row, column=1, columnspan=15, sticky=W, ipady=3)
    overviewvariables.append(Label20)
    
    v0 =  StringVar()
    Label0 = Label(left1, textvariable=v0)
    Label0.grid(row=row, column=column, sticky=W, padx=1)
    v0.set('DFT  Ref')
    overviewvariables.append(Label0)
    column+=1        
    v1 =  StringVar()
    Label1 = Label(left1, textvariable=v1)
    Label1.grid(row=row, column=column, sticky=W)
    v1.set('Crime Ref')
    overviewvariables.append(Label1)
    column+=1 
    v2 =  StringVar()
    Label2 = Label(left1, textvariable=v2)
    Label2.grid(row=row, column=column, sticky=W)
    v2.set('Suspect')
    overviewvariables.append(Label2)
    column+=1 
    v3 =  StringVar()
    Label3 = Label(left1, textvariable=v3)
    Label3.grid(row=row, column=column, sticky=W)
    v3.set('OIC')
    overviewvariables.append(Label3)
    column+=1 
    v4 =  StringVar()
    Label4 = Label(left1, textvariable=v4)
    Label4.grid(row=row, column=column, sticky=W)
    v4.set('Date started')
    overviewvariables.append(Label4)
    column+=1 
    v5 =  StringVar()
    Label5 = Label(left1, textvariable=v5)
    Label5.grid(row=row, column=column, sticky=W)
    v5.set('# of exhibits')
    overviewvariables.append(Label5)
    column+=1 
    v6 =  StringVar()
    Label6 = Label(left1, textvariable=v6)
    Label6.grid(row=row, column=column, sticky=EW)
    '''v6.set('Pre-Img')
    overviewvariables.append(Label6)
    column+=1 
    v7 =  StringVar()
    Label7 = Label(left1, textvariable=v7)
    Label7.grid(row=row, column=column, sticky=EW)
    v7.set('Image')
    overviewvariables.append(Label7)'''
    column+=1
    v8 =  StringVar()
    Label8 = Label(left1, textvariable=v8)
    Label8.grid(row=row, column=column, sticky=EW)
    v8.set('QC')
    overviewvariables.append(Label8)
    column+=1 
    v9 =  StringVar()
    Label9 = Label(left1, textvariable=v9)
    Label9.grid(row=row, column=column, sticky=EW)
    v9.set('Server')
    overviewvariables.append(Label9)


    '''edit1b.grid(row=0, column=15, columnspan=1, sticky=W)
    edit1b.grid_forget()'''
    

#    launch.grid(row=0, column=13, columnspan=1, sticky=W)


    row += 1
    column = 1
    for each in opencases:
        Entry1a = StringVar()
        Entry1a.set(each[1])
        dft=each[1]
        Entry1a.trace("w", lambda name, index, mode, Entry1a=Entry1a: callback(Entry1a))
        entry1 = Button(left1, text=dft, width= 10, textvariable=Entry1a)
        entry1.bind('<Button-1>', populate_individual_case)
        entry1.grid(row=row, column=column, sticky=EW)

        column+=1
        print('opencases: ', each[1])

        opencasevariables.append(entry1)
        count += 1
        entry2 = (str("e"+(str(count))))
        Entry2a = StringVar()
        Entry2a.set(each[2])
        Entry2a.trace("w", lambda name, index, mode, Entry2a=Entry2a: callback(Entry2a))
        entry2 = Entry(left1, relief=SUNKEN,width=15, state='disabled', textvariable=Entry2a)
        entry2.grid(row=row, column=column, sticky=EW, ipady=3, padx=2)
        opencasevariables.append(entry2)
        count += 1
        column+=1
        
        entry3 = (str("e"+(str(count))))
        Entry3a = StringVar()
        Entry3a.set(each[8])
        Entry3a.trace("w", lambda name, index, mode, Entry3a=Entry3a: callback(Entry3a))
        entry3 = Entry(left1, relief=SUNKEN,width=25, state='disabled', textvariable=Entry3a)
        entry3.grid(row=row, column=column, sticky=EW, ipady=3)
        opencasevariables.append(entry3)
        count += 1
        column+=1
        
        entry4 = (str("e"+(str(count))))
        Entry4a = StringVar()
        Entry4a.set(each[4])
        Entry4a.trace("w", lambda name, index, mode, Entry4a=Entry4a: callback(Entry4a))
        entry4 = Entry(left1, relief=SUNKEN,width=30, state='disabled', textvariable=Entry4a)
        entry4.grid(row=row, column=column, sticky=W, ipady=3)
        opencasevariables.append(entry4)
        count += 1
        column+=1
        
        entry5 = (str("e"+(str(count))))
        Entry5a = StringVar()
        Entry5a.set(each[5])
        Entry5a.trace("w", lambda name, index, mode, Entry5a=Entry5a: callback(Entry5a))
        entry5 = Entry(left1, relief=SUNKEN,width=12, state='disabled', textvariable=Entry5a)
        entry5.grid(row=row, column=column, columnspan=1, sticky=W, ipady=3)
        opencasevariables.append(entry5)
        count += 1
        column+=1

        entry7 = (str("e"+(str(count))))
        Entry7a = StringVar()
        Entry7a.set(each[3])
        Entry7a.trace("w", lambda name, index, mode, Entry5a=Entry5a: callback(Entry7a))
        entry7 = Entry(left1, relief=SUNKEN,width=12, state='disabled', textvariable=Entry7a)
        entry7.grid(row=row, column=column, columnspan=1, sticky=W, ipady=3)
        opencasevariables.append(entry7)
        count += 1
        column+=2
        
        '''e30a = IntVar()
        e30a.set(0)
        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
        e30b = Checkbutton(left1, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
        e30b.grid(row=row, column=column, sticky=EW)
        overviewvariables.append(e30b)
        column+=2
        overviewvariables.append(e30b)
        
        e30a = IntVar()
        e30a.set(0)
        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
        e30b = Checkbutton(left1, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
        e30b.grid(row=row, column=column, sticky=EW)
        column+=1
        overviewvariables.append(e30b)'''
        
        e30a = IntVar()
        e30a.set(0)
        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
        e30b = Checkbutton(left1, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
        e30b.grid(row=row, column=column, sticky=EW)
        column+=1
        opencasevariables.append(e30b)
        
        e30a = IntVar()
        e30a.set(0)
        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
        e30b = Checkbutton(left1, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
        e30b.grid(row=row, column=column, sticky=EW)
        opencasevariables.append(e30b)
        column=1
        
        # NOTES
        row+=1
        entry6 = (str("e"+(str(count))))
        Entry6a = StringVar()
        Entry6a.set(each[6])
        Entry6a.trace("w", lambda name, index, mode, Entry6a=Entry6a: callback(Entry6a))
        entry6 = Entry(left1, relief=SUNKEN, width=112,  state='disabled', textvariable=Entry6a)
        entry6.grid(row=row, column=2, columnspan=14, sticky=EW, ipady=0)
        opencasevariables.append(entry6)
        count += 1
        row += 1

        #label=Label(left1, text=" - ").grid(row=row, column=2, columnspan=1, sticky=EW)
        
        #Label0 = Label(left1, text=' ', width=10)
        #Label0.grid(row=row, column=1, columnspan=1, sticky=EW, ipady=3, ipadx=20)
        #overviewvariables.append(Label0)

        #row += 2
    photoScrollv = Scrollbar(left_frame, orient=VERTICAL)
    photoScrollv.config(command=photoCanvas1.yview)
    photoScrollh = Scrollbar(left_frame, orient=HORIZONTAL)
    photoScrollh.config(command=photoCanvas1.xview)
    photoCanvas1.config(yscrollcommand=photoScrollv.set)
    photoCanvas1.config(xscrollcommand=photoScrollh.set)
    photoScrollv.grid(row=0, column=1, sticky="ns")
    photoScrollh.grid(row=7, column=0, sticky="ew")
    left1.bind("<Configure>", update_scrollregion)
    photoScrollv.bind("<MouseWheel>", update_scrollregion)

    photoScrollv = Scrollbar(right_frame, orient=VERTICAL)
    photoScrollv.config(command=photoCanvas2.yview)
    photoScrollh = Scrollbar(right_frame, orient=HORIZONTAL)
    photoScrollh.config(command=photoCanvas2.xview)
    photoCanvas2.config(yscrollcommand=photoScrollv.set)
    photoCanvas2.config(xscrollcommand=photoScrollh.set)
    photoScrollv.grid(row=0, column=1, sticky="ns")
    photoScrollh.grid(row=7, column=0, sticky="ew")
    right1.bind("<Configure>", update_scrollregion)
    photoScrollv.bind("<MouseWheel>", update_scrollregion)


    root.update()
############################################################################################
def get_individual_case_data():
    global d, case, tabs, key, value, ryan, Indiv_Case, Indiv_Case1, Indiv_Case2, Indiv_Case3, Indiv_Case4, Indiv_Case5, Indiv_Case6, Indiv_Case7, Indiv_Case8, Indiv_Case8a, the_exhibit, Loop_Indiv_Case1, Loop_Indiv_Case2, Loop_Indiv_Case3, Loop_Indiv_Case1a, Loop_Indiv_Case2a, Loop_Indiv_Case3a, Loop_Indiv_Case6
    the_case = []
    ryan = {}
#    launch.grid_forget()
    d = (TEXT[5:12])
    print('ddddddddddddd', d)
    if d == "No entries":
        pass
    else:
        conn = sqlite3.connect(sqlprolocal, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        c.execute("SELECT * FROM cases WHERE full_dft_ref like '%'||?||'%' and status != ?", (d, 'closed',))
        
        for each in c:
            print(each)
            the_case.append(each)
        case_status = (each[15])
        the_exhibit = (each[4])
        case_pw = (each[12])
        exhibit_notes = (each[14])
        print('The Case no of entries: ', (len(the_case)))
        try:
            if 'normal' == case.state():
                case.destroy()
            elif 'normal' == pd_case.state():
                pd_case.destroy()
            else:
                pass
        except:
            pass
        case = Toplevel()
        width  = case.winfo_screenwidth()
        height = case.winfo_screenheight()
        case.geometry('720x700') #widthxheight
        print(width)
        print(height)
        case.title("CASE - "+TEXT)
        case.resizable(width=False, height=False)
        case.protocol("WM_DELETE_WINDOW", close_individual_case)

        tabs = ttk.Notebook(case)
        overview=ttk.Frame(tabs)
        tabs.add(overview,text='Overview')

        print('The case: ', the_case)
        count_no2 = 1 
        for exhib in the_case:
            #tabs = ttk.Notebook(case)
            print('the case: ',exhib)
            name=str(exhib[4])
            print(name)
            print(type(name))
            name=ttk.Frame(tabs)
            tabs.add(name,text=(exhib[4]))

            rows=31
            columns=20
            conn.close()
            # Set row height here
            height=5
            for frame in the_case:
                count=0
                count2=0

                if frame == the_case[0]:
                    while count < rows:
                        Label(name, text=" ", width=2).grid(row=count, column=0, sticky=EW, ipady=height)
                        count+=1
                    while count2 < columns:
                        Label(name, text=" ", width=2).grid(row=0, column=count2, sticky=EW, ipady=height)
                        count2+=1
                        
            Loop_Indiv_Case1a = StringVar()
            Loop_Indiv_Case1a.set(exhib[4])
            Loop_Indiv_Case1a.trace("w", lambda name, index, mode, Loop_Indiv_Case1a=Loop_Indiv_Case1a: callback(Loop_Indiv_Case1a))
            Loop_Indiv_Case1 = Entry(name, relief=SUNKEN,width=25, state='normal', textvariable=Loop_Indiv_Case1a)
            Loop_Indiv_Case1.grid(row=2, column=1, sticky=W)
            
            individualcasevariables.append(Loop_Indiv_Case1)
            count += 1
            Loop_Indiv_Case2 = (str("e"+(str(count))))
            Loop_Indiv_Case2a = StringVar()
            Loop_Indiv_Case2a.set(exhib[5])
            Loop_Indiv_Case2a.trace("w", lambda name, index, mode, Loop_Indiv_Case2a=Loop_Indiv_Case2a: callback_Loop_Indiv_Case_exhibit(Loop_Indiv_Case2a))
            Loop_Indiv_Case2 = Entry(name, relief=SUNKEN,width=25, state='normal', textvariable=Loop_Indiv_Case2a)
            Loop_Indiv_Case2.grid(row=2, column=3, sticky=W)
            individualcasevariables.append(Loop_Indiv_Case2)
            count += 1
            Loop_Indiv_Case3 = (str("e"+(str(count))))
            Loop_Indiv_Case3a = StringVar()
            Loop_Indiv_Case3a.set(exhib[9])
            Loop_Indiv_Case3a.trace("w", lambda name, index, mode, Loop_Indiv_Case3a=Loop_Indiv_Case3a: callback_Loop_Indiv_Case_property_ref(Loop_Indiv_Case3a))
            Loop_Indiv_Case3 = Entry(name, relief=SUNKEN,width=15, state='normal', textvariable=Loop_Indiv_Case3a)
            Loop_Indiv_Case3.grid(row=2, column=5, columnspan=4, sticky=W)
            individualcasevariables.append(Loop_Indiv_Case3)
        
            oic_label=Label(name, text=" Exhibit Ref")
            oic_label.grid(row=1, column=1, sticky=W)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Exhibit Seal")
            oic_label.grid(row=1, column=3, sticky=W)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Property Ref")
            oic_label.grid(row=1, column=5, sticky=W)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Location:")
            oic_label.grid(row=3, column=8, sticky=W)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Action:")
            oic_label.grid(row=3, column=1, sticky=W)
            individualcasevariables.append(oic_label)
            
            oic_label=Label(name, text=" Property of: ")
            oic_label.grid(row=1, column=8, sticky=W)
            individualcasevariables.append(oic_label)
            
            row=2

            vic_or_susa = StringVar()
            vic_or_susa.set('--Select--')
            vic_or_susa.trace("w", lambda name, index, mode, vic_or_susa=vic_or_susa: callback(vic_or_susa))
            vic_or_susab = OptionMenu(name, vic_or_susa, *property_of, command=qwerty)
            vic_or_susab.grid(row=row, column=8, columnspan=1, sticky=W)
            individualcasevariables.append(vic_or_susab)
            vic_or_susab.config(width=18)

            row=4

            locationa = StringVar()
            locationa.set('--Select--')
            locationa.trace("w", lambda name, index, mode, locationa=locationa: callback(locationa))
            locationab = OptionMenu(name, locationa, *location, command=qwerty)
            locationab.grid(row=row, column=8, columnspan=1, sticky=W)
            individualcasevariables.append(locationab)
            locationab.config(width=18)
            count_no2+=1

            actiona = StringVar()
            actiona.set('--Select--')
            actiona.trace("w", lambda name, index, mode, actiona=actiona: callback(actiona))
            actionab = OptionMenu(name, actiona, *action, command=qwerty)
            actionab.grid(row=row, column=1, columnspan=1, sticky=W)
            individualcasevariables.append(actionab)
            actionab.config(width=18)
            count_no2+=1

            row=5
            
            '''v6 =  StringVar()
            Label6 = Label(name, textvariable=v6)
            Label6.grid(row=row, column=1, padx=5, sticky=W)
            v6.set('Pre-Img')
            overviewvariables.append(Label6)

            v7 =  StringVar()
            Label7 = Label(name, textvariable=v7)
            Label7.grid(row=row, column=1, padx=55, sticky=W)
            v7.set('Image')
            overviewvariables.append(Label7)

            v8 =  StringVar()
            Label7 = Label(name, textvariable=v8)
            Label7.grid(row=row, column=1, columnspan=2, padx=105, sticky=W)
            v8.set('Re-sealed')
            overviewvariables.append(Label7)

            row+=1
            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=row, column=1, sticky=W)
            overviewvariables.append(e30b)

            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=row, column=1, padx=45, sticky=W)
            overviewvariables.append(e30b)

            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=row, column=1, columnspan=2, padx=105, sticky=W)
            overviewvariables.append(e30b)      '''
            

            Loop_Indiv_Action6 = (str("t"+(str(count_no2))))
            print(Loop_Indiv_Action6)
            key=(exhib[4])
            Loop_Indiv_Action6scrollbar = Scrollbar(name)
            Loop_Indiv_Action6=Text(name, wrap=WORD, width=47, yscrollcommand=Loop_Indiv_Action6scrollbar.set)
            print(Loop_Indiv_Action6)
            Loop_Indiv_Action6.grid(row=6, column=1, columnspan=11, sticky=EW, rowspan=1)
            print(Loop_Indiv_Action6)
            value=Loop_Indiv_Action6
            
            Loop_Indiv_Action6_notes = (str.replace(exhib[14],"\\n","\n"))
            Loop_Indiv_Action6.insert(INSERT, Loop_Indiv_Action6_notes)

            Loop_Indiv_Action6.grid_propagate(False)
            Loop_Indiv_Action6.bind('<KeyRelease>', Loop_Indiv_Action_exhibit_notes)
            Loop_Indiv_Action6scrollbar.config( command = Loop_Indiv_Action6.yview)
            Loop_Indiv_Action6scrollbar.grid(row=6, column=12, columnspan=1, rowspan=1,  sticky='NS')

            ryan[key] = value
            
            #individualActionvariables.append(Loop_Indiv_Action6scrollbar)
            #individualActionvariables.append(Loop_Indiv_Action6)



            Loop_Indiv_Case6 = (str("t"+(str(count_no2))))
            print(Loop_Indiv_Case6)
            key=(exhib[4])
            Loop_Indiv_Case6scrollbar = Scrollbar(name)
            Loop_Indiv_Case6=Text(name, wrap=WORD, width=47, yscrollcommand=Loop_Indiv_Case6scrollbar.set)
            print(Loop_Indiv_Case6)
            Loop_Indiv_Case6.grid(row=20, column=1, columnspan=11, sticky=EW, rowspan=6)
            print(Loop_Indiv_Case6)
            value=Loop_Indiv_Case6
            
            Loop_Indiv_Case6_notes = (str.replace(exhib[14],"\\n","\n"))
            Loop_Indiv_Case6.insert(INSERT, Loop_Indiv_Case6_notes)

            Loop_Indiv_Case6.grid_propagate(False)
            Loop_Indiv_Case6.bind('<KeyRelease>', Loop_Indiv_Case_exhibit_notes)
            Loop_Indiv_Case6scrollbar.config( command = Loop_Indiv_Case6.yview)
            Loop_Indiv_Case6scrollbar.grid(row=20, column=12, columnspan=1, rowspan=6,  sticky='NS')

            ryan[key] = value
            
            individualcasevariables.append(Loop_Indiv_Case6scrollbar)
            individualcasevariables.append(Loop_Indiv_Case6)
        
        tabs.pack(fill='both', expand=Y)
        for key in ryan:
            print('key: ',key)
        print(ryan.values())
        
        Indiv_Case_note_label=Label(overview, text=" Notes")
        Indiv_Case_note_label.grid(row=7, column=1, sticky=W)
        individualcasevariables.append(Indiv_Case_note_label)

        oic_label=Label(overview, text=" DFT Ref")
        oic_label.grid(row=1, column=1, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Niche/Crime Ref")
        oic_label.grid(row=1, column=2, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Suspect")
        oic_label.grid(row=1, column=3, sticky=W)
        individualcasevariables.append(oic_label)
        
        oic_label=Label(overview, text=" # of exhibits")
        oic_label.grid(row=1, column=4, sticky=W)
        individualcasevariables.append(oic_label)
        
        oic_label=Label(overview, text=" OIC")
        oic_label.grid(row=3, column=3, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Date started")
        oic_label.grid(row=3, column=1, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Days open")
        oic_label.grid(row=3, column=2, sticky=W)
        individualcasevariables.append(oic_label)

        case_password=Label(overview, text=" Case Password: ")
        case_password.grid(row=5, column=3, sticky=W)

        statuslabel=Label(overview, text=" Case Status: ")
        statuslabel.grid(row=5, column=2, sticky=W)

        v8 =  StringVar()
        Label8 = Label(overview, textvariable=v8)
        Label8.grid(row=5, column=1, padx=15, sticky=W)
        v8.set('QC')
        overviewvariables.append(Label8)

        v9 =  StringVar()
        Label9 = Label(overview, textvariable=v9)
        Label9.grid(row=5, column=1, padx=70, columnspan=1, sticky=W)
        v9.set('Server')
        
        overviewvariables.append(Label9)
        frames=["case"] 
        rows=31
        columns=7
        conn.close()
        # Set row height here
        height=5
        for frame in frames:
            count=0
            count2=0
            frame=(str(frame))
            if frame == frames[0]:
                while count < rows:
                    Label(overview, text=" ", width=2).grid(row=count, column=0, sticky=EW, ipady=height)
                    count+=1
                while count2 < columns:
                    Label(overview, text=" ", width=2).grid(row=0, column=count2, sticky=EW, ipady=height)
                    count2+=1

        conn = sqlite3.connect(sqlprolocal, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        c.execute("SELECT * FROM opencases WHERE full_dft_ref like '%'||?||'%'", (d,))
        #c.execute("SELECT * FROM opencases WHERE full_dft_ref like '%'||?||'%'", (d,))

        for each in c:
            print(each)

        count = 1   
        row = 2

        print('each1: ', each[1])

        Indiv_Case = each[1]

        Indiv_Case1a = StringVar()
        Indiv_Case1a.set(each[1])
        Indiv_Case1a.trace("w", lambda name, index, mode, Indiv_Case1a=Indiv_Case1a: callback(Indiv_Case1a))
        Indiv_Case1 = Entry(overview, relief=SUNKEN,width=10, state='disabled', textvariable=Indiv_Case1a)
        Indiv_Case1.grid(row=row, column=1, sticky=EW)
        
        individualcasevariables.append(Indiv_Case1)
        count += 1
        Indiv_Case2 = (str("e"+(str(count))))
        Indiv_Case2a = StringVar()
        Indiv_Case2a.set(each[2])
        Indiv_Case2a.trace("w", lambda name, index, mode, Indiv_Case2a=Indiv_Case2a: callback_Indiv_Case2(Indiv_Case2a))
        Indiv_Case2 = Entry(overview, relief=SUNKEN,width=15, state='normal', textvariable=Indiv_Case2a)
        Indiv_Case2.grid(row=row, column=2, sticky=EW)
        individualcasevariables.append(Indiv_Case2)
        count += 1

        Indiv_Case9 = (str("e"+(str(count))))
        Indiv_Case9a = StringVar()
        Indiv_Case9a.set(each[8])
        Indiv_Case9a.trace("w", lambda name, index, mode, Indiv_Case9a=Indiv_Case9a: callback(Indiv_Case9a))
        Indiv_Case9 = Entry(overview, relief=SUNKEN,width=10, state='normal', textvariable=Indiv_Case9a)
        Indiv_Case9.grid(row=row, column=3, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case9)
        
        Indiv_Case3 = (str("e"+(str(count))))
        Indiv_Case3a = StringVar()
        Indiv_Case3a.set((len(the_case)))
        Indiv_Case3a.trace("w", lambda name, index, mode, Indiv_Case3a=Indiv_Case3a: callback_Indiv_Case3(Indiv_Case3a))
        Indiv_Case3 = Entry(overview, relief=SUNKEN,width=12, state='normal', textvariable=Indiv_Case3a)
        Indiv_Case3.grid(row=row, column=4, columnspan=1, sticky=W)
        individualcasevariables.append(Indiv_Case3)
        count += 1
        row += 2

        Indiv_Case4 = (str("e"+(str(count))))
        Indiv_Case4a = StringVar()
        Indiv_Case4a.set(each[4])
        Indiv_Case4a.trace("w", lambda name, index, mode, Indiv_Case4a=Indiv_Case4a: callback_Indiv_Case4(Indiv_Case4a))
        Indiv_Case4 = Entry(overview, relief=SUNKEN,width=30, state='normal', textvariable=Indiv_Case4a)
        Indiv_Case4.grid(row=row, column=3, sticky=EW)
        individualcasevariables.append(Indiv_Case4)
        count += 1

        Indiv_Case5 = (str("e"+(str(count))))
        Indiv_Case5a = StringVar()
        Indiv_Case5a.set(each[5])
        Indiv_Case5a.trace("w", lambda name, index, mode, Indiv_Case5a=Indiv_Case5a: callback_Indiv_Case5(Indiv_Case5a))
        Indiv_Case5 = Entry(overview, relief=SUNKEN,width=30, state='disabled', textvariable=Indiv_Case5a)
        Indiv_Case5.grid(row=row, column=1, columnspan=1, sticky=W)
        individualcasevariables.append(Indiv_Case5)
        count += 1

        #timestamp = (each[13])
        #selected_month_rec = (timestamp[:-9])

        selected_month_rec = (each[5])
        print(selected_month_rec)
        start = date(int(selected_month_rec.split('-')[0]),int(selected_month_rec.split('-')[1]),int(selected_month_rec.split('-')[2]))
        today = date.today()
        res = today - start
        res.days

        Indiv_Case7 = (str("e"+(str(count))))
        Indiv_Case7a = StringVar()
        Indiv_Case7a.set(res.days)
        Indiv_Case7a.trace("w", lambda name, index, mode, Indiv_Case7a=Indiv_Case7a: callback(Indiv_Case7a))
        Indiv_Case7 = Entry(overview, relief=SUNKEN,width=25, state='disabled', textvariable=Indiv_Case7a)
        Indiv_Case7.grid(row=row, column=2, columnspan=1, sticky=W)
        individualcasevariables.append(Indiv_Case7)
        count += 1
        row += 2

        Indiv_Case6scrollbar = Scrollbar(overview)
        Indiv_Case6=Text(overview, wrap=WORD, width=51, yscrollcommand=Indiv_Case6scrollbar.set)
        Indiv_Case6.grid(row=8, column=1, columnspan=5,  rowspan=5, sticky=EW)

        Indiv_Case6_notes = (str.replace(each[6],"\\n","\n"))
        Indiv_Case6.insert(INSERT, Indiv_Case6_notes)

        Indiv_Case6.grid_propagate(False)
        Indiv_Case6.bind('<KeyRelease>', Indiv_Case_notes)
        Indiv_Case6scrollbar.config( command = Indiv_Case6.yview)
        Indiv_Case6scrollbar.grid(row=8, column=6, rowspan=5,  sticky='NS')

        Indiv_Case8 = (str("e"+(str(count))))
        Indiv_Case8a = StringVar()
        Indiv_Case8a.set(case_pw)
        Indiv_Case8a.trace("w", lambda name, index, mode, Indiv_Case8a=Indiv_Case8a: callback(Indiv_Case8a))
        Indiv_Case8 = Entry(overview, relief=SUNKEN,width=25, state='disabled', textvariable=Indiv_Case8a)
        Indiv_Case8.grid(row=6, column=3, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case8)

        e30a = IntVar()
        e30a.set(0)
        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
        e30b = Checkbutton(overview, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
        e30b.grid(row=6, column=1, sticky=W)
        overviewvariables.append(e30b)
        
        e30a = IntVar()
        e30a.set(0)
        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
        e30b = Checkbutton(overview, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
        e30b.grid(row=6, column=1, padx=60, sticky=W)
        overviewvariables.append(e30b)

        submit2a= StringVar()
        submit2a.trace("w", lambda name, index, mode, submi2ta=submit2a: callback(submit2a))
        submit2b = Button(overview, text="Copy to clip",  width= 10, command=copytoclip_individual_case)
        submit2b.grid(row=6, column=4, sticky=W)
        
        individualcasevariables.append(Indiv_Case6scrollbar)
        individualcasevariables.append(Indiv_Case6)

        #        Label(overview, text=" Status:").grid(row=row, column=1, sticky=W)
        status_dda = StringVar()
        status_dda.set(case_status)
        status_dda.trace("w", lambda name, index, mode, status_dda=status_dda: callback_Indiv_Case_status(status_dda))
        status_ddb = OptionMenu(overview, status_dda, *status, command=0)
        status_ddb.grid(row=6, column=2, columnspan=1, sticky=EW)
        individualcasevariables.append(status_ddb)

        count += 1

        del_close1=Button(overview, text="Delete/Close", width=17, command=close)
        del_close1.grid(row=13, column=4, sticky=W)
        del_close1.config(state='normal')
        individualcasevariables.append(del_close1)

        count += 1
        Indiv_Case6.focus()
        case.update()
        name.update()
        case.attributes('-topmost',True)
        case.after_idle(case.attributes,'-topmost',False)
        case.mainloop()
############################################################################################

gui()
