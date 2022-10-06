import tkinter
import datetime
import string
info={}
def calc1(month,date,year):
    dayss=0
    if month in [1,3,5,7,8,10,12]:
        dayss=31
    elif month in[4,6,9,11]:
        dayss=30
    if month==2:
        if (year%4==0 and year%100!=0)or year%400==0:
            dayss=29
        else:
            dayss=28
    if date<=dayss and month<=12:
        return dayss,True
    else:
        return dayss,False
def past():
    
    f1=open("data.txt","r")
    lines=f1.readlines()
    f1.close()
    f1=open("data.txt","w")
    for i in lines:
        a=i.split()[1]
        b=a.split("/")
        d=int(b[0])
        m=int(b[1])
        y=int(b[2])
        present1=datetime.date.today()
        D=present1.day-d
        M=present1.month-m
        Y=present1.year-y
        if D<0:
            if M<0 and Y>=0:
                f1.write(i)
            elif M>0 and Y<0:
                f1.write(i)
        elif D>=0:
            if M<0 and Y<=0:
                f1.write(i)
            elif M>0 and Y<0:
                f1.write(i)
        textArea=tkinter.Text(window,height=3,width=20,font=("Copperplate Gothic Bold",12))
        textArea.grid(column=1,columnspan=3,row=11)
        textArea.insert(tkinter.END,"Successfully Deleted")
def add_event():
    new=tkinter.Toplevel(window)
    new.title("SAVE")
    new.configure(background='skyblue')
    new.geometry("463x600")
    new.resizable(0,0)
    label1=tkinter.Label(new,text="NAME          :",font=("ALGERIAN",18),bg="skyblue")
    label1.grid(column=0,row=2)
    label1=tkinter.Label(new,text="DATE(dd/mm/yyyy):",font=("ALGERIAN",18),bg="skyblue")
    label1.grid(column=0,row=3)
    label1=tkinter.Label(new,text="DETAILS       :",font=("ALGERIAN",18),bg="skyblue")
    label1.grid(column=0,row=4)
    NameEntry=tkinter.Entry(new,width=35)
    NameEntry.grid(column=1,columnspan=3,row=2)
    DateEntry=tkinter.Entry(new,width=8)
    DateEntry.grid(column=1,row=3)
    MonthEntry=tkinter.Entry(new,width=8)
    MonthEntry.grid(column=2,row=3)
    YearEntry=tkinter.Entry(new,width=17)
    YearEntry.grid(column=3,row=3)
    DetailEntry=tkinter.Entry(new,width=35)
    DetailEntry.grid(column=1,columnspan=3,row=4)
    def insert():
        global info
        try:
            Name=NameEntry.get()
            Date=int(DateEntry.get())
            Month=int(MonthEntry.get())
            Year=int(YearEntry.get())
            Details=DetailEntry.get()
        except:
            textArea=tkinter.Text(new,height=3,width=12,font=("Copperplate Gothic Bold",12))
            textArea.grid(column=1,columnspan=3,row=6)
            textArea.insert(tkinter.END,"Invalid Inputs")
        else:
            textArea=tkinter.Text(new,height=3,width=12,font=("Copperplate Gothic Bold",12))
            textArea.grid(column=1,columnspan=3,row=6)
            if type(Year)==int:
                    a,b=calc1(Month,Date,Year)
                    if b:
                        date=str(Date)+"/"+str(Month)+"/"+str(Year)
                        info[Name]=(date,Details)
                        textArea.insert(tkinter.END,"Successfully saved")
                        try:
                            f1=open("data.txt","a+")
                        except:
                            f1=open("data.txt","w")
                            f1.close()
                            f1=open("data.txt","a+")
                        else:
                            f1.write(Name+" "+date+" "+Details+"\n")
                            f1.close()
                    else:
                        textArea.insert(tkinter.END,"Invalid Date")
            else:
                    textArea.insert(tkinter.END,"Invalid Date")
    Button1=tkinter.Button(new,text="SAVE",command=insert,font=("ALGERIAN",14),bg="purple",fg="white").grid(column=1,columnspan=3,row=5)
def view():
    new=tkinter.Toplevel(window)
    new.title("VIEW")
    new.configure(background='skyblue')
    new.geometry("463x600")
    new.resizable(0,0)
    def display():
        new1=tkinter.Toplevel(new)
        new1.title("VIEW")
        new1.configure(background='skyblue')
        new1.geometry("463x600")
        textArea1=tkinter.Text(new1,height=100,width=100,font=("Copperplate Gothic Bold",12))
        textArea1.grid(columnspan=2,rowspan=3)
        global info
        f1=open("data.txt","r")
        for i in f1:
            textArea1.insert(tkinter.END,i)
    Button1=tkinter.Button(new,text="VIEW ALL",command=display,font=("ALGERIAN",20),width=27)
    Button1.grid(column=1,row=3)
    def displaybydate():
        new1=tkinter.Toplevel(new)
        new1.title("VIEW")
        new1.configure(background='skyblue')
        new1.geometry("463x600")
        global info
        label1=tkinter.Label(new1,text="DATE(dd/mm/yy):",font=("ALGERIAN",14))
        label1.grid(column=0,row=3)
        DateEntry=tkinter.Entry(new1,width=11)
        DateEntry.grid(column=1,row=3)
        MonthEntry=tkinter.Entry(new1,width=11)
        MonthEntry.grid(column=2,row=3)
        YearEntry=tkinter.Entry(new1,width=17)
        YearEntry.grid(column=3,row=3)
        def Display():
            try:
                Date=int(DateEntry.get())
                Month=int(MonthEntry.get())
                Year=int(YearEntry.get())
            except:
                textArea=tkinter.Text(new1,height=3,width=12,font=("Copperplate Gothic Bold",12))
                textArea.grid(column=1,columnspan=3,row=6)
                textArea.insert(tkinter.END,"Invalid Inputs")
            else:
                new2=tkinter.Toplevel(new)
                date=str(Date)+"/"+str(Month)+"/"+str(Year)
                new2.title("VIEW")
                new2.configure(background='skyblue')
                new2.geometry("463x600")
                textArea=tkinter.Text(new2,height=100,width=100,font=("Copperplate Gothic Bold",12))
                textArea.grid(columnspan=2,row=6)
                f1=open("data.txt","r")
                for i in f1:
                    if i.split()[1]==date:
                        textArea.insert(tkinter.END,i)
                textArea.insert(tkinter.END,"No Further Matches")
        Button1=tkinter.Button(new1,text="VIEW",command=Display,font=("ALGERIAN",14),bg="purple",fg="white")
        Button1.grid(column=1,row=5)
    Button1=tkinter.Button(new,text="VIEW BY DATE",command=displaybydate,font=("ALGERIAN",20),width=27)
    Button1.grid(column=1,row=5)
    def displaybyname():
        new1=tkinter.Toplevel(new)
        new1.title("VIEW")
        new1.configure(background='skyblue')
        new1.geometry("463x600")
        new1.resizable(0,0)
        label1=tkinter.Label(new1,text="NAME :",font=("ALGERIAN",18),bg="skyblue")
        label1.grid(column=0,row=3)
        global info
        NameEntry=tkinter.Entry(new1,width=40)
        NameEntry.grid(column=1,columnspan=3,row=3)
        def Display1():
            try:
                Name=NameEntry.get()
            except:
                textArea=tkinter.Text(new1,height=3,width=12,font=("Copperplate Gothic Bold",12))
                textArea.grid(column=1,columnspan=3,row=6)
                textArea.insert(tkinter.END,"Invalid Inputs")
            else:
                new2=tkinter.Toplevel(new)
                new2.title("VIEW")
                new2.geometry("463x600")
                new2.configure(background='skyblue')
                textArea=tkinter.Text(new2,height=100,width=100,font=("Copperplate Gothic Bold",12))
                textArea.grid(columnspan=2,row=6)
                f1=open("data.txt","r")
                for i in f1:
                    if str.lower(i.split()[0])==str.lower(Name):
                        textArea.insert(tkinter.END,i)
                textArea.insert(tkinter.END,"No Further Matches")
        Button1=tkinter.Button(new1,text="VIEW",command=Display1,font=("ALGERIAN",14),bg="purple",fg="white")
        Button1.grid(column=1,row=5)
    Button1=tkinter.Button(new,text="VIEW BY EVENT NAME",command=displaybyname,font=("ALGERIAN",20),width=27)
    Button1.grid(column=1,row=7)
def remove_event():
    new=tkinter.Toplevel(window)
    new.title("DELETE")
    new.configure(background='skyblue')
    new.geometry("463x600")
    new.resizable(0,0)
    label1=tkinter.Label(new,text="EVENT NAME         :",font=("ALGERIAN",18),bg="skyblue")
    label1.grid(column=0,row=2)
    NameEntry=tkinter.Entry(new,width=40)
    NameEntry.grid(column=1,columnspan=3,row=2)
    def delete():
        try:
            Name=NameEntry.get()
        except:
            textArea=tkinter.Text(new,height=3,width=12,font=("Copperplate Gothic Bold",12))
            textArea.grid(column=1,columnspan=3,row=6)
            textArea.insert(tkinter.END,"Invalid Inputs")
        else:
            f1=open("data.txt","r")
            f=f1.readlines()
            f1.close()
            f1=open("data.txt","w")
            for i in f:
                if str.lower(i.split()[0])!=str.lower(Name):
                    f1.write(i)
            textArea=tkinter.Text(new,height=3,width=20,font=("Copperplate Gothic Bold",12))
            textArea.grid(column=1,columnspan=3,row=4)
            if str.lower(i.split()[0])==str.lower(Name):
                textArea.insert(tkinter.END,"Successfully Deleted")
            else:
                textArea.insert(tkinter.END,"Doesn't Exist")
    Button1=tkinter.Button(new,text="DELETE",command=delete,font=("ALGERIAN",14),bg="purple",fg="white")
    Button1.grid(column=1,columnspan=3,row=3)
window=tkinter.Tk()
window.title("EVENT DETAILS")
window.configure(background="purple")
window.geometry("463x600")
window.resizable(0,0)
icon=tkinter.PhotoImage(file="events3.png")
label1=tkinter.Label(window,image=icon)
label1.grid(columnspan=6,rowspan=4)
Button1=tkinter.Button(window,text="ADD_EVENT",command=add_event,font=("ALGERIAN",22),bg="white",width=25).grid(column=1,columnspan=3,row=6)
Button2=tkinter.Button(window,text="REMOVE_EVENT",command=remove_event,font=("ALGERIAN",22),bg="white",width=25).grid(column=1,columnspan=3,row=7)
Button3=tkinter.Button(window,text="VIEW_EVENT",command=view,font=("ALGERIAN",22),bg="white",width=25).grid(column=1,columnspan=3,row=8)
Button4=tkinter.Button(window,text="DELETE_PAST_EVENT",command=past,font=("ALGERIAN",22),bg="white",width=25).grid(column=1,columnspan=3,row=9)





