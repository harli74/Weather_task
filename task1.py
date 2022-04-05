from apifuncs import locationcodes,average,coldest,singletowncheck
from tkinter import *
from tkinter import ttk 
#randcodes=[]
#apilinksfromid=[]
appwindow=Tk()
root=appwindow
modify=Entry(root)
modify.grid(column=1, row=1)
outputtemp=StringVar()
outputavg=StringVar()
outputcoldest=StringVar()

def singletownsearch():
    temps1,weather1,hmdt1=singletowncheck(modify.get())
    outputtemp.set("Stats of "+modify.get()+" are :\n Temps:"+str(temps1)+"\n Weather: "
                   +weather1+"\n Humidity: "+str(hmdt1)+" %")

def avgtogui():
    numberoftowns=0.0
    avg=0.0
    numberoftowns, avg=average()
    outputavg.set("Average temp of "+str(numberoftowns)+" is "+str(avg)+" degrees")

def coldestgui():
    return "Coldest town is "+ coldest()

appwindow.title("City Checker App")
appwindow.geometry('640x480')

lblsearch=Label(appwindow,text='Enter City to Find:').grid(column=0,row=1)
lblsearch1=Label(appwindow,textvariable=outputtemp).grid(column=0,row=2)
lblrand_cities = Label(appwindow, text="Random Cities:").grid(column=0, row=0)
lblaveragevalue = Label(appwindow, text="AverageTemps:").grid(column=0, row=3)
lblaverageguiresponce=Label(appwindow,textvariable=outputavg).grid(column=2,row=3)
lblcoldest = Label(appwindow, text="Find Coldest City:").grid(column=0, row=4)
lblcoldestguiresponce=Label(appwindow,textvariable=outputcoldest).grid(column=1,row=4)

btn = Button(appwindow, text="Collect Data!",fg="red",command=locationcodes).grid(column=1, row=0)
btn1=Button(appwindow,text="Generate",command=avgtogui).grid(column=1,row=3)
btn2=Button(appwindow,text="Coldest City:",fg="blue",command=coldestgui).grid(column=0,row=5)
btn3=Button(appwindow,text="Check City:",fg="black",command=singletownsearch).grid(column=2,row=1)
btn4=ttk.Button(appwindow, text="Quit", command=root.destroy).grid(column=5, row=5)

root.mainloop()
appwindow.mainloop()