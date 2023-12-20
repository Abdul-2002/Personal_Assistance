# The above code defines a class called `main` that acts as a virtual assistant and performs various
# tasks such as opening applications, searching the web, taking screenshots, and more.
# The line `from typing_extensions import Self` is importing the `Self` type hint from the
# `typing_extensions` module. The `Self` type hint is used to indicate that a method's return type
# should be the same as the class it belongs to.
# The line `from pylab import rcParams` is importing the `rcParams` object from the `pylab` module.
# `rcParams` is a dictionary-like object that stores the default settings for various plot parameters
# in Matplotlib. By importing `rcParams`, you can access and modify these default settings to
from typing_extensions import Self
from fnmatch import translate
from unittest import result
from IPython.display import Image
from playsound import playsound

# customize your plots.
from googletrans import Translator
from subprocess import call
import pywhatkit
import webbrowser
import pyttsx3 
import speech_recognition as sr 
import datetime
import pyautogui    
import os
import cv2
import wikipedia
import easyocr
import wikipedia
import imaplib
import email

#dictonary module 
class main:
    def speak(self,audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',200)
        engine.say(audio)
        engine.runAndWait()

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("Good Morning Sir")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon Sir")   
        else:
            self.speak("Good Evening Sir")       
        
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:    
            print("Say that again please...")  
            return "None"
        return query

    def main(self):
        self.wishMe()
        main().speak("Please tell me how may I help you")
        while True:
            query = self.takeCommand().lower()
                
            if 'open' in query:
                if 'browser' in query:
                    open().open_on_edge(query)
                    return
                if 'folder' in query:
                    open().open_folder(query)
                    return
                else:
                    open().open_on_windows(query)

            elif 'remind' in query:
                timeget = automation().remind(query)

            elif 'search' in query:
                query = query.replace("search","")
                pass

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M")    
                self.speak(f"Sir, the time is {strTime}")

            elif 'take a screenshot' in query:
                self.speak("Would you like to save it or copy it or extract the text")
                tamp = self.takeCommand().lower()

                if 'save' in tamp:
                        imagetasks.imagesave()   
                        return
                elif 'copy' in tamp:
                        imagetasks.imgcopy()  
                        return
                elif 'extract' in tamp:
                        imagetasks.photoextration()       

            elif 'thank you' in query:
                break
    
class class_schedule:
    
    def mon(self):
        class1 = [8,30,10,00,"FUZZY LOGIC CLASS"]
        class2 = [10,5,11,35,"DEEP LEARNING"]
        class3 = [11,40,13,10,"REINFORCEMENT LEARNING"]
        class4 = [16,25,17,55,"fOUNDATION OF DATA SCIENCE"]
        monlist = [class1,class2,class3,class4]
        return monlist

    def check_day_and_no_of_class(self):
        if (datetime.datetime.now().strftime('%A') == "Monday"):
            return class_schedule().mon()
        else:
            return []
        
    def check_if_there_is_class(self,classes_today):
        if classes_today  == []:
            return
        dt = datetime.datetime.now()
        for i in range(0,len(classes_today)):
            if(int(dt.strftime('%H'))==classes_today[i][0]):
                if(int(dt.strftime('%M'))==((classes_today[i][1]-5))):
                    main().speak("Sir 5 minute are remaining for your"+classes_today[i][4]+"class")
                    return
                        
                    
                if(int(dt.strftime('%M'))==((classes_today[i][1]))):
                    main().speak("Sir you are having your"+classes_today[i][4]+"class now")
                    return

        return 

class open:

    def open_on_windows(self,toopen):
        toopen = toopen.replace("open","")
        pyautogui.hotkey('win','q')
        pyautogui.write(toopen)
        pyautogui.press('enter')
        return

    def open_on_edge(self,toopen):
        if 'youtube' in toopen:
            webbrowser.open("youtube.com")
            return 

        elif 'google' in toopen:
            webbrowser.open("google.com")
            return 

        elif 'stackoverflow' in toopen:
            webbrowser.open("stackoverflow.com")
            return 

    def open_folder(self,toopen):
        if 'music' in toopen:
            music_dir = 'C:\\Users\\A.A.S\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            return 
        if 'documents' in toopen:
            music_dir = 'C:\\Users\\A.A.S\\Documents'
            os.open(music_dir)
            return 

class search:
    def search_on_web(self,toopen):
        if 'youtube' in toopen:
            toopen = toopen.replace("on youtube","")
            webbrowser.open("https://www.youtube.com/results?search_query="+toopen)
            return

        elif 'google' in toopen:
            toopen = toopen.replace("on google","")
            pywhatkit.search(toopen)
            return

        elif 'wikipedia' in toopen:
            toopen = toopen.replace("on wikipedia","")
            res = "According to wikipedia "+(wikipedia.summary(toopen,2))
            print(res)
            main.speak(res )
            return

class imagetasks:

    def imagesave():
        fi = pyautogui.screenshot()
        fi.save('C:\\Users\\A.A.S\\Pictures\\screenshot.jpg')
        return

    def imgcopy():
        pyautogui.press('printscreen')
        return None

    def photoextration():
        rcParams['figure.figsize'] = 8, 16
        #file = input("Write the path make sure you write it with \\")
        reader = easyocr.Reader(['en'])
        output = reader.readtext(pyautogui.screenshot())
        for i in output:
            main.speak(i[-2])
            print(i[-2])
        return

class whatsapp:

    def whatsapp(toopen):
        toopen = toopen.replace("whatsapp","")
        if 'aunber' in toopen:
            toopen.replace("aunber","")
            pywhatkit.sendwhatmsg("+918120020213","hello world",20,31)
        return

class automation:
    def translate(self,toopen):
        tra = Translator()
        result = tra.translate(toopen)
        print(result.text)
        return

    def removeextention(self,filename0):
        filename1=""
        for ch in filename0:
            if(ch!='.'):
                filename1=filename1+ch
            else:
                break
        return filename1

class close:
    def close_win(self,toopen):
        if 'photos' in toopen:
            os.system("TASKKILL /F /im Microsoft.Photos.exe ")
        return

class MailClient:
    def __init__(self):
        self.imap_host = 'imap.gmail.com'
        self.imap_port = 993
        self.mail = imaplib.IMAP4_SSL(self.imap_host, self.imap_port)
        self.mail.login("abdul.aziz2020@vitbhopal.ac.in", "kojrkjlxfxhtdndi")
        self.mail.select("inbox")

    def check_for_new_mail(self):
        result, data = self.mail.search(None, "UNSEEN")
        if result == 'OK':
            email_ids = data[0].split()
            return len(email_ids) > 0  # Return True if there are unseen emails, otherwise False
        return False
        
    def fetch_and_print_new_mail(self):
        result, data = self.mail.search(None, "UNSEEN")
        email_ids = data[0].split()
        for email_id in email_ids:
            result, data = self.mail.fetch(email_id, "(RFC822)")
            if result == 'OK':
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
                # Get the sender and subject of the email
                sender = email.utils.parseaddr(email_message['From'])[1]
                subject = email_message['Subject']
                # Print the details of the email
                print(f"New email from {sender} with subject: {subject}")

    def close_connection(self):
        self.mail.close()
        self.mail.logout()
    

if __name__ == "__main__":
    main().wishMe()

    main().speak(f" Today is   "+(datetime.datetime.now().strftime('%A')))
    print(f"  Today is "+(datetime.datetime.now().strftime('%A')))

    #today_classes = class_schedule().check_day_and_no_of_class()
    #main().speak(f" and you have "+((str)(len(today_classes)))+" classes")
    #print(f" and you have "+((str)(len(today_classes)))+" classes")

    while True:
        #class_schedule().check_if_there_is_class(today_classes)
        if(MailClient().check_for_new_mail>0):
            print("You have a new mail")
        hellocomp = main().takeCommand().lower()
        if hellocomp == 'hello computer':
            main().main()

        elif hellocomp == 'shutdown':
            break
