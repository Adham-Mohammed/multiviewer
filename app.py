from tkinter import *
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.animation as animation
import matplotlib
from matplotlib import style
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
from tkinter.filedialog import askopenfile
from scipy.io import loadmat
from scipy.misc import electrocardiogram


viewer=Tk() 

style.use('ggplot')
viewer.title("MultiSignal monitoring")
viewer.geometry('1400x700')
signal1=Label(viewer,text="ECG",font=20)
signal1.place(x=1,y=1)

# b1 = Button(viewer, text='Browse File', 
#    width=20,command = lambda:upload_file())
# b1.pack()
 

# def upload_file():
#     f_types = [('CSV files',"*.csv"),('All',"*.*")]
#     file = filedialog.askopenfilename(filetypes=f_types) 
#     df=pd.read_csv(file) # create DataFrame
#     return df

# ecg_data=pd.read_csv("signals\ecg.csv")
# t=np.arange(len(ecg_data))/10

# Signal=loadmat("100m (0).mat")
# ECG =(Signal["val"][0])/200   # 200 is a data gain  
# Samples = len( ECG)
# Fs = Samples/100
# T = 1 / Fs
# Time=np.linspace(0,Samples*T,Samples)

ecg = electrocardiogram()
fs = 360
time = np.arange(ecg.size) / fs

fig= Figure(figsize=(5, 5),dpi=100)
plot1=fig.add_subplot(1,1,1)
xar=[]
yar=[]
def animate(i):
    data=ecg
    ti=time
    for i in range(len(data)):
        yar.append(data[i])
        xar.append(ti[i])
    
    plot1.clear() 
    plot1.plot(xar,yar)
    
    



# plot1.plot(time,ecg)
canvas=FigureCanvasTkAgg(fig,viewer)
canvas.get_tk_widget().grid()

#make toolbar 
# toolbar = NavigationToolbar2Tk(canvas,viewer)
# toolbar.update()
# canvas.get_tk_widget().pack()
ani = animation.FuncAnimation(fig, animate, interval = 1000)
viewer.mainloop()