"""
Speech Recognition and print the words or
Sentences Using python
"""
"""
 * Basic and Funtional. 
 * Uses google API (means needs Internet Connection)
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:  #هنا البرنامج هيستخدم المايك 
    print("say besm allah and talk only english\n")     #هنا بدي أمر للمستخدم انه يتكلم
    audio = r.listen(source)     #هنا بيسجل الكلام اللي بيتقال

    text = r.recognize_google(audio)  
    print(text)        #هنا كلامك اللي انتا قولته