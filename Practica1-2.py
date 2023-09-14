import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen con transiciones de colores notorias mediante OpenCV
imagen = cv2.imread('cielo.jpg',1)

#Función para generar histograma considearndo todos los canales
def hist_plot(img):
    height, width, channels = img.shape
    # Lista para almacenar la frecuencia de valores de cada canal de color
    count = [[] for _ in range(channels)]

    # Lista para todos los posibles valores de intensidad
    r = list(range(256))

    for c in range(channels):
        for k in range(256):
            conta1 = 0
            for i in range(height):
                for j in range(width):
                    if img[i, j, c] == k:
                        conta1 += 1
            count[c].append(conta1)

    return (r, count)

# Obtener el histograma
r, count = hist_plot(imagen)

# Dibujar el histograma para cada canal de color en un mismo gráfico
for c in range(imagen.shape[2]):
    plt.plot(r, count[c], label=f'Canal {c}')

plt.xlabel('Intensidad')
plt.ylabel('Pixeles')
plt.title('Histograma de la imagen (todos los canales)')
plt.legend()
plt.show()