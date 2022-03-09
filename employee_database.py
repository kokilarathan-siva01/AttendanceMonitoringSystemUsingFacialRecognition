import sqlite3
import os
from tkinter import *
from tkinter import messagebox

# retrining the current directory so that when this code is excuted on another machine 
# it will work without any errors
currentDir = os.getcwd()
try:
    emp_data = sqlite3.connect(currentDir+"/Database/Employee_Data.db")
    cursor_ = emp_data.cursor()
except Exception as error:
    messagebox.showerror("Error", "Invalid Directory, Please fix and try agian.")

try:
    # primary key might need to be chnaged.
    cursor_.execute('''CREATE TABLE IF NOT EXISTS employee(
        userID PRIMARY KEY text,
        password text,
        forename text,
        surname text,
        gender text,
        email text
        )''')
    emp_data.commit()
except Exception as error:
    messagebox.showwarning("Warning", "Table has not been created due to invalid directory.")
   
def update_data(userID,password,forename,surname,gender,email):
    
    cursor_.execute("INSERT INTO employee VALUES (:userID, :password, :forename, :surname, :gender, :email)", {
        'userID': userID,
        'password': password,
        'forename': forename,
        'surname': surname,
        'gender': gender,
        'email': email
        
    })
    emp_data.commit()

def getUserPass():
    allUsername = []
    allPassword = []
    
    for i in cursor_.execute("SELECT * from employee"):
        allUsername = i[0]
        allPassword = i[1]
    
    return allUsername,allPassword