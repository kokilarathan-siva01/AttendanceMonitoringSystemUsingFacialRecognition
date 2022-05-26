import student_database
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import seaborn as sns
import csv

iDs,fname,lname,email = student_database.GetAllInfo() ### gathering all the information from the student database

### this function is used to find out all the student who are absent, by eliminating all the student who were present from the database and then storing the rest of them into a list.
def findAbsentStudent():
    attendace_df = pd.read_csv("Attendance/Attendance.csv")
    presentStudent= attendace_df['StudentID'] ### present student gathered from the .csv file while taking attendance.
    absentStudent = [] ### this is be gathered using the database and the present student, to elimiate the present students and get the absent students
    totalStudent =[]
    for i in range(len(iDs)):
        if str(iDs[i]) not in str(presentStudent):
            absentStudent.append(iDs[i])
            totalStudent.append(iDs[i])
            
    
    for i in range(len(presentStudent)):
        totalStudent.append(presentStudent[i])
            
    
    return presentStudent,absentStudent,totalStudent

### a pie chart showing the ratio of present and absent students.
def pieGraph():
    present,absent,total = findAbsentStudent()

    studentLength = [len(present),len(absent)]
    titles = ['Present','Absent']

    colours = sns.color_palette('pastel')[0:9]

    plt.pie(studentLength,labels=titles,colors=colours)
    plt.title("Student Attendace Pie Chart Analysis")
    plt.show()

### This function will be used when the button on main page is clicked.
### This function will display all the students and whether they were absent or present during the recent attendance monitoring.
def showAttendance():

    def show():
        present,absent,total_student = findAbsentStudent()

        for i in present:
            studentDetail = student_database.GetStudentInfo(i)
            listBox.insert("", "end", values=(i,(str(studentDetail[1])+" "+str(studentDetail[2])),"Present"))
        for i in absent:
            studentDetail = student_database.GetStudentInfo(i)
            listBox.insert("", "end", values=(i,(str(studentDetail[1])+" "+str(studentDetail[2])),"Absent"))
        

    display_attendance = tk.Tk() 
    display_attendance.title("Attendance")
    tk.Label(display_attendance, text="Recent Attendance", font=("Arial",28)).grid(row=0, columnspan=3)
    # create Treeview with needed columns
    headers = ('StudentID', 'Name', 'Attendance')
    listBox = ttk.Treeview(display_attendance, columns=headers, show='headings')
    # set column headings using the provided list.
    for i in headers:
        listBox.heading(i, text=i)    
    listBox.grid(row=1, column=0, columnspan=2)
    show()
    tk.Button(display_attendance, text="Pie Chart", width=15, command=pieGraph).grid(row=4, column=0)
    tk.Button(display_attendance, text="Exit", width=15, command=display_attendance.destroy).grid(row=4, column=1)

    display_attendance.mainloop()




