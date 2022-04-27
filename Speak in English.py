
import pyttsx3
from deep_translator import GoogleTranslator
import speech_recognition as sr
import winsound
import PySimpleGUI as sg

r = sr.Recognizer()
m = sr.Microphone()

layout = [[sg.Text('Select Input Language:')],
          [sg.Combo(['Afrikaans', 'Arabic', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Finnish', 'French', 'Gujarati', 'Hindi', 'Marathi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian', 'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Malayalam', 'Myanmar (Burmese)', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Chinese'],default_value='Marathi',key='langg')],
          [sg.ReadButton('Speak', size=(10, 2))],
          [sg.Output(size=(80, 10))],
          [sg.Exit(size=(10, 2))]]

window = sg.Window("Speak in English  (!!! Email: vaumtol@gmail.com !!!)",layout,size=(500,400))

while True:
    event, values = window.Read()
    if event == 'Speak':
        lang_dict = {'Afrikaans': 'af', 'Arabic': 'ar', 'Bulgarian': 'bg', 'Bengali': 'bn', 'Bosnian': 'bs',
                     'Catalan': 'ca', 'Czech': 'cs', 'Welsh': 'cy', 'Danish': 'da', 'German': 'de', 'Greek': 'el',
                     'English': 'en', 'Esperanto': 'eo', 'Spanish': 'es', 'Estonian': 'et', 'Finnish': 'fi',
                     'French': 'fr', 'Gujarati': 'gu', 'Hindi': 'hi', 'Croatian': 'hr', 'Hungarian': 'hu',
                     'Armenian': 'hy', 'Indonesian': 'id', 'Icelandic': 'is', 'Italian': 'it', 'Japanese': 'ja',
                     'Javanese': 'jw', 'Khmer': 'km', 'Kannada': 'kn', 'Korean': 'ko', 'Latin': 'la', 'Latvian': 'lv',
                     'Macedonian': 'mk', 'Malayalam': 'ml', 'Marathi': 'mr', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne',
                     'Dutch': 'nl', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro',
                     'Russian': 'ru', 'Sinhala': 'si', 'Slovak': 'sk', 'Albanian': 'sq', 'Serbian': 'sr',
                     'Sundanese': 'su', 'Swedish': 'sv', 'Swahili': 'sw', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th',
                     'Filipino': 'tl', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Vietnamese': 'vi',
                     'Chinese': 'zh-CN'}
        lang = values['langg']
        language = lang_dict.get(lang)
        try:
            with m as source:
                r.adjust_for_ambient_noise(source)
                print('----')
                winsound.Beep(1500, 100)
                aud = r.listen(source)
                value = r.recognize_google(aud, language=language)
                translated = GoogleTranslator(source='auto', target='en').translate(value)
                print(value)
                print(translated)
                engine = pyttsx3.init()
                rate = engine.getProperty('rate')
                engine.setProperty('rate', 100)
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[1].id)
                engine.say(translated)
                engine.runAndWait()

                winsound.Beep(2000, 100)
        except:
            sg.popup('error')
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
window.Close()
