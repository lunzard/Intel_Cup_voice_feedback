import pyttsx3
import time

engine = pyttsx3.init()

is_connected = True

rate = engine.getProperty('rate')
print('the rate is', rate)
voices = engine.getProperty('voices')

for voice in voices:
    print(voice)

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

while is_connected:
    text_input = input('Text to Convert: ')
    if text_input == 'exit':
        is_connected = False
        engine.say('Your command is exit')
        engine.runAndWait()
        time.sleep(1)
        engine.say('Goodbye')
    else:
        engine.say(text_input)
    engine.runAndWait()

engine.stop()
print('Engine stopped')