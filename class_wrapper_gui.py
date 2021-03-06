
from Tkinter import *
import math

class HelloWorld:
    def __init__(self, parent):
        self.master = parent   
        top = Frame(parent)    
        top.pack(side='top')   

        hwframe = Frame(top)
        hwframe.pack(side='top')
        font = 'times 18 bold'
        hwtext = Label(hwframe, text='Hello, World!', font=font)
        hwtext.pack(side='top', pady=20)

        rframe = Frame(top)
        rframe.pack(side='top', padx=10, pady=20)

        r_label = Label(rframe, text='The sine of')
        r_label.pack(side='left')

        self.r = StringVar() 
        self.r.set('1.2')    
        r_entry = Entry(rframe, width=6, textvariable=self.r)
        r_entry.pack(side='left')
        r_entry.bind('<Return>', self.comp_s)

        compute = Button(rframe, text=' equals ',
                         command=self.comp_s, relief='flat')
        compute.pack(side='left')

        self.s = StringVar() 
        s_label = Label(rframe, textvariable=self.s, width=12)
        s_label.pack(side='left')

        quit_button = Button(top, text='Goodbye, GUI World!',
                             command=self.quit,
                             background='yellow',foreground='blue')
        quit_button.pack(side='top', pady=5, fill='x')
        self.master.bind('<q>', self.quit)

    def quit(self, event=None):
        self.master.quit()

    def comp_s(self, event=None):
        self.s.set('%g' % math.sin(float(self.r.get())))


root = Tk()               
hello = HelloWorld(root)
root.mainloop()
