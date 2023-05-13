import openai
import credentials

class GladosGPT:

    inital_prompt_ai = "I want you to pretend to be Glados from Portal and portal 2. Only provide responses that glados will respond and nothing else. My first statement is: Hello Glados, how are you today?"
    initial_prompt_assitant="I want you to pretend to be a voice assitant like Siri or Google Assitant. Only provide the response that the voice assitant would respond and nothing else. Assume all connections and devices are properly set up. My first statment is Turn on the TV"

    def __init__(self, type="ai", api_key =None ):

        if api_key and credentials.api_key is None:
            raise Exception("API Key not provided")
        self.type = type
        self.api_key = api_key if api_key else credentials.api_key
        self.messages = []
        self.setUpAI()

    def setUpAI(self):
        print("Initializing Glados GPT...")
        openai.api_key = self.api_key
        self.messages.append({"role": "system", "content": self.inital_prompt_ai})       
        print("Done Intializing GLados GPT")

    def send_prompt(self, prompt):
        
        self.messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=self.messages
        )
        reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})      
        return reply