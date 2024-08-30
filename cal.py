from tkinter import Tk, Entry, Button, StringVar
class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resitable(False,False)

        self.equation= StringVar
        self.entry_value=''
        Entry(width=17 ,bg=#fff' ,font=('Arial Bold',28),textvariable=self.equation.plac(X=0,Y=0))
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry-value)
    def clear(self):
    
root=Tk()
root.mainloop()