#from case_main import *
############################################################################################
 
############################################################################################
def mget_individual_case_data(text):
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
        case.geometry('670x650') #widthxheight
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
                count=1
                count2=1

                if frame == the_case[0]:
                    while count < rows:
                        Label(name, text=" ").grid(row=count, column=0, sticky=EW)
                        count+=1
                    while count2 < columns:
                        Label(name, text=" ").grid(row=0, column=count2, sticky=EW)
                        count2+=1
                        
        
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

            oic_label=Label(name, text=" PRQC:")
            oic_label.grid(row=3, column=1, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Strategy:")
            oic_label.grid(row=3, column=2, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Pre-imaging:")
            oic_label.grid(row=3, column=3, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Imaging:")
            oic_label.grid(row=3, column=4, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Analysis:")
            oic_label.grid(row=3, column=5, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Reports:")
            oic_label.grid(row=3, column=6, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" QC:")
            oic_label.grid(row=3, column=7, sticky=EW)
            individualcasevariables.append(oic_label)

            oic_label=Label(name, text=" Docs:")
            oic_label.grid(row=3, column=8, sticky=EW)
            individualcasevariables.append(oic_label)
            
            oic_label=Label(name, text=" Property of: ")
            oic_label.grid(row=1, column=7, sticky=EW)
            individualcasevariables.append(oic_label)

            Loop_Indiv_Case1a = StringVar()
            Loop_Indiv_Case1a.set(exhib[4])
            Loop_Indiv_Case1a.trace("w", lambda name, index, mode, Loop_Indiv_Case1a=Loop_Indiv_Case1a: callback(Loop_Indiv_Case1a))
            Loop_Indiv_Case1 = Entry(name, relief=SUNKEN,width=15, state='normal', textvariable=Loop_Indiv_Case1a)
            Loop_Indiv_Case1.grid(row=2, column=1, columnspan=2, sticky=EW)
            
            individualcasevariables.append(Loop_Indiv_Case1)
            count += 1
            Loop_Indiv_Case2 = (str("e"+(str(count))))
            Loop_Indiv_Case2a = StringVar()
            Loop_Indiv_Case2a.set(exhib[5])
            Loop_Indiv_Case2a.trace("w", lambda name, index, mode, Loop_Indiv_Case2a=Loop_Indiv_Case2a: callback_Loop_Indiv_Case_exhibit(Loop_Indiv_Case2a))
            Loop_Indiv_Case2 = Entry(name, relief=SUNKEN,width=15, state='normal', textvariable=Loop_Indiv_Case2a)
            Loop_Indiv_Case2.grid(row=2, column=3, columnspan=2, sticky=EW)
            individualcasevariables.append(Loop_Indiv_Case2)
            count += 1
            Loop_Indiv_Case3 = (str("e"+(str(count))))
            Loop_Indiv_Case3a = StringVar()
            Loop_Indiv_Case3a.set(exhib[9])
            Loop_Indiv_Case3a.trace("w", lambda name, index, mode, Loop_Indiv_Case3a=Loop_Indiv_Case3a: callback_Loop_Indiv_Case_property_ref(Loop_Indiv_Case3a))
            Loop_Indiv_Case3 = Entry(name, relief=SUNKEN,width=15, state='normal', textvariable=Loop_Indiv_Case3a)
            Loop_Indiv_Case3.grid(row=2, column=5, columnspan=2, sticky=EW)
            individualcasevariables.append(Loop_Indiv_Case3)
            
            row=2
            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=1, sticky=EW)
            overviewvariables.append(e30b)
            
            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=2, padx=1, sticky=EW)
            overviewvariables.append(e30b)

            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=3, sticky=EW)
            overviewvariables.append(e30b)
            
            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=4, padx=1, sticky=EW)
            overviewvariables.append(e30b)

            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=5, sticky=EW)
            overviewvariables.append(e30b)
            
            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=6, padx=1, sticky=EW)
            overviewvariables.append(e30b)

            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=7, padx=1, sticky=EW)
            overviewvariables.append(e30b)

            e30a = IntVar()
            e30a.set(0)
            e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
            e30b = Checkbutton(name, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
            e30b.grid(row=4, column=8, padx=1, sticky=EW)
            overviewvariables.append(e30b)
            
            vic_or_susa = StringVar()
            vic_or_susa.set('--Select--')
            vic_or_susa.trace("w", lambda name, index, mode, vic_or_susa=vic_or_susa: callback(vic_or_susa))
            vic_or_susab = OptionMenu(name, vic_or_susa, *property_of, command=qwerty)
            vic_or_susab.grid(row=row, column=7, columnspan=3, sticky=W)
            individualcasevariables.append(vic_or_susab)
            vic_or_susab.config(width=18)
##
##            row=4
##
##            locationa = StringVar()
##            locationa.set('--Select--')
##            locationa.trace("w", lambda name, index, mode, locationa=locationa: callback(locationa))
##            locationab = OptionMenu(name, locationa, *location, command=qwerty)
##            locationab.grid(row=row, column=8, columnspan=1, sticky=W)
##            individualcasevariables.append(locationab)
##            locationab.config(width=18)
##            count_no2+=1
##
##            actiona = StringVar()
##            actiona.set('--Select--')
##            actiona.trace("w", lambda name, index, mode, actiona=actiona: callback(actiona))
##            actionab = OptionMenu(name, actiona, *action, command=qwerty)
##            actionab.grid(row=row, column=1, columnspan=1, sticky=W)
##            individualcasevariables.append(actionab)
##            actionab.config(width=18)
##            count_no2+=1

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
            Loop_Indiv_Action6=Text(name, wrap=WORD, width=75, yscrollcommand=Loop_Indiv_Action6scrollbar.set)
            print(Loop_Indiv_Action6)
            Loop_Indiv_Action6.grid(row=6, column=1, columnspan=11, sticky=W, rowspan=1)
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



##            Loop_Indiv_Case6 = (str("t"+(str(count_no2))))
##            print(Loop_Indiv_Case6)
##            key=(exhib[4])
##            Loop_Indiv_Case6scrollbar = Scrollbar(name)
##            Loop_Indiv_Case6=Text(name, wrap=WORD, width=47, yscrollcommand=Loop_Indiv_Case6scrollbar.set)
##            print(Loop_Indiv_Case6)
##            Loop_Indiv_Case6.grid(row=20, column=1, columnspan=11, sticky=EW, rowspan=6)
##            print(Loop_Indiv_Case6)
##            value=Loop_Indiv_Case6
##            
##            Loop_Indiv_Case6_notes = (str.replace(exhib[14],"\\n","\n"))
##            Loop_Indiv_Case6.insert(INSERT, Loop_Indiv_Case6_notes)
##
##            Loop_Indiv_Case6.grid_propagate(False)
##            Loop_Indiv_Case6.bind('<KeyRelease>', Loop_Indiv_Case_exhibit_notes)
##            Loop_Indiv_Case6scrollbar.config( command = Loop_Indiv_Case6.yview)
##            Loop_Indiv_Case6scrollbar.grid(row=20, column=12, columnspan=1, rowspan=6,  sticky='NS')
##
##            ryan[key] = value
##            
##            individualcasevariables.append(Loop_Indiv_Case6scrollbar)
##            individualcasevariables.append(Loop_Indiv_Case6)
        
        tabs.pack(fill='both', expand=Y)
        for key in ryan:
            print('key: ',key)
        print(ryan.values())
        
        Indiv_Case_note_label=Label(overview, text=" Notes")
        Indiv_Case_note_label.grid(row=6, column=1, sticky=W)
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
        oic_label.grid(row=1, column=5, sticky=W)
        individualcasevariables.append(oic_label)
        
        oic_label=Label(overview, text=" OIC")
        oic_label.grid(row=1, column=4, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Date allocated")
        oic_label.grid(row=3, column=1, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Date started")
        oic_label.grid(row=3, column=2, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Days open")
        oic_label.grid(row=3, column=3, sticky=W)
        individualcasevariables.append(oic_label)

        oic_label=Label(overview, text=" Date finished")
        oic_label.grid(row=3, column=4, sticky=W)
        individualcasevariables.append(oic_label)

        case_password=Label(overview, text=" Case Password: ")
        case_password.grid(row=3, column=5, sticky=W)

##        statuslabel=Label(overview, text=" Case Status: ")
##        statuslabel.grid(row=5, column=2, sticky=W)

##        v8 =  StringVar()
##        Label8 = Label(overview, textvariable=v8)
##        Label8.grid(row=5, column=1, padx=15, sticky=W)
##        v8.set('QC')
##        overviewvariables.append(Label8)
##
##        v9 =  StringVar()
##        Label9 = Label(overview, textvariable=v9)
##        Label9.grid(row=5, column=1, padx=70, columnspan=1, sticky=W)
##        v9.set('Server')
##        overviewvariables.append(Label9)
        
        frames=["case"] 
        rows=31
        columns=7
        conn.close()
        # Set row height here
        height=5
        for frame in frames:
            count=0
            count2=1
            frame=(str(frame))
            if frame == frames[0]:
                while count < rows:
                    Label(overview, text=" ").grid(row=count, column=0, sticky=W)
                    count+=1
                while count2 < columns:
                    Label(overview, text="", width=15).grid(row=0, column=count2, sticky=W)
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

        # OIC
        Indiv_Case4 = (str("e"+(str(count))))
        Indiv_Case4a = StringVar()
        Indiv_Case4a.set(each[4])
        Indiv_Case4a.trace("w", lambda name, index, mode, Indiv_Case4a=Indiv_Case4a: callback_Indiv_Case4(Indiv_Case4a))
        Indiv_Case4 = Entry(overview, relief=SUNKEN,width=15, state='normal', textvariable=Indiv_Case4a)
        Indiv_Case4.grid(row=row, column=4, sticky=EW)
        individualcasevariables.append(Indiv_Case4)
        count += 1

        # NO OF EXHIBITS
        Indiv_Case3 = (str("e"+(str(count))))
        Indiv_Case3a = StringVar()
        Indiv_Case3a.set((len(the_case)))
        Indiv_Case3a.trace("w", lambda name, index, mode, Indiv_Case3a=Indiv_Case3a: callback_Indiv_Case3(Indiv_Case3a))
        Indiv_Case3 = Entry(overview, relief=SUNKEN,width=12, state='normal', textvariable=Indiv_Case3a)
        Indiv_Case3.grid(row=row, column=5, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case3)
        count += 1
        row += 2

##        Indiv_Case4 = (str("e"+(str(count))))
##        Indiv_Case4a = StringVar()
##        Indiv_Case4a.set(each[4])
##        Indiv_Case4a.trace("w", lambda name, index, mode, Indiv_Case4a=Indiv_Case4a: callback_Indiv_Case4(Indiv_Case4a))
##        Indiv_Case4 = Entry(overview, relief=SUNKEN,width=15, state='normal', textvariable=Indiv_Case4a)
##        Indiv_Case4.grid(row=row, column=3, sticky=EW)
##        individualcasevariables.append(Indiv_Case4)
##        count += 1

        selected_month_rec = (timestamp[:-9])
        #date allocated
        Indiv_Case9 = (str("e"+(str(count))))
        Indiv_Case9a = StringVar()
        Indiv_Case9a.set('05/04/1980')#each[13])
        Indiv_Case9a.trace("w", lambda name, index, mode, Indiv_Case9a=Indiv_Case9a: callback_Indiv_Case9(Indiv_Case9a))
        Indiv_Case9 = Entry(overview, relief=SUNKEN,width=15, state='disabled', textvariable=Indiv_Case9a)
        Indiv_Case9.grid(row=row, column=1, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case9)
        count += 1

        #date started
        Indiv_Case5 = (str("e"+(str(count))))
        Indiv_Case5a = StringVar()
        Indiv_Case5a.set('05/04/1980')#each[13])
        Indiv_Case5a.trace("w", lambda name, index, mode, Indiv_Case5a=Indiv_Case5a: callback_Indiv_Case5(Indiv_Case5a))
        Indiv_Case5 = Entry(overview, relief=SUNKEN,width=15, state='disabled', textvariable=Indiv_Case5a)
        Indiv_Case5.grid(row=row, column=2, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case5)
        count += 1

        #timestamp = (each[13])
        selected_month_rec = (timestamp[:-9])

        #selected_month_rec = (each[13])
        print(selected_month_rec)
        start = date(int(selected_month_rec.split('-')[0]),int(selected_month_rec.split('-')[1]),int(selected_month_rec.split('-')[2]))
        today = date.today()
        res = today - start
        res.days

        #days open
        Indiv_Case7 = (str("e"+(str(count))))
        Indiv_Case7a = StringVar()
        Indiv_Case7a.set(res.days)
        Indiv_Case7a.trace("w", lambda name, index, mode, Indiv_Case7a=Indiv_Case7a: callback(Indiv_Case7a))
        Indiv_Case7 = Entry(overview, relief=SUNKEN,width=15, state='disabled', textvariable=Indiv_Case7a)
        Indiv_Case7.grid(row=row, column=3, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case7)
        count += 1
        row += 2

        Indiv_Case6scrollbar = Scrollbar(overview)
        Indiv_Case6=Text(overview, wrap=WORD, width=75, yscrollcommand=Indiv_Case6scrollbar.set)
        Indiv_Case6.grid(row=7, column=1, columnspan=20,  rowspan=5, sticky=W)

        Indiv_Case6_notes = (str.replace(each[6],"\\n","\n"))
        Indiv_Case6.insert(INSERT, Indiv_Case6_notes)

        Indiv_Case6.grid_propagate(False)
        Indiv_Case6.bind('<KeyRelease>', Indiv_Case_notes)
        Indiv_Case6scrollbar.config( command = Indiv_Case6.yview)
        Indiv_Case6scrollbar.grid(row=7, column=6,  columnspan=1, rowspan=5,  sticky='NS')

        Indiv_Case8 = (str("e"+(str(count))))
        Indiv_Case8a = StringVar()
        Indiv_Case8a.set(case_pw)
        Indiv_Case8a.trace("w", lambda name, index, mode, Indiv_Case8a=Indiv_Case8a: callback(Indiv_Case8a))
        Indiv_Case8 = Entry(overview, relief=SUNKEN,width=15, state='disabled', textvariable=Indiv_Case8a)
        Indiv_Case8.grid(row=4, column=5, columnspan=1, sticky=EW)
        individualcasevariables.append(Indiv_Case8)

##        e30a = IntVar()
##        e30a.set(0)
##        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
##        e30b = Checkbutton(overview, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
##        e30b.grid(row=6, column=1, sticky=W)
##        overviewvariables.append(e30b)
##        
##        e30a = IntVar()
##        e30a.set(0)
##        e30a.trace("w", lambda name, index, mode, e30a=e30a: callbacke30(e30a))
##        e30b = Checkbutton(overview, text=" ", width=5, onvalue=1,offvalue=0,variable=e30a)
##        e30b.grid(row=6, column=1, padx=60, sticky=W)
##        overviewvariables.append(e30b)
        default_font = font.Font(family="Arial", size=8)
        submit2a= StringVar()
        submit2a.trace("w", lambda name, index, mode, submi2ta=submit2a: callback(submit2a))
        submit2b = Button(overview, text="Copy to clip", font=default_font,  width=9, command=copytoclip_individual_case)
        submit2b.grid(row=4, column=6, sticky=W)
        
        individualcasevariables.append(Indiv_Case6scrollbar)
        individualcasevariables.append(Indiv_Case6)

        #        Label(overview, text=" Status:").grid(row=row, column=1, sticky=W)
##        status_dda = StringVar()
##        status_dda.set(case_status)
##        status_dda.trace("w", lambda name, index, mode, status_dda=status_dda: callback_Indiv_Case_status(status_dda))
##        status_ddb = OptionMenu(overview, status_dda, *status, command=0)
##        status_ddb.grid(row=6, column=2, columnspan=1, sticky=W)
##        individualcasevariables.append(status_ddb)

        count += 1

        del_close1=Button(overview, text="Delete/Close", width=15, command=close)
        del_close1.grid(row=13, column=5, sticky=W)
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
