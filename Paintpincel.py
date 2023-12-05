import cv2
import numpy as np

# Variables globales
drawing = False
last_point = (-1, -1)

# Función para manejar el evento del mouse
def mouse_handler(event, x, y, flags, param):
    global drawing, last_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(image, last_point, (x, y), (0, 0, 255), 2)
            last_point = (x, y)
            cv2.imshow("Dibujar Líneas", image)

# Crear una imagen en blanco
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Crear una ventana y asociar la función de manejo del mouse
cv2.namedWindow("Dibujar Líneas")
cv2.setMouseCallback("Dibujar Líneas", mouse_handler)