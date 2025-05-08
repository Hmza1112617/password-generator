import tkinter as tk
from tkinter import ttk
import random,string,pyperclip
class PasswordGenerator:
    def __init__(self,root):
        self.root=root
        self.root.title("مولد كلمات المرور")
        self.root.geometry("400x500")
        self.password_length=tk.IntVar(value=12)
        self.include_uppercase=tk.BooleanVar(value=True)
        self.include_numbers=tk.BooleanVar(value=True)
        self.include_symbols=tk.BooleanVar(value=True)
        self.setup_ui()
    def setup_ui(self):
        main_frame=ttk.Frame(self.root,padding="20")
        main_frame.grid(row=0,column=0,sticky=(tk.W,tk.E,tk.N,tk.S))
        ttk.Label(main_frame,text="مولد كلمات المرور",font=("Arial",16,"bold")).grid(row=0,column=0,columnspan=2,pady=10)
        self.password_var=tk.StringVar()
        self.password_entry=ttk.Entry(main_frame,textvariable=self.password_var,font=("Arial",12),width=30)
        self.password_entry.grid(row=1,column=0,columnspan=2,pady=10)
        ttk.Label(main_frame,text="طول كلمة المرور:").grid(row=2,column=0,sticky=tk.W,pady=5)
        length_spinbox=ttk.Spinbox(main_frame,from_=8,to=32,textvariable=self.password_length,width=5)
        length_spinbox.grid(row=2,column=1,sticky=tk.W,pady=5)
        ttk.Checkbutton(main_frame,text="تضمين أحرف كبيرة",variable=self.include_uppercase).grid(row=3,column=0,columnspan=2,sticky=tk.W,pady=5)
        ttk.Checkbutton(main_frame,text="تضمين أرقام",variable=self.include_numbers).grid(row=4,column=0,columnspan=2,sticky=tk.W,pady=5)
        ttk.Checkbutton(main_frame,text="تضمين رموز خاصة",variable=self.include_symbols).grid(row=5,column=0,columnspan=2,sticky=tk.W,pady=5)
        ttk.Button(main_frame,text="توليد كلمة مرور",command=self.generate_password).grid(row=6,column=0,columnspan=2,pady=20)
        ttk.Button(main_frame,text="نسخ كلمة المرور",command=self.copy_password).grid(row=7,column=0,columnspan=2)
    def generate_password(self):
        chars=string.ascii_lowercase
        if self.include_uppercase.get():chars+=string.ascii_uppercase
        if self.include_numbers.get():chars+=string.digits
        if self.include_symbols.get():chars+=string.punctuation
        if chars:
            password="".join(random.choice(chars) for _ in range(self.password_length.get()))
            self.password_var.set(password)
        else:
            self.password_var.set("الرجاء اختيار خيار واحد على الأقل")
    def copy_password(self):
        password=self.password_var.get()
        if password:pyperclip.copy(password)
if __name__=="__main__":
    root=tk.Tk()
    root.configure(bg="white")
    app=PasswordGenerator(root)
    root.mainloop()
