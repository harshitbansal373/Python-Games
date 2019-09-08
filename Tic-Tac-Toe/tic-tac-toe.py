from tkinter import *
import tkinter.messagebox
root=Tk()
root.title('tic-tac-toe')
root.config(bg='#fffaaa')
img1=PhotoImage(file='o.png')
img2=PhotoImage(file='x.png')

def intial():
  global lb
  for i in range(3):
    for j in range(3):
      lb.append(Button(root,bg='#abcdef',height=15,width=30,state='disable',command=lambda t=(i,j):solve(t)))
      lb[-1].grid(row=i,column=j,padx=5,pady=5,sticky='nswe')

def start():
  global lb
  global sb
  sb['state']='disable'
  for b in lb:
    b['state']='active'

def restart():
  global sc1
  global sc2
  global pl1
  global pl2
  sc1=0
  sc2=0
  pl1['text']='Player1 : 0'
  pl2['text']='Player2 : 0'
  reset()

def reset():
  global lb
  global sb
  global p
  global p1
  global p2
  global count
  lb=[]
  p=True
  p1.clear()
  p2.clear()
  count=0
  sb['state']='active'
  intial()

def check():
  global sc1
  global sc2
  global pl1
  global pl2
  win=[{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{6,4,2}]
  if p==True:
    for s in win:
      if s<=p2:
        tkinter.messagebox.showinfo('Result','Player2 won!!!')
        sc2=sc2+1
        pl2['text']='Player2 : '+str(sc2)
        reset()
  else:
    for s in win:
      if s<=p1:
        tkinter.messagebox.showinfo('Result','Player1 won!!!')
        sc1=sc1+1
        pl1['text']='Player1 : '+str(sc1)
        reset()
  if count==9:
    tkinter.messagebox.showinfo('Result','Draw')
    reset()

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
count=0
p=True
p1=set()
p2=set()
sc1=0
sc2=0
intial()

f=Frame(root)
pl1=Label(f,text='Player1 : 0',bg='#abcdef',height=5)
pl1.pack(side='left',padx=5,pady=5,expand=YES,fill=BOTH)
sb=Button(f,text='Start',bg='#abcdef',height=5,command=start)
sb.pack(side='left',padx=5,pady=5,expand=YES,fill=BOTH)
rb=Button(f,text='Restart',bg='#abcdef',height=5,command=restart)
rb.pack(side='left',padx=5,pady=5,expand=YES,fill=BOTH)
pl2=Label(f,text='Player2 : 0',bg='#abcdef',height=5)
pl2.pack(side='left',padx=5,pady=5,expand=YES,fill=BOTH)
f.grid(row=3,column=0,columnspan=3,sticky='nswe')

for i in range(3):
  root.grid_rowconfigure(i,weight=1)
  root.grid_columnconfigure(i,weight=1)
root.mainloop()
