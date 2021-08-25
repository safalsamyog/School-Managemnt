from tkinter import *
from tkinter import LabelFrame, ttk
from ttkbootstrap import Style
from tkinter import messagebox as msg
import sqlite3

conn=sqlite3.connect("school7.db")
#cursor=conn.cursor()
#cursor.execute("CREATE TABLE Users (StudentName TEXT,ROll INTEGER ,Class INTEGER,Caste TEXT,FatherName TEXT,MotherName TEXT,PhoneNumber INTEGER,Gender TEXT)")
#conn.close()
style=Style()
window=style.master
window.geometry('1400x700')
window.title('Bhubaneshowari School')
#window.attributes('-fullscreen',True)
# window.resizable(False,False)
d1=StringVar()
d2=StringVar()
d3=StringVar()
d4=StringVar()
d5=StringVar()
d6=StringVar()
d7=StringVar()
d8=StringVar()


def add():
  try:
    if (d1.get()=='') or d2.get()=='' or d3.get()=='' or d4.get()=='' or d5.get()=='' or d6.get()=='' or d7.get()=='' or d8.get()=='':
      msg.showwarning('Value Error','All filed are reuired to input. So plz enter all values')
    elif int(d2.get())==str(d2.get()) or int(d3.get())==str(d3.get()) or int(d7.get())==str(d7.get()):
     pass

    else:
      conn=sqlite3.connect("school7.db")
      cursor=conn.cursor()
      cursor.execute("INSERT INTO Users (StudentName,ROll,Class,Caste,FatherName,MotherName,PhoneNumber,Gender)  values(?,?,?,?,?,?,?,?)",(d1.get(),d2.get(),d3.get(),d4.get(),d5.get(),d6.get(),d7.get(),d8.get()))
   
      cursor.execute("SELECT*FROM Users")
      users=cursor.fetchall()
      for row in users:
        a,b,c,d,e,f,g,h=row
      std.insert(parent='',index=END,values=(a,b,c,d,e,f,g,h))   
      conn.commit()
      ff()
      cursor.close()
      conn.close()
    
    
      msg.showinfo('Success','Sucessfully Added :)') 
  except:
     msg.showwarning('error','Dont add text in numeric field or numner in text field ')
   

def ff():
  conn=sqlite3.connect("school7.db")
  cursor=conn.cursor()
   
  cursor.execute("SELECT*FROM Users")
  users=cursor.fetchall()
  if len(users)!=0:
    std.delete(*std.get_children())
    for row in users:
    # a,b,c,d,e,f,g,h=row
     std.insert(parent='',index=END,values=row)
    conn.commit()
  cursor.close()
  conn.close()

def get_cursor(e):

  cursor_row=std.focus()
  content=std.item(cursor_row)
  row=content['values']
  d1.set(row[0])
  d2.set(row[1])
  d3.set(row[2])
  d4.set(row[3])
  d5.set(row[4])
  d6.set(row[5])
  d7.set(row[6])
  d8.set(row[7])
      
def clr():
  d1.set('')
  d2.set('')
  d3.set('')
  d4.set('')
  d5.set('')
  d6.set('')
  d7.set('')
  d8.set('')
  
def d():
  conn=sqlite3.connect("school7.db")
  cursor=conn.cursor()
      
  cursor.execute("DELETE FROM Users WHERE ROll=%s"%d2.get())
  conn.commit()
  msg.showinfo('Sucess','Sucessfully deleted')
  conn.close()

  ff()
  clr()
 

def update():
  conn=sqlite3.connect("school7.db")
  cursor=conn.cursor()
  cursor.execute("UPDATE Users SET StudentName=?,Class=?,Caste=?,FatherName=?,MotherName=?,PhoneNumber=?,Gender=? WHERE ROll=?",(d1.get(),d3.get(),d4.get(),d5.get(),d6.get(),d7.get(),d8.get(),d2.get()))
  conn.commit()
  msg.showinfo('Sucess','Sucessfully Updated')
  conn.close()
 
  ff()
  clr()

def view():
  ll1=ttk.Label(frame5,text='Name :').place(x=120*8.8,y=10*6.6)
  g1=ttk.Label(frame5,text=d1.get()).place(x=120*9.4,y=10*6.6)
  ll2=ttk.Label(frame5,text='Roll :').place(x=120*8.8,y=10*8.9)
  g2=ttk.Label(frame5,text=d2.get()).place(x=120*9.4,y=10*8.9)
  ll3=ttk.Label(frame5,text='Class :').place(x=120*8.8,y=10*11.5)
  g3=ttk.Label(frame5,text=d3.get()).place(x=120*9.4,y=10*11.5)
  ll4=ttk.Label(frame5,text='Caste : ').place(x=120*8.8,y=10*14.2)
  g4=ttk.Label(frame5,text=d4.get()).place(x=120*9.4,y=10*14.2) 
  ll5=ttk.Label(frame5,text='Father Name :').place(x=120*8.8,y=10*16.5)
  g5=ttk.Label(frame5,text=d5.get()).place(x=120*9.8,y=10*16.5)
  ll6=ttk.Label(frame5,text='Mother Name :').place(x=120*8.8,y=10*18.9)
  g6=ttk.Label(frame5,text=d6.get()).place(x=120*9.8,y=10*18.9) 
  ll7=ttk.Label(frame5,text='Phone No. :').place(x=120*8.8,y=10*21.3)
  g7=ttk.Label(frame5,text=d7.get()).place(x=120*9.6,y=10*21.3) 
  ll8=ttk.Label(frame5,text='Gender :').place(x=120*8.8,y=10*23.8)
  g8=ttk.Label(frame5,text=d8.get()).place(x=120*9.4,y=10*23.7)
 


frame1=ttk.Labelframe(window, text='Student Detail', style='TLabelframe').place(x=30,y=10,width=1307,height=720)
frame2=ttk.Labelframe(frame1, text='Detail Input', style='TLabelframe').place(x=40*2,y=10*3.2,width=930,height=190)
label1=ttk.Label(frame2,text='Student Name').place(x=40*3,y=10*7)
e1=ttk.Entry(frame2, style='info.TEntry',textvariable=d1).place(x=40*5.3,y=10*6.5,width=120,height=28)
label2=ttk.Label(frame2,text='Student Roll').place(x=40*9,y=10*7)
e2=ttk.Entry(frame2, style='info.TEntry',textvariable=d2).place(x=40*11.2,y=10*6.5,width=106,height=28)
label3=ttk.Label(frame2,text='Class').place(x=40*14.4,y=10*7)
e3=ttk.Entry(frame2, style='info.TEntry',textvariable=d3).place(x=40*15.8,y=10*6.5,width=120,height=28)
label4=ttk.Label(frame2,text='Caste').place(x=40*19.9,y=10*7)
e4=ttk.Entry(frame2, style='info.TEntry',textvariable=d4).place(x=40*21.6,y=10*6.5,width=130,height=28)
label5=ttk.Label(frame2,text='Fathers Name').place(x=40*3,y=10*14)
e5=ttk.Entry(frame2, style='info.TEntry',textvariable=d5).place(x=40*5.4,y=10*13.5,width=140,height=28)
label6=ttk.Label(frame2,text='Mothers Name').place(x=40*9.2,y=10*14)
e6=ttk.Entry(frame2, style='info.TEntry',textvariable=d6).place(x=40*11.7,y=10*13.5,width=130,height=28)
label7=ttk.Label(frame2,text='Phone Number').place(x=40*15.4,y=10*14)
e7=ttk.Entry(frame2, style='info.TEntry',textvariable=d7).place(x=40*17.8,y=10*13.5,width=130,height=28)
label8=ttk.Label(frame2,text='Gender').place(x=40*21.2,y=10*14)
# e8=ttk.Entry(frame2, style='info.TEntry').place(x=40*22.5,y=10*13.5,width=100,height=28)
c1=ttk.Combobox(frame2,value=['Male','Female'],style='info.TCombobox',textvariable=d8).place(x=40*22.5,y=10*13.5,width=100,height=28)


frame3=ttk.Labelframe(frame1, text='Student data', style='TLabelframe').place(x=40*2,y=50*4.8,width=935,height=268)
scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
scroll_y=Scrollbar(frame3,orient=VERTICAL)

std = ttk.Treeview(frame3,columns=('Student Name', 'Roll', 'Class', 'Caste','Fathers Name','Mothers Name','Phone Number','Gender'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,style='danger.Treeview')
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=std.xview)
scroll_y.config(command=std.yview)

std.heading('Student Name',text='Student Name',anchor=W)
std.heading('Roll',text='Roll')
std.heading('Class',text='Class')
std.heading('Caste',text='Caste')
std.heading('Fathers Name',text='Fathers Name')
std.heading('Mothers Name',text='Mothers Name')
std.heading('Phone Number',text='Phone Number')
std.heading('Gender',text='Gender')
std['show']='headings'
std.column('Student Name',width=120,anchor=CENTER)
std.column('Roll',width=120,anchor=CENTER)
std.column('Class',width=120,anchor=CENTER)
std.column('Caste',width=120,anchor=CENTER)
std.column('Fathers Name',width=120,anchor=CENTER)
std.column('Mothers Name',width=120,anchor=CENTER)
std.column('Phone Number',width=120,anchor=CENTER)
std.column('Gender',width=120,anchor=CENTER)
std.bind("<ButtonRelease-1>",get_cursor)
ff() 
std.place(x=40*2.8,y=50*5.3,height=218/2+120,width=870)

frame4=ttk.Labelframe(frame1, text='Work', style='TLabelframe').place(x=40*2,y=70*7.5,width=1200,height=100)
btn1=ttk.Button(frame4,text='Add',style='info.TButton',command=add).place(x=40*3,y=70*8.1,width=100,height=35)
btn2=ttk.Button(frame4,text='Edit',style='info.Outline.TButton',command=update).place(x=40*6,y=70*8.1,width=100,height=35)
btn3=ttk.Button(frame4,text='Delete',style='info.Outline.TButton',command=d).place(x=40*9,y=70*8.1,width=100,height=35)
btn4=ttk.Button(frame4,text='CLear',style='danger.TButton',command=clr).place(x=40*(18+9)/2+40,y=70*8.1,width=100,height=35)
btn6=ttk.Button(frame4,text='View',style='danger.TButton',command=view).place(x=40*18,y=70*8.1,width=100,height=35)
#btn7=ttk.Button(frame4,text='Sort',style='danger.Outline.TButton').place(x=40*21.5,y=70*8.1,width=100,height=35)
btn8=ttk.Button(frame4,text='Exit',style='success.TButton',command=window.quit).place(x=40*26.5,y=70*8.1,width=100,height=35)

frame5=ttk.Labelframe(frame1, text='view', style='TLabelframe').place(x=120*8.5,y=10*3,width=300,height=320)
frame5=ttk.Labelframe(frame5, style='TLabelframe').place(x=120*8.65,y=10*5,width=260,height=280)
ll=ttk.Label(frame5,text='Enter the Name for Search',foreground='red').place(x=120*8.8,y=40*9)
s1=ttk.Entry(frame5,style='danger.TEntry').place(x=120*8.8,y=40*9.8,height=30,width=150)
s11=ttk.Button(frame1,text='Search',style='info.TButton').place(x=120*10.1,y=40*9.8,width=100,height=30)
lastbtn=ttk.Button(frame1,text='Detail Page',style='primary.TButton').place(x=120*8.8,y=40*11.3,height=50,width=230)

window.mainloop()

