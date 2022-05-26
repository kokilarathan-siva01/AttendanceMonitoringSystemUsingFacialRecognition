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
        userID text,
        password text,
        forename text,
        surname text,
        gender text,
        email text
        )''')
    emp_data.commit()
except Exception as error:
    messagebox.showwarning("Warning", "Table has not been created due to invalid directory.")

### function to insert new data into the database.
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

## Function used to retrive the teachers username and password, and will be used to verify when logging in.
def getUserPass():
    allUsername = []
    allPassword = []
    
    for i in cursor_.execute("SELECT * from employee"):
        allUsername.append(i[0])
        allPassword.append(i[1])

    
    return allUsername,allPassword

### this function is used to get information based on a given userID.
def GetTeacherName(userID):
    currentPP = "SELECT * FROM employee WHERE userID="+str(userID)
    cursoR =cursor_.execute(currentPP)
    names = None
    
    for i in cursoR:
        names = i
    
    return names

