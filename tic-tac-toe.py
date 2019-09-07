from tkinter import *
import tkinter.messagebox
root=Tk()
root.title('tik-tak-toe')
root.config(bg='#fffaaa')
img1=PhotoImage(file='o.png')
img2=PhotoImage(file='x.png')

def solve(t):
  global p
  global count
  global p1
  global p2
  i=t[0]*3+t[1]
  b=lb[i]
  b['state']='disable'
  count=count+1
  if p==True:
    b['image']=img1
    p1.add(i)
    p=False
  else:
    b['image']=img2
    p2.add(i)
    p=True
  if count>=5:
    check()

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
