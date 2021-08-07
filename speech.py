import gtts
from playsound import playsound
import os

tts = gtts.gTTS("jani na", lang="bn")

tts.save("out.mp3")
playsound("out.mp3")

os.system("rm out.mp3")
