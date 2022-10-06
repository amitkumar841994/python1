
import pyttsx3
engine=pyttsx3.init()
book =open('story.txt','rb')
book_txt=book.readlines()
engine=pyttsx3.init()
for i in book_txt:
    engine.say(i)
    engine.runAndWait()