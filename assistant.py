
import speech_recognition
from engine_class import *
from gladosGPT import GladosGPT
import sys
import threading
import tkinter as tk

class Assitant:

    commands = ["turn on", "increase", "watch", "turn off"]
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()

        self.root = tk.Tk()
        self.label = tk.Label(text="G", font=("Arial", 120, "bold") )
        self.label.pack()
        self.speaker = GladosTTS()
        self.ai = GladosGPT()
        print("Starting Thread now")
        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()



    def run_assistant(self):
        first = True
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    print("got text:", text)
                    if "hey glados" in text or "okay glados" == text or "okay gladys" in text or "hey gladys" in text:
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        # text = self.recognizer.recognize_google(audio)
                        self.label.config(fg="black")
                        text = text.lower()
                        if text == "stop":
                            self.speaker.tts("It was nice knowing you. Goodbye!",  key=False, speak=True,)
                            self.root.destroy()
                            sys.exit(0)
                        if text is not None:
                            response = self.ai.send_prompt(text)
                            if response is not None:
                                self.speaker.tts(response, key=False, speak=True )
            except:
                self.label.config(fg="black")
                continue


Assitant()