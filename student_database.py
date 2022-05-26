import sqlite3
import os
from tkinter import *
from tkinter import messagebox

# retrining the current directory so that when this code is excuted on another machine 
# it will work without any errors
currentDir = os.getcwd()
try:
    student_data = sqlite3.connect(currentDir+"/Database/Student_Data.db")
    cursor_ = student_data.cursor()
except Exception as error:
    messagebox.showerror("Error", "Invalid Directory, Please fix and try agian.")
 
try:
    # primary key might need to be chnaged.
    cursor_.execute('''CREATE TABLE IF NOT EXISTS students(
        studentID text,
        firstname text,
        lastname text,
        email text,
        gender text,
        department text
        )''')
    student_data.commit()
except Exception as error:
    messagebox.showwarning("Warning", "Table has not been created due to invalid directory.")

### function to insert new data into the database.
def update_data(studentID,firstname,lastname,email,gender,department):
    
    cursor_.execute("INSERT INTO students VALUES (:studentID, :firstname, :lastname, :email, :gender, :department)", {
        'studentID': studentID,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'gender': gender,
        'department': department
    })
    student_data.commit()

### This function will allow me to get all information from the database about a student when the student's ID is given.
def GetStudentInfo(studentIDs):
    currentPP = "SELECT * FROM students WHERE studentID="+str(studentIDs)
    cursoR =cursor_.execute(currentPP)
    names = None
    
    for i in cursoR:
        names = i
    
    return names
    
### This function collects all information on the student and returns it as an array ( each arrary for each Value)
def GetAllInfo():
    allID = []
    allFname = []
    allLname = []
    allEmail = []
    
    
    for i in cursor_.execute("SELECT * from students"):
        allID.append(i[0])
        allFname.append(i[1])
        allLname.append(i[2])
        allEmail.append(i[3])
    
    return allID,allFname,allLname,allEmail
