
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, color
from warnings import warn_explicit
import side_windows
import employee_database
import os

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
      
      list_info = {'userID': userIDinfo,'password': passwordinfo,'confirmPassword':confirmPassinfo,'forename':forenameinfo,
                   'surname':surnameinfo,'gender':genderinfo,'email':emailinfo,'code':codeinfo}
      
      column_names = ['userID','password','confirmPassword','forename','surname','gender','email','code']
      counter = 0
      warn_mess = []
      for i in range(len(column_names)):
            if not list_info[column_names[i]]:
                  warn_mess.append(column_names[i]) 
            else:
                  counter += 1
                                
      if counter == len(list_info):
            if codeinfo == authorisation_code:
                  if passwordinfo == confirmPassinfo:
                        deleteEntry()
                        employee_database.update_data(userIDinfo,passwordinfo,forenameinfo,surnameinfo,genderinfo,emailinfo)
                        Label(screen_signup,text = "Sign Up Process Compeleted Successfully.", fg="green", font=("Ariel", 12)).pack()
                        
                  else:
                        signup_password_ent.delete(0,END)
                        confirmPass_ent.delete(0,END)
                        signup_password_ent.config(background="orange")
                        confirmPass_ent.config(background="orange")
                        Label(screen_signup,text = "Passwords do not match. Please Try Again.", fg="orange", font=("Ariel", 12)).pack()
                        
            else: 
                  code_ent.delete(0,END)
                  Label(screen_signup,text = "Authorisation code is invalid. Please Try Again.", fg="red", font=("Ariel", 12)).pack()
                  code_ent.config(background="orange")
      else:
            wanring = "Please fill in the following blank entries: \n"
            for i in range(len(warn_mess)):
                  wanring += "({0}) ".format(i+1) + warn_mess[i] + "\n"
            messagebox.showwarning("Warning", message=wanring)
                  
              
            

def verify_login():
      
      allUser, allPass = employee_database.getUserPass()
      userIDinfo = login_userID.get()
      passwordinfo = login_password.get()
      
      login_userID_ent.delete(0, END)
      login_password_ent.delete(0, END)
      
      if userIDinfo in allUser:
            if passwordinfo in allPass:
                  Label(screen_login,text = "Login Successful", fg="green", font=("Ariel", 12)).pack()
                  screen_login.destroy()
                  main_Screen.destroy()
                  side_windows.splash_popup()
            else:
                  Label(screen_login,text = "Invalid Password", fg="red", font=("Ariel", 12)).pack()
      else:
            Label(screen_login,text = "Invalid UserID", fg="red", font=("Ariel", 12)).pack()
            # these code should be in the login success area ######
            
            
            
            
      

# Function which will enables the teacher to sign up
def signUp():
    global screen_signup
    screen_signup = Toplevel(main_Screen)
    screen_signup.title("Sign Up")
    screen_signup.geometry("700x700")
    Label(screen_signup, text="Please Sign Up using your credentials (Teachers Use ONLY!)", 
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
    Label(screen_signup, text="").pack() # Instead of padx or pady, used another lable with blank space to generate space.

    Label(screen_signup, text="User ID").pack()
    signup_userID_ent = Entry(screen_signup, textvariable= signup_userID)
    signup_userID_ent.pack()
    Label(screen_signup, text="").pack()

    Label(screen_signup, text= "Password").pack()
    signup_password_ent = Entry(screen_signup, textvariable= signup_password, show='*')
    signup_password_ent.pack()
    Label(screen_signup, text="").pack()
    
    Label(screen_signup, text= "Confirm Password").pack()
    confirmPass_ent = Entry(screen_signup, textvariable= confirmPass, show='*')
    confirmPass_ent.pack()
    Label(screen_signup, text="").pack()
    
    Label(screen_signup, text= "Forename").pack()
    forename_ent = Entry(screen_signup, textvariable= forename)
    forename_ent.pack()
    Label(screen_signup, text="").pack()
    
    Label(screen_signup, text= "Surname").pack()
    surname_ent = Entry(screen_signup, textvariable= surname)
    surname_ent.pack()
    Label(screen_signup, text="").pack()
    
    Label(screen_signup, text= "Email").pack()
    email_ent = Entry(screen_signup, textvariable= email)
    email_ent.pack()
    Label(screen_signup, text="").pack()
    
    Label(screen_signup, text="Authorisation Code").pack()
    code_ent = Entry(screen_signup, textvariable= code, show='*')
    code_ent.pack()
    Label(screen_signup, text="").pack()
    
    Label(screen_signup, text= "Gender").pack()
    gender_frame = Frame(screen_signup, bd=1, relief="groove")
    gender_frame.pack()
    Label(screen_signup,text="").pack 
    
    for i in gender_temp:  
      gender_but = Radiobutton(gender_frame, text= i, variable=gender, value=i)
      gender_but.pack(side="left")
      
    Button(screen_signup, text ="Sign Up", height="2", width= "10", command=verify_signup).pack()
    
    screen_signup.mainloop()
    
# login into the system using existing information / accounts.
def logIn():
    global screen_login
    screen_login = Toplevel(main_Screen)
    screen_login.title("Login")
    screen_login.geometry("700x700")
    Label(screen_login, text="Please Login using your valid credentials", 
          bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
    
    global login_userID
    global login_password
    
    global login_userID_ent
    global login_password_ent
    
    login_userID = StringVar()
    login_password = StringVar()
    
    Label(screen_login, text="User ID").pack()
    login_userID_ent = Entry(screen_login, textvariable= login_userID)
    login_userID_ent.pack()
    Label(screen_login, text="").pack()
    
    Label(screen_login, text= "Password").pack()
    login_password_ent = Entry(screen_login, textvariable= login_password, show='*')
    login_password_ent.pack()
    Label(screen_login, text="").pack()
    
    
    Button(screen_login, text ="Login", height="2", width= "10", command= verify_login).pack()
    
    screen_login.mainloop()


def main():
    global main_Screen
    main_Screen = Tk()
    main_Screen.geometry("700x700")
    main_Screen.title("Welcome")
    Label(text="Welcome To Attendace Monitoring System",
          bg="grey", width="300", height= "2", font =("Ariel", 12)).pack()
    Label(text="").pack()
    Button(text= "Login", width="30", height="2", command=logIn).pack()
    Label(text="").pack()
    Button(text= "Sign up", width="30", height="2", command=signUp).pack()
    
    main_Screen.mainloop()

main()