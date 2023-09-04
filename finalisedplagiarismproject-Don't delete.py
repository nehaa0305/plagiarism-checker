# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:16:35 2021

@author: DELL
"""

from logging import error
from tkinter import * 
from tkinter import messagebox
import spacy



import random
from tkinter import filedialog
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import numpy
import pytesseract
import cv2
import math
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import pathlib
import re
import os
from os import listdir
from os.path import isfile,join
from PIL import Image,ImageTk



#FORMALITIES



log = tk.Tk()
log.title('Log in')
log.attributes('-fullscreen', False)
log.geometry('1200x700')
log.resizable(False, False)

log.update_idletasks()

winwidth = log.winfo_width()
winheight = log.winfo_height()
photo = ImageTk.PhotoImage(file = r"C:\Users\NehaaIndhu\Downloads\Plagiarism Checker 1280 (1).png")

def dileet(win): #the destroyer of worlds
    for widgets in win.winfo_children():
        widgets.destroy()

#----------------------------------------------------------------------------------------------------------------------------------------
#Open Commands
    global langChoosen
    global fileNameA
    
def openA():
    global my_labelA
    global fileNameA
    #log.filenameA = filedialog.askopenfilename(initialdir="d:\nehaa", title="Select a file type", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
    fileNameA = filedialog.askopenfilename(initialdir="d:\nehaa\PlagiarismFinalProject",title="Select a file type", filetypes=(("PNG Files", "*.png"), ("Text Files", "*.txt")))
    my_labelA = Label(log, text="Selected File:   "+fileNameA,font=('Sans-serif font', 10),padx=10,pady=5).place(relx=0.10, rely=0.35)
    #print(fileNameA)
    return fileNameA
   
	
def openB():
    global my_labelB
    global fileNameB
    #log.filenameB = filedialog.askopenfilename(initialdir="d:\nehaa", title="Select a file type", filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
    fileNameB= filedialog.askopenfilename(initialdir="d:\nehaa\PlagiarismFinalProject",title="Select a file type", filetypes=(("PNG Files", "*.png"), ("Text Files", "*.txt")))
    my_labelB = Label(log, text="Selected File:   "+fileNameB,font=('Sans-serif font', 10),padx=10,pady=5).place(relx=0.55, rely=0.35)
    return fileNameB
            
    
def openC():
    global my_labelC
    log.filenameC = filedialog.askopenfilename(initialdir="d:\nehaa\PlagiarismFinalProject",title="Select a file type", filetypes=(("Text Files", "*.txt"),("PNG Files", "*.png")))
    my_labelC = Label(log, text=log.filenameC).place(relx=0.34, rely=0.4)


def openD():
    global my_labelD
    log.filenameD = filedialog.askopenfilename(initialdir="d:\nehaa\PlagiarismFinalProject",title="Select a file type", filetypes=(("Text Files", "*.txt"),("PNG Files", "*.png")))
    my_labelD = Label(log, text=log.filenameD).place(relx=0.34, rely=0.4)
	

#----------------------------------------------------------------------------------------------------------------------------------------
def openimage(path):
    if fileNameA !="" :
        imag=Image.open(path);
        imag.show();
    else:
        messagebox.error('Error','Select the image that is to be displayed')
def openingimage(path):
    if fileNameA !="" and fileNameB!="":
        imag=Image.open(path);
        imag.show();
    if fileNameA=="" and fileNameB!="" :
        messagebox.showerror('Error','Please select the first image ')
    if fileNameA!="" and fileNameB=="":
        messagebox.showerror('Error','Please select the image')
    
global buttonClicked

def clicked(buttonname):
    #to check if a button is clicked
    buttonClicked=False
    if buttonClicked:
        buttonClicked=False
    if not buttonClicked:
        buttonClicked=True
    return buttonClicked

def _getattr_(attr):
        "Delegate attribute access to the interpreter object"
        return getattr('_tkinter.tkapp',str(attr),'0')
def single(txt):
    l=[]
    p= ["\n","\t","\x0b"," ","  ","\\","\a","\b","\f","\r","\v","\\ooo","\\xhh"]
    f = open('creatfile.txt', 'r')
    lines = f.readlines()
    mystr = '\t\n\r\v'.join([line.strip() for line in lines])
    #mystr=str(lines).replace("\n", "\t")
    for char in mystr:
            l.append(char)
    for ch in l:
        if ch in p:
            l.remove(ch)
    strng=''.join([str(item) for item in l])
    return strng

def wordSplitFromFile(splitLines):      
    wordList =[]
    for line in splitLines:
         wordList.append(line.split())
    return wordList;





def plagiarismPercentage(strng1,strng2):
      
    splitLineFromFile1=lineSplitFromFile(strng1)
    #print("Lines extracted from file1" , splitLineFromFile1,"\n")
    wordList =wordSplitFromFile(splitLineFromFile1)
    #print("No of lines in file1 ", len(wordList),"\n")
##    for x in wordList:
##        print("Words extracted from file1:",x,"\n")

    #Open and Read File2
    #fileName2 = input("Enter file Name2 to compare against")
    #print("File name to compare against",fileName2)

    splitLineFromFile2=lineSplitFromFile(strng2)
    #print("Lines extracted from file2" , splitLineFromFile2,"\n")
    wordList2 =wordSplitFromFile(splitLineFromFile2)
    #print("No of lines in file2 ", len(wordList),"\n")
    #for x in wordList2:
        #print("Words extracted from file2:",x,"\n")
    
    
    
    
    
    #print("Compared Line from file1,file 2",comparedLine,"\n")



    #all possible common sub strings among every line of the both the functions would be returned
    #cline=1
    #global finallistforresult
    #finallistforresult=[]
    #print(wordList)
    
    for item in wordList:
        cline2=1
        for itemcheck in wordList2:
            list3 = set(item)&set(itemcheck)
            if len(list3)!=0:
                #print("the common words in line",cline,"of file1 and line",cline2,"file2 is",list3)
                #sentence wise similarity percent if common words are present
                rvector = set(item).union(set(itemcheck))
                l1,l2=[],[]
                for w in rvector:
                    
                    
                    if w in item: l1.append(1) 
                    else: l1.append(0)
                    if w in itemcheck: l2.append(1)
                    else: l2.append(0)
                c = 0


                for i in range(len(rvector)):
                    
                    c+= l1[i]*l2[i]
                if float((sum(l1)*sum(l2))**0.5)!= 0:
                     cosine = c / float((sum(l1)*sum(l2))**0.5)
                    
                #print("similarity: ", cosine)
                avg=(len(item)+len(itemcheck))/2
                simratio=len(list3)/avg
                #print("plagiarism percent",cosine*100)
                float_cosineSimilarity = cosine*100
                cosineSimilarity = str(float_cosineSimilarity)
                strngresult="Overall Plagiarism Percent:"+cosineSimilarity
    return strngresult

def openK():
    global my_LabelK
    filenameK = plagiarismPercentage(content1, content2)
    return filenameK
 
def openAndReadFileforpic(filename):
    line=[]
    try:
        
         with open((str(filename)+'.txt'),'r') as f:
            for lines in f:
                line.append(lines.lower())
         return line
    except IOError:
        print("Error: Can\'t find file or read data")
    else:
        print("File Open successful and read data")
        f.close()
def openAndReadFile(filename):
    line=[]
    try:
         with open(filename) as f:
            for lines in f:
                line.append(lines.lower())
         return line
    except IOError:
        print("Error: Can\'t find file or read data")
    else:
        print("File Open successful and read data")
        f.close()
        
          


#Read Line by Line as array
def lineSplitFromFile(lines):      
    for lineFromFile in lines:
        #print ("From WordSplitFromFile",lineFromFile)
        #Splitting the text
        
        splitLine =lineFromFile.split(".")
        print("SplitLine",splitLine)
        return splitLine
       
   
       
#Read word by word
def wordSplitFromFile(splitLines):      
    wordList =[]
    for line in splitLines:
         wordList.append(line.split())
    return wordList;

#Read file name from command prompt
'''
def readFileName():
    fileName =input("Enter file Name 1 to compare")
    print("File Name",fileName)
    fileName2 = input("Enter file Name2 to compare against")
    print("File name to compare against",fileName2)'''





#Compare line by line{simplified checking where only exact sentences would be printed}
def compareByLine(a,b):
    a_set = set(a)
    #print("A set is:",a_set)
    b_set = set(b)
    #print ("B set is :",b_set)
 
    if (a_set & b_set):
        return a_set & b_set
    else:
         return ("No common elements in file1 and file 2")


def checkingpart(item1,item2):
    print(item1)
    splitLineFromFile1=lineSplitFromFile(item1)
    print("Lines extracted from file1" , splitLineFromFile1,"\n")
    wordList =wordSplitFromFile(splitLineFromFile1)
    print("No of lines in file1 ", len(wordList)-1,"\n")

    splitLineFromFile2=lineSplitFromFile(item2)
    print("Lines extracted from file2" , splitLineFromFile2,"\n")
    wordList2 =wordSplitFromFile(splitLineFromFile2)
  
    comparedLine=compareByLine(splitLineFromFile1,splitLineFromFile2)
    print("Common Line from file1 and file2",str(comparedLine).lstrip("{'").rstrip("'}").split("."))
    #compareLineStr="Common Line from file1 and file2"+(str(comparedLine).lstrip("{'").rstrip("'}").split("."))
##    
##    
##    global strj
##    strj = "\n".join(comparedLine)
##    #for i in str(S).rstrip("'}").lstrip("{'").split("."):
##        #strj=strj+str(i).lstrip("[").rstrip("]")+"\n"
##   # print("Common Lines ",con)
##    
    return comparedLine
def checkplag(item1,item2):
     
    splitLineFromFile1=lineSplitFromFile(item1)
    print("Lines extracted from file1" , splitLineFromFile1,"\n")
    wordList =wordSplitFromFile(splitLineFromFile1)
    print("No of lines in file1 ", len(wordList),"\n")
##    for x in wordList:
##        print("Words extracted from file1:",x,"\n")

    #Open and Read File2
    #fileName2 = input("Enter file Name2 to compare against")
    #print("File name to compare against",fileName2)

    splitLineFromFile2=lineSplitFromFile(item2)
    print("Lines extracted from file2" , splitLineFromFile2,"\n")
    wordList2 =wordSplitFromFile(splitLineFromFile2)
    #print("No of lines in file2 ", len(wordList),"\n")
    #for x in wordList2:
        #print("Words extracted from file2:",x,"\n")
    
    
    
    
    
    #print("Compared Line from file1,file 2",comparedLine,"\n")



    #all possible common sub strings among every line of the both the functions would be returned
    cline=1
    global finallistforresult
    finallistforresult=[]
    #print(wordList)
    
    for item in wordList:
        cline2=1
        for itemcheck in wordList2:
            list3 = set(item)&set(itemcheck)
            if len(list3)!=0:
                print("the common words in line",cline,"of file1 and line",cline2,"file2 is",list3)
                #sentence wise similarity percent if common words are present
                rvector = set(item).union(set(itemcheck))
                l1,l2=[],[]
                for w in rvector:
                    
                    
                    if w in item: l1.append(1) 
                    else: l1.append(0)
                    if w in itemcheck: l2.append(1)
                    else: l2.append(0)
                c = 0


                for i in range(len(rvector)):
                    
                    c+= l1[i]*l2[i]
                if float((sum(l1)*sum(l2))**0.5)!= 0:
                     cosine = c / float((sum(l1)*sum(l2))**0.5)
                    
                #print("similarity: ", cosine)
                avg=(len(item)+len(itemcheck))/2
                simratio=len(list3)/avg
                print("plagiarism percent",cosine*100)
                float_cosineSimilarity = cosine*100
                cosineSimilarity = str(float_cosineSimilarity)
                
                compareLineStr=""
                compareLineStr = ','.join([str(i) for i in list3])
                
                linesFromFile="the common words in line"+str(cline)+" of file1 and line"+str(cline2)+" file2 is "+compareLineStr         
                result="\nPlagiarism percent : "+cosineSimilarity
                finallistforresult.append(linesFromFile+" \n")
                finallistforresult.append(result+"\n")
                print("Compared Result",result)
                                  
             
            cline2=cline2+1
        cline=cline+1

    return finallistforresult


'''def checkplag(item1,item2):
     
    splitLineFromFile1=lineSplitFromFile(item1)
    print("Lines extracted from file1" , splitLineFromFile1,"\n")
    wordList =wordSplitFromFile(splitLineFromFile1)
    print("No of lines in file1 ", len(wordList),"\n")
##    for x in wordList:
##        print("Words extracted from file1:",x,"\n")

    #Open and Read File2
    #fileName2 = input("Enter file Name2 to compare against")
    #print("File name to compare against",fileName2)

    splitLineFromFile2=lineSplitFromFile(item2)
    print("Lines extracted from file2" , splitLineFromFile2,"\n")
    wordList2 =wordSplitFromFile(splitLineFromFile2)
    #print("No of lines in file2 ", len(wordList),"\n")
    #for x in wordList2:
        #print("Words extracted from file2:",x,"\n")
    
    
    
    
    
    #print("Compared Line from file1,file 2",comparedLine,"\n")



    #all possible common sub strings among every line of the both the functions would be returned
    cline=1
    global finallistforresult
    finallistforresult=[]
    #print(wordList)
    
    for item in wordList:
        cline2=1
        for itemcheck in wordList2:
            list3 = set(item)&set(itemcheck)
            if len(list3)!=0:
                print("the common words in line",cline,"of file1 and line",cline2,"file2 is",list3)
                #sentence wise similarity percent if common words are present
                rvector = set(item).union(set(itemcheck))
                l1,l2=[],[]
                for w in rvector:
                    
                    
                    if w in item: l1.append(1) 
                    else: l1.append(0)
                    if w in itemcheck: l2.append(1)
                    else: l2.append(0)
                c = 0


                for i in range(len(rvector)):
                    
                    c+= l1[i]*l2[i]
                if float((sum(l1)*sum(l2))**0.5)!= 0:
                     cosine = c / float((sum(l1)*sum(l2))**0.5)
                    
                #print("similarity: ", cosine)
                avg=(len(item)+len(itemcheck))/2
                simratio=len(list3)/avg
                print("plagiarism percent",cosine*100)
                float_cosineSimilarity = cosine*100
                cosineSimilarity = str(float_cosineSimilarity)
                
                compareLineStr=""
                compareLineStr = ','.join([str(i) for i in list3])
                
                linesFromFile="the common words in line"+str(cline)+" of file1 and line"+str(cline2)+" file2 is "+compareLineStr         
                result="\nPlagiarism percent : "+cosineSimilarity
                finallistforresult.append(linesFromFile+" \n")
                finallistforresult.append(result+"\n")
                print("Compared Result",result)
                                  
             
            cline2=cline2+1
        cline=cline+1

    return finallistforresult'''




def preprocess(path,language):
    ot1 = cv2.imread(str(path))
   # print('Path inside preprocess',path,language)
    pytesseract.pytesseract.tesseract_cmd = r'D:\Software\Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = r'--tessdata-dir "D:\Software\Tesseract-OCR\tessdata"'
   
    gray= cv2.cvtColor(ot1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1,1), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel,iterations=1)
    invert = 255 - opening  
    
    '''
    cv2.imshow('thresh', thresh)
    cv2.imshow('opening', opening)
    cv2.imshow('invert', invert)
    cv2.waitKey()'''
    
    
    #pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    #tessdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
    st = pytesseract.image_to_string(invert, lang=str(language),config=tessdata_dir_config)
    t=str(st)
    return t


    

def openE():
    
    '''frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
    frameHead.grid(row=0, column=-0, columnspan=2)
    
    backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Terminal', 10), command=lambda: homepage_main())
    backbutton.place(relx=0.06, rely=0.22)

    frame1 = Frame(log, bg='#2294ff', width=winwidth, height=winheight*0.9)
    frame1.grid(row=1, column=0)
    global my_labelE
    log.filenameE = checkingpart(content1, content2)
   # print("inside opneE()",log.filenameE)
   
    
    log.filenameF = checkplag(content1, content2)
   # print("inside opneE()",log.filenameF)
   # my_labeF = Label(log, text=str(log.filenameF)).place(relx=0.15, rely=0.35)

    log.filenameK =openK()
   
    textArea_labeA = Label(frame1, fg='white', bg='light coral',text="Plagiarism Result",font=('Sans-serif font', 20),padx=10,pady=5).place(relx=0.25, rely=0.10)

    my_labeE = Label(frame1, text="Common Lines from file1 and file2")
    my_labeE.place(relx=0.25, rely=0.20)
    
    txtarea = tk.Text(frame1, width=100, height=15,bg="#FFFF00",fg="#FF0000")
    txtarea.place(relx=0.25,rely=0.25)
    txtarea.insert(END, log.filenameE )

    txtarea2 = tk.Text(frame1, width=100, height=15,bg="#FFFF00",fg="#FF0000")
    txtarea2.place(relx=0.25,rely=0.70)
    for i in log.filenameF:
        txtarea2.insert(END,i)'''
    

def openE():
   
    frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
    frameHead.grid(row=0, column=-0, columnspan=2)
    
    backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Terminal', 10), command=lambda: homepage_main())
    backbutton.place(relx=0.06, rely=0.22)

    frame1 = Frame(log, bg='#2294ff', width=winwidth, height=winheight*0.9)
    frame1.grid(row=1, column=0)
    global my_labelE
    log.filenameE = checkingpart(content1, content2)
    print("inside opneE()",len(log.filenameE))
    list_of_strings = [str(s) for s in log.filenameE]
    joined_string = "\n".join(list_of_strings)
    line_Str=""
    if len(joined_string) >0:
        line_Str =joined_string
    else:
        line_Str="No Common Lines Found"
    
    log.filenameF = checkplag(content1, content2)
   # print("inside opneE()",log.filenameF)
   # my_labeF = Label(log, text=str(log.filenameF)).place(relx=0.15, rely=0.35)
    log.filenameK =openK()
   
    textArea_labeA = Label(frame1, fg='white', bg='light coral',text="Plagiarism Result",font=('Sans-serif font', 20),padx=10,pady=5)
    textArea_labeA.config(anchor=CENTER)
    textArea_labeA.place(relx=0.25, rely=0.05)

    my_labeE = Label(frame1, text="Common Lines from file1 and file2")
    my_labeE.place(relx=0.25, rely=0.20)
    
    txtarea = tk.Text(frame1, width=75, height=15,bg="#FFFF00",fg="#FF0000",font=('Sans-serif font', 12))
    txtarea.place(relx=0.25,rely=0.25)
    #txtarea.insert(END, log.filenameE)
    txtarea.insert(END, line_Str)

    txtarea2 = tk.Text(frame1, width=75, height=15,bg="#FFFF00",fg="#FF0000",font=('Sans-serif font', 12))
    txtarea2.place(relx=0.25,rely=0.50)
    for i in log.filenameF:
        txtarea2.insert(END,i)
        
    my_labek = Label(frame1, width=75, height=7,bg="#FFFF00",fg="#FF0000",text=log.filenameK,font=('Sans-serif font', 12))
    my_labek.place(relx=0.25, rely=0.88)

 
    
def resultpage(content1,content2):
        
    dileet(log)

    frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
    frameHead.grid(row=0, column=-0, columnspan=2)

    backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Sans-serif font', 10), command=lambda: homepage_main())
    backbutton.place(relx=0.06, rely=0.22)

    frame1 = Frame(log, bg='#2294ff', width=winwidth, height=winheight*0.9)
    frame1.grid(row=1, column=0)

    #frame2 = PhotoImage(file=imagefilename, format="gif -index 2")
    textArea_labeA = Label(frame1, text="File 1:   "+fileNameA,font=('Sans-serif font', 10),padx=10,pady=5).place(relx=0.15, rely=0.10)

    txtarea = tk.Text(frame1, width=50, height=15,bg="#66CDAA",fg="#800080", font=('Sans-serif font', 12))
    txtarea.place(relx=0.15,rely=0.20)
    tf = open(content1)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
    #txtarea.insert(tk.END, content1)
    textArea_labeB = Label(frame1, text="File 2:   "+fileNameB,font=('Sans-serif font', 10),padx=10,pady=5).place(relx=0.55, rely=0.10)

    txtarea2 = tk.Text(frame1, width=50, height=15,bg="#66CDAA",fg="#800080", font=('Sans-serif font', 12))
    txtarea2.place(relx=0.55,rely=0.20)
    tf2 = open(content2)  # or tf = open(tf, 'r')
    data = tf2.read()
    txtarea2.insert(END, data)
    tf2.close()
    #txtarea.insert(tk.END, content1)




    wish= Label(frame1, fg='white', bg='light coral' ,text='Do you wish to compare the similar Words/Lines in selected files? ', font=('Sans-serif font', 15))
    wish.place(relx=0.30, rely=0.70)

    button= Button(frame1, padx=15, pady=20, text='Yes', font=('Sans-serif font', 15), command=lambda: openE())
    button.place(relx=0.34, rely=0.75)

    button1= Button(frame1, padx=15, pady=20, text='No', font=('Sans-serif font', 15),command=log.destroy)
    button1.place(relx=0.45, rely=0.75)

    button2= Button(frame1, padx=15, pady=20, text='Check Again', font=('Sans-serif font', 15),command=lambda:homepage_main())
    button2.place(relx=0.55, rely=0.75)
    


global s3

def nextandopen(langchoosen):
     if langchoosen=='':
         
         messagebox.askretrycancel('Error','Language not selected,english would be used as default','Continue')
     else:
         
         
        #print('Next and Open Method',langchoosen)
        s2=langchoosen.index("-")
        c=s2+1
        s3=langchoosen[c:]
        selectedLang = s3
        #print("Selected Language",selectedLang)
        
        #lang1=input("SELECT THE LANGUAGE IN WHICH OCR HAS TO BE PERFORMED(French-fra,Tamil-tam,Telugu-tel, Italian-ita, German-deu, Spanish-spa,Brazilian Portuguese-por,hindi-hin,korean- kor,Chinese(traditional-ch_tra/simplified-ch_sim)/Japanese-jpn/arabic-ara),English-eng:") # to be added in the form of options in the gui
        print("MAKE SURE BOTH THE IMAGES ARE OF SAME LANGUAGE")
        
        fileName1=fileNameA
        fileName2=fileNameB

           
        dirname1 = os.path.dirname(fileName1)
       # print(dirname1)

        dirname2 = os.path.dirname(fileName2)
        #print(dirname2)

        fileType1=fileName1.index(".")
        #print("File Type",fileType1)
        c=fileType1+1
        s3=fileName1[c:]
        fileExtension1= s3
        #print("File Extension",fileExtension1)

        fileType2=fileName2.index(".")
        c=fileType2+1
        s3=fileName2[c:]
        fileExtension1= s3
        #print("File Extension",fileExtension1)
        
        if (fileExtension1=='png' and fileExtension1=='png'):
            #print("Inside image processing after checking file extension")
            #image1=Image.open(imagepath1+'\\'+str(name1));
            image1=Image.open(fileName1)
            image1.save(dirname1+'\\pic1.png')
            #image1.show();


            #image2=Image.open(imagepath2+'\\'+str(name2));
            image2=Image.open(fileName2)
            image2.save(dirname2+'\\pic2.png')
            #image2.show();
           
            FileName1=open(dirname1+'\\sample1.txt','w',encoding="utf-8")
            #FileName1.write(str(preprocess(('pic1.png'),str(lang1))))
            FileName1.write(str(preprocess(fileName1,selectedLang)))
            FileName1.close()

            FileName2=open(dirname2+'\\sample2.txt','w',encoding="utf-8")
            FileName2.write(str(preprocess(fileName2,selectedLang)))
            #FileName2.write(str(preprocess(('pic2.png'),str(lang1))))

            FileName2.close()
            if selectedLang in ["fra","tam","tel", "ita","eng","ara"]:

                #print("inside If loop for Language check",selectedLang)
                contents1 = ""
                f = open(dirname1+'\\sample1.txt', 'r',encoding="utf-8")
                if f.mode == 'r':
                   # contents1 = f.read().strip()
                   for line in f:
                       stripped_line = line.rstrip()
                       contents1 += " "+stripped_line
    # a_file.close()

                #print(contents1)
                from googletrans import Translator

                file_translate1 = Translator()
                result = file_translate1.translate(contents1)
                #print(result.text)

                with open(dirname1+'\\translatedSample1.txt', 'w+',encoding="utf-8") as f:
                    f.write(result.text)
                

                f2 = open(dirname2+'\\sample2.txt', 'r',encoding="utf-8")
                contents2=""
                if f2.mode == 'r':
                   
                    f2 = open(dirname1+'\\sample2.txt', 'r',encoding="utf-8")
                    for line1 in f2:
                              
                           stripped_line1 = line1.rstrip()
                           contents2 += " "+stripped_line1
                    
                    #contents2 = f2.read()
                #print(contents2)
                from googletrans import Translator

                file_translate2 = Translator()
                result2 = file_translate2.translate(contents2)
                #print(result.text)
                with open(dirname2+'\\translatedSample2.txt', 'w+',encoding="utf-8") as f2:
                    f2.write(result2.text)
            
                
                     
        global content1,content2
        if (fileExtension1=='png' and fileExtension1=='png'):
            content1 = openAndReadFile(dirname1+'\\translatedSample1.txt')
            content2 = openAndReadFile(dirname2+'\\translatedSample2.txt')
        else:
            content1 = openAndReadFile(fileName1)
            content2 = openAndReadFile(fileName2)
        
        #print("Content 1",content1)
       # print("Content 2",content2)
        
        dileet(log)
        frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
        frameHead.grid(row=0, column=-0, columnspan=2)
        
        backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Terminal', 10), command=lambda: homepage_main())
        backbutton.place(relx=0.06, rely=0.22)

        frame1 = Frame(log, bg='#2294ff', width=winwidth, height=winheight*0.9)
        frame1.grid(row=1, column=0)
       #my_labelContent1 = Label(log, text=str(content1).place(relx=0.15, rely=0.35)
       
       
        
    ##    wish= Label(frame1, fg='white', bg='light coral' ,text=content1, font=('Terminal', 25))
    ##    wish.place(relx=0.0, rely=0.43)
    ##    
    ##    button= Button(frame1, padx=15, pady=20, text='Yes', font=('Terminal', 20), command=lambda: resultpage())
    ##    button.place(relx=0.34, rely=0.6)
    ##    
    ##    button1= Button(frame1, padx=15, pady=20, text='No', font=('Terminal', 20),command=lambda: log.quit())
    ##    button1.place(relx=0.45, rely=0.6)
    ##    
    ##    button2= Button(frame1, padx=15, pady=20, text='CHECK AGAIN', font=('Terminal', 20),command=lambda: log.mainloop())
    ##    button2.place(relx=0.41, rely=0.8)
        
        if (fileExtension1=='png' and fileExtension1=='png'):
            b=resultpage(dirname1+'\\translatedSample1.txt',dirname1+'\\translatedSample2.txt')
        else:
             b=resultpage(fileName1,fileName2)
        
   

def open_win():
     if x123==True and (fileNameA=="" or fileNameB==""):
         messagebox.showerror('Error', 'Please select images')
     else:
         
         
        
         
        
      
         dileet(log)
         #Homepage Layout
         frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
         frameHead.grid(row=0, column=-0, columnspan=2)
         frameLeft = Frame(log, bg='#0e75ff', width=winwidth, height=winheight*0.9)
         frameLeft.grid(row=1, column=0)
         #Widget Placement

         def click():
         
            n= langchoosen.get()# button Creation  
            print(n)
            global langSelected
            langSelected =n
            print("Langchoosen set to",langSelected)

            
         n = tk.StringVar()
        # n.set(' English-eng')
         langchoosen = ttk.Combobox(log, width = 27,textvariable = n,state='readonly')
         comboLabel= Label(frameLeft, text="Select the Language :", bg='#0e75ff', font=('Terminal', 20))
         comboLabel.place(relx=0.14, rely=0.2)
          
        # Adding combobox drop down list
         langchoosen['values'] = (' English-eng',
                                  ' French-fra',
                                  ' Tamil-tam',
                                  ' Telugu-tel',
                                  ' Italian-ita',
                                  ' German-deu',
                                  ' Spanish-spa', 
                                  ' Brazilian Portuguese-por', 
                                  ' hindi-hin', 
                                  ' korean- kor', 
                                  ' Chinese(traditional-ch_tra', 
                                  ' Chinesesimplified-ch_sim', 
                                  ' Japanese-jpn',
                                  ' Arabic-ara')
              
         #monthchoosen.grid(row=15,column=10)
         langchoosen.place(relx=0.45, rely=0.3)
         
         selectButton = Button(frameLeft, padx=15, pady=15, text='select language>>', font=('Terminal', 10), command= lambda: click())
         selectButton.place(relx=0.45, rely=0.3)

         
         nextp = Button(frameLeft, padx=15, pady=15, text='Next>>', font=('Terminal', 20), command= lambda: nextandopen(langSelected))
         nextp.place(relx=0.75, rely=0.86)
              
        # Shows february as a default value
         logoutbutton = Button(frameHead, padx=15, pady=10, text='Quit', font=('Terminal', 10), command=lambda: log.quit())
         logoutbutton.place(relx=0.06, rely=0.22)


def file():
    

        dileet(log)
        #Homepage Layout
        frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
        frameHead.grid(row=0, column=-0, columnspan=2)

        frameLeft = Frame(log, bg='#0e75ff', width=winwidth/2, height=winheight*0.9)
        frameLeft.grid(row=1, column=0)

        frameRight = Frame(log, bg='#2294ff', width=winwidth/2, height=winheight*0.9)
        frameRight.grid(row=1, column=1)

        #Widget Placement
        backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Sans-serif font', 10), command=lambda: homepage_main())
        backbutton.place(relx=0.06, rely=0.22)

        header = Label(frameHead, fg='white', bg='light coral' ,text='Text File', font=('Sans-serif font', 25))
        header.place(relx=0.22, rely=0.28)

        Image1= Label(frameLeft, text="Directory of Reference File :", font=('Sans-serif font', 20))
        Image1.place(relx=0.14, rely=0.2)

        Image2= Label(frameRight, text="Directory of File to be Checked:", font=('Sans-serif font', 20))
        Image2.place(relx=0.14, rely=0.2)

        regbutton = Button(frameLeft, padx=15, pady=20, text='File 1', font=('Sans-serif font', 10), command=lambda: openA())
        regbutton.place(relx=0.34, rely=0.6)

        alumbutton = Button(frameRight, padx=15, pady=20, text='File 2', font=('Sans-serif font', 10), command=lambda: openB())
        alumbutton.place(relx=0.34, rely=0.6)
        
        nextp = Button(frameRight, padx=15, pady=15, text='Next>>', font=('Sans-serif font', 10), command= lambda:resultpage ())
        nextp.place(relx=0.75, rely=0.86)
        
        
        
        dileet(log)
        #Homepage Layout
        frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
        frameHead.grid(row=0, column=-0, columnspan=2)

        frameLeft = Frame(log, bg='#0e75ff', width=winwidth/2, height=winheight*0.9)
        frameLeft.grid(row=1, column=0)

        frameRight = Frame(log, bg='#2294ff', width=winwidth/2, height=winheight*0.9)
        frameRight.grid(row=1, column=1)

        #Widget Placement
        backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Sans-serif font', 10), command=lambda: homepage_main())
        backbutton.place(relx=0.06, rely=0.22)

        header = Label(frameHead, fg='white', bg='light coral' ,text='Text File Comparison', font=('Sans-serif font', 25))
        header.place(relx=0.22, rely=0.28)

        Image1= Label(frameLeft, text="Directory of Reference File :", font=('Sans-serif font', 15))
        Image1.place(relx=0.14, rely=0.2)

        Image2= Label(frameRight, text="Directory of File to be Checked:", font=('Sans-serif font', 15))
        Image2.place(relx=0.14, rely=0.2)

        regbutton = Button(frameLeft, padx=15, pady=10, text='Select File1', font=('Sans-serif font', 10), command=openA)
        regbutton.place(relx=0.14, rely=0.4)

        alumbutton = Button(frameRight, padx=15, pady=10, text='Select File2', font=('Sans-serif font', 10), command=openB)
        alumbutton.place(relx=0.14, rely=0.4)
        
        #nextp = Button(frameRight, padx=15, pady=20, text='Next>>', font=('Terminal', 20), command= lambda: resultpage())
        nextp = Button(frameRight, padx=15, pady=20, text='Next>>', font=('Sans-serif font', 15), command= lambda:nextandopen(' English-eng') )
        nextp.place(relx=0.75, rely=0.75)
        global x1234
        x1234=clicked(nextp)
        

def image():
   
    dileet(log)
    #Homepage Layout
    frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
    frameHead.grid(row=0, column=-0, columnspan=2)

    frameLeft = Frame(log, bg='#0e75ff', width=winwidth/2, height=winheight*0.9)
    frameLeft.grid(row=1, column=0)
    global frameRight
    frameRight = Frame(log, bg='#2294ff', width=winwidth/2, height=winheight*0.9)
    frameRight.grid(row=1, column=1)

    #Widget Placement
    backbutton = Button(frameHead, padx=15, pady=10, text='Back', font=('Sans-serif font', 10), command=lambda: homepage_main())
    backbutton.place(relx=0.06, rely=0.22)

    header = Label(frameHead, fg='white', bg='light coral' ,text='Image Comparison', font=('Sans-serif font', 25))
    header.place(relx=0.22, rely=0.28)

    Image1= Label(frameLeft, text="Directory of Reference Image :", bg='#0e75ff', font=('Sans-serif font', 15))
    Image1.place(relx=0.14, rely=0.2)

    Image2= Label(frameRight, text="Directory of Image to be Checked:",bg='#2294ff', font=('Sans-serif font', 15))
    Image2.place(relx=0.14, rely=0.2)
    
    regbutton = Button(frameLeft, padx=15, pady=20, text='Image 1', font=('Sans-serif font', 10), command=lambda: openA())
    regbutton.place(relx=0.14, rely=0.40)

    alumbutton = Button(frameRight, padx=15, pady=20, text='Image 2', font=('Sans-serif font', 10), command=lambda: openB())
    alumbutton.place(relx=0.14, rely=0.40)

    regbutto = Button(frameLeft, padx=15, pady=20, text='Show image 1', font=('Sans-serif font', 10), command=lambda: openimage(str(fileNameA)))
    regbutto.place(relx=0.14, rely=0.60)
    
    alumbutto = Button(frameRight, padx=15, pady=20, text='Show image 2', font=('Sans-serif font', 10), command=lambda: openimage(str(fileNameB)))
    alumbutto.place(relx=0.14, rely=0.60)


    nextp = Button(frameRight, padx=15, pady=15, text='Next>>', font=('Sans-serif font', 10), command= lambda:  open_win())
    nextp.place(relx=0.75, rely=0.86)
    global x123
    x123=clicked(nextp)
        
   
    
def homepage_main():
    dileet(log)
    global regbutton
    global viewbutton
    #Homepage Layout
    frameHead = Frame(log, bg='light coral', width=winwidth, height=winheight*0.1)
    frameHead.grid(row=0, column=-0, columnspan=2)

    frameLeft = Frame(log, bg='#0e75ff', width=winwidth, height=winheight*0.9)
    frameLeft.grid(row=1, column=0)

    #Widget Placement
    logoutbutton = Button(frameHead, padx=15, pady=10, text='Quit', font=('Sans-serif font', 10), command=log.destroy)
    logoutbutton.place(relx=0.06, rely=0.22)

    header = Label(frameHead, fg='white', bg='light coral' ,text='Home Page', font=('Terminal', 25))
    header.place(relx=0.22, rely=0.28)

    regbutton = Button(frameLeft, padx=15, pady=10, text='Using Images', font=('Sans-serif font', 25), command=lambda: image())
    regbutton.place(relx=0.20, rely=0.2)

    viewbutton = Button(frameLeft, padx=15, pady=10, text='Using Text Files', font=('Sans-serif font', 25), command=lambda: file())
    viewbutton.place(relx=0.60, rely=0.2)

my_button1=Button(log,image=photo,command=lambda:homepage_main()).pack()



log.mainloop()
