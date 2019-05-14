import pyttsx3

# initializing the engine for speaking. Windows already has 2 by default, Male and Female
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# For setting male set id = 0, for female id = 1
engine.setProperty("voice", voices[0])

# Voice Rate
rate = engine.getProperty("rate")
engine.setProperty("rate", 130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def main():
    speak("Hi my name is anna, and I will be helping you today.")

if __name__ == "__main__":
    main()


