from cProfile import label
from cgitb import text
from glob import glob
from struct import pack
from tkinter import *
from tkinter import messagebox



def employer_signup():
      
      authorisation_code = "123456789"
      userIDinfo = userID.get()
      passwordinfo = password.get()
      emailinfo = email.get() 
      codeinfo = code.get()
      
      if codeinfo == authorisation_code:
            # Change this section later to connect with the database.
            file = open(userIDinfo+".txt", "w")
            file.write(userIDinfo)
            file.write(passwordinfo)
            file.write(emailinfo)
            file.close()
            
            userID_ent.delete(0,END)
            password_ent.delete(0,END)
            email_ent.delete(0,END)
            code_ent.delete(0,END)
            
            Label(screen_signup,text = "Sign Up Process Compeleted Successfully.", fg="green", font=("Ariel", 12)).pack()
      else:
            userID_ent.delete(0,END)
            password_ent.delete(0,END)
            email_ent.delete(0,END)
            code_ent.delete(0,END)
            Label(screen_signup,text = "Authorisation code is invalid. Please Try Again.", fg="red", font=("Ariel", 12)).pack()
            
      
      
      
      
      



# Function which will enables the teacher to sign up
def signUp():
    global screen_signup
    screen_signup = Toplevel(main_Screen)
    screen_signup.title("Sign Up")
    screen_signup.geometry("700x700")
    Label(screen_signup, text="Please Sign Up using your credentials (Teachers Use ONLY!)", 
          bg="green", width="300", height= "2", font =("Ariel", 12)).pack()
    
    global userID
    global password
    global email
    global code
    global userID_ent
    global password_ent
    global email_ent
    global code_ent
    
    userID = StringVar()
    password = StringVar()
    email = StringVar()
    code = StringVar()
    
    Label(screen_signup, text="User ID").pack()
    Label(screen_signup, text="").pack()
    userID_ent = Entry(screen_signup, textvariable= userID)
    userID_ent.pack()

    Label(screen_signup, text= "Password").pack()
    Label(screen_signup, text="").pack()
    password_ent = Entry(screen_signup, textvariable= password)
    password_ent.pack()
    
    Label(screen_signup, text= "email").pack()
    Label(screen_signup, text="").pack()
    email_ent = Entry(screen_signup, textvariable= email)
    email_ent.pack()
    
    Label(screen_signup, text="Authorisation Code").pack()
    Label(screen_signup, text="").pack()
    code_ent = Entry(screen_signup, textvariable= code)
    code_ent.pack()
    
    Button(screen_signup, text ="Sign Up", height="2", width= "10", command=employer_signup).pack()
    
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