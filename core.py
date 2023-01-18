import pyttsx3 as tts
import speech_recognition as sr
from speech_recognition import AudioData
from event import eventHandler


class ai:
    _name__ = ""
    abilities = []

    def __init__(self, name=None):

        self.engine = tts.init()
        # creating recognizer and microphone instances for speech recognition
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self._name__ = name

        # Set up the handlers for the start and stop events
        self.beforeSpeak = eventHandler()
        self.afterSpeak = eventHandler()
        self.beforeListening = eventHandler()
        self.afterListening = eventHandler()

        # listens to the background noise and adjust the energy threshold
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

        voices = self.engine.getProperty('voices')
        for voice in voices:
            self.engine.setProperty('voice', voices[0].id)
            self.engine.setProperty('rate', 150)
            name = voices[0].name
            print(name)
            # self.engine.say(f"my name is {name}")
            # self.engine.runAndWait()


    @property
    def name(self):
        return self._name__

    @name.setter
    def name(self, value):
        self._name__ = value

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
        return sentence

    def listen(self):

        global phrase
        print("Say Something")
        self.engine.say('say something')
        with self.m as source:
            audio: AudioData = self.r.listen(source)

        # recognise speech engine been used is Sphinx
        try:
            phrase = self.r.recognize_sphinx(audio, show_all=False, language="en-GB")
            sentence = f"You just said that   {phrase}"
            self.engine.say(sentence)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
            self.engine.say("Sphinx could not understand")
            self.engine.runAndWait()
        print("You said", phrase)
        try:
            phrase = self.r.recognize_sphinx(audio, show_all=False, language="en-GB")
            if phrase == "Sphinx ":
                self.engine.say("Im listening")
                self.engine.runAndWait()
                with self.m as source:
                    audio = self.r.listen(source)
                phrase = self.r.recognize_sphinx(audio)
                print(f"you said + {self.r.recognize_sphinx(audio)}")
                self.engine.say(f"you said + {self.r.recognize_sphinx(audio)}")
                self.engine.runAndWait()
                return phrase

        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        return phrase

    def stop_ai(self):
        self.r.stop_listening()
        self.engine.stop()
        self.engine.runAndWait()
        self.engine.stop()
        print("stopped Sphinx engine")
