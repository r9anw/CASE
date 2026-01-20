
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
from wordlist import *
from tkinterdnd2 import DND_FILES, TkinterDnD
#from individual_cases import *
#from contemp_add_entry import *
############################################################################################
drive='C'
############################################################################################
### contemp_add_entry ###
############################################################################################
def analysis_disgard_exit():
    addanalysis.destroy()
    entry3.insert(8, 'Entry disgarded')
    root.update()
    enable_buttons()
############################################################################################
def gen_unique_id():
    global unique_id
    length = 12
    P = string.ascii_uppercase  # 'A' to 'Z
    unique_id=''.join(random.sample(P, length))
    return unique_id
############################################################################################
def createentrydb():
    global crime_exhibit
    if not os.path.exists(drive+":\\CASE\\"):
        os.makedirs(drive+":\\CASE\\")
        print('made folder')
    crime_exhibit = (drive+":\\CASE\\crime_exhibit.sqlite3")
    conn = sqlite3.connect(crime_exhibit, isolation_level=None)
    conn.execute('pragma journal_mode=wal')
    c=conn.cursor()
    try:
        c.execute("""create table exhibit (id_no, crime, exhibit, timestamp_start, timestamp_end, text)""")
    except:
        pass
    conn.commit()
    conn.close()
############################################################################################
def writeentrytodb():
    gen_unique_id()
    try:
        conn = sqlite3.connect(crime_exhibit, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        c.execute(""" insert into exhibit values(?,?,?,?,?,?);""", (unique_id, 'crime ref', 'exhibit ref', timestamp, '-', 'text'))
        conn.commit()
        conn.close()
    except:
        pass
############################################################################################
def Indiv_Case_notes(*args):
    global get
    get=Indiv_Case6.get(1.0, END)
    thread_2()
    #print(get)
##    try:
##        conn = sqlite3.connect(crime_exhibit, isolation_level=None)
##        conn.execute('pragma journal_mode=wal')
##        c=conn.cursor()
##        c.execute("""UPDATE exhibit SET text = ? WHERE crime like '%'||?||'%'""", (get, 'crime ref'))
##        conn.commit()
##        conn.close()
##    except:
##        pass
##    addanalysis.update
############################################################################################
def thread_Indiv_Case_notes(*args):
    get=Indiv_Case6.get(1.0, END)
    #print(get)
    try:
        conn = sqlite3.connect(crime_exhibit, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        c.execute("""UPDATE exhibit SET text = ? WHERE crime like '%'||?||'%'""", (get, 'crime ref'))
        conn.commit()
        conn.close()
    except:
        pass
    addanalysis.update
############################################################################################
def thread_1():
    t1 = threading.Thread(target=addimagetodb)
    t1.start()   
############################################################################################
def thread_2():
    t2 = threading.Thread(target=thread_Indiv_Case_notes)
    t2.start()   
############################################################################################
def addimagetodb():
    try:
        binary_data = convert_to_binary(file_path)
        conn = sqlite3.connect(crime_exhibit, isolation_level=None)
        conn.execute('pragma journal_mode=wal')
        c=conn.cursor()
        c.execute("ALTER TABLE exhibit ADD COLUMN '%s' BLOB" % unique_id)
        sql = "UPDATE exhibit SET "+unique_id+" =? "
        c.execute(sql, (binary_data,))
        conn.commit()
        conn.close()
    except:
        pass
    addanalysis.update
############################################################################################
def convert_to_binary(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
############################################################################################
def addline():
    global row
    Label(addanalysis, text=row).grid(row=row, column=0, sticky=W)
    entry = (str("e"+(str(row))+(str(row))))
    entry = Entry(addanalysis,text="",width=20)
    #f1variables.append(entry)
    entry.grid(row=row, column=1)
    entry.insert(10,timestamp)

    entry = (str("e"+(str(row))+(str(row))))
    entry = Entry(addanalysis,text="",width=180)
    #f1variables.append(entry)
    entry.grid(row=row, column=2, columnspan=55)
    row+=1
    addanalysis.update()
############################################################################################
def addimagecolumnvalue():
    global column_1, row_1
    
    if caseimagecount == 0:
        column_1 = 2
        row_1 = 1
    elif caseimagecount == 1:
        column_1 = 45
        row_1 = 1

    x = caseimagecount+2
    y = caseimagecount
    if caseimagecount >=2:
        if x >= y:
            if x % 2 == 0:
                row_1 = (row_1)+12
            else:
                row_1
    else:
        row_1 = 1

    if caseimagecount % 2 == 0:
        column_1 = 2
    else:
        column_1 = 45
##    print('caseimagecount', caseimagecount)
##    print('column_1', column_1)
##    print('row_1', row_1)
##    print('x: ', x)
##    print('y: ', y)
############################################################################################
def drop(event):
    global caseimagecount, image_ref, panel1, unique_id, python_path, filename1, file_path
    addimagecolumnvalue()
    gen_unique_id()
    file_path = event.data.strip("{}")  
    #python_path = str.replace(file_path,'/', '\\')
    # Validate file
    if not os.path.isfile(file_path):
        label.config(text="Not a valid file.")
        return
    imageno = str(caseimagecount+1)
    try:
        imageentry = "Image "+(imageno)+": "+file_path
        print(imageentry)
        unique_id = Image.open(file_path)
        width, height = unique_id.size
        w = (width/100)*35
        h = (height/100)*35
        Imagewidth = round(w)
        Imageheight = round(h)
        #wpercent = Imagewidth / float(unique_id.size[0])
        #hsize = int((float(unique_id.size[1]) * float(wpercent)))
        unique_id = unique_id.resize((Imagewidth, Imageheight),Image.Resampling.LANCZOS)
        unique_id = ImageTk.PhotoImage(unique_id)
        filename1 = Label(left1, text=imageentry)
        filename1.grid(row=(row_1)-1, column=column_1, columnspan=30, rowspan=1, sticky=EW)
        panel1 = Label(left1, image=unique_id, width=Imagewidth, background="white")
        panel1.image = unique_id
        panel1.grid(row=row_1, column=column_1, columnspan=30, rowspan=10, sticky=EW)
        caseimagecount+=1
        addanalysis.update()
    except Exception as e:
        pass #qwertylabel.config(text=f"Error loading image: {e}")
    
    thread_1()
############################################################################################
def add_analysis():
    global addanalysis, caseimagecount, left1, img1#, photoCanvas1, left_frame, caseimagecount, Indiv_Case6, img1, panel2, row, extend, panel, addanalysis, addanalysis_case_vars, d1a, d1b, d2a, d2b, d3a, d3b, e1a, e1b, e2a, e2b, e3a, e3b, e4, e4a, e4b, e5a, e5b, e6a, e6b, e7a, e7b, e24a, e24b, e2, e3, e4, e5, e6, e7, e8, e9, e10a, e10b, submitb, LoadButtona, LoadButtonb, LoadButtona1, LoadButtonb1, text_zoom, pw_generator, desktop, Refresh, e1a, e1b, e2a, e2b, e3a, e3b, e4, e5a, e5b, e6a, e6b, e7a, e7b, e24a, e24b, LoadButtona, LoadButtonb, notepad_n59b, canvas, text_var, lab1, lab2, viewTypea, v0, v1, v2, v3, v4, v5, v6, delEntry_a, delEntry_b, pw_generator, addanalysiscase, pw_generator_e1, e1a, e1b, e2, e3, e4, e5, e6, e7, e8, e9, submitb, pw_generator_e1a, label1, submit, edit1b, e2a, e3a, e4a, e5a, e6a, e7a, e8a, e9a, launch, e21a, e21b, e22a, e22b, startup_e1a, startup_e1b, startup_e2a, startup_e2b, pw_customa, pw_customb, pw_generator, default_font, zoomed_font
    addline()
    disable_buttons()
    createentrydb()
    writeentrytodb()
    caseimagecount = 0
    addanalysis = Toplevel()#TkinterDnD.Tk()
    #addanalysis_case.iconbitmap(iconfile)
    #addanalysis.geometry('570x427')#600x410')765x427')
    addanalysis.resizable(True, True)#width=False, height=False)
    addanalysis.title("CASE - V1.0 - ryan.ward@sussex.police.uk")
    
    addanalysis.protocol('WM_DELETE_WINDOW', disgard_exit)
    image_refs=[]
    screenratio=[]
    width  = addanalysis.winfo_screenwidth()
    height = addanalysis.winfo_screenheight()
    screenratio.append(str(width))
    screenratio.append(str(height))
    screensize='_'.join(screenratio)
    print(screensize)

    if screensize == '1536_960':
        print(screensize)
    elif screensize == '1920_1028':
        pass
    
    addanalysis_case_vars = []
    rows=31
    columns=3

    # Set row height here
    height=4
    frames=[addanalysis]#, settings_tab, structure]

    for row in range(1):
        for col in range(90):
            tk.Button(addanalysis,text='',width=1,height=1).grid(row=row, column=col)
    for col in range(1):
        for row in range(50):
            tk.Button(addanalysis,text='',width=1,height=1).grid(row=row, column=col)
    try: 
        img1 = Image.open("C:\\Case Creator\\_logos\\Surrey-Sussex-Police-logo.jpg")
        #(height, width)
        img1 = img1.resize((125, 125), Image.ADAPTIVE)
        img1 = ImageTk.PhotoImage(img1)
        panel = Label(addanalysis, image=img1, width=125, background="white")
        panel.image = img1
        panel.grid(row=1, column=1, columnspan=10, rowspan=4, sticky=EW)
        panel.bind('<Triple-Button-1>', lambda x: expandview())
    except:
        pass
    
    row=5
    Indiv_Case6scrollbar = Scrollbar(addanalysis)
    Indiv_Case6=Text(addanalysis, wrap=WORD,  yscrollcommand=Indiv_Case6scrollbar.set, height = 16)
    Indiv_Case6.grid(row=5, column=11, columnspan=78,  rowspan=10, sticky=EW)
    try:
        Indiv_Case6_notes = (str.replace(each[6],"\\n","\n"))
        Indiv_Case6.insert(INSERT, Indiv_Case6_notes)
    except:
        pass
    Indiv_Case6.grid_propagate(False)
    Indiv_Case6.bind('<KeyRelease>', Indiv_Case_notes)
    Indiv_Case6scrollbar.config( command = Indiv_Case6.yview)
    Indiv_Case6scrollbar.grid(row=5, column=89,  columnspan=78, rowspan=10, padx= 1, sticky='NS')
    
    #tk.Button(addanalysis, text="Span 2 rows", width=10, height=4).grid(row=1,column=0,rowspan=4,sticky="ns")
    Button(addanalysis, text="Add multiple images", width=24, command=0).grid(row=5, column=1, columnspan=10, sticky=W)
    Button(addanalysis, text="Remove image", command =0).grid(row=6, column=1, columnspan=10, sticky=EW)
    Button(addanalysis, text="Commit Entry", command=0).grid(row=7, column=1, columnspan=10, sticky=EW)
    Button(addanalysis, text="Disgard & exit", command =disgard_exit).grid(row=8, column=1, columnspan=10, sticky=EW)

    # Label to show instructions or image
    qwertylabel = Label(addanalysis, text="Drag and drop an image files ", bg="lightgray")#, width=40, height=4)
    qwertylabel.grid(row=15, column=11, columnspan=79, rowspan=1, sticky=EW)

    
    left_frame = Frame(addanalysis, borderwidth=1,relief=RIDGE)
    left_frame.grid(row=16, column=11, columnspan=79, rowspan=18, sticky=EW) 

    photoCanvas1 = Canvas(left_frame, width=1325, height=450) #width=width, height=(height)-45)
    photoCanvas1.grid(sticky=NSEW)

    left1 = Frame(photoCanvas1, width=1325, height=400)
    photoCanvas1.create_window(0, 0, window=left1, anchor='nw')
    left1.drop_target_register(DND_FILES)
    left1.dnd_bind('<<Drop>>', drop)

    for row in range(1):
        for col in range(90):
            tk.Label(left1,text='',width=1,height=1).grid(row=row, column=col)
    for col in range(1):
        for row in range(20):
            tk.Label(left1,text='',width=1,height=1).grid(row=row, column=col)
    ############################################################################################

    #populate_history()
    ############################################################################################
    def update_scrollregion(event):
        photoCanvas1.configure(scrollregion=photoCanvas1.bbox("all"))
    ############################################################################################

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
    addanalysis.attributes('-topmost',True)
    addanalysis.mainloop()
    #analysis()
############################################################################################
### contemp_add_entry ### END ###
############################################################################################

############################################################################################
def disgard_exit():
    addanalysis.destroy()
    enable_buttons()
############################################################################################
def timestampnow():
    global timestamp
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    return timestamp
##############################################################################################
def togglebind(event):
    global TEXT
    if togglepreview.config(relief="raised") == True:
        togglepreview.config(relief="sunken")
        print('raised')
    else:
        pass
    
    if togglepreview.config(relief="sunken") == True:
        togglepreview.config(relief="raised")
        print('sunken')
    else:
        pass
    root.update()
############################################################################################
def getaddentrybutton(event):
    global TEXT
    print(event.widget["text"])
    TEXT = (event.widget["text"])[4:]
    #getaddentrybutton()
##    event.widget["text"] = "DONE"
##    event.widget["bg"] = "green"
##    TEXT = (event.widget["text"])
##    print('button text: ', TEXT)
##    print(entry1.keys())
##    for each in pindecryptvariables:
##        each.destroy()
##    print('open case vars: ', opencasevariables)
##    get_individual_pd_data()
############################################################################################
def enable_buttons():
    for button in button_list:
        button.config(state='normal')
############################################################################################
def disable_buttons():
    for button in button_list:
        button.config(state='disabled')
############################################################################################
def addline():
    global row, entry3
    timestampnow()
    print('row ', row)
    Label(contemp_entry, text=row).grid(row=row, column=1, columnspan=5, sticky=W)
    
    entry = (str("e"+(str(row))+(str(row))))
    print(entry)
    entry = Entry(contemp_entry,text="")
    #f1variables.append(entry)
    entry.grid(row=row, column=2, columnspan=7, sticky=EW)
    entry.insert(8, timestamp)
    entry.config(state='disabled')

    entry = (str("e"+(str(row))+(str(row))))
    print(entry)
    entry = Entry(contemp_entry,text="")
    #f1variables.append(entry)
    entry.grid(row=row, column=10, columnspan=10, sticky=EW)
    entry.insert(8, TEXT)
    entry.config(state='disabled')

    entry3 = (str("e"+(str(row))+(str(row))))
    print(entry3)
    entry3 = Entry(contemp_entry,text="")
    #f1variables.append(entry)
    entry3.grid(row=row, column=21, columnspan=50, sticky=EW)
    entry3.insert(8, '')
    entry3.config(state='disabled')
    row+=1

    root.update()
############################################################################################
def contemp():
    global root, button_list, row, contemp_entry
    
    root = TkinterDnD.Tk()#Tk()
    #root_case.iconbitmap(iconfile)
    #root.geometry('570x427')#600x410')765x427')
    root.resizable(True, True)#width=False, height=False)
    root.title("CASE - V1.0 - ryan.ward@sussex.police.uk")
    
    root.protocol('WM_DELETE_WINDOW', sys.exit)
    
    width  = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(width)
    print(height)
    root_case_vars = []
    rows=31
    columns=3

    # Set row height here
    height=4
    frames=[root]#, settings_tab, structure]

    for row in range(1):
        for col in range(90):
            tk.Button(root,text='',width=1,height=1).grid(row=row, column=col)
    for col in range(1):
        for row in range(50):
            tk.Button(root,text='',width=1,height=1).grid(row=row, column=col)

    img1 = Image.open("C:\\Case Creator\\_logos\\Surrey-Sussex-Police-logo.jpg")#C:\\Case Creator\\_logos\\Surrey-Sussex-Police-logo.jpg")
    #(height, width)
    img1 = img1.resize((125, 125), Image.ADAPTIVE)
    img1 = ImageTk.PhotoImage(img1)
    panel = Label(root, image=img1, width=125, background="white")
    panel.image = img1
    panel.grid(row=1, column=1, columnspan=10, rowspan=4, sticky=EW)
    panel.bind('<Triple-Button-1>', lambda x: expandview())

    dynamic_col_span = 10

    Label1=Label(root, text="Action: ", borderwidth=2, relief="groove")
    Label1.grid(row=5, column=1, columnspan=10, sticky=EW)

    button_list = []
    
    add1 = Button(root, text="Add Case Note", command=addline)
    add1.bind('<Button-1>', getaddentrybutton)
    add1.grid(row=6, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add1)
    
    add2 = Button(root, text="Add Communiaction", command =addline)
    add2.bind('<Button-1>', getaddentrybutton)
    add2.grid(row=7, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add2)
    
    add3 = Button(root, text="Add Internal Exhibit Movement", command=addline)
    add3.bind('<Button-1>', getaddentrybutton)
    add3.grid(row=8, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add3)
    
    add4 = Button(root, text="Add Exhibit Photographs", command =addline)
    add4.bind('<Button-1>', getaddentrybutton)
    add4.grid(row=9, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add4)
    
    add5 = Button(root, text="Add Exhibit Pre-imaging", command =addline)
    add5.bind('<Button-1>', getaddentrybutton)
    add5.grid(row=10, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add5)
    
    add6 = Button(root, text="Add Exhibit Imaging", command =addline)
    add6.bind('<Button-1>', getaddentrybutton)
    add6.grid(row=11, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add6)
    
    add7 = Button(root, text="Add Exhibit Post-imaging", command =addline)
    add7.bind('<Button-1>', getaddentrybutton)
    add7.grid(row=12, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add7)
    
    add8 = Button(root, text="Add Analysis", command =add_analysis)
    add8.bind('<Button-1>', getaddentrybutton)
    add8.grid(row=13, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add8)
    
    add9 = Button(root, text="Add Exhibit Reseal", command =addline)
    add9.bind('<Button-1>', getaddentrybutton)
    add9.grid(row=14, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add9)
    
    add10 = Button(root, text="Add External Exhibit Movement", command =addline)
    add10.bind('<Button-1>', getaddentrybutton)
    add10.grid(row=15, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add10)
    
    add11 = Button(root, text="Add Quality Review", command =addline)
    add11.bind('<Button-1>', getaddentrybutton)
    add11.grid(row=16, column=1, columnspan=dynamic_col_span, sticky=EW)
    button_list.append(add11)
    
    left_frame = Frame(root, borderwidth=1,relief=RIDGE)
    left_frame.grid(row=5, column=11, columnspan=79, rowspan=28, sticky=EW) 
    
    photoCanvas1 = Canvas(left_frame, width=1325, height=710) #width=width, height=(height)-45)
    photoCanvas1.grid(sticky=NSEW)

    contemp_entry = Frame(photoCanvas1, width=1325, height=400)
    photoCanvas1.create_window(0, 0, window=contemp_entry, anchor='nw')
    

    #left1.drop_target_register(DND_FILES)
    #left1.dnd_bind('<<Drop>>', drop)

    for row in range(1):
        for col in range(62):
            tk.Label(contemp_entry,text='',width=2,height=1).grid(row=row, column=col)
    for col in range(1):
        for row in range(20):
            tk.Label(contemp_entry,text='',width=2,height=1).grid(row=row, column=col)

    Label2=Label(contemp_entry, text="Timestamp: ", borderwidth=2, relief="groove")
    Label2.grid(row=0, column=2, columnspan=7, ipadx=0, sticky=EW)

    Label3=Label(contemp_entry, text="Entry type: ", borderwidth=2, relief="groove")
    Label3.grid(row=0, column=10, columnspan=10, sticky=EW)

    Label4=Label(contemp_entry, text="Details: ", borderwidth=2, relief="groove")
    Label4.grid(row=0, column=21, columnspan=50, sticky=EW)
    def toggle():
        pass
    togglepreview = Button(contemp_entry, text="Preview", height=1, command=toggle)
    togglepreview.grid(row=0, column=74, columnspan=2, sticky=EW)
    togglepreview.config(relief="sunken", background = 'grey')
    togglepreview.bind('<Button-1>', togglebind)
    
    row=1
    ############################################################################################

    #populate_history()
    ############################################################################################
    def update_scrollregion(event):
        photoCanvas1.configure(scrollregion=photoCanvas1.bbox("all"))
    ############################################################################################

    photoScrollv = Scrollbar(left_frame, orient=VERTICAL)
    photoScrollv.config(command=photoCanvas1.yview)
    photoScrollh = Scrollbar(left_frame, orient=HORIZONTAL)
    photoScrollh.config(command=photoCanvas1.xview)
    photoCanvas1.config(yscrollcommand=photoScrollv.set)
    photoCanvas1.config(xscrollcommand=photoScrollh.set)
    photoScrollv.grid(row=0, column=1, sticky="ns")
    photoScrollh.grid(row=7, column=0, sticky="ew")
    contemp_entry.bind("<Configure>", update_scrollregion)
    photoScrollv.bind("<MouseWheel>", update_scrollregion)
    root.mainloop()


contemp()


