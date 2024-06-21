from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1366x740+0+0")
        self.root.resizable(False, False)

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finallprice_var=StringVar()

        labltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        labltitle.pack(side=TOP,fill=X)

        frame =Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1367,height=384)

        # ___________________data frame left_______________#

        dataframeleft = LabelFrame(frame,text="Library Mambership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dataframeleft.place(x=0,y=5,width=800,height=350)

        lablmamebr = Label(dataframeleft,text="Member",font=("arial",12,"bold"),bg="powder blue",padx=2,pady=6)
        lablmamebr.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(dataframeleft,font=("arial",12,"bold"),width=27,textvariable=self.member_var,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lablprnno = Label(dataframeleft,text="PRN_No",font=("arial",12,"bold"),bg="powder blue",padx=2,pady=6)
        lablprnno.grid(row=1,column=0,sticky=W)
        txtprn_no=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.prn_var,width=29)
        txtprn_no.grid(row=1,column=1)

        lablTitle=Label(dataframeleft,font=("arial",12,"bold"),text="ID No:",bg="powder blue",padx=2,pady=6)
        lablTitle.grid(row=2,column=0,sticky=W)
        lablTitle=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.id_var,width=29)
        lablTitle.grid(row=2,column=1)

        lblfirstname=Label(dataframeleft,font=("arial",12,"bold"),text="First Name",bg="powder blue",padx=2,pady=6)
        lblfirstname.grid(row=3,column=0,sticky=W)
        lblfirstname=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.firstname_var,width=29)
        lblfirstname.grid(row=3,column=1)

        lbllastname=Label(dataframeleft,font=("arial",12,"bold"),text="Last Name",bg="powder blue",padx=2,pady=6)
        lbllastname.grid(row=4,column=0,sticky=W)
        lbllastname=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.lastname_var,width=29)
        lbllastname.grid(row=4,column=1)

        lbladdress1=Label(dataframeleft,font=("arial",12,"bold"),text="Address1",bg="powder blue",padx=2,pady=6)
        lbladdress1.grid(row=5,column=0,sticky=W)
        lbladdress1=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.address1_var,width=29)
        lbladdress1.grid(row=5,column=1)

        lbladdress2=Label(dataframeleft,font=("arial",12,"bold"),text="Address2",bg="powder blue",padx=2,pady=6)
        lbladdress2.grid(row=6,column=0,sticky=W)
        lbladdress2=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.address2_var,width=29)
        lbladdress2.grid(row=6,column=1)

        lblpostcode=Label(dataframeleft,font=("arial",12,"bold"),text="Post Code",bg="powder blue",padx=2,pady=6)
        lblpostcode.grid(row=7,column=0,sticky=W)
        lblpostcode=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.postcode_var,width=29)
        lblpostcode.grid(row=7,column=1)

        lblmobile=Label(dataframeleft,font=("arial",12,"bold"),text="Mobile",bg="powder blue",padx=2,pady=6)
        lblmobile.grid(row=8,column=0,sticky=W)
        lblmobile=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.mobile_var,width=29)
        lblmobile.grid(row=8,column=1)

        lblbookId=Label(dataframeleft,font=("arial",12,"bold"),text="Book ID:",bg="powder blue",padx=2,pady=6)
        lblbookId.grid(row=0,column=2,sticky=W)
        lblbookId=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=28)
        lblbookId.grid(row=0,column=3)

        lblbooktitle=Label(dataframeleft,font=("arial",12,"bold"),text="Book Title:",bg="powder blue",padx=2,pady=6)
        lblbooktitle.grid(row=1,column=2,sticky=W)
        lblbooktitle=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=28)
        lblbooktitle.grid(row=1,column=3)

        lblbookauther=Label(dataframeleft,font=("arial",12,"bold"),text="Auther Name:",bg="powder blue",padx=2,pady=6)
        lblbookauther.grid(row=2,column=2,sticky=W)
        lblbookauther=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.auther_var,width=28)
        lblbookauther.grid(row=2,column=3)

        lbldateborrowed=Label(dataframeleft,font=("arial",12,"bold"),text="Date Borrowed:",bg="powder blue",padx=2,pady=6)
        lbldateborrowed.grid(row=3,column=2,sticky=W)
        lbldateborrowed=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=28)
        lbldateborrowed.grid(row=3,column=3)

        lbldatedue=Label(dataframeleft,font=("arial",12,"bold"),text="Due Date:",bg="powder blue",padx=2,pady=6)
        lbldatedue.grid(row=4,column=2,sticky=W)
        lbldatedue=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=28)
        lbldatedue.grid(row=4,column=3)

        lbldaysonbook=Label(dataframeleft,font=("arial",12,"bold"),text="Days On Book:",bg="powder blue",padx=2,pady=6)
        lbldaysonbook.grid(row=5,column=2,sticky=W)
        lbldaysonbook=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=28)
        lbldaysonbook.grid(row=5,column=3)

        lbllatereturnfine=Label(dataframeleft,font=("arial",12,"bold"),text="Late Return Fine:",bg="powder blue",padx=2,pady=6)
        lbllatereturnfine.grid(row=6,column=2,sticky=W)
        lbllatereturnfine=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=28)
        lbllatereturnfine.grid(row=6,column=3)

        lbldateoverdate=Label(dataframeleft,font=("arial",12,"bold"),text="Date Over Due:",bg="powder blue",padx=2,pady=6)
        lbldateoverdate.grid(row=7,column=2,sticky=W)
        lbldateoverdate=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=28)
        lbldateoverdate.grid(row=7,column=3)

        lblactualprice=Label(dataframeleft,font=("arial",12,"bold"),text="Actual Price:",bg="powder blue",padx=2,pady=6)
        lblactualprice.grid(row=8,column=2,sticky=W)
        lblactualprice=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.finallprice_var,width=28)
        lblactualprice.grid(row=8,column=3)

        #____________________data frame right______________#

        dataframeright = LabelFrame(frame,text="Book Details",bg="powder blue",padx=10,fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dataframeright.place(x=810,y=5,width=490,height=350)

        self.txtbox=Text(dataframeright,font=("arial",12,"bold"),width=30,height=14,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        listscrolbar=Scrollbar(dataframeright)
        listscrolbar.grid(row=0,column=1,sticky="ns")

        listboooks=['Python','Rich Dad Poor Dad','Atomic Habits','Programming With C','Learn Python The Hard Way','Python Programming','History Of India','Bharat Ki Khoj','MahaBharta','Ramayana','The Geeta','Psycology Of Money','Power Of Thought','The Power Of Subconcious Mind']

        def selectbook(event=""):
            value=str(listbox.get(listbox.curselection()[0]))
            x=value
            if(x=="Pyhton"):
                self.bookid_var.set("BKID345")
                self.booktitle_var.set("Python")
                self.auther_var.set("Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.788")

            elif(x=="Rich Dad Poor Dad"):
                self.bookid_var.set("BKID340")
                self.booktitle_var.set("Rich Dad Poor Dad")
                self.auther_var.set("Robert T. Duke")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.988")

            elif(x=="Atomic Habits"):
                self.bookid_var.set("BKID335")
                self.booktitle_var.set("Atomic Habits")
                self.auther_var.set("James Clear")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.500")

            elif(x=="Programming With C"):
                self.bookid_var.set("BKID245")
                self.booktitle_var.set("Programming With C")
                self.auther_var.set("Brian Kernighan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1000")

            elif(x=="Learn Python : The Hard Way"):
                self.bookid_var.set("BKID349")
                self.booktitle_var.set("Learn Python : The Hard Way")
                self.auther_var.set("Zed A. Shaw")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.999")

            elif(x=="Python Programming"):
                self.bookid_var.set("BKID385")
                self.booktitle_var.set("Python Programming")
                self.auther_var.set("Guido Van Rossum")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.348")

            elif(x=="History Of India"):
                self.bookid_var.set("BKID700")
                self.booktitle_var.set("History Of India")
                self.auther_var.set("James Mill")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.788")

            elif(x=="Bharat Ki Khoj"):
                self.bookid_var.set("BKID780")
                self.booktitle_var.set("Bharat Ki Khoj")
                self.auther_var.set("Jawaharlal Nehru")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.788")

            elif(x=="MahaBharta"):
                self.bookid_var.set("BKID365")
                self.booktitle_var.set("MahaBharta")
                self.auther_var.set("Ved Vyasa")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.788")

            elif(x=="Ramayana"):
                self.bookid_var.set("BKID234")
                self.booktitle_var.set("Ramayana")
                self.auther_var.set("Valmiki")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.998")

            elif(x=="The Geeta"):
                self.bookid_var.set("BKID765")
                self.booktitle_var.set("The Geeta")
                self.auther_var.set("Ved Vyasa")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.900")

            elif(x=="Psycology Of Money"):
                self.bookid_var.set("BKID225")
                self.booktitle_var.set("Psycology Of Money")
                self.auther_var.set("Housel Morgan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.879")

            elif(x=="Power Of Thought"):
                self.bookid_var.set("BKID355")
                self.booktitle_var.set("Power Of Thought")
                self.auther_var.set("Swami Mukundananda")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.999")

            elif(x=="The Power Of Subconcious Mind"):
                self.bookid_var.set("BKID945")
                self.booktitle_var.set("The Power Of Subconcious Mind")
                self.auther_var.set("Joseph Murphy")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1000")



        listbox=Listbox(dataframeright,font=("arial",10,"bold"),width=19,height=16)
        listbox.bind("<<ListboxSelect>>",selectbook)
        listbox.grid(row=0,column=0,padx=4)
        listscrolbar.config(command=listbox.yview)

        for item in listboooks:
            listbox.insert(END,item)

        # ___________________buttons frame_________________ #
        framebutton =Frame(self.root,bd=12,relief=RIDGE,padx=1,pady=6,bg="powder blue")
        framebutton.place(x=0,y=514,width=1367,height=70)

        butnaddata=Button(framebutton,text="Add Data",command=self.add_data,font=("arial",12,"bold"),width=22,bg="green",fg="white")
        butnaddata.grid(row=0,column=0)

        butnaddata=Button(framebutton,text="Show Data",command=self.showdata,font=("arial",12,"bold"),width=22,bg="green",fg="white")
        butnaddata.grid(row=0,column=1)

        butnaddata=Button(framebutton,text="Update",command=self.update,font=("arial",12,"bold"),width=22,bg="green",fg="white")
        butnaddata.grid(row=0,column=2)

        butnaddata=Button(framebutton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=22,bg="green",fg="white")
        butnaddata.grid(row=0,column=3)

        butnaddata=Button(framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=22,bg="green",fg="white")
        butnaddata.grid(row=0,column=4)

        butnaddata=Button(framebutton,text="Exit",command=self.iexit,font=("arial",12,"bold"),width=18,bg="green",fg="white")
        butnaddata.grid(row=0,column=5)

         # ___________________information frame_________________ #
        framedetails =Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framedetails.place(x=0,y=584,width=1367,height=135)

        tableframe=Frame(framedetails,bd=6,relief=RIDGE,bg="powder blue")
        tableframe.place(x=0,y=2,width=1287,height=102)

        xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.library_table=ttk.Treeview(tableframe,column=("memebertype","prnno","id","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype",text="Member")
        self.library_table.heading("prnno",text="PRN_No")
        self.library_table.heading("id",text="ID")
        self.library_table.heading("firstname",text="First_Name")
        self.library_table.heading("lastname",text="Last_Name")
        self.library_table.heading("adress1",text="Address1")
        self.library_table.heading("adress2",text="Address2")
        self.library_table.heading("postid",text="Post_ID")
        self.library_table.heading("mobile",text="Mobile_Number")
        self.library_table.heading("bookid",text="Book_ID")
        self.library_table.heading("booktitle",text="Book_Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date_Of_Borrowed")
        self.library_table.heading("datedue",text="Due_Date")
        self.library_table.heading("days",text="Days_On_Book")
        self.library_table.heading("latereturnfine",text="Late_Return_Fine")
        self.library_table.heading("dateoverdue",text="Date_Over_Due")
        self.library_table.heading("finalprice",text="Final_Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("memebertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("id",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_curser)


    def add_data(self):
        # old password W@2915djkq#
        conn = mysql.connector.connect(host="localhost",user="root",password="Root123@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.member_var.get(),
                                                                                           self.prn_var.get(),
                                                                                            self.id_var.get(),
                                                                                     self.firstname_var.get(),
                                                                                      self.lastname_var.get(),
                                                                                      self.address1_var.get(),
                                                                                      self.address2_var.get(),
                                                                                      self.postcode_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.bookid_var.get(),
                                                                                     self.booktitle_var.get(),
                                                                                        self.auther_var.get(),
                                                                                  self.dateborrowed_var.get(),
                                                                                       self.datedue_var.get(),
                                                                                    self.daysonbook_var.get(),
                                                                                  self.lateratefine_var.get(),
                                                                                   self.dateoverdue_var.get(),
                                                                                   self.finallprice_var.get()
        ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Root123@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)

            conn.commit()
        conn.close()
       
    def get_curser(self,evalt=""):
        curser_row=self.library_table.focus()
        content = self.library_table.item(curser_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finallprice_var.set(row[1])

    def showdata(self):
        self.txtbox.insert(END,"Member\t\t"+self.member_var.get() + "\n")
        self.txtbox.insert(END,"PRN_No:\t\t"+self.prn_var.get() + "\n")
        self.txtbox.insert(END,"ID_No:\t\t"+self.id_var.get() + "\n")
        self.txtbox.insert(END,"First_Name\t\t"+self.firstname_var.get() + "\n")
        self.txtbox.insert(END,"Last_Name\t\t"+self.lastname_var.get() + "\n")
        self.txtbox.insert(END,"Address1\t\t"+self.address1_var.get() + "\n")
        self.txtbox.insert(END,"Address2\t\t"+self.address2_var.get() + "\n")
        self.txtbox.insert(END,"Post_Code\t\t"+self.postcode_var.get() + "\n")
        self.txtbox.insert(END,"Mobile_No.\t\t"+self.mobile_var.get() + "\n")
        self.txtbox.insert(END,"Book_ID\t\t"+self.bookid_var.get() + "\n")
        self.txtbox.insert(END,"Book_Title\t\t"+self.booktitle_var.get() + "\n")
        self.txtbox.insert(END,"Auther\t\t"+self.auther_var.get() + "\n")
        self.txtbox.insert(END,"Date_Of_Borrowed\t\t"+self.dateborrowed_var.get() + "\n")
        self.txtbox.insert(END,"Due_Date\t\t"+self.datedue_var.get() + "\n")
        self.txtbox.insert(END,"Days_On_Book\t\t"+self.daysonbook_var.get() + "\n")
        self.txtbox.insert(END,"Late_Return_Fine\t\t"+self.lateratefine_var.get() + "\n")
        self.txtbox.insert(END,"Date_Over_Due\t\t"+self.dateoverdue_var.get() + "\n")
        self.txtbox.insert(END,"Final_Price\t\t"+self.finallprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finallprice_var.set("")
        self.txtbox.delete("1.0",END)

    def iexit(self):
        iexit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if(iexit>0):
            self.root.destroy()
        return
    
    def update(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Root123@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s, ID=%s,First_Name=%s,Last_Name=%s,Address1=%s,Address2=%s,Post_ID=%s,Mobile_Number=%s,Book_ID=%s,Book_Title=%s,Auther=%s,Data_Of_Borrowed=%s,Due_Date=%s,Days_On_Book=%s,Late_Return_Fine=%s,Date_Over_Due=%s,Final_Price=%s where PRN_No=%s",(
                                                                                        self.member_var.get(),
                                                                                            self.id_var.get(),
                                                                                     self.firstname_var.get(),
                                                                                      self.lastname_var.get(),
                                                                                      self.address1_var.get(),
                                                                                      self.address2_var.get(),
                                                                                      self.postcode_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.bookid_var.get(),
                                                                                     self.booktitle_var.get(),
                                                                                        self.auther_var.get(),
                                                                                  self.dateborrowed_var.get(),
                                                                                       self.datedue_var.get(),
                                                                                    self.daysonbook_var.get(),
                                                                                  self.lateratefine_var.get(),
                                                                                   self.dateoverdue_var.get(),
                                                                                   self.finallprice_var.get(),
                                                                                           self.prn_var.get()

        ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Sucess","Member has been updated successfully")

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","Please select the member first")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Root123@",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value = (self.prn_var.get(),)
            # print(value)
            my_cursor.execute(query,value)
            conn.commit()
            self.fatch_data()
            # self.reset()
            conn.close()
            messagebox.showinfo("Sucess","Member has been deleted")

 # ___________________To update fine,date over due,days on book_________________ #
 
    def update_Data(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='mydata',
                user='root',
                password='Root123@'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                
                query = '''
                        SELECT * FROM library
                        '''
                cursor.execute(query)

                records = cursor.fetchall()

                today_date = datetime.date.today()

                for row in records:
                    data = row[12]
                    bk_id = row[2]
                    if(data == ''):
                        continue
                    data = data[0:10]
                    data_date = datetime.datetime.strptime(data, '%Y-%m-%d').date()

                    diff_days = (today_date - data_date).days
                    days_on_book = 15-diff_days
                    late_return_fine = abs(days_on_book)*50

                    if(diff_days > 0):
                        query1 = ''' UPDATE LIBRARY SET Date_Over_Due = "Yes" WHERE ID = {} '''.format(bk_id)
                        cursor.execute(query1)

                        query2 = ''' UPDATE LIBRARY SET Days_On_Book = {1} WHERE ID = {0}  '''.format(bk_id,days_on_book)
                        cursor.execute(query2)

                        query3 = ''' UPDATE LIBRARY SET Late_Return_Fine = {1} WHERE ID = {0}  '''.format(bk_id,late_return_fine)
                        cursor.execute(query3)

                        connection.commit()

        except mysql.connector.Error as error:
            print(f"Error while fetching data from MySQL: {error}")

        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

if __name__== "__main__" :
    root = Tk()
    obj = LibraryManagementSystem(root)
    obj.update_Data()
    root.mainloop()
