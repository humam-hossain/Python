import speech_recognition as sr
# import pyttsx3
import gtts
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2
import numpy as np
import pyautogui
# import winsound
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from FarizaUi3 import *

class enginex:

    def say(self, stringx):
        tts = gtts.gTTS(stringx, lang='en')
        tts.save("out.mp3")
        playsound("out.mp3")
        os.system("rm out.mp3")

listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty("rate", 150)

engine = enginex()

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.run_fariza()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            command = r.recognize_google(audio, language='en')

        except Exception as e:
            engine.say("Say it again....")
            return "none"
        return command

    def run_fariza(self):
        while True:
            self.command = self.take_command()
            if 'play' in self.command:
                song = self.command.replace('play', '')
                engine.say('playing' + song)
                pywhatkit.playonyt(song)

            elif 'hello' in self.command:
                engine.say('hello user, how are you')
            elif 'i am fine' in self.command:
                engine.say('that is great, i am fine too')
            elif 'can we be friends' in self.command:
                engine.say('sure why not')
            elif 'introduce yourself' in self.command:
                engine.say(
                    'i am fariza, an intelligent bot made by farazi i can do many things for you')
            elif 'time' in self.command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                engine.say('Current time is ' + time)
            elif 'tell me about' in self.command:
                person = self.command.replace('tell me about', '')
                info = wikipedia.summary(person, 3)
                engine.say(info)
            elif 'let us go' in self.command:
                engine.say('sorry, i have a headache')
            elif 'are you single' in self.command:
                engine.say('i am in a relationship with your computer')

            elif 'joke' in self.command:
                engine.say(pyjokes.get_joke())

            elif 'sleep' in self.command:
                sys.exit()
            elif 'navigate' in self.command:
                cap = cv2.VideoCapture(0)
                yellow_lower = np.array([22, 93, 0])
                yellow_upper = np.array([45, 255, 255])
                prev_y = 0

                while True:
                    ret, frame = cap.read()
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
                    contours, hierarchy = cv2.findContours(
                        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    for c in contours:
                        area = cv2.contourArea(c)
                        if area > 300:
                            x, y, w, h = cv2.boundingRect(c)
                            cv2.rectangle(
                                frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                            if y < prev_y:
                                pyautogui.press('down')
                            prev_y = y

                    cv2.imshow('Fariza v1.0 scrolling cam', frame)
                    if cv2.waitKey(10) == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'motion' in self.command:
                engine.say('Opening motion camera')
                cam = cv2.VideoCapture(0)
                while cam.isOpened():
                    ret, frame1 = cam.read()
                    ret, frame2 = cam.read()
                    diff = cv2.absdiff(frame1, frame2)
                    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                    blur = cv2.GaussianBlur(gray, (5, 5), 0)
                    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                    dilated = cv2.dilate(thresh, None, iterations=3)
                    contours, _ = cv2.findContours(
                        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    for c in contours:
                        if cv2.contourArea(c) < 5000:
                            continue
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(frame1, (x, y),
                                      (x+w, y+h), (0, 255, 0), 2)

                        # winsound.Beep(500,200)
                    cv2.imshow('Fariza v1.0 motion cam', frame1)
                    if cv2.waitKey(10) == ord('q'):
                        break
                cam.release()
                cv2.destroyAllWindows()

            # engine.runAndWait()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Fariza()
        self.ui.setupUi(self)
        self.ui.Run_Button.clicked.connect(self.startTask)
        self.ui.Exit_button.clicked.connect(self.close)

    def startTask(self):
        startExecution.start()


app = QApplication(sys.argv)
Fariza = Main()
Fariza.show()
sys.exit(app.exec_())
