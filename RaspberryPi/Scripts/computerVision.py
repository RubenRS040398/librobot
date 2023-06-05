import numpy as np
import cv2                      # opencv
from picamera import PiCamera
import pytesseract
import time

# Elimina las lineas que estén muy juntas
def removeLines(lines):
    remove = []
    for j in range(0, len(lines)):
        for k in range(0, len(lines)):
            # Evitar comparar con líneas que ya se ha decidido que se van a borrar
            if np.isin(lines[j], remove).all() or np.isin(lines[k], remove).all():
                continue

            # No comparo con lineas que esten detrás en x1 de la actual
            if lines[k][0][0] - lines[j][0][0] <= 0:
                continue

            # Si las lineas están muy juntas eliminamos una
            if lines[k][0][0] - lines[j][0][0] > 30 and lines[k][0][2] - lines[j][0][2] > 30:
                break

            # Elimino la que tenga el valor x1 mayor (Aún no se me ocurre una forma mejor de elegir cual eliminar)
            remove.append(lines[k])

    keep = []
    for line in lines:
        if np.isin(line, remove).all():
            continue

        keep.append(line)

    return keep


# Extiende las lineas al tamaño de la imagen original 
def extendLines(lines, h, new_h1):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]

            # Cambia el valor de y respecto al tamño original de la imagen
            y1 = y1 + new_h1
            y2 = y2 + new_h1

            if y1 > y2:  # Si el angulo de la linea respecto al eje horizontal menos de 90
                delta_x = x1 - x2
                if delta_x != 0:  # Si Delta_X es 0 el angulo son 90 grados
                    delta_y = y1 - y2

                    # Calculo el angulo del triángulo
                    angle = 90 - abs(math.atan(delta_y / delta_x)) * 180 / np.pi
                    tangent = math.tan(angle * np.pi / 180)

                    # Calculo los catetos opuestos del triangulo sabiendo el angulo i es cateto adyacente
                    co_x1 = tangent * (h - y1)
                    co_x2 = tangent * y2

                    # Calculo la x sabiendo la distancia del cateto opuesto
                    x1 = int(x1 + co_x1)
                    x2 = int(x2 - co_x2)

            else:  # Si el angulo de la linea respecto al eje horizontal es 90 o más
                delta_x = x2 - x1
                if delta_x != 0:  # Si Delta_X es 0 el angulo son 90 grados
                    delta_y = y2 - y1

                    # Calculo el angulo del triángulo
                    angle = 90 - abs(math.atan(delta_y / delta_x)) * 180 / np.pi
                    tangent = math.tan(angle * np.pi / 180)

                    # Calculo los catetos opuestos del triangulo sabiendo el angulo i es cateto adyacente
                    co_x1 = tangent * y1
                    co_x2 = tangent * (h - y2)

                    # Calculo la x sabiendo la distancia del cateto opuesto
                    x1 = int(x1 - co_x1)
                    x2 = int(x2 + co_x2)

            # Alargo la linea respecto al tamño original de la imagen        
            y1 = 20
            y2 = h - 20
            line[0] = [x1, y1, x2, y2]

    return lines


# Guarda los libros individualmente en la carpeta 'result' i devuelve un diccionario con el path y el transform
def recortar(path, extended):
    recortes = {}
    for j in range(0, len(extended)):
        if j == len(extended) - 1:
            break
        x1 = extended[j][0][0]
        y1 = extended[j][0][1]
        x2 = extended[j][0][2]
        y2 = extended[j][0][3]

        x3 = extended[j + 1][0][0]
        y3 = extended[j + 1][0][1]
        x4 = extended[j + 1][0][2]
        y4 = extended[j + 1][0][3]

        if x4 <= x1 or x3 <= x2:
            continue

        im = Image.open(path)

        # Define 8-tuple with x,y coordinates of top-left, bottom-left, bottom-right and top-right corners and apply
        transform = [x1, y1, x2, y2, x4, y4, x3, y3]
        result = im.transform((abs(x1 - x3), abs(y1 - y2)), ImageTransform.QuadTransform(transform))

        result.save('/home/pi/rlp-librobot/result/' + str(j) + '.jpg')

        recortes[j] = ['/home/pi/rlp-librobot/result/' + str(j) + '.jpg', transform, ""]

    return recortes


def hacerFoto():
    path = '/home/pi/rlp-librobot/img/prueba.jpg'
    camera = PiCamera()
    camera.start_preview()
    time.sleep(1)
    camera.capture('/home/pi/rlp-librobot/img/prueba.jpg')
    camera.stop_preview()
    camera.close()
    return path


def getlibros(path):
    # Tratar la imagen

    # Leer imagen
    imagen = cv2.imread(path)

    # Pasar a gris
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Median blur
    blur = cv2.medianBlur(gray, 7)
    
    # Cortar imagen
    h, w = np.shape(blur)  # dimensiones originales
    
    new_h1 = int(h * 0.4)  # Nueva altura
    new_h2 = int(h * 0.6)
    
    cropped_blur = blur[new_h1:new_h2, 0:w]  # Cortar
    
    # Canny Edge Detection
    edges = cv2.dilate(cv2.Canny(image=cropped_blur, threshold1=100, threshold2=100), None)
    
    # Open
    kernel = np.ones((25, 1), np.uint8)
    opening = cv2.morphologyEx(edges, cv2.MORPH_OPEN, kernel)
    
    # Encontrar contornos
    
    # Hough
    lines = cv2.HoughLinesP(opening, 1, np.pi / 180, threshold=200, minLineLength=h / 15, maxLineGap=h / 10)
    
    # Ordenar de izquierda a derecha
    lines = sorted(lines, key=lambda a_entry: a_entry[..., 0])
    
    # Eliminar lineas que estén muy juntas
    keep = removeLines(lines)
    
    # Extender lineas al tramaño de la imagen original
    extended = extendLines(keep, h, new_h1)
    
    # Recortar libros
    recortes = recortar(path, extended)
    
    libros = {}
    for key in recortes:
        # Leer imagen
        imagen = cv2.imread(recortes[key][0])
        
        # Pasar a gris
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        
        # Canny Edge Detection
        edges = cv2.dilate(cv2.Canny(image=gray, threshold1=500, threshold2=100), None)
        
        edges = cv2.rotate(edges, cv2.ROTATE_90_CLOCKWISE)
            
        text = pytesseract.image_to_string(edges)
        
        if strlen(text) > 0:
            libros[text] = transform
    
    return libros


def getLibros(path):
    libros = {"el amor en los tiempos del cólera": [1, 1], "la historia interminable": [1, 2],
              "el llibre dels nostres fills": [0, 3], "porta falsa": [1, 4], "el otoño del patriarca": [0, 1],
              "bodas de sangre": [0, 2], "la colmena": [1, 3], "libro de buen amor": [0, 4]}

    time.sleep(5)
    return libros
