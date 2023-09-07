import speech_recognition
import sys
import threading
import tkinter as tk
from engine_class import GladosTTS
from gladosGPT import GladosGPT
import re

class Assistant:
    commands = ["turn on", "increase", "watch", "turn off"]
    
    def __init__(self, mode="voice"):
        self.recognizer = speech_recognition.Recognizer()
        self.root = tk.Tk()
        self.label = tk.Label(text="G", font=("Arial", 120, "bold"))
        self.label.pack()
        self.speaker = GladosTTS()
        self.ai = GladosGPT()
        self.mode = mode.lower()
        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()

    def run_assistant(self):
        if self.mode == "voice":
            self.run_voice_assistant()
        elif self.mode == "typing":
            self.run_typing_assistant()
    
    def _split_into_groups(text, max_sentences=3):
        print("SPLITTING NOW:")
        print(type(text))
        groups = text.split(".")
        # delimiters = ['.', '?']
        # start = 0
        # all_splits = []

        # for idx, char in enumerate(text):
        #     if char in delimiters:
        #         all_splits.append(text[start:idx+1].strip())
        #         start = idx + 1

        # # Remove any empty strings from the list (e.g., if there were multiple spaces between sentences)
        # all_splits = [s for s in all_splits if s]

        # # Group the sentences and questions
        # groups = []
        # for i in range(0, len(all_splits), max_sentences):
        #     groups.append(' '.join(all_splits[i:i+max_sentences]))

        print("DONE SPLITTING")
        return groups

    def run_voice_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    print("Listening...")
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio).lower()
                    print("got text:", text)
                    
                    if any(keyword in text for keyword in ["ok google", "hey glados", "okay glados", "okay gladys", "hey gladys"]):
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio).lower()
                        self.label.config(fg="black")
                        
                        if text == "stop":
                            self.speaker.tts("It was nice knowing you. Goodbye!", key=False, speak=True)
                            self.root.destroy()
                            sys.exit(0)
                        
                        if text:
                            response = self.ai.send_prompt(text).strip("\n")
                            if response:
                                print("Got OPenAI Rresponse: ",response)

                                # groups = self._split_into_groups(response)
                                groups = response.split(".")
                                print("Split up into groups")
                                print(groups)
                                # Create an initially set event for the first thread to start immediately
                                start_event = threading.Event()
                                start_event.set()

                                for id, group in enumerate(groups, start=1):
                                    
                                     # Start a new thread for this group of sentences
                                    if group:
                                        # Create an event for signaling when this thread is done
                                        done_event = threading.Event()
                                        threading.Thread(target=self.speaker.tts, args=(group, start_event, done_event), kwargs={'key': str(id), 'speak': True}).start()

                                        # The next thread will wait for this thread to signal it's done before starting
                                        start_event = done_event
                                
            except:
                self.label.config(fg="black")
                continue
    
    def run_typing_assistant(self):
        while True:
            try:
                text = input("Enter your command: ").lower()
                print("got text:", text)
                
                if text == "stop":
                    self.speaker.tts("It was nice knowing you. Goodbye!", key=False, speak=True)
                    break
                
                if text:
                    response = self.ai.send_prompt(text)
                    if response:
                        self.speaker.tts(response, key=False, speak=True)
            except KeyboardInterrupt:
                break

assistant = Assistant(mode="voice")
