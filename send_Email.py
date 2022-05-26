from curses.ascii import EM
import smtplib
import ssl
import student_database
import Attendance_graphs
from email.message import EmailMessage
from datetime import datetime
from datetime import date

### This script is used to create all the function that is needed to send email to the students, teachers, and admin team.


### since we are sending an email from one single email, I've decalred it in the local area to be used by all functions.
### THIS IS NOT A PERSONAL EMAIL, CREATED FOR THE PURPOSE OF THE project
senderEmail = "attendanceservice2022@gmail.com"
passwordEmail = "Universityoflincoln@2022"

### this function will send an email to students who are absent.
def sendAllAbsent():
    ### the absent's students names and email address is gathered from the database using the findabsentstudent function.
    presentStudent,absentStudent,totalStudent =Attendance_graphs.findAbsentStudent()
    fullName = []
    fullEmail = []
    for i in absentStudent:
        name = str(student_database.GetStudentInfo(i)[1] + " " + student_database.GetStudentInfo(i)[2])
        email = str(student_database.GetStudentInfo(i)[3])
        fullName.append(name)
        fullEmail.append(email)
    ### sending an email to all the students that were absent when monitoring attendance ended.
    if absentStudent != None:
        for i in range(len(fullEmail)):
            sendAbsentStudentEmail(str(fullName[i]),str(fullEmail[i])) ### this is the funtion that will send the email
        
### send an email to the absent students.
def sendAbsentStudentEmail(studentName,studentEmail):
    todayDate = date.today()
    formatDate = todayDate.strftime("%d %b %Y")
    
    currTime = datetime.now()
    formatTime = currTime.strftime("%H:%M")
    
    receiverEmail = str(studentEmail)
    
    emailSubject = "You have been marked absent "
    body = "Hey, " + studentName +"\nYou have been marked absent for " +formatDate+"'s Class at: " + formatTime
    body2= "Please contact admin team if this information seems incorrect." 
    body3 = "Many Thanks"
    body4 = "This is an automated service."
    
    
    mess = EmailMessage()
    mess["From"] = senderEmail
    mess["To"] = receiverEmail
    mess["Subject"] = emailSubject
    #mess.set_content(body)

    html= f"""
        <html>
            <body>
                <h1>{emailSubject}</h1>
                <p>{body}</p>
                <p>{body2}</p>
                <p>{body3}</p>
                <b>{body4}</b>
            </body>
        </html>
        """
    mess.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
        server.login(senderEmail,passwordEmail)
        server.sendmail(senderEmail,receiverEmail,mess.as_string())

### send an email containing an attachment of the recent recorded attendance.
def sendAttendaceReportEmail():
    todayDate = date.today()
    formatDate = todayDate.strftime("%d %b %Y")
    
    receiverEmail = "attendanceservice2022@gmail.com"
    
    currTime = datetime.now()
    formatTime = currTime.strftime("%H:%M")
    
    emailSubject = "Attendace Report for "+ formatDate
    body = "Please find the attachement of the attendace report for " + formatDate + " Collected at: " + formatTime
    
    mess = EmailMessage()
    mess["From"] = senderEmail
    mess["To"] = receiverEmail
    mess["Subject"] = emailSubject


    html= f"""
        <html>
            <body>
                <h1>{emailSubject}</h1>
                <p>{body}</p>
            </body>
        </html>
        """
    mess.add_alternative(html, subtype="html")

    with open("Attendance/Attendance.csv", 'rb') as file:
        file_info =file.read()
        mess.add_attachment(file_info,maintype="application", subtype="csv",filename=("Attendance - " +formatDate +" "+formatTime+".csv"))


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
        server.login(senderEmail,passwordEmail)
        server.sendmail(senderEmail,receiverEmail,mess.as_string())
    
### send the information on the note section when the program is exited.
def sendTempNoteEmail(name):
    todayDate = date.today()
    formatDate = todayDate.strftime("%d %b %Y")
    
    receiverEmail = "attendanceservice2022@gmail.com"
    
    currTime = datetime.now()
    formatTime = currTime.strftime("%H:%M")
    
    emailSubject = "Temporary Note for: " + name  + " On " + formatDate
    body = "Temporary Note for user: " + name + " for: "+ formatDate + " Collected at: " + formatTime
    
    mess = EmailMessage()
    mess["From"] = senderEmail
    mess["To"] = receiverEmail
    mess["Subject"] = emailSubject


    html= f"""
        <html>
            <body>
                <h1>{emailSubject}</h1>
                <p>{body}</p>
            </body>
        </html>
        """
    mess.add_alternative(html, subtype="html")

    with open("Temp Note.txt", 'rb') as file:
        file_info =file.read()
        mess.add_attachment(file_info,maintype="application", subtype="txt",filename=("Temp Note.txt"))


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server: ### using gmail as my host and port numbet "465"
        server.login(senderEmail,passwordEmail)
        server.sendmail(senderEmail,receiverEmail,mess.as_string())
        
