import serial
import time


def activarVentosa():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    time.sleep(3)
    ser.reset_input_buffer()

    ser.write(b"1\n")
    time.sleep(2)
    ser.close()


def desactivarVentosa():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    time.sleep(3)
    ser.reset_input_buffer()

    ser.write(b"0\n")
    ser.close()

def avanzar(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"1,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)


def retroceder(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"2,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)


def girar90(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"3,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)


def acercarse(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"4,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)


def alejarse(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"5,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)


def subir(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"6,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)


def bajar(tiempo, base):
    tiempoBytes = bytes(str(tiempo) + "\n", 'utf-8')
    metodo = b"7,"
    base.write(b"".join([metodo, tiempoBytes]))
    time.sleep(tiempo / 1000 + 2)