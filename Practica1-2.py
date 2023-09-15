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


#**************************************** función que tome una imagen como entrada y genere un histograma de todos los canales
def plot_histogram(image):
    # Comprobar si la imagen es en escala de grises o a color
    if len(image.shape) == 2:  # Imagen en escala de grises
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])

        # Grafica el histograma
        plt.figure()
        plt.title("Histograma de la Imagen")
        plt.xlabel("Valor de Píxel")
        plt.ylabel("Número de Píxeles")

        plt.plot(hist, color='k', label='Canal Gris')
        plt.legend()
        plt.show()
    else:  # Imagen a color
        hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
        hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])

        # Grafica los histogramas
        plt.figure()
        plt.title("Histograma de la Imagen")
        plt.xlabel("Valor de Píxel")
        plt.ylabel("Número de Píxeles")

        plt.plot(hist_r, color='r', label='Canal Rojo')
        plt.plot(hist_g, color='g', label='Canal Verde')
        plt.plot(hist_b, color='b', label='Canal Azul')

        plt.legend()
        plt.show()
    