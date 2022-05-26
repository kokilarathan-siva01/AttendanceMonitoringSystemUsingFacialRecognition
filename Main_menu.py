from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import os
import send_Email
import student_database
import Face_Recognition
import Attendance_graphs
from datetime import datetime

### This script will be used to create the main menu section after the user/teacher logins into the system.
### Along with the main menu page, additional pages like train student, add student pages will also be created here.


### This function is used to verify when a new student is registered into the database.
### This logic and syntax follows the same as the one in main.py, to verify user login/signup.
def verify_student():
	studentFirstName_verify = studentFirstName.get()
	studentLastName_verify  = studentLastName.get()
	studentID_verify  = studentID.get()
	studentEmail_verify  = studentEmail.get()
	studentGender_verify  = studentGender.get()
	studentDepartment_verify  = studentDepartment.get()
 
	list_info = {'studentID': studentID_verify,'firstname': studentFirstName_verify,'lastname':studentLastName_verify,'email':studentEmail_verify,
                   'gender':studentGender_verify,'department':studentDepartment_verify}
	
	counter = 0
	warn_mess = "Please fill in the following blank entries: \n"
	column_names = ['studentID','firstname','lastname','email','gender','department']
	for i in range(len(column_names)):
		if not list_info[column_names[i]]:
				warn_mess += "({0}) ".format(i+1) + column_names[i] + "\n"
		else:
				counter += 1
    
	if counter == len(list_info):
		student_database.update_data(studentID_verify,studentFirstName_verify,studentLastName_verify,
                               studentEmail_verify,studentGender_verify,studentDepartment_verify)
		studentID_ent.delete(0,END)
		studentFirstName_ent.delete(0,END)
		studentLastName_ent.delete(0,END)
		studentEmail_ent.delete(0,END)
		studentDepartment_ent.delete(0,END)
		messagebox.showinfo("Successful", message="Registration Complete! Please get student to register their face.")
		messagebox.showinfo("Register Face", message="Click OK to proceed to take student's face!")
		Face_Recognition.RegisterStudentImage(studentID_verify)
		Face_Recognition.trainStudentFaces()
		messagebox.showinfo("Register Face Complete", message="Face Registartion Complete")
	else:       
		messagebox.showwarning("Warning", message=warn_mess)

### This is the register page, open when the button is clicked. representing information to register new students. follows the same template as the user signup page.
def Register_page():
	global RegisterPage
	RegisterPage = Toplevel(mainMenu)
	RegisterPage.geometry('700x700')
	RegisterPage.resizable(0,0)
	RegisterPage.configure(bg="#708090")
	RegisterPage.title('Register')

 
	Label(RegisterPage, text="Please Register the student with valid information", 
	bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
	Label(RegisterPage, text="", bg="#708090").pack()
	

	global studentFirstName
	global studentLastName
	global studentID
	global studentEmail
	global studentGender
	global studentDepartment
	
	global studentFirstName_ent
	global studentLastName_ent
	global studentID_ent
	global studentEmail_ent
	global studentDepartment_ent


	# since these variables will be changing, therefore, I am using Var().
	studentFirstName = StringVar()
	studentLastName = StringVar()
	studentID = StringVar()
	studentEmail = StringVar()
	studentGender = StringVar()
	studentDepartment = StringVar()
	
	### Entry boxes to student to input information about the student which will then get registered when the button is clicked.
 
	Label(RegisterPage, text="Student ID").pack()
	studentID_ent = Entry(RegisterPage, textvariable= studentID, bg="#708090")
	studentID_ent.pack()
	Label(RegisterPage, text="", bg="#708090").pack()
 
	Label(RegisterPage, text="First Name").pack()
	studentFirstName_ent = Entry(RegisterPage, textvariable= studentFirstName, bg="#708090")
	studentFirstName_ent.pack()
	Label(RegisterPage, text="", bg="#708090").pack()
	
	Label(RegisterPage, text="Last Name").pack()
	studentLastName_ent = Entry(RegisterPage, textvariable= studentLastName, bg="#708090")
	studentLastName_ent.pack()
	Label(RegisterPage, text="", bg="#708090").pack()
	
	Label(RegisterPage, text="Student Email").pack()
	studentEmail_ent = Entry(RegisterPage, textvariable= studentEmail, bg="#708090")
	studentEmail_ent.pack()
	Label(RegisterPage, text="", bg="#708090").pack()
 
	Label(RegisterPage, text= "Gender").pack()
	gender_frame = Frame(RegisterPage, bd=1, relief="groove")
	gender_frame.pack()
	Label(RegisterPage,text="").pack 

	gender_temp = ["Male", "Female", "Other"]
	for i in gender_temp:  
		gender_but = Radiobutton(gender_frame, text= i, variable=studentGender, value=i)
		gender_but.pack(side="left")
	Label(RegisterPage, text="", bg="#708090").pack()
  
	Label(RegisterPage, text="Subject Department").pack()
	studentDepartment_ent = Entry(RegisterPage, textvariable= studentDepartment, bg="#708090")
	studentDepartment_ent.pack()
	Label(RegisterPage, text="", bg="#708090").pack()
	
 
	
	Button(RegisterPage, text ="R E G I S T E R", height="2", width= "10", command=verify_student).pack()
	Button(RegisterPage, text="Exit", command=RegisterPage.destroy, bg='#708090',activebackground='#708090',border=0).pack()



### This is the home page or mainmenu page. This page will pop up when a user is successfully logged into the system with valid credentials.
### this windows will always be opened until the program is exterminated.
### from this page the user can navigate to different pages like taking attendance, viewing attendance, and registering a new student.    
def home_page():
	
	global mainMenu
	mainMenu = Tk()
	mainMenu.geometry('700x700')
	mainMenu.resizable(0,0)
	mainMenu.configure(bg="#708090")
	mainMenu.title('Main Menu')
	currentDir = os.getcwd()
	global open_button_img
	open_button_img = ImageTk.PhotoImage(Image.open(currentDir+"/images/Hamburger_Button.png"))
	v_smallfont =("Comic Sans MS", 13, "bold")
	smallfont =("Comic Sans MS", 20, "bold")
	mediumfont =("Comic Sans MS", 40, "bold")
	Largefont = ("Comic Sans MS", 60, "bold")
	### These code is used for produce the clock and make the seconds work.
	current_Time = datetime.now()
	current_time2 = "Time: " + current_Time.strftime('%H:%M:%S')
	clock = Label(mainMenu, text=current_time2, font=Largefont, background="#708090", foreground='black')
	clock.pack(side='top')
	
	### geting the current users name to display on the main screen.
	tName = " "
	with open('currentUser.txt') as f:
		tName = f.read()
	

	welcome = "Welcome to Attendnace Monitoring System"
	welcome2= "Using Face Recognition"
	registration_page = "REGISTER page, is used to add a new student into the database and train their faces"
	attendance_page = "ATTEDANCE page, is used to take attendance of the class. Please press 'q' to quit"
	inspect_page = "INSPECT page, is used to view the present and absent students"
	Label(mainMenu, text=tName, font=mediumfont, background="#708090", foreground='black').pack(side='top')
	Label(mainMenu, text=welcome, font=smallfont, background="#708090", foreground='black').pack(side='top')
	Label(mainMenu, text=welcome2, font=smallfont, background="#708090", foreground='black').pack(side='top')
	
	Label(mainMenu, text="", bg="#708090").pack()
 
	Label(mainMenu, text=registration_page, font=v_smallfont, background="lightblue", foreground='black').pack(side='top')
	Label(mainMenu, text=attendance_page, font=v_smallfont, background="lightblue", foreground='black').pack(side='top')
	Label(mainMenu, text=inspect_page, font=v_smallfont, background="lightblue", foreground='black').pack(side='top')
	
	Label(mainMenu, text="", bg="#708090").pack()

 
	
	
	### Enables the user to note down any infromations
	global textinfo	
	textinfo = Text(mainMenu)
	textinfo.insert(INSERT,"Note down any temporary infromation in this section. when 'Exit' button is interacted with, the system will close and any information in the notes section will be sent to the admin team")
	textinfo.pack(side='top')
	
 	### This function is used to save the notes into a text file.
	def save_text():
		text_file = open("Temp Note.txt", 'w')
		text_file.write(textinfo.get(1.0,END))
		text_file.close()
  
	### This function is used to create the clocks automatic 'tick', every second it loops to create the indefinate loop of the time.
	def clock_Tick():
		current_time2 = "Time: " + datetime.now().strftime('%H:%M:%S')
		clock.configure(text=current_time2)
		clock.after(200, clock_Tick) 
	
	clock_Tick()
	
 	### All the events that i want the program to do when its closed is in this function. which is then passed when the exit button is clicked.
	def closeFRAS():
		save_text()
		send_Email.sendTempNoteEmail(tName)
		exit()
	
	Button(mainMenu, text="Exit", command=closeFRAS, bg='#708090',activebackground='#708090',border=0).pack()

	Button(mainMenu, image=open_button_img,bg='#708090', activebackground='#708090', border=0, command=side_bar).place(x=620,y=5)
	mainMenu.mainloop()

### This function is used for the side menu bar, it allows the user to generate the other pages when navigating on the home screen.
def side_bar():

	global sideBar
	sideBar = Frame(mainMenu, background="#3e6082", width= 350, height=700)
	sideBar.place(x=350,y=0)
	
	def deleteSide():
		sideBar.destroy()
	
	def change_page(x,y,text,bcolor,fcolor, cmd):
		def hoverOn(e):
			mybutton['background']= bcolor
			mybutton['foreground']= "#3e6082"
		def hoverOff(e):
			mybutton['background']=bcolor
			mybutton['foreground']=bcolor

		mybutton=Button(sideBar,width=32, height=2,text=text,
						fg="#3e6082",
						bg="#3e6082",
						border=0,
						activeforeground=fcolor,
						activebackground=bcolor, 
						command= cmd)
		mybutton.pack()
		
		mybutton.bind("<Enter>", hoverOn)
		mybutton.bind("<Leave>", hoverOff)
		
		mybutton.place(x=x,y=y)
	
	currentDir = os.getcwd()
	global close_button_img
	close_button_img = ImageTk.PhotoImage(Image.open(currentDir+"/images/Round_X.png"))
	
	Button(sideBar, image=close_button_img, activebackground='#3e6082', border=0 ,command=deleteSide).place(x=270,y=5)
	
	change_page(15,100,"R E G I S T E R ","#3e6082",'#708090',Register_page)    
	change_page(15,150,"A T T E D A N C E","#3e6082",'#708090',Face_Recognition.facialRecognitionSystem)    
	change_page(15,200,"I N S P E C T","#3e6082",'#708090',Attendance_graphs.showAttendance)    




### colour pallate

'''slategray // THIS IS USED FOR BACKGROUND OF MAIN MENU
#708090
rgb(112,128,144)

# THIS WILL BE USED FOR BACKGROUND OF MENU BAR / SIDE MENU
# #3e6082

tomato
#FC644D
rgb(252,100,77)

whitesmoke
#F5F5F5
rgb(245,245,245)'''