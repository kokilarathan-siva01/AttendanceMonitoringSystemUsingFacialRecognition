from cProfile import label
from cgitb import text
from struct import pack
from tkinter import *


def teacher_signup():
      allUserID = userID.get()
      allPassword = password.get()



# Function which will enables the teacher to sign up
def signUp():
    screen_signup = Toplevel(main_Screen)
    screen_signup.title("Sign Up")
    screen_signup.geometry("700x700")
    Label(screen_signup, text="Please Sign Up using your credentials (Teachers Use ONLY!)", 
          bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
    
    global userID
    global password
    global confirmPass
    userID = StringVar()
    password = StringVar()
    confirmPass = StringVar()
    
    Label(screen_signup, text="User ID").pack()
    Label(screen_signup, text="").pack()
    Entry(screen_signup, textvariable= userID).pack()
    
    Label(screen_signup, text= "Password").pack()
    Label(screen_signup, text="").pack()
    Entry(screen_signup, textvariable= password).pack()
    
    Label(screen_signup, text= "Confirm Password").pack()
    Label(screen_signup, text="").pack()
    Entry(screen_signup, textvariable= confirmPass).pack()
    
    Button(screen_signup, text ="Sign Up", height="2", width= "10").pack()
    
    screen_signup.mainloop()
    
# login into the system using existing information / accounts.
def logIn():
    screen_login = Toplevel(main_Screen)
    screen_login.title("Login")
    screen_login.geometry("700x700")
    Label(screen_login, text="Please Login using valid credentials", 
          bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
    
    userID = StringVar()
    password = StringVar()
    
    Label(screen_login, text="User ID").pack()
    Label(screen_login, text="").pack()
    Entry(screen_login, textvariable= userID).pack()
    
    Label(screen_login, text= "Password").pack()
    Label(screen_login, text="").pack()
    Entry(screen_login, textvariable= password).pack()
    
    
    Button(screen_login, text ="Login", height="2", width= "10").pack()
    
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