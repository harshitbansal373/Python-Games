from tkinter import *
import tkinter.messagebox
root=Tk()
root.title('tik-tak-toe')
root.config(bg='#fffaaa')
img1=PhotoImage(file='o.png')
img2=PhotoImage(file='x.png')

lb=[]
flag=True
p=True
p1=set()
p2=set()
count=0
intial()
sb=Button(root,width=10,height=5,text='start',bg='#abcdef',command=start)
sb.grid(row=3,column=1,padx=5,pady=5,sticky='nswe')

for i in range(3):
  root.grid_rowconfigure(i,weight=1)
  root.grid_columnconfigure(i,weight=1)
root.mainloop()
