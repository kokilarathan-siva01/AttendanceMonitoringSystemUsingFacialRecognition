# this script is used to create any side / popup that will be then used in the system.

from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
from random import randint
import time
import threading

def progress_bar():
    styleMain = ttk.Style()
    styleMain.theme_use('clam')
    styleMain.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
    progressBar=Progressbar(splash,style="green.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')
    progressBar.pack(padx= 2, pady= 15)
    #progressBar.place(x = 0, y = 235)
    loading = Label(splash,text = "Verifying...", fg="green", font=("Ariel", 30))
    loading_2 = Label(splash,text = "Verifying", fg="green", font=("Ariel", 30))
        
    
    progress = 0
    random_int = randint(50,100)
    
    for i in range(random_int):
        if i/2 == 0:
           loading.pack()

        progressBar.pack()
        progressBar['value']=progress
        splash.update_idletasks()
        time.sleep(0.05)
        progress += 1
        
    splash.destroy()
    # instead of the new_win, link to the main windows when created later on ############
    new_win()
    

def new_win():
      # w.destroy()
    q=Tk()
    q.title('Main window')
    q.geometry('427x250')
    l1=Label(q,text='ADD TEXT HERE ',fg='grey',bg=None)
    l=('Calibri (Body)',24,'bold')
    l1.config(font=l)
    l1.place(x=80,y=100)
    
    
    
    q.mainloop()
    
def splash_popup():
    global splash
    splash = Tk()
    splash.title("Verifying")
    # Hides the title bar, Currently causeing problems for mac, Test on windows later.
    #splash.overrideredirect(1)
    
    # These measure are used to calcualte the centre of the window
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x_val = (screen_width/2)-(427/2)
    y_val = (screen_height/2)-(250/2)
    splash.geometry(("%dx%d+%d+%d") %(427,100,x_val,y_val))
    # Add an image later on to make it more visually appealing
    progress_bar()
    splash.mainloop()
    