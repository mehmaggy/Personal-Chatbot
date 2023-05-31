import speech_recognition as sr       # import speech recognition module
import playsound                      # to play saved mp3 file
from gtts import gTTS                 # google text to speech


import os                             # to save/open files
import wolframalpha                   # to calculate strings into formula

from googlesearch import search       # to control browser operations


num = 1
def assistant_speaks(output):
    global num                        # number to rename every audio file with different name
    num += 1
    print("Chatty : ", output)
  
    toSpeak = gTTS(text = output, lang ='en', slow = False)

    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    #playsound.playsound(file, True) 
    os.remove(file)

def get_audio():
  
    record = sr.Recognizer()
    audio = ''
  
    with sr.Microphone() as source:
        print("Speak...")
          
        # record the audio using speech recognition
        audio = record.listen(source, phrase_time_limit = 5) 

    print("Stop.") # wait time limit 5 secs
  
    try:
  
        text = record.recognize_google(audio, language ='en-US')

        print("You : ", text)
        return text
  
    except:
        assistant_speaks("Could not understand your audio, PLease try again!")
        return 0 

def process_text(input):
    try:
        if "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am chatty. Your personal assistance. I am here to make ur life easier.'''
            assistant_speaks(speak)
            return
        elif "what can you do" in input:
            speak = "You can command me to perform various tasks such as calculations or opening applications"
            assistant_speaks(speak)
            return
        elif 'open' in input:
            open_application(input.lower())
            return
        elif 'search' in input or 'google' in input:
            search_web(input)
            return
        else:
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans):
                search_web(input)
            else:
                return
    except:
        assistant_speaks("I dont understand.I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans):
            search_web(input)

def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in input:
        assistant_speaks("Opening MS Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\WordPad.lnk')
    elif "excel" in input:
        assistant_speaks("Opening MS Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel 2016.lnk')
    else:
        assistant_speaks("App not available")
        return
    
def search_web(input):
    if 'google' in input or 'search' in input:
        for j in search(input,tld="co.in",num=10,stop=10,pause=2):
            print(j)


# Main Code

if __name__ == "__main__":

    assistant_speaks("What's your name friend?")
    name ='Friend'
    name = get_audio()

    assistant_speaks("Hello, " + name + '.')
      
    while(1):
  
        assistant_speaks("What can i do for you?")
        text = get_audio().lower()
  
        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, "+ name+'.')
            break


        process_text(text)