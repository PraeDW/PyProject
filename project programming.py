from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
gui = Tk()
gui.title('Balance sheet and Net income')
var = IntVar()

def sum(a1,a2,a3,a4,a5,varl1,vare1,varl2,vare2,varl3,vare3,varl4,vare4,varl5,vare5):
       a=int(varl1.get()) 
       b=int(vare1.get())
       c=a+b
       a1.insert(0,c)
       d=int(varl2.get())
       e=int(vare2.get())
       f=d+e
       a2.insert(0,f)
       g=int(varl3.get())
       h=int(vare3.get())
       i=g+h
       a3.insert(0,i)
       j=int(varl4.get())
       k=int(vare4.get())
       l=j+k
       a4.insert(0,l)
       m=int(varl5.get())
       n=int(vare5.get())
       i=m+n
       a5.insert(0,i)


# balance sheet show graph
def opg(vara1,vara2,vara3,vara4,vara5,vary1,vary2,vary3,vary4,vary5,varl1,varl2,varl3,varl4,varl5,vare1,vare2,vare3,vare4,vare5):
        x=np.array([int(vara1.get()),int(vara2.get()),int(vara3.get()),int(vara4.get()),int(vara5.get())]) #assest
        y=np.array([vary1.get(),vary2.get(),vary3.get(),vary4.get(),vary5.get()]) #year
        L=np.array(([varl1.get(),varl2.get(),varl3.get(),varl4.get(),varl5.get()])) #liabilities
        E=np.array(([vare1.get(),vare2.get(),vare3.get(),vare4.get(),vare5.get()])) #equity
        plt.axes(xticks=y)
        plt.bar(y-0.2,E,width=0.4,label='equity',align='center')
        plt.bar(y+0.2,L,width=0.4,label='liabilities',align='center')
        plt.plot(y,x,label='asset',c='b')
        plt.title('balance sheet')
        plt.ylabel('amount (Million Baht)')
        plt.xlabel('years')
        plt.legend(loc='best')
        plt.show()


def delbalsh(y1,l1,e1,a1,y2,l2,e2,a2,y3,l3,e3,a3,y4,l4,e4,a4,y5,l5,e5,a5) :
    y1.delete(0,END)
    l1.delete(0,END)
    e1.delete(0,END)
    a1.delete(0,END)

    y2.delete(0,END)
    l2.delete(0,END)
    e2.delete(0,END)
    a2.delete(0,END)

    y3.delete(0,END)
    l3.delete(0,END)
    e3.delete(0,END)
    a3.delete(0,END)

    y4.delete(0,END)
    l4.delete(0,END)
    e4.delete(0,END)
    a4.delete(0,END)

    y5.delete(0,END)
    l5.delete(0,END)
    e5.delete(0,END)
    a5.delete(0,END)

# balance sheet GUI
def openwindow():
    Info = Tk()
    Info.title('Balance sheet information')
    Info.geometry('800x500')
    Info.configure(background='white')
    Label(Info,text='1',font=10,bg='white',fg='white').grid(row=1,column=1)
    Label(Info,text='Input information',font=10,bg='white',fg='black').grid(row=1,column=5)
    Label(Info,text='(Unit: Million Baht)',font=10,bg='white',fg='black').grid(row=1,column=8)

    Label(Info,text='Year 1',font=10,bg='white',fg='black').grid(row=2,column=2)
    Label(Info,text='year: ',font=10,bg='white',fg='black').grid(row=3,column=3)
    vary1=IntVar()
    y1=Entry(Info,textvariable=vary1)
    y1.grid(row=3,column=4)

    varl1=IntVar()
    Label(Info,text='liabilities: ',font=10,bg='white',fg='black').grid(row=4,column=3)
    l1=Entry(Info,textvariable=varl1)
    l1.grid(row=4,column=4)

    vare1=IntVar()
    Label(Info,text='equity:  ',font=10,bg='white',fg='black').grid(row=5,column=3)
    e1=Entry(Info,textvariable=vare1)
    e1.grid(row=5,column=4)

    vara1=StringVar()
    Label(Info,text='assests: ',font=10,bg='white',fg='black').grid(row=6, column=3)
    a1=Entry(Info,textvariable=vara1)
    a1.grid(row=6,column=4)

    Label(Info,text='Year 2',font=10,bg='white',fg='black').grid(row=7,column=2)
    Label(Info,text='year:',font=10,bg='white',fg='black').grid(row=8,column=3)
    vary2=IntVar()
    y2=Entry(Info,textvariable=vary2)
    y2.grid(row=8,column=4)

    varl2=IntVar()
    Label(Info,text='liabilities: ',font=10,bg='white',fg='black').grid(row=9,column=3)
    l2=Entry(Info,textvariable=varl2)
    l2.grid(row=9,column=4)

    vare2=IntVar()
    Label(Info,text='equity:  ',font=10,bg='white',fg='black').grid(row=10,column=3)
    e2=Entry(Info,textvariable=vare2)
    e2.grid(row=10,column=4)

    vara2=StringVar()
    Label(Info,text='assests: ',font=10,bg='white',fg='black').grid(row=11, column=3)
    a2=Entry(Info,textvariable=vara2)
    a2.grid(row=11,column=4)

    Label(Info,text='Year 3',font=10,bg='white',fg='black').grid(row=12,column=2)
    Label(Info,text='year:',font=10,bg='white',fg='black').grid(row=13,column=3)
    vary3=IntVar()
    y3=Entry(Info,textvariable=vary3)
    y3.grid(row=13,column=4)

    Label(Info,text='liabilities: ',font=10,bg='white',fg='black').grid(row=14,column=3)
    varl3=IntVar()
    l3=Entry(Info,textvariable=varl3)
    l3.grid(row=14,column=4)

    Label(Info,text='equity:  ',font=10,bg='white',fg='black').grid(row=15,column=3)
    vare3=IntVar()
    e3=Entry(Info,textvariable=vare3)
    e3.grid(row=15,column=4)

    Label(Info,text='assests: ',font=10,bg='white',fg='black').grid(row=16, column=3)
    vara3=StringVar()
    a3=Entry(Info,textvariable=vara3)
    a3.grid(row=16,column=4)

    Label(Info,text='Year 4',font=10,bg='white',fg='black').grid(row=2,column=6)
    Label(Info,text='year:',font=10,bg='white',fg='black').grid(row=3,column=7)
    vary4=IntVar()
    y4=Entry(Info,textvariable=vary4)
    y4.grid(row=3,column=8)

    Label(Info,text='liabilities: ',font=10,bg='white',fg='black').grid(row=4,column=7)
    varl4=IntVar()
    l4=Entry(Info,textvariable=varl4)
    l4.grid(row=4,column=8)

    Label(Info,text='equity:  ',font=10,bg='white',fg='black').grid(row=5,column=7)
    vare4=IntVar()
    e4=Entry(Info,textvariable=vare4)
    e4.grid(row=5,column=8)

    Label(Info,text='assests: ',font=10,bg='white',fg='black').grid(row=6, column=7)
    vara4=StringVar()
    a4=Entry(Info,textvariable=vara4)
    a4.grid(row=6,column=8)

    Label(Info,text='Year 5',font=10,bg='white',fg='black').grid(row=7,column=6)
    Label(Info,text='year:',font=10,bg='white',fg='black').grid(row=8,column=7)
    vary5=IntVar()
    y5=Entry(Info,textvariable=vary5)
    y5.grid(row=8,column=8)

    Label(Info,text='liabilities: ',font=10,bg='white',fg='black').grid(row=9,column=7)
    varl5=IntVar()
    l5=Entry(Info,textvariable=varl5)
    l5.grid(row=9,column=8)

    Label(Info,text='equity:  ',font=10,bg='white',fg='black').grid(row=10,column=7)
    vare5=IntVar()
    e5=Entry(Info,textvariable=vare5)
    e5.grid(row=10,column=8)

    Label(Info,text='assests: ',font=10,bg='white',fg='black').grid(row=11, column=7)   
    vara5=StringVar()
    a5=Entry(Info,textvariable=vara5)
    a5.grid(row=11,column=8)

    Button(Info,text=' Calculate assest',font = 3,fg='black',bg='white',command=lambda:sum(a1,a2,a3,a4,a5,varl1,vare1,varl2,vare2,varl3,vare3,varl4,vare4,varl5,vare5)).grid(row=13,column=8)
    Button(Info, text="Show your graph",font = 3, fg='black', bg='white',command=lambda:opg(vara1,vara2,vara3,vara4,vara5,vary1,vary2,vary3,vary4,vary5,varl1,varl2,varl3,varl4,varl5,vare1,vare2,vare3,vare4,vare5)).grid(row=14,column=8)
    Button(Info , text='clear', font = 3,fg='black', bg='white',command=lambda:delbalsh(y1,l1,e1,a1,y2,l2,e2,a2,y3,l3,e3,a3,y4,l4,e4,a4,y5,l5,e5,a5)).grid(row=15,column=8)
    Info.mainloop()

# net income calculatifon
def Tax(net0,net1,net2,net3,net4,net5,net6,net7,net8,net9,net10,net11,net12,net13,net14,net15,net16,net17,net18,net19,n1,n2,n3,n4,n5):
        
        b1 = float(net1.get())
        b2 = float(net5.get())
        b3 = float(net9.get())
        b4 = float(net13.get())
        b5 = float(net17.get())

        c1 = float(net2.get()) 
        c2 = float(net6.get())
        c3 = float(net10.get())
        c4 = float(net14.get())
        c5 = float(net18.get())

        income = (b1,b2,b3,b4,b5)
        expense = (c1,c2,c3,c4,c5)
        p1 = (b1-c1)
        p2 = (b2-c2)
        p3 = (b3-c3)
        p4 = (b4-c4)
        p5 = (b5-c5)

        profit = [p1,p2,p3,p4,p5]
        for i in range(len(profit)) :
            if income < expense:
                tax = 0
            elif profit[i] < 3000000: #SME
                if profit[i] < 300000:
                    tax = 0
                elif profit[i] in range(300000, 30000000):
                    tax[i] = 0.15 * profit
                elif profit in range(30000001,):
                    tax[i] = 0.20 * profit
            else:
                profit[i] > 30,000,000 # out SME
                tax = 0.2*profit[i]

        b1 = int(net1.get())
        c1 = int(net2.get())
        d1 = p1- tax 
        n1.insert(0,d1)
        b2 = int(net5.get())
        c2 = int(net6.get())
        d2 = p2-tax
        n2.insert(0,d2)
        b3 = int(net9.get())
        c3 = int(net10.get())
        d3 = p3-tax
        n3.insert(0,d3)
        b4 = int(net13.get())
        c4 = int(net14.get())
        d4 = p4-tax
        n4.insert(0,d4)
        b5 = int(net17.get())
        c5 = int(net18.get())
        d5 = p5-tax
        n5.insert(0,d5)    

# net income show graph
def kiki(net0,net1,net2,net3,net4,net5,net6,net7,net8,net9,net10,net11,net12,net13,net14,net15,net16,net17,net18,net19):
        x=np.array(([float(net3.get()),float(net7.get()),float(net11.get()),float(net15.get()),float(net19.get())])) #net income
        y=np.array([net0.get(),net4.get(),net8.get(),net12.get(),net16.get()]) #year
        L=np.array(([net1.get(),net5.get(),net9.get(),net13.get(),net17.get()])) #income
        E=np.array(([net2.get(),net6.get(),net10.get(),net14.get(),net18.get()]))*(-1) #expenses
        plt.axes(xticks=y)
        plt.bar(y-0.2,E,width=0.4,label='expenses',align='center')
        plt.bar(y+0.2,L,width=0.4,label='income',align='center')
        plt.plot(y,x,label='net profit',c = 'black')
        plt.ylabel('amount (Million baht))')
        plt.xlabel('years')
        plt.title('Net income')
        plt.legend(loc='best')
        plt.show()

# clear data 
def delnetin(y1,i1,x1,n1,y2,i2,x2,n2,y3,i3,x3,n3,y4,i4,x4,n4,y5,i5,x5,n5) :
    y1.delete(0,END)
    i1.delete(0,END)
    x1.delete(0,END)
    n1.delete(0,END)

    y2.delete(0,END)
    i2.delete(0,END)
    x2.delete(0,END)
    n2.delete(0,END)

    y3.delete(0,END)
    i3.delete(0,END)
    x3.delete(0,END)
    n3.delete(0,END)

    y4.delete(0,END)
    i4.delete(0,END)
    x4.delete(0,END)
    n4.delete(0,END)

    y5.delete(0,END)
    i5.delete(0,END)
    x5.delete(0,END)
    n5.delete(0,END)

# net income GUI
def ow2():
    NI = Tk()
    NI.title('Comprehensive income information')
    NI.configure(background="white")
    NI.geometry('800x500')
    Label(NI,text='Net Income ',font=10,bg='white',fg='black').grid(row=1, column=5)
    Label(NI,text='(Unit: Million Baht)',font=10,bg='white',fg='black').grid(row=1,column=8)
    Label(NI,text='year1 ',font=10,bg='white',fg='black').grid(row=2, column=1)
    Label(NI,text='year: ',font=10,bg='white',fg='black').grid(row=3, column=2)
    net0 = IntVar()
    y1 = Entry(NI,textvariable=net0)
    y1.grid(row=3,column=3)

    Label(NI,text='total income: ',font=10,bg='white',fg='black').grid(row=4, column=2)
    net1 = IntVar()
    i1=Entry(NI,textvariable=net1)
    i1.grid(row=4,column=3)

    Label(NI,text='total expense: ',font=10,bg='white',fg='black').grid(row=5, column=2)
    net2 = IntVar()
    x1=Entry(NI,textvariable=net2)
    x1.grid(row=5,column=3)

    Label(NI,text='net profit: ',font=10,bg='white',fg='black').grid(row=6, column=2)
    net3 = StringVar()
    n1=Entry(NI,textvariable=net3)
    n1.grid(row=6,column=3)

    Label(NI,text='year2 ',font=10,bg='white',fg='black').grid(row=7, column=1)
    Label(NI,text='year: ',font=10,bg='white',fg='black').grid(row=8, column=2)
    net4 = IntVar()
    y2 = Entry(NI,textvariable=net4)
    y2.grid(row=8,column=3)

    Label(NI,text='total income: ',font=10,bg='white',fg='black').grid(row=9, column=2)
    net5 = IntVar()
    i2=Entry(NI,textvariable=net5)
    i2.grid(row=9,column=3)

    Label(NI,text='total expense: ',font=10,bg='white',fg='black').grid(row=10, column=2)
    net6 = IntVar()
    x2=Entry(NI,textvariable=net6)
    x2.grid(row=10,column=3)

    Label(NI,text='net profit: ',font=10,bg='white',fg='black').grid(row=11, column=2)
    net7 = StringVar()
    n2=Entry(NI,textvariable=net7)
    n2.grid(row=11,column=3)

    Label(NI,text='year3 ',font=10,bg='white',fg='black').grid(row=12, column=1)
    Label(NI,text='year: ',font=10,bg='white',fg='black').grid(row=13, column=2)
    net8 = IntVar()
    y3 = Entry(NI,textvariable=net8)
    y3.grid(row=13,column=3)

    Label(NI,text='total income: ',font=10,bg='white',fg='black').grid(row=14, column=2)
    net9 = IntVar()
    i3=Entry(NI,textvariable=net9)
    i3.grid(row=14,column=3)

    Label(NI,text='total expense: ',font=10,bg='white',fg='black').grid(row=15, column=2)
    net10 = IntVar()
    x3=Entry(NI,textvariable=net10)
    x3.grid(row=15,column=3)

    Label(NI,text='net profit: ',font=10,bg='white',fg='black').grid(row=16, column=2)
    net11 = StringVar()
    n3=Entry(NI,textvariable=net11)
    n3.grid(row=16,column=3)

    Label(NI,text='year4 ',font=10,bg='white',fg='black').grid(row=2, column=6)
    Label(NI,text='year: ',font=10,bg='white',fg='black').grid(row=3, column=7)
    net12 = IntVar()
    y4 = Entry(NI,textvariable=net12)
    y4.grid(row=3,column=8)

    Label(NI,text='total income: ',font=10,bg='white',fg='black').grid(row=4, column=7)
    net13 = IntVar()
    i4=Entry(NI,textvariable=net13)
    i4.grid(row=4,column=8)

    Label(NI,text='total expense: ',font=10,bg='white',fg='black').grid(row=5, column=7)
    net14 = IntVar()
    x4=Entry(NI,textvariable=net14)
    x4.grid(row=5,column=8)

    Label(NI,text='net profit: ',font=10,bg='white',fg='black').grid(row=6, column=7)
    net15 =StringVar()
    n4=Entry(NI,textvariable=net15)
    n4.grid(row=6,column=8)

    Label(NI,text='year5 ',font=10,bg='white',fg='black').grid(row=7, column=6)
    Label(NI,text='year: ',font=10,bg='white',fg='black').grid(row=8, column=7)
    net16 = IntVar()
    y5 = Entry(NI,textvariable=net16)
    y5.grid(row=8,column=8)

    Label(NI,text='total income: ',font=10,bg='white',fg='black').grid(row=9, column=7)
    net17 = IntVar()
    i5=Entry(NI,textvariable=net17)
    i5.grid(row=9,column=8)

    Label(NI,text='expense: ',font=10,bg='white',fg='black').grid(row=10, column=7)
    net18 = IntVar()
    x5=Entry(NI,textvariable=net18)
    x5.grid(row=10,column=8)

    Label(NI,text='net profit: ',font=10,bg='white',fg='black').grid(row=11, column=7)
    net19 = StringVar()
    n5=Entry(NI,textvariable=net19)
    n5.grid(row=11,column=8)

    Button(NI, text='Calculate net profit',font= 3,fg='black', bg='white',command=lambda:Tax(net0,net1,net2,net3,net4,net5,net6,net7,net8,net9,net10,net11,net12,net13,net14,net15,net16,net17,net18,net19,n1,n2,n3,n4,n5)).grid(row=14,column=8)
    Button(NI,text='Show your graph',font= 3,fg='black', bg='white',command=lambda:kiki(net0,net1,net2,net3,net4,net5,net6,net7,net8,net9,net10,net11,net12,net13,net14,net15,net16,net17,net18,net19)).grid(row=15,column=8)
    Button(NI,text='clear',font= 3,fg='black', bg='white',command=lambda:delnetin(y1,i1,x1,n1,y2,i2,x2,n2,y3,i3,x3,n3,y4,i4,x4,n4,y5,i5,x5,n5)).grid(row=16,column=8)
    NI.mainloop()

# GUI
def gui():
    gui = Tk()
    gui.title('Balance sheet and Net income')
    var = IntVar()
    gui.geometry('300x200')
    gui.configure(background="white")
    Label(gui, text='Please choose', font=20, bg='white', fg='black').pack()

    var1 = IntVar()
    R1 = Checkbutton(gui, text="Balance sheet",variable=var,command=openwindow, bg='white',font=10)
    R1.pack( anchor = W,padx=30,pady=10)
    R2 = Checkbutton(gui, text="Statement of Net income", variable=var1,command=ow2,bg='white',font=10)
    R2.pack( anchor = W, padx=30,pady=5 )
    gui.mainloop()
    
gui()
