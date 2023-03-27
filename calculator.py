from tkinter import *
from math import *
root=Tk()
root.geometry("360x450")
root.configure(bg="#778899")
def press(s):
    t.insert(END,s)    
def clear():
    t.delete(1.0,END)
    t1.delete(1.0,END)
def expression():
    exp=t.get(1.0,END)
    t.delete(1.0,END)
    t1.delete(1.0,END)
    t1.insert(END,exp)
    exp=eval(exp)
    t.insert(END,'\n'+str(exp))  
def percentage():
    exp=t.get(1.0,END)
    if '+' in exp:
        exp1=exp.split('+')
        ans=1/float(exp1[0])
        exp1=exp1[0]
        ans=f"{exp1}+{str(ans)}"
        print(ans)
        t.delete(1.0,END)
        t.insert(END,ans)
    elif '-' in exp:
        exp1=exp.split('-')
        ans=1/float(exp1[0])
        exp1=exp1[0]
        ans=f"{exp1}-{str(ans)}"
        print(ans)
        t.delete(1.0,END)
        t.insert(END,ans)
    elif '*' in exp:
        exp1=exp.split('*')
        ans=1/float(exp1[0])
        exp1=exp1[0]
        ans=f"{exp1}*{str(ans)}"
        print(ans)
        t.delete(1.0,END)
        t.insert(END,ans)
    elif '/' in exp:
        exp1=exp.split('/')
        ans=1/float(exp1[0])
        exp1=exp1[0]
        ans=f"{exp1}/{str(ans)}"
        print(ans)
        t.delete(1.0,END)
        t.insert(END,ans)

def square():
    exp=t.get(1.0,END)
    ans=pow(float(exp),2)
    t.delete(1.0,END)
    t.insert(END,ans)
def backspace():
    global exp
    exp=t.get(1.0,END)
    t2=exp[0:len(exp)-2]
    t.delete(1.0,END)
    t.insert(END,str(t2))   
def square_root():
    exp=t.get(1.0,END)
    ans=sqrt(float(exp))
    t.delete(1.0,END)
    t.insert(END,ans)
def decimal():
    exp=t.get(1.0,END)
    t.delete(1.0,END)
    ans=1/int(exp)
    t.insert(END,ans)
def plusminus():
    t1.delete(1.0,END)
    exp=int(t.get(1.0,END))
    t1.insert(END,exp)
    t.delete(1.0,END)
    exp*=-1
    t.insert(END,exp)
#text t1 for display and text t for calculation   
t1=Text(root,bg='#778899',width=40,height=2,bd=0)
t1.grid(row=0,column=0,columnspan=4,sticky=NSEW)
t=Text(root,bg='#778899',width=45,height=5,bd=0)
t.grid(row=1,column=0,rowspan=3,columnspan=4,sticky=NSEW,padx=0,pady=0)
b1=Button(root,text="7",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("7"))
b1.grid(row=5,column=0,sticky=NSEW)
Button(root,text='_|x',fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:square_root()).grid(row=4,column=0,sticky=NSEW)
Button(root,text="8",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("8")).grid(row=5,column=1,sticky=NSEW)
Button(root,text="9",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("9")).grid(row=5,column=2,sticky=NSEW)
Button(root,text="4",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("4")).grid(row=6,column=0,sticky=NSEW)
Button(root,text="/",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("/")).grid(row=4,column=3,sticky=NSEW)
Button(root,text="5",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("5")).grid(row=6,column=1,sticky=NSEW)
Button(root,text="6",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("6")).grid(row=6,column=2,sticky=NSEW)
Button(root,text="+/-",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:plusminus()).grid(row=7,column=3,sticky=NSEW)
Button(root,text="x",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("*")).grid(row=5,column=3,sticky=NSEW)
Button(root,text="1",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("1")).grid(row=7,column=0,sticky=NSEW)
Button(root,text="2",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("2")).grid(row=7,column=1,sticky=NSEW)
Button(root,text="3",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("3")).grid(row=7,column=2,sticky=NSEW)
Button(root,text="-",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("-")).grid(row=6,column=3,sticky=NSEW)
Button(root,text=".",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press(".")).grid(row=8,column=0,sticky=NSEW)
Button(root,text="0",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("0")).grid(row=8,column=1,sticky=NSEW)
Button(root,text="+",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:press("+")).grid(row=8,column=2,sticky=NSEW)
Button(root,text="=",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=expression).grid(row=8,column=3,rowspan=2,sticky=NSEW)
Button(root,text="C",fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=clear).grid(row=9,column=0,sticky=NSEW)
Button(root,text='x2',fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:square()).grid(row=4,column=2,sticky=NSEW)
Button(root,text='<--',fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:backspace()).grid(row=9,column=1,columnspan=2,sticky=NSEW)
Button(root,text='1/x',fg="#ffffff",bg="black",width=1,height=3,padx=1,pady=1,command=lambda:percentage()).grid(row=4,column=1,sticky=NSEW)

root.mainloop()