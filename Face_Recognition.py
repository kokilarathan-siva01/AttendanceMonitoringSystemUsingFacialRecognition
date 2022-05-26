from datetime import datetime
import cv2
import os
import numpy as np
from PIL import Image
import student_database
import csv
from datetime import datetime
from datetime import date
import send_Email

currentDIR = os.getcwd()
### The following file was taken from a "free to use" github repo. inked below -->
### https://github.com/kipr/opencv/tree/master/data/haarcascades
### this is used to detect facial feature of a human's face
### especially features like the eyes, nose, and mouths, as this is what I'm mainly using to recognise a person.
faceRecognitionClassifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

### This function allows the function to capture "32", in this case images of the student to preform the training.
### when a student id is provide, the program takes 32 picture using the main camera and stores them as the the student id, which is needed later on.
def RegisterStudentImage(id):
    video_cam=cv2.VideoCapture(0)
    binSize=0 # The amount of pictures to be taken, the more the greater the accuracy but process time also increase.
    
   # if not os.path.exists("studentImages/"+id):
    #    os.makedirs("studentImages/"+id)
    
    while(binSize<33):
        ret,img=video_cam.read()
        image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face_detec =faceRecognitionClassifier.detectMultiScale(image,1.3,5)
        for(x,y,w,h)in face_detec:
            binSize += 1
            cv2.imwrite("studentImages/Students."+str(id)+"."+str(binSize)+".jpg",image[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.waitKey(100);
        cv2.imshow("Caputering Face",img)
        cv2.waitKey(1);

    video_cam.release()
    cv2.destroyAllWindows()

    

detector = cv2.face.LBPHFaceRecognizer_create()  ### using openCV built in function to detect and recognise faces, and this funciton also needed to be accompanied with the haarcascade file.

### The next two functions are used to train the student's faces into the system and store them as a single ymal file.
### This function will gather all the images in the images file of the students, and the assign them to their respective student ID by spliting and formatting the name of the image file.
def GetStudentImages():
    loc = 'studentImages'
    ### Since everytime a new person is added, a .DS_store file is created, therefore this if loop is used to delete that file.
    if os.path.exists("studentImages/.DS_Store"):
        os.remove("studentImages/.DS_Store")
    studentImages=[os.path.join(loc,f)for f in os.listdir(loc)] # getting all the image files into one list to loop through
    #studentImages.pop(0) # since working on a mac, "/.DS_Store'," this file will be created without user's visibility, to remove this unwanted file from the list, this operation is done.
    studentFaces=[]
    studentIDs=[]
    for students in studentImages:
        studentFace =Image.open(students).convert('L'); # converting the image to a gray scale if not already one, for recognition purpose
        studentfaceNP=np.array(studentFace,'uint8')
        ID=int(os.path.split(students)[-1].split('.')[1]) # getting the ID of the student by splitting the name of the file name and getting what I want
        studentFaces.append(studentfaceNP)
        #print(ID) // this should be enables if the Id of the student needed to be shown
        studentIDs.append(ID)
        #cv2.imshow("training",studentfaceNP) // This should be enables if the training process wanted to be seen by the user.
        cv2.waitKey(10)
    return studentFaces, studentIDs 

### This function will train all the images of the student with their respective studenID, and also same that information as a ymal file in the designated folder.
def trainStudentFaces():
    studentFaces, studentIDs=GetStudentImages()
    detector.train(studentFaces,np.array(studentIDs))
    detector.save('TrainedStudentData/trainedStudentData.yml') # yml or ymal file used to compressed all the student image data into one single file for identification purpose
    cv2.destroyAllWindows()


### This function is the main Face Recognition system which will gather information from the ymal file create before and use that to identify the person on the camera.
def facialRecognitionSystem():
    '''
    This is used to clear the attendance.csv file once the monitoring processing is restarted .
    also this set of code will add the headers for the csv file.
    '''
    run = 0
    if run == 0:
        clearCSVfile()
        run = 1
    video_cam=cv2.VideoCapture(0)
    # "TrainedStudentData\trainedStudentData.yml"
    detector.read('TrainedStudentData/trainedStudentData.yml') # the ymal file with all the students information
    
    studentid = 0
    
    textFont = cv2.FONT_HERSHEY_SIMPLEX
    textScaleFont = 1
    textColourFont = (255,255,255)
    ### While loop is initated to keep the camera on until the user click on "q"
    while(True):
        _, studentImage=video_cam.read()
        grayScale = cv2.cvtColor(studentImage,cv2.COLOR_BGR2GRAY)
        studentFace = faceRecognitionClassifier.detectMultiScale(studentImage,1.3,5) ### the method detectMiltiScale i
        ### Also this for loop will enalbes the recognition to take place frame by frame.
        for(x,y,w,h)in studentFace:
            cv2.rectangle(studentImage,(x,y),(x+w,y+h),(0,255,0),2) ### This is used to create the border around the face which will then be recognised and displayed
            studentid,temp =detector.predict(grayScale[y:y+h, x:x+w]) ### recognise the student and get their student id and image.
            allNames = student_database.GetStudentInfo(studentid) ### get the students detail like nameto display using the recognised student id
            markedList = []
            run_time = 0
            if allNames != None: ### infinite loop of displaying their names frame by frame until the program is exited. since allNames will not none, this loop will be infinite.
                cv2.putText(studentImage,str(allNames[0]),(x,y+h+30),textFont,textScaleFont,textColourFont) 
                cv2.putText(studentImage,(str(allNames[1])+" "+str(allNames[2])),(x,y+h+60),textFont,textScaleFont,textColourFont)
                monitorAttendance(allNames[0],allNames[1],allNames[2])
                
        cv2.imshow("Monitoring Attendance", studentImage)
        
        if(cv2.waitKey(1)==ord('q')):
            ### When the user clicks 'q' the attendnace report is sent to the admin team, any student who wasnt recorded will be marked as absent and an email will be sent.
            send_Email.sendAttendaceReportEmail()
            send_Email.sendAllAbsent()
            break
    video_cam.release()
    cv2.destroyAllWindows()


'''
### The next sets of code will enable the system to take attendace while face recognition is enabled.
'''

### recording the attendance when the camera is up and running
def monitorAttendance(studentID,firstName,lastName):
    
    currTime = datetime.now()
    formatTime = currTime.strftime("%H:%M") 
    
    with open("Attendance/Attendance.csv", "r+") as file:
        dataList = file.readlines()
        s_IDs = []
        
        for i in dataList:
            temp = i.split(',')
            s_IDs.append(temp[0]) 
        
        ### This loop is used to stop mutiple entry of the same student for a single session of monitoring.
        if studentID not in s_IDs:
            file.writelines(f'\n{studentID},{firstName},{lastName},{formatTime}')

### used to create a new csv file whenever a new session is initated. (HAVE NOT USED YET, MAY NOT BE NEEDED IF I USE THE SAME CSV FILE)
def createCSVfile():
    todayDate = date.today()
    formatDate = todayDate.strftime("%d-%b-%Y")
    fileName = (formatDate + ".csv")
    # creating a new file directory if it doesnt exist
    if os.path.exists("Attendance/"):
        os.chdir("Attendance/") # changing the current directory to save the attendace files into that.
    # headers to be inserted into the new csv file everytime its created 
    headers = ['StudentID', 'Firstname', 'Lastname', 'Time']
    with open (fileName, 'w') as file:
        insertion = csv.writer(file)
        insertion.writerow(headers)
    return fileName

### This function will create a new csv file and clear all the previous information when a new monitoring session is started.
### also the header will be automatically added so that it can be easier to analyse later on, or when a new person is looking at the document. 
def clearCSVfile():
        file = open("Attendance/Attendance.csv", "w+")
        writer = csv.DictWriter(
                file, fieldnames=['StudentID', 'Firstname', 'Lastname', 'Time'])
        writer.writeheader()
        file.close()

