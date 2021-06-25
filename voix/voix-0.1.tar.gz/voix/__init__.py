#dependencies

from gtts import gTTS
from googletrans import Translator
import playsound
import os


#variable defintion

translator = Translator()


#main function to genarate voice "speak"

def speak(text, lang="en",save=False , fileName="default",translate=False ):
    try:


        if(translate):
            translatedText=translator.translate(text,dest=lang)
            tts=gTTS(translatedText.text ,lang=lang) 

        else:
            tts = gTTS(text ,lang=lang)    

        if(save):
            tts.save(fileName+'.mp3')
            playsound.playsound(fileName+'.mp3')
            

        if(not save):
            tts.save('deafult.mp3')
            playsound.playsound('deafult.mp3')
            os.remove("deafult.mp3")
    except:
        print("Something went wrong :/")


#the specific key for each language

Key_for_Languages = ['ar', 'bn', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'gu', 'hi', 'hu', 'id', 'it',
'ja', 'kn', 'ko', 'ml', 'pl', 'pt', 'ro', 'ru', 'sk', 'es', 'sv', 'ta', 'te', 'th', 'tr', 'uk', 'vi']


#Number of supported language

Number_of_Supported_Language=32


#all supported languages

Supported_Languages = {
    'Arabic' : 'ar',
    'Bengali' : 'bn',
    'Czech' : 'cs',
    'Danish' : 'dn',
    'Dutch' : 'nl',
    'English' : 'en',
    'Finnish' : 'fi',
    'French' : 'fr',
    'German' : 'de',
    'Greek' : 'el',
    'Gujrati' : 'gu',
    'Hindi' : 'hi',
    'Hungarian' : 'hu',
    'Indonesian' : 'id',
    'Italian' : 'it',
    'Japanese' : 'ja',
    'Kannada' : 'kn',
    'Korean' : 'ko',
    'Malayalam' : 'ml',
    'Polish' : 'pl',
    'Portuguese' : 'pt',
    'Romanian' : 'ro',
    'Russian' : 'ru',
    'Slovak' : 'sk',
    'Spanish' : 'es',
    'Swedish' : 'sv',
    'Tamil' : 'ta',
    'Telungu' : 'te',
    'Thai' : 'th',
    'Turkish' : 'tr',
    'Ukrainian' : 'uk',
    'Vietnamese':'vi'
}
