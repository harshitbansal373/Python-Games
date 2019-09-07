from tkinter import *
root=Tk()
root.title('Guess Table')
root.config(bg='sky blue')
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
root.mainloop()
