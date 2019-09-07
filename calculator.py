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

l=['#aabbcc','#bbccdd','#ccddee','#ddeeff']
for i in ['789/','456*','123+','.0-=']:
  f=Frame(root,bg=l.pop())
  for j in i:
    b=Button(f,text=j,bg='#00a8ff',fg='#353b48',font='roboto 34 italic',command=(lambda x=j:display(x)) if j!='=' else solve)
    b.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
  f.pack(side=TOP,padx=10,pady=10,expand=YES,fill=BOTH)

f1=Frame(root,bg='#dcdde1')
clear=Button(f1,text='C',bg='#00a8ff',fg='#353b48',font='Roboto 34',command=clear)
clear.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
clear1=Button(f1,text='CE',bg='#00a8ff',fg='#353b48',font='Roboto 34',command=clear1)
clear1.pack(side=LEFT,padx=10,pady=10,expand=YES,fill=BOTH)
f1.pack(side=TOP,padx=10,pady=10,expand=YES,fill=BOTH)

root.mainloop()
