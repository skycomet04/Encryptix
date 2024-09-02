import tkinter as tk
import random as rn
import string
class password():
    def __init__(self):
        self.win=tk.Tk()
        width=520
        height=450
        self.screen_wh = self.win.winfo_screenwidth()  # Width of the screen
        self.screen_ht = self.win.winfo_screenheight() # Height of the screen
        x = (self.screen_wh/2) - (width/2)
        y = (self.screen_ht/2) - (height/2)
        
        self.win.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.win.configure(bg="white")
        self.win.resizable(0,0)
        tk.Label(self.win,text="WELCOME TO PASSWORD GENERATOR",bg="white",fg="#add8e6",font=("Elephant",20),wraplength=500).place(x=40,y=10)
    def generate_password(self):
        self.fpass.delete(0,tk.END)
        if self.length.get()<4:
            self.final_password.set("Length should be atleast 4")
        elif self.selected.get()=="Easy":
            self.password="".join(rn.choices(string.ascii_letters,k=self.length.get()))
            self.fpass.insert(0,f"{self.password}")
        elif self.selected.get()=="Difficult":    
            self.special=["@","#","&","*","-","!"]
            self.password=rn.choices(string.ascii_letters,k=self.length.get()-3)
            self.password+=rn.choice(self.special)
            self.digit=rn.choices(string.digits,k=2)
            self.password+=self.digit
            rn.shuffle(self.password)
            self.final_pass="".join(self.password)
            self.final_password.set(f"{self.final_pass}")

    def input(self):
        self.length=tk.IntVar()
        self.selected = tk.StringVar()
        self.final_password=tk.StringVar()
        self.label=tk.Label(self.win,text="Enter the length of the passsword to be created ",bg="white",fg="#add8e6",font=("TimesNewRoman",16),wraplength=380)
        self.label.place(x=1,y=120,height=60,width="460")
        self.pass_length=tk.Entry(self.win,textvariable=self.length,borderwidth=0)
        self.pass_length.configure(font=("TimesNewRoman",16))
        self.pass_length.place(x=460,y=120,width=60,height=60)
        self.r1 = tk.Radiobutton(self.win, text='Easy', value='Easy',bg="white",fg="#add8e6", variable=self.selected,font=("TimesNewRoman",16))
        self.r1.place(x=3,y=195,height="60")
        self.r2 = tk.Radiobutton(self.win, text='Difficult', value='Difficult',bg="white", fg="#add8e6",variable=self.selected,font=("TimesNewRoman",16))
        self.r2.place(x=80,y=195,height="60")
        b1= tk.Button(self.win,text="Generate Password",bg="dark blue",fg="#add8e6",command=self.generate_password,font=("TimesNewRoman",16))
        b1.place(x=150,y=255,width=200,height=70)
        self.fpass=tk.Entry(self.win,textvariable=self.final_password)
        self.fpass.configure(font=("TimesNewRoman",18))
        self.fpass.place(x=120,y=335,height=50,width=300)
        self.win.mainloop()
pg=password()
pg.input()