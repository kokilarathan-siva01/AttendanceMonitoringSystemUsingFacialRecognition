### This file is used to create a .dmg file for MAC OSX users. it will create a single file which can be run on any mac device, without any code files.
##########
# ONLY TO BE USED BY MAC OSX USERS.
#########
from setuptools import setup

APP=['Main.py']

DATA_FILES = ['currentUser.txt', 'haarcascade_frontalface_default.xml','Temp Note.txt','trainedStudentData.yml'
                            ,'Attendance.csv','Employee_Data.db','Student_Data.db']
OPTIONS = {
    'argv_emulation': True,
    
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options ={'py2app': OPTIONS},
    setup_requires=['py2app']
)