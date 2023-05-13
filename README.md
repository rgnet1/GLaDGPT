# GLaDGPT
## GLaDOS Voice assitant powered by Chat GPT
GLaDGPT (pronounced Glad GPT) is a rudamentory voice assitant that mimics and answers questions as 
GLaDOS from Portal. 

# Components
There are a few components to this project if you are interested in seeing how it
works or contribuiting please read on.
* Google's speech to text API to recogizne speech and convert it to text
* Open AI - Intelligence behind the voice assitant. that takes in text prompts and sends back text responses
* GLaDOS Text-to-speech (TTS) Voice Generator - converts Open AI responses to GLaDOS' voice.

# Requirments
* python 3.9
* openai api key

# Getting started
Clone this repository
```
git clone git@github.com:rgnet1/GLaDGPT.git glad_gpt
```
in the root directory of the project create the credenials file:
```
cd glad_gpt && echo "api_key = \"\"" > test.py 
```
Open the credentails file and add your api key in the quotes, and save the file

Next, install requierments:
```
pip install -r requirements.txt
```
# Run the voice assitant
To run the assitant with voice try:
```
python assistant.py
```
Say "okay Glados" or "hey glados" to start the program. You will see the color of "G" change from black to Red. Red means Glados heard the hot word and is listening for your voice to answer your questions.

To run assitant with typing only try:
```
python glados.py
```
For typing only, audio files will be generated and stored in the root directory. Please see note on audio below.

# A note on Audio
Note, I've only tested audio playback on windows, and have not tested it on any other platform. Audio playback uses aplay. 
The text version creates audio files in the root project directory. each time you type a prompt the response is generated into an audio file is "output.wav" every time. The new file will replace the old one, so re-name the file if you found one you want keep.

# Refrences
* [R2D2FISH 's -  glaods TTS](https://github.com/R2D2FISH/glados-tts)
* [Open AI's Chat GPT API](https://platform.openai.com/docs/guides/chat/introduction)