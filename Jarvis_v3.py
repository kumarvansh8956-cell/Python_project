from google import genai
import google.generativeai as genai
import subprocess
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()  # Add this line to pull the key into memory

#======================AI_brain=============================# 
class AI_brain:



    def __init__(self,name):

        self.name = name
        self.command_map = {
    "open google": self.google,
    "open youtube": self.youtube,
    "time":  self.time,
    "whatsapp": self.whatsapp,
    "weather": self.weather,
    "notepad":self.notepad,
    "word" : self.word,
    "calculator": self.calculator,
    "chorme": self.chrome
    }
        self.active = False
        self.last_command = None
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        #self.command_map = command_map
        self.wake_words = ["jarvis", "arya"]
        self.sleep_words = ["sleep", "stop listening", "go to sleep"]
        #self.ai_brain = AI_Brain()
    #============== AI_setup =============#
    def AI_setup(self, command):
    # Retrieve the key from the hidden .env file using the 'os' module
     
     api_key = os.getenv("GEMINI_API_KEY") 
     genai.configure(api_key = api_key)
    

    # Initialize the model (Use the 'self.' version so other functions can see it)
     self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Generate the response
     response = self.model.generate_content(command)
    
     print(f"Alva: {response.text}")
     self.speak(response.text)


    def speak(self, text):
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()


    # Long listening (full command)
    def listen_long(self):
        with sr.Microphone() as source:
            print(" i'm listening.... ")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio).lower()
                self.process_command(command)
                return command
            except:
                ()
    #=============== instruction_setups===========#
    
    def google(self):
        webbrowser.open("http://www.google.com")


    def whatsapp(self):
        webbrowser.open("http://www.whatsapp.com")

    def youtube(self):
        webbrowser.open("http://www.youtube.com")
    def chrome(self):
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

        webbrowser.get(chrome_path).open("https://www.google.com")
    def notepad(self):
        subprocess.run("notepad")
    def calculator(self):
        subprocess.run("calculator")

    def weather(self):
        webbrowser.open("http://www.weather.com")

    def calender(self):
        subprocess.run("calender")
    def word(self):
        word_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        subprocess.Popen(word_path)

    def process_command(self, command):
        self.listen_long()
        if any(word in command for word in self.sleep_words):
            self.speak("Going to sleep, bro.")
            self.active = False
            return
        for key, func in self.command_map.items():
         if key in command:
            self.speak(f"Executing: {key}")
            result = func()
            if result:
                self.speak(result)
            self.last_command = key
            return
        ai_response = self.ai_brain.get_response(command, context=self.last_command)
        self.speak(ai_response)
        self.last_command = command


if __name__ ==" __main__":
    if __name__ == "__main__":
      Jarvis = AI_brain()   # create object once

      while True:
         command = Jarvis.listen_long()
         if command:
          Jarvis.process_command(command)
