from tkinter import *
root=Tk()
root.title('Guess Table')
root.config(bg='sky blue')
def display(t):
  b=Label(root,text=(t[0]+1)*(t[1]+1),bg='#fffaaa',fg='black',font='arial 34 italic')
  b.grid(row=t[0],column=t[1],padx=10,pady=10,sticky='nswe')

for i in range(1,11):
  b=Label(root,text=str(i),bg='#fffaaa',fg='black',font='arial 35 italic')
  b.grid(row=0,column=i-1,padx=10,pady=10,sticky='nswe')
for i in range(1,10):
  b=Label(root,text=str(i+1),bg='#fffaaa',fg='black',font='arial 35 italic')
  b.grid(row=i,column=0,padx=10,pady=10,sticky='nswe')
for i in range(1,10):
  for j in range(1,10):
    b=Button(root,text='?',bg='#fffaaa',fg='black',font='arial 34 italic',command=lambda t=(i,j):display(t))
    b.grid(row=i,column=j,padx=10,pady=10,sticky='nswe')
for i in range(10):
  root.grid_rowconfigure(i,weight=1)
  root.grid_columnconfigure(i,weight=1)
root.mainloop()
