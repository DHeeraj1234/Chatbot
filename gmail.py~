from Tkinter import *
import smtplib
import getpass

root = Tk(className ="My first GUI")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
foo = Label(root,text="Sender Email:")
foo.pack()
unm = StringVar()
foo1 = Label(root,text="Password")

pwd = StringVar()
foo2 = Label(root,text="Message")

m1 = StringVar()
foo3 = Label(root,text="Receiver Email")
r1=StringVar()
#svalue = StringVar() # defines the widget state as string
w = Entry(root,textvariable=unm)
x = Entry(root,textvariable=pwd)
m = Entry(root,textvariable=m1)
r=Entry(root,textvariable=r1) 
 # adds a textarea widget
#print(svalue.get())
w.pack()
foo1.pack()
x.pack()
foo2.pack()
m.pack()
foo3.pack()
r.pack()
foo4 = Label(root,text="Sent Succesfully")
def act():
    global s
    global unm
    global r1
    global m1
    global pwd	
    global foo4
    s.login(unm.get(),pwd.get())
    print "you entered"
    print '%s' % unm.get()
    s.sendmail(unm.get(), r1.get(), m1.get())
    foo4.pack()	
    # terminating the session
    s.quit()


foo = Button(root,text="Press Me", command=act)
foo.pack()
root.mainloop()
