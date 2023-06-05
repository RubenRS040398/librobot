import speech_recognition as sr
import nltk
from gtts import gTTS
from playsound import playsound
# import multiprocessing
import os
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from googletrans import Translator
from text2digits import text2digits as t2d
import pyaudio

def recognize_speech_from_mic(reconocedor, microfono):
    #Prepara el diccionario para devolver
    respuesta = {
        "success": False,
        "error": None,
        "transcription": None
    }

    # Comprueba que el recognizer y el micrófono hayan sido declarados
    if not isinstance(reconocedor, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microfono, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # Flag que nos sirve para saber si se ha detectado un audio o solo silencio
    audioReconocido = True

    # Se usa el microfono como fuente
    with microfono as fuente:
        print("Habla ahora:")
        # Ajusta la sensibilidad del micrófono al sonido ambiente
        reconocedor.adjust_for_ambient_noise(fuente, duration=0.5)

        # Intenta grabar el sonido del micrófono
        try:
            audio = reconocedor.listen(fuente, timeout=5)
        except OSError:
            audioReconocido = False
            pass
        except sr.WaitTimeoutError:
            audioReconocido = False
            pass

    # Si el audio ha sido extraído...
    if audioReconocido:
        # ...Intenta un try/except para evitar errores al no entender la voz o no poder conectarse con la API.
        try:
            #Transcribe el texto si puede
            respuesta["transcription"] = reconocedor.recognize_google(audio, language='es-ES')
            respuesta["success"] = True
        except sr.RequestError:
            #Si no ha podido conectarse a la API, obtenemos un error
            respuesta["error"] = "API unavailable"
        except sr.UnknownValueError:
            #Si no se ha podido reconocer la voz,
            respuesta["error"] = "Unable to recognize speech"

    return respuesta

def escucharOrdenes(fraseGrabada, traductor, traducir = 1):
    # Se traduce la frase para preprocesar las frases en ingles (mejor para el stemming y lemmatizing)
    if traducir:
        fraseTraducida = traducirFrase(fraseGrabada, traductor)
    else:
        fraseTraducida = fraseGrabada

    # Se declaran las stopwords y lemmatizers
    stop_words = set(stopwords.words('english'))
    lemmatizador = WordNetLemmatizer()

    #No hace falta sent_tokenize porque la grabacion pilla 1 sola frase -> No hay que separar frases.
    # Se tokeniza la frase recibida por palabras (parecido a string.split(), pero con mas criterios)
    listaPalabras = nltk.word_tokenize(fraseTraducida)
    listaLemmatizador = []
    #print("wordList: ", wordList)

    for palabra in listaPalabras:
        # Se le aplica lemmatizing: reduccion a la raiz generica
        listaLemmatizador.append(lemmatizador.lemmatize(palabra))

    #print("lem list :", lemmList)
    # Se eliminan las stopwords: palabras con poco valor semantico
    listaLemmatizador = [palabra for palabra in listaLemmatizador if palabra not in stop_words]

    #Se le aplica tagging para relacionar cada token con un tipo de sintagma (verbo, sujeto...)
    fraseFinal = nltk.pos_tag(listaLemmatizador)

    return fraseFinal, fraseTraducida

def traducirFrase(fraseGrabada, traductor):
    # Se eliminan las mayusculas y se eliminan algunos signos de puntuacion
    fraseBase = fraseGrabada.lower()
    #fraseBase = re.sub('\[.*?¿\]\%', ' ', fraseBase)
    fraseBase = re.sub('\[.*?¿\]\%', ' ', fraseBase)
    # Se detecta el idioma y si es español...
    print("Frase: ", fraseBase)
    idioma = str(traductor.detect(fraseBase).lang)

    print(idioma)

    # ...se traduce la frase a ingles
    if (idioma == 'en'):
        fraseTraducida = fraseBase
    else:
        fraseBase = traductor.translate(fraseBase, src='es')
        fraseTraducida = fraseBase.text

    #print("frase traducida :", fraseTraducida)
    return fraseTraducida