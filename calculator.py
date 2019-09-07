from tkinter import *
import time
root=Tk()
root.title('Calculator')
root.config(bg='wheat')
s=''
text=StringVar()
f=Frame(root,bg='#dcdde1')
e=Entry(f,textvariable=text,bg='#f5f6fa',fg='#353b48',font='roboto 34 bold',justify='right',relief=RAISED)
e.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
f.pack(side=TOP,padx=10,pady=10,expand=YES,fill=BOTH)

root.mainloop()
