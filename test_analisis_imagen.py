# Carga la imagen
image = cv2.imread('cielo.jpeg')

# Muestra el histograma
plot_histogram(image)

#**************************************** subventana de la imagen a escala de grises y mostrar su histograma


# Definir las coordenadas de la subventana (área de interés)
x, y, width, height = 100, 100, 200, 200  # Esto es un ejemplo, ajusta las coordenadas según tu necesidad

# Extraer la subventana
subwindow = image[y:y+height, x:x+width]

# Convertir la subventana a escala de grises
gray_subwindow = cv2.cvtColor(subwindow, cv2.COLOR_BGR2GRAY)

# Mostrar el histograma de la subventana en escala de grises
plot_histogram(gray_subwindow)


#****************************************analizar 5 filas aleatorias de la imagen en escala de grises:

# Obtener el número de filas y columnas de la subventana en escala de grises
num_rows, num_cols = gray_subwindow.shape

# Generar 5 filas aleatorias
random_rows = np.random.randint(0, num_rows, 5)

# Crear un gráfico para visualizar las transiciones de intensidad en las filas aleatorias
plt.figure(figsize=(12, 6))
plt.title("Transiciones de Intensidad en Filas Aleatorias")
plt.xlabel("Columna")
plt.ylabel("Intensidad")

for row in random_rows:
    row_values = gray_subwindow[row, :]
    plt.plot(row_values, label=f"Fila {row}")

plt.legend()
plt.show()