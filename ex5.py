def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
     speak("moti jiji")
     speak("Tona choooo")
     speak("hello govind")
