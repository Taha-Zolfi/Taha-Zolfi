import pyautogui
import os
import time
import tkinter as tk
import os
import wikipedia
import pyautogui
import pyttsx3
import time
import speech_recognition as sr
import webbrowser
import requests
import pywhatkit
from playsound import playsound
import glob
def playlist(path):
    for song in glob.glob(path):
        playsound(song)

r = sr.Recognizer() # درک کردن صدای شما

def talk(text):
    engine.say(text)
    engine.runAndWait()


engine = pyttsx3.init() # روشن کردن ماشین حرف زدن
voices = engine.getProperty('voices') # انتخاب جنسیت ربات
engine.setProperty('voice', voices[0].id) # برای مرد بودن عدد 0 برای زن بودن 1 
engine.setProperty('rate', 120) #سرعت حرف زدن ربات 
talk(f"hi {os.getlogin()} im elliot how can i help you") #engine.say("حرف دلخواهی که میخواهید زده بشه")
print(f"hi {os.getlogin()} im elliot how can i help you")


def dastor_giri():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = r.record(source, duration=3.5)
            dastor = r.recognize_google(voice)
            dastor = dastor.lower()
            #if 't' in dastor:
             #   dastor = dastor.replace('t', '')
             #   print(dastor)
    except:
        pass
    return dastor

def warzone():
        engine.say("opening warzone")
        engine.runAndWait()
        print("opening warzone..")
        os.startfile('Battle.net.lnk')
        time.sleep(7.5)
        pyautogui.moveTo(288, 700)
        pyautogui.click()    



def run_elliot():

    dastor = dastor_giri()

    print(dastor)
    if 'youtube' in dastor:
        song = dastor.replace('youtube', '')
        pywhatkit.playonyt(song)

    elif 'who is' in dastor:
        person = dastor.replace('whos', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'warzone' in dastor:
        warzone()

    elif "i'm feel good" in dastor:
        playsound("rp.wav")

    elif 'thanks' or 'thank you' or 'bye' in dastor:
        exit()    
    elif 'music' in dastor:
        playlist('C:/Users/taha zolfi/Desktop/output/songs/*.wav')


# def text(text):
#     a = dastor_giri(text)
try:
    while True:
        run_elliot()
except UnboundLocalError:
    talk("huh")