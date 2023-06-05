from speechRecognition import *
from computerVision import *
from arduinoOrders import *

import serial
import time
import pyaudio
import speech_recognition as sr

def main():
    base = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    time.sleep(3)
    base.reset_input_buffer()
    
    desactivarVentosa()
    time.sleep(1)
    
    """Visión por computador"""
    path_foto = hacerFoto()
    libros = getLibros(path_foto)

    """Reconocedor de voz"""
    stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=0)
    reconocedor = sr.Recognizer()
    microfono = sr.Microphone()
    ## Error  traductor = googletrans.Translator()
    traductor = Translator()
    
    # Para saber cuando hablar
    alejarse(10, base)
    acercarse(10, base)
    
    intentos = 0
    encontrado = False
    while True:
        # Si detecta mas de 3 intentos fallidos, se apaga
        if intentos >= 3:
            break
        intentos += 1

        resultado = recognize_speech_from_mic(reconocedor, microfono)
        print(resultado)

        if resultado['transcription'] is not None:
            for key in libros:
                if key == resultado['transcription']:
                    position = libros[key]
                    encontrado = True
                    break
            break
    
    if encontrado == True:
        """Movimiento"""
        tiempo = int(position[1] * 1.1 * 120)

        avanzar(tiempo, base)

        boolbajar = False
        if position[0] == 1:
            subir(3000, base)
            boolbajar = True

        acercarse(300, base)
        activarVentosa()
        alejarse(1000, base)
        
        if boolbajar == True:
            bajar(3000, base)

        girar90(750, base)
        desactivarVentosa()
        time.sleep(5)

main()