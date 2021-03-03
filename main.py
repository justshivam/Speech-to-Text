import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()


with mic as source:
    print('start')
    audio = r.listen(source)
    print('end')
    print(r.recognize_google(audio))
