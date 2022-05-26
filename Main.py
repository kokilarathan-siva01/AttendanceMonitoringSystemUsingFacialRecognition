
from tkinter import *
from tkinter import messagebox
import side_windows
import employee_database
from PIL import ImageTk
from PIL import Image
import os

### This function will be used to retrive information about the corresponding teaching given the userID
def getTecherName(userID):
      alldetail = employee_database.GetTeacherName(userID)
      global currentTeacher
      currentTeacher = str(alldetail[2] +" "+ alldetail[3])
      return currentTeacher

# Deletes the information contained in the entry fields.
def deleteEntry():
      signup_userID_ent.delete(0,END)
      signup_password_ent.delete(0,END)
      confirmPass_ent.delete(0,END)
      forename_ent.delete(0,END)
      surname_ent.delete(0,END)
      email_ent.delete(0,END)
      code_ent.delete(0,END)

# used to verify the signup process and check if all the fields are correct.
def verify_signup():
      
      authorisation_code = "123456789"
      userIDinfo = signup_userID.get()
      passwordinfo = signup_password.get()
      confirmPassinfo = confirmPass.get()
      forenameinfo = forename.get()
      surnameinfo = surname.get()
      genderinfo = gender.get()
      emailinfo = email.get() 
      codeinfo = code.get()
      
      
      signup_password_ent.config(background='#D3D3D3')
      confirmPass_ent.config(background='#D3D3D3')
      code_ent.config(background='#D3D3D3')
      
      list_info = {'userID': userIDinfo,'password': passwordinfo,'confirmPassword':confirmPassinfo,'forename':forenameinfo,
                   'surname':surnameinfo,'gender':genderinfo,'email':emailinfo,'code':codeinfo}
      
      column_names = ['userID','password','confirmPassword','forename','surname','gender','email','code']
      counter = 0
      warn_mess = "Please fill in the following blank entries: \n"
      
      ### If loop used to check if all the entry boxes are filled in
      for i in range(len(column_names)):
            if not list_info[column_names[i]]:
                  warn_mess += "({0}) ".format(i+1) + column_names[i] + "\n"
            else:
                  counter += 1
      ### Checking both password are same and output the results                      
      if counter == len(list_info):
            if codeinfo == authorisation_code:
                  if passwordinfo == confirmPassinfo:
                        deleteEntry()
                        employee_database.update_data(userIDinfo,passwordinfo,forenameinfo,surnameinfo,genderinfo,emailinfo)
                        messagebox.showinfo("SUCCESS", message="Sign Up Process Compeleted Successfully.")
                  else:
                        signup_password_ent.delete(0,END)
                        confirmPass_ent.delete(0,END)
                        signup_password_ent.config(background="orange")
                        confirmPass_ent.config(background="orange")
                        messagebox.showwarning("INVALID", message="Passwords do not match. Please Try Again.")
            else: 
                  code_ent.delete(0,END)
                  messagebox.showwarning("INVALID", message="Authorisation code is invalid. Please Try Again.")
                  code_ent.config(background="orange")
      else:       
            messagebox.showwarning("Warning", message=warn_mess)
                  
              
            
### This function is used to verify when a user logins into the system.
def verify_login():
      
      allUser, allPass = employee_database.getUserPass()
      userIDinfo = login_userID.get()
      passwordinfo = login_password.get()
      
      login_userID_ent.delete(0, END)
      login_password_ent.delete(0, END)
      
      ### if loops to check if userID and password matches 
      if userIDinfo in allUser:
            if passwordinfo in allPass:
                  tName = getTecherName(userIDinfo)
                  with open('currentUser.txt', 'w') as f: ### This statement will save the user's/teacher's name into a file which i can then use to display it on the main menu.
                        f.write(tName)
                  messagebox.showinfo("SUCCESS", message="Login Successful")
                  screen_login.destroy()
                  main_Screen.destroy()
                  side_windows.splash_popup()
            else:
                  messagebox.showwarning("INVALID", message="Invalid Password")
      else:
            messagebox.showwarning("INVALID", message="Invalid UserID")
            
            

# Function which will enables the teacher to sign up
def signUp():
    global screen_signup
    screen_signup = Toplevel(main_Screen)
    screen_signup.title("Sign Up")
    screen_signup.geometry("700x700")
    screen_signup.resizable(0,0)
    screen_signup.config(bg="medium sea green")
    Label(screen_signup, text="Please Sign Up using your credentials (Teachers ONLY!)", 
          bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
    
    global signup_userID
    global signup_password
    global confirmPass
    global forename
    global surname
    global gender
    global email
    global code # used for authorising, to make sure that only the authorised people are creating new accounts.
    
    global signup_userID_ent
    global signup_password_ent
    global confirmPass_ent
    global forename_ent
    global surname_ent
    global email_ent
    global code_ent
    
    # since these variables will be changing, therefore, I am using Var().
    signup_userID = StringVar()
    signup_password = StringVar()
    confirmPass = StringVar()
    forename = StringVar()
    surname = StringVar()
    gender = StringVar()
    email = StringVar()
    code = StringVar()
    
    gender_temp = ["Male", "Female", "Other"]
    Label(screen_signup, bg="medium sea green", text="").pack() # Instead of padx or pady, used another lable with blank space to generate space.


    Label(screen_signup, bg="medium sea green", text="User ID").pack()
    signup_userID_ent = Entry(screen_signup, textvariable= signup_userID)
    signup_userID_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()

    Label(screen_signup, bg="medium sea green", text= "Password").pack()
    signup_password_ent = Entry(screen_signup, textvariable= signup_password, show='*')
    signup_password_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()
    
    Label(screen_signup, bg="medium sea green", text= "Confirm Password").pack()
    confirmPass_ent = Entry(screen_signup, textvariable= confirmPass, show='*')
    confirmPass_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()
    
    Label(screen_signup, bg="medium sea green", text= "Forename").pack()
    forename_ent = Entry(screen_signup, textvariable= forename)
    forename_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()
    
    Label(screen_signup, bg="medium sea green", text= "Surname").pack()
    surname_ent = Entry(screen_signup, textvariable= surname)
    surname_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()
    
    Label(screen_signup, bg="medium sea green", text= "Email").pack()
    email_ent = Entry(screen_signup, textvariable= email)
    email_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()
    
    Label(screen_signup, bg="medium sea green", text="Authorisation Code").pack()
    code_ent = Entry(screen_signup, textvariable= code, show='*')
    code_ent.pack()
    Label(screen_signup, bg="medium sea green", text="").pack()
    
    Label(screen_signup, bg="medium sea green", text= "Gender").pack()
    gender_frame = Frame(screen_signup, bg="pale green", bd=1, relief="groove")
    gender_frame.pack()
    Label(screen_signup, bg="medium sea green",text="").pack 
    
    for i in gender_temp:  
      gender_but = Radiobutton(gender_frame, bg="pale green", text= i, variable=gender, value=i)
      gender_but.pack(side="left")
      
    Button(screen_signup, bg="medium sea green", text ="Sign Up", height="2", width= "10", command=verify_signup).pack()
    Button(screen_signup, bg="medium sea green", text ="Exit", height="3", width= "20", command=screen_signup.destroy).pack()
    
    screen_signup.mainloop()
    
# login into the system using existing information / accounts.
def logIn():
    global screen_login
    screen_login = Toplevel(main_Screen)
    screen_login.title("Login")
    screen_login.geometry("700x700")
    screen_login.resizable(0,0)
    screen_login.config(bg="medium sea green")
    Label(screen_login, text="Please Login using your valid credentials", 
          bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
    
    global login_userID
    global login_password
    
    global login_userID_ent
    global login_password_ent
    
    login_userID = StringVar()
    login_password = StringVar()
    
    Label(screen_login, bg="medium sea green", text="User ID").pack()
    login_userID_ent = Entry(screen_login, textvariable= login_userID)
    login_userID_ent.pack()
    Label(screen_login, bg="medium sea green", text="").pack()
    
    Label(screen_login, bg="medium sea green", text= "Password").pack()
    login_password_ent = Entry(screen_login, textvariable= login_password, show='*')
    login_password_ent.pack()
    Label(screen_login, bg="medium sea green", text="").pack() 
    
    
    Button(screen_login, bg="medium sea green", text ="Login", height="2", width= "10", command= verify_login).pack()
    Button(screen_login, bg="medium sea green", text ="Exit", height="3", width= "20", command=screen_login.destroy).pack()
    
    currentDir = os.getcwd()
    login_image = ImageTk.PhotoImage(Image.open(currentDir+"/images/login.png"))
    Label(screen_login, bg="medium sea green", text="").pack() 
    Label(screen_login, bg="medium sea green", text="").pack()  
    Button(screen_login, image=login_image, activebackground='#3e6082', border=0).pack()
    
    screen_login.mainloop()

### Main function which will Initiate the program, as this will connect to all the other parts of the program.
### The main screen tkinter screen will the parent screen to other screen that pops up, hence, the other screens are implemented as the toplevel to main_Screen.
def main():
    global main_Screen
    main_Screen = Tk()
    main_Screen.geometry("700x700")
    main_Screen.resizable(0,0)
    main_Screen.title("Welcome to AutoAtendie")
    main_Screen.config(bg="medium sea green")
    Label(text="Welcome To Attendace Monitoring System using Face Recognition",
          bg="grey", width="300", height= "2", font =("Ariel", 20)).pack()
    Label(text="", bg="medium sea green").pack()
    Label(text="", bg="medium sea green").pack()
    Label(text="", bg="medium sea green").pack()
    Label(text="", bg="medium sea green").pack()
    Button(text= "Login", width="60", height="8",bg="medium sea green", command=logIn).pack()
    Label(text="", bg="medium sea green").pack()
    Button(text= "Sign up", width="60", height="8",bg="medium sea green", command=signUp).pack()
    Label(text="", bg="medium sea green").pack()
    Button(text= "Exit", width="60", height="8",bg="medium sea green", command=exit).pack()
    
    main_Screen.mainloop()

### Run the main() program 
if __name__ == "__main__":
    main()