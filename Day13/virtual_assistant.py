import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from numpy.f2py.auxfuncs import replace


# LISTEN OUR MIC AND RETURN THE AUDIO AS TEXT
def audio2text():
    # Save recognizer into a variable
    rec = sr.Recognizer()
    # Config mic
    with sr.Microphone() as source:
        # hold time
        rec.pause_threshold = 0.8
        # Log info. Record start
        print("Say something!")
        # Save audio
        audio = rec.listen(source)
        try:
            # search in google
            request = rec.recognize_google(audio, language="es-mx")
            # Log info.
            print("This is what i understand: " + request)
            # Return request
            return request
        # Error: Audio not understood
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            # return error
            return "Holding ..."
        # Error: Request incomplete
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return "Holding ..."
        # Other Error
        except:
            print("Oops. Something bad happened")
            return "Holding ..."

# ASSISTANT TALK
def talk(message):
    # Start pyttsx3 engine
    engine = pyttsx3.init()

    # Available voices
    voices = engine.getProperty('voices')
    # count = 0
    # for voice in voices:
    #     print(f"Voice: {voice.name}, ID: {voice.id}[{count}] ")
    #     count += 1

    # Select voice language
    engine.setProperty('voice', voices[36].id)  # Select Spanish, latin america
    # Config speed talk
    engine.setProperty('rate', 190)

    # Pronounce message
    engine.say(message)
    engine.runAndWait()
    engine.stop()

# Info about day week
def req_day():
    day = datetime.date.today()
    # Get day of week
    week_day = day.weekday()
    # Days of week dictionary
    calendar = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    talk(f"Te entiendo Klee. El día de hoy es {calendar[week_day]}. ¿Necesitas algo más? o")
    print(calendar[week_day])

# Info current hour
def req_hour():
    hour = datetime.datetime.now()
    hour = f'En este momento son las {hour.hour} horas y {hour.minute} minutos con {hour.second} segundos. o'
    print(hour)
    # say current time
    talk(hour)

# Welcome function
def welcome():
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = "Buenas noches"
    elif 6 <= hour.hour < 13:
        moment = "Buen dia"
    else:
        moment = "Buenas tardes"

    talk(f"{moment} Klee, soy Boberto, tu asistente virtual. ¿En qué te puedo ayudar hoy? o")

# Main assistant function
def req_something():
    welcome()
    start = True
    # Main loop
    while start:
        # Turn on main and save the request into string
        request = audio2text().lower()
        if 'abrir youtube' in request:
            talk("¡Claro!. Abriendo YouTube")
            webbrowser.open_new_tab('https://www.youtube.com')
            continue
        elif 'abrir navegador' in request:
            talk("Entiendo. Abriendo Navegador")
            webbrowser.open("https://www.google.com")
            continue
        elif 'qué día es hoy' in request:
            req_day()
            continue
        elif 'qué hora es' in request:
            req_hour()
            continue
        elif 'busca en wikipedia' in request:
            talk("Haciendo busqueda en wikipedia o")
            request = request.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            result = wikipedia.summary(request, sentences=1)
            talk("Encontre la siguiente información: " + result)
            continue
        elif 'busca en internet' in request:
            talk("Haciendo busqueda, espera un segundo o")
            request = request.replace('busca en internet', '')
            pywhatkit.search(request)
            talk("Esto es lo que encontré o")
            continue
        elif 'reproducir' in request:
            pywhatkit.playonyt(request)
            talk("Buena elección. Estoy seleccionando el mejor video")
            continue
        elif 'broma' in request:
            talk(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in request:
            action = request.split('de')[-1].strip()
            wallet = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                action_search = wallet[action]
                action_search = yf.Ticker(action_search)
                current_price = action_search.info['regularMarketPrice']
                talk(f'Esto es lo que encontré, el precio de {action} es {current_price} o')
                continue
            except:
                talk("Perdón Klee, aun soy torpe y no pude encontrar nada")
                continue
        elif 'adios' in request:
            talk("Me ire a descanzar")

req_something()

# req_hour()
# day_week()
# audio2text()



















