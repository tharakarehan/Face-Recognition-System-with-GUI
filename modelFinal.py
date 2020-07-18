#importing libraries
import PIL
from PIL import Image,ImageTk,ImageEnhance
import cv2
import sys
if "Tkinter" not in sys.modules:
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
import os
import csv
import pandas as pd
import numpy as np
import statistics 
from statistics import mode 
import shutil



#global variable
global Name
global sample_count
global ID
global DetectMode
global W
global lside
global lbright
global s1
global ListDetect
global Info
global label2
global label3
global label4
global label5
global label6
global Ck2
global Ck3
global Ck4
global Ck7
global face_count

face_count=0
sample_count=100
DetectMode=False
W=False



###############################################################
#this function extracts the person's unique iD from the image name and return it with the image
#Use to make the dataset for the recognizer to train upon
def getImagesAndLabels(path): 
    # get the path of all the files in the folder 
    imagePaths =[os.path.join(path, f) for f in os.listdir(path)]  
    faces =[] 
    # creating empty ID list 
    Ids =[] 
    # now looping through all the image paths and loading the 
    # Ids and the images saved in the folder 
    for imagePath in imagePaths:
        if not(imagePath[15:]=='.DS_Store'):
            # loading the image and converting it to gray scale 
            pilImage = PIL.Image.open(imagePath).convert('L') 
            # Now we are converting the PIL image into numpy array 
            imageNp = np.array(pilImage, 'uint8') 
            # getting the Id from the image 
            Id = int(os.path.split(imagePath)[-1].split(".")[1]) 
            # extract the face from the training image sample 
            faces.append(imageNp) 
            Ids.append(Id)         
    return faces, Ids 

#######################################################################

#these are used to handle the text entry boxes

def focus1(event): 
    # set focus on the name_field box 
    name_field.focus_set()  
  
# Function to set focus 
def focus2(event): 
    # set focus on the age_field box 
    age_field.focus_set() 
  
# Function to set focus 
def focus3(event): 
    # set focus on the address_field box 
    address_field.focus_set() 
def clear(): 
    # clear the content of text entry box 
    username_field.delete(0, END) 
    name_field.delete(0, END) 
    age_field.delete(0, END) 
    address_field.delete(0, END)
    print("Done")
#########################################################################   
#inserting user information into the csv file
def insert():
    global Name
    global sample_count
    global ID
    data=pd.read_csv("Data.csv")
    
      
    # if user not fill any entry 
    # then show error message 
    if (username_field.get() == "" or
        name_field.get() == "" or
        age_field.get() == "" or
        address_field.get() == "" ): 
              
        messagebox.showerror(title="Message", message="Please fill out all the information",icon='error')
    elif(username_field.get() in list(data['UserID']) ): #if the username is used again by someone else error message
        messagebox.showerror(title="Message", message="This UserID is already taken",icon='error')
  
    else: 
        ID+=1
        row = [ID,username_field.get(),name_field.get(),age_field.get(),address_field.get()]  
        with open('Data.csv', 'a+') as csvFile: 
            writer = csv.writer(csvFile) 
            # Entry of the row in csv file 
            writer.writerow(row)  
        csvFile.close()
        Name=name_field.get()
        username_field.focus_set()
        #By setting sample_count=0, you can snap some pictures of particular people.
        sample_count=0
        clear()
#####################################################################       

#enabling decting mode. Also train the recognizer
def Detect():
    global DetectMode
    global ListDetect
    global Info
    ListDetect=[]
    Info="Detecting......."
    data=pd.read_csv("Data.csv")
    Count=len(data["ID"])
    if Count==0:
        messagebox.showerror(title="Message", message="Database is Empty",icon='error')
    elif Count==1:
        messagebox.showerror(title="Message", message="Add at least two data records",icon='error')
        
    else:
        faces, Id = getImagesAndLabels("TrainingImages")
        if 'Trainner.yml' not in os.listdir('TrainingImageLabel'):
            recognizer.train(faces, np.array(Id))      
            recognizer.save("TrainingImageLabel/Trainner.yml")
            messagebox.showinfo(title="Message", message="Finished Training",icon='info')
            file1 = open("TrainingImageLabel/Counter.txt","w") 
            file1.write(str(Count)) 
            file1.close() 
        else:
            file1 = open("TrainingImageLabel/Counter.txt") 
            R=file1.readlines(0)
            file1.close()
            CountV=int(R[0])

            if Count==CountV:
                recognizer.read("TrainingImageLabel/Trainner.yml")


            else:
                file1 = open("TrainingImageLabel/Counter.txt","w") 
                file1.write(str(Count)) 
                file1.close() 
                recognizer.train(faces, np.array(Id))      
                recognizer.save("TrainingImageLabel/Trainner.yml")
                messagebox.showinfo(title="Message", message="Finished Training",icon='info')

        DetectMode=True
########################################################################   
#accessing Monitor Mode      
def Monitor():
    global DetectMode
    DetectMode=False
########################################################################        
#loading images from profile folders (to show when a person is recognized)
def ProfileLoad(N):
    try:
    
        pilImage = PIL.Image.open('ProfileImages/ '+str(N)+".jpg")
        pilImage = pilImage.resize((250, 250), PIL.Image.ANTIALIAS)
        imgTK = ImageTk.PhotoImage(image=pilImage)
        return imgTK
    except:
        pass
#loading images from profile folders (to show in the database management system)
def ProfileLoad1(N):
    try:
    
        pilImage = PIL.Image.open('ProfileImages/ '+str(N)+".jpg")
        pilImage = pilImage.resize((150, 150), PIL.Image.ANTIALIAS)
        imgTK = ImageTk.PhotoImage(image=pilImage)
        return imgTK    
    except:
        pass
######################################################################## 

#showing the information and the photos of the system users
def DataBaseManagement():
    global DetectMode
    DetectMode=False
    data4=pd.read_csv("Data.csv")
    Plist=[]

    #loading images to be shown from the ProfileImages folder
    for i in range(len(data4["ID"])):
        Plist.append(ProfileLoad1(i+1))
        
    def data():
        for i in range(len(data4["ID"])):
            label=Label(frame)
            label.grid(row=i,column=0)
            imgx = Plist[i]
            label.imgx=imgx
            label.configure(image=imgx)

            Txt='Username :  '+str(data4.at[i,"UserID"])+"\n"+'Name        :  '+str(data4.at[i,"Name"])+"\n"+'Age           :  '+str(data4.at[i,"Age"])+"\n"+'Address    :  '+str(data4.at[i,"Address"])
            Label(frame,text=Txt,height=4,bg='light blue',justify=tk.LEFT,font=("Helvetica", 20)).grid(row=i,column=1)


    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=500)

    root=Toplevel(gui)
    sizex = 590
    sizey = 625
    posx  = 100
    posy  = 100
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    #frame
    myframe=Frame(root,relief=GROOVE,width=100,height=100,bd=1)
    myframe.place(x=35,y=50)

    #label
    label0=Label(root,bg='black',fg='white',text="Database Management System", font=("Helvetica", 25))
    label0.place(x=300, y=25,anchor='c')
    
    #button
    DeleteRecord = Button(root, text="Delete last record", fg="black", 
                                bg="red", command=Delete,height=2, width=20) 
    DeleteRecord.place(x=175, y=590,anchor='c')
    EmptyData = Button(root,bg="red", text="Empty Database",command=Empty, fg="black", 
                                height=2, width=20) 
    EmptyData.place(x=425, y=590,anchor='c')

    #canvas and scroll bar
    canvas=Canvas(myframe)
    frame=Frame(canvas)
    myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    data()
    root.mainloop()     
########################################################################   
        
#Delete the last record and the corresponding images
def Delete():
    global ID
    
    Pdata=pd.read_csv("Data.csv")
    ln=len(Pdata['ID'])
    
    if ln==0:
        messagebox.showerror(title="Message", message="No records left",icon='error')
    else:
        Nme=Pdata.at[ln-1,"Name"]
        Pdata=Pdata.drop(Pdata.index[ln-1])
        Pdata.to_csv("Data.csv",index=False,header=True)
        for j in range(1,32):
            os.remove("TrainingImages/ "+str(Nme)+"."+str(ln)+"."+str(j)+".jpg")
            
        os.remove("ProfileImages/ "+str(ln)+".jpg")
        ID=ID-1

########################################################################
#reset the database deleting all the records
def Empty():
    shutil.rmtree('TrainingImageLabel')
    os.makedirs('TrainingImageLabel')
    shutil.rmtree('ProfileImages')
    os.makedirs('ProfileImages')
    shutil.rmtree('TrainingImages')
    os.makedirs('TrainingImages')
    with open('Data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID","UserID", "Name", "Age","Address"])
########################################################################
#function to close the application      
def Quit():
    gui.destroy()
    capmain.release()
    
######################################################################## 

#this is a recursive function. at the end of the function it will call the next function
def show_Mainframe():
    global DetectMode
    global sample_count
    global W
    global lside
    global lbright
    global s1
    global ListDetect
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global Info
    global Ck2
    global Ck3
    global Ck4
    global Ck7
    global face_count

    isValid=True
    try :
        ret, framemain = capmain.read()

    except:
        print("error the take a image")
        isValid = False


    if isValid == True:
    
        framemain = cv2.flip(framemain, 1)
        framemain = cv2.resize(framemain, (400, 300))
        frameside= cv2.resize(framemain, (200, 150))
        framebright= cv2.resize(framemain, (200, 150))

        #coverting image to grayscale
        gray = cv2.cvtColor(framemain, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        #counting number of faces
        if len(faces)>0 and face_count>0:
            face_count-=1
        elif len(faces)==0 and face_count<=16:
            face_count+=1
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(framemain, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if DetectMode:
                data2=pd.read_csv("Data.csv")
                #predicting the face
                iDs, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
                # If confidence is less them 100 ==> "0" : perfect match 
                if (confidence < 100):
                    iD = data2.at[iDs-1,"Name"]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    iD = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                #collecting 10 IDs of the detected faces
                if len(ListDetect)<10:
                    if iD=='unknown':
                        ListDetect.append(str(iD))
                    else:
                        ListDetect.append(str(iDs))
                else:
                    ListDetect=[]
                
                #putting a label of the detected persons name
                cv2.putText(
                        framemain, 
                        str(iD), 
                        (x+5,y-5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1, 
                        (255,255,255), 
                        2
                       )

                #putting a label of the probability 
                cv2.putText(
                            framemain, 
                            str(confidence), 
                            (x+5,y+h-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            1, 
                            (255,255,0), 
                            1
                           )  
            
            
            #to collect data for training
            if sample_count<=30:
                sample_count+=1
                cv2.imwrite( 
                    "TrainingImages/ "+Name +'.'+str(ID)+"."+ str( 
                        sample_count) + ".jpg", gray[y:y + h, x:x + w])

                # this image is used to represent the person detected
                #this saves in the ProfileImages folder
                if sample_count==10:
                    propic=cv2.resize(frameside, (400, 300))
                    cv2.imwrite( 
                    "ProfileImages/ "+str(ID)+".jpg", propic[y-int(h/10):y + h+int(h/10), x-int(w/10):x + w+int(w/10)])
                    
                if sample_count==31:
                    messagebox.showinfo(title="Message", message="Finished taking photos",icon='info')


        cv2image = cv2.cvtColor(framemain, cv2.COLOR_BGR2RGBA)
        cv2image1 = cv2.cvtColor(frameside, cv2.COLOR_BGR2RGBA)
        cv2image2 = cv2.cvtColor(framebright, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        img1 = PIL.Image.fromarray(cv2image1)
        img2 = PIL.Image.fromarray(cv2image2)

        #this is for changing the brightness of the frames
        if v1.get()==0.0:
            img2=img2
        else:
            img2=ImageEnhance.Brightness(img2).enhance(1+2/10*v1.get() if v1.get()>0.0 else 1-1/10*(-1*v1.get()))
        
        imgtk = ImageTk.PhotoImage(image=img)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        imgtk2 = ImageTk.PhotoImage(image=img2)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        if not DetectMode:
            if label2.winfo_exists():
                label2.destroy()
                Ck2=True
            if label3.winfo_exists():
                label3.destroy()
                Ck3=True
            if label4.winfo_exists():
                print("Test")
                label4.destroy()
                label5.destroy()
                label6.destroy()
                Ck4=True
            if label7.winfo_exists():
                label7.destroy()
                Ck7=True
                
            
            if W:
                lside=Label(gui)
                lside.place(x=650, y=200,anchor='c')
                lbright=Label(gui)
                lbright.place(x=900, y=200,anchor='c')
                s1 = Scale( gui, variable = v1,  
                       from_ = -10, to = 10,  
                           orient = HORIZONTAL,length=300,width=20,tickinterval=1)
                s1.place(x=775, y=325,anchor='c')
                W=False
                
            
            lside.imgtk1 = imgtk1
            lbright.imgtk2 = imgtk2
            lside.configure(image=imgtk1)
            lbright.configure(image=imgtk2)

        else:
            data3=pd.read_csv("Data.csv")
            if lside.winfo_exists() and lbright.winfo_exists() and s1.winfo_exists():
                lside.destroy()
                lbright.destroy()
                s1.destroy()
                W=True

            if face_count>=8:

                if label3.winfo_exists():
                    label3.destroy()
                    Ck3=True
                if label4.winfo_exists():
                    label4.destroy()
                    label5.destroy()
                    label6.destroy()
                    Ck4=True
                if label2.winfo_exists():
                    label2.destroy()
                    Ck2=True
                if Ck7:
                    label7=Label(gui, height=1,bg="light green",justify=tk.CENTER,font=("Helvetica", 30))
                    label7.place(x=775, y=400,anchor='c')
                    Ck7=False
                label7.configure(text="No Face Detected")

            else:
                
                if len(ListDetect)==10:
                    Info=max(set(ListDetect), key=ListDetect.count)


                if Info=='unknown':
                    if label3.winfo_exists():
                        label3.destroy()
                        Ck3=True
                    if label4.winfo_exists():
                        label4.destroy()
                        label5.destroy()
                        label6.destroy()
                        Ck4=True
                    if label7.winfo_exists():
                        label7.destroy()
                        Ck7=True
                    if Ck2:
                        label2=Label(gui, bg="light green",font=("Helvetica", 45))
                        label2.place(x=775, y=400,anchor='c')
                        Ck2=False
                    label2.configure(text="Unknown")

                elif Info=="Detecting.......":
                    if Ck3:
                        label3=Label(gui, bg="light green",font=("Helvetica", 45))
                        label3.place(x=775, y=400,anchor='c')
                        Ck3=False
                    label3.configure(text='Detecting.......')

                else:
                    if label2.winfo_exists():
                        label2.destroy()
                        Ck2=True
                    if label3.winfo_exists():
                        label3.destroy()
                        Ck3=True
                    if label7.winfo_exists():
                        label7.destroy()
                        Ck7=True
                    if Ck4:
                        label4=Label(gui, height=4,bg="light green",justify=tk.LEFT,font=("Helvetica", 25))
                        label4.place(x=775, y=550,anchor='c')
                        label5=Label(gui)
                        label5.place(x=775, y=290,anchor='c')
                        label6=Label(gui, height=1,bg="light green",justify=tk.CENTER,font=("Helvetica", 30))
                        label6.place(x=775, y=100,anchor='c')
                        Ck4=False
                    Txt='Username :  '+str(data3.at[int(Info)-1,"UserID"])+"\n"+'Name        :  '+str(data3.at[int(Info)-1,"Name"])+"\n"+'Age           :  '+str(data3.at[int(Info)-1,"Age"])+"\n"+'Address    :  '+str(data3.at[int(Info)-1,"Address"])
                    label4.configure(text=Txt)
                    label6.configure(text="Face Detected")

                    try:
                        imgtk5=ProfileLoad(int(Info))
                        label5.imgtk5 = imgtk5
                        label5.configure(image=imgtk5)
                    except:

                        pass
                    

        
        #this calls the function again. So this time we will process the next frame coming from the web cam stream
        lmain.after(30, show_Mainframe)


########################################################################
#path to the pre-trained face detector 
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
#loading the face detector
faceCascade = cv2.CascadeClassifier(cascPath)
#creating a recognizer(LBPH)
recognizer = cv2.face.LBPHFaceRecognizer_create()

#setting up the web cam
width, height = 400, 300
capmain = cv2.VideoCapture(0)
capmain.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capmain.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

data1=pd.read_csv("Data.csv")
ID=len(data1['ID'])

#staring the main window    
gui = Tk() 
v1 = DoubleVar()
gui.configure(background="light green") 
gui.title("Face Recognition System") 
gui.geometry("1050x775")

#setting up the title
label1=Label(gui,bg='black',fg='white',text="FACE RECOGNITION SYSTEM", font=("Helvetica", 30))
label1.place(x=525, y=25,anchor='c')
#setting up the main display unit
lmain = Label(gui)
lmain.place(x=250, y=275,anchor='c')

if not DetectMode:
    lside=Label(gui)
    lside.place(x=650, y=200,anchor='c')
    lbright=Label(gui)
    lbright.place(x=900, y=200,anchor='c')
    s1 = Scale( gui, variable = v1,  
               from_ = -10, to = 10,  
               orient = HORIZONTAL,length=300,width=20,tickinterval=1)
    s1.place(x=775, y=325,anchor='c')
    print(lside.winfo_exists())
    label2=Label(gui, text="Initial Testing", bg="light green",font=("Helvetica", 25))
    label2.place(x=775, y=500,anchor='c')
    label3=Label(gui, text="Initial Testing", bg="light green",font=("Helvetica", 25))
    label3.place(x=775, y=550,anchor='c')
    label4=Label(gui, text="Initial Testing", bg="light green",font=("Helvetica", 16))
    label4.place(x=775, y=600,anchor='c')
    label5=Label(gui, text="Initial Testing", bg="light green",font=("Helvetica", 16))
    label5.place(x=775, y=600,anchor='c')
    label6=Label(gui, text="Initial Testing", bg="light green",font=("Helvetica", 16))
    label6.place(x=775, y=600,anchor='c')
    label7=Label(gui, text="Initial Testing", bg="light green",font=("Helvetica", 16))
    label7.place(x=775, y=600,anchor='c')


#setting up labels for the text entry boxes
heading = Label(gui, text="Form", bg="light green",font=("Helvetica", 20)) 
heading.place(x=250, y=505,anchor='c')
username = Label(gui, text="Username", bg="light green",font=("Helvetica", 16))
username.place(x=125, y=540,anchor='c')
name = Label(gui, text="Name", bg="light green",font=("Helvetica", 16))  
name.place(x=125, y=590,anchor='c')
age = Label(gui, text="Age", bg="light green",font=("Helvetica", 16))
age.place(x=125, y=640,anchor='c')
address = Label(gui, text="Address", bg="light green",font=("Helvetica", 16)) 
address.place(x=125, y=690,anchor='c')

#setting up text entry boxes
username_field = Entry(gui)
username_field.place(x=300, y=540,anchor='c')
name_field = Entry(gui) 
name_field.place(x=300, y=590,anchor='c')
age_field = Entry(gui)
age_field.place(x=300, y=640,anchor='c')
address_field = Entry(gui) 
address_field.place(x=300, y=690,anchor='c')

username_field.bind("<Return>", focus1) 
name_field.bind("<Return>", focus2) 
age_field.bind("<Return>", focus3) 

#setting up buttons of the main window
addperson = Button(gui, text="Add Person", fg="Black", 
                            bg="Red", command=insert,height=2, width=20)
addperson.place(x=250, y=745,anchor='c')
DetectFace = Button(gui, text="Detect Face", fg="Black", 
                            bg="Red", command=Detect,height=2, width=20) 
DetectFace.place(x=250, y=460,anchor='c')
MonitorB = Button(gui, text="Monitor", fg="Black", 
                            bg="Red", command=Monitor,height=2, width=20) 
MonitorB.place(x=360, y=85,anchor='c')
UR = Button(gui, text="User Registration",command=DataBaseManagement, fg="Black", 
                            bg="Red",height=2, width=20) 
UR.place(x=140, y=85,anchor='c')

QuitAll=Button(gui, text="Quit",command=Quit, fg="Black", 
                            bg="Red",height=2, width=20) 
QuitAll.place(x=925, y=745,anchor='c')




show_Mainframe()

gui.mainloop()
########################################################################

