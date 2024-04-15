'''-> Voice assistant is the software used to carry users qurey via voice. 
   -> In python we have a SpeechRecogination as a API which  convert ours voice into a text.
   ->webbrowser is a built-in module.'''

import speech_recognition as sr                       #import the speech recognition module
import webbrowser                                     #built-in python module

sr.Microphone(device_index=1)                         #sr.microphone is the class from sr library in python to 
                                                      #device_index is a parameter in sr.microphone which takes a specific microphone device to use for audio input

r=sr.Recognizer()                                     #initialize a recoginiser

r.energy_threshold=5000                               #energy_threshold represents the i/p audio of the min range .
                                                      #threshold helps to filter out the unwanted noise and capyure meaningful audio.

with sr.Microphone() as source:                       #microphone as a source
    print("Speak!!")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)                #convert audio to text
        url='https://www.google.co.in/search?q='      #url of the browser
        search_url=url+text                           #combines url + source text
        webbrowser.open(search_url)                   #open in the browser
    except:
        print("Can't Recoginize")
    print(f">>{text.capitalize()}")                   #prints what user said