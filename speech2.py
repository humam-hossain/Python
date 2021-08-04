import pyttsx3

engine = pyttsx3.init()

text = "flex koro tumi naaaaaaaaa??"

voices = engine.getProperty('voices')
for voice in voices:
    print(voice)

engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 150)
engine.say(text)

# engine.save_to_file(text, "flex.mp3")

engine.runAndWait()
