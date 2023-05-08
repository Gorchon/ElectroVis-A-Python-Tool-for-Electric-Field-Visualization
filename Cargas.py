import numpy as np                          # NumPy: librería para cálculo científico con Python
import matplotlib.pyplot as plt             # Matplotlib: librería para visualización de gráficos
from matplotlib.patches import Polygon      # Matplotlib.patches: clase para dibujar figuras poligonales

# Definir la función para dibujar el campo eléctrico
def draw_field(long):
    # Configurar el gráfico1
    figura, ax = plt.subplots()                 # Crear una figura y un conjunto de ejes
    ax.set_xlim(-20, 20)                     # Establecer los límites del eje x
    ax.set_ylim(-10-(long/2), 10+(long/2))   # Establecer los límites del eje y
    ax.set_aspect('equal')                   # Establecer la relación de aspecto (para que los ejes tengan la misma escala)
    ax.set_facecolor('#333333')      
    figura.suptitle('Charges And Fields', fontname='Arial', fontsize=16, fontweight='bold')
    figura.patch.set_facecolor('#aa8caf')
    

    
    # Crear una lista de coordenadas para el primer rectángulo
    rect1_coords = [(-8, -long/2), (-5, -long/2), (-5, long/2), (-8, long/2)]

    # Crear el primer rectángulo usando la lista de coordenadas
    rect1 = Polygon(rect1_coords, facecolor='red', edgecolor='black')   # Crear un objeto Polygon con las coordenadas y los colores especificados
    ax.add_patch(rect1)                        # Añadir el objeto Polygon al gráfico

    # Añadir el símbolo de carga positiva dentro del primer rectángulo
    ax.text(-6.5, 0, '+', fontsize=20, horizontalalignment='center', verticalalignment='center')  # Añadir texto en la posición indicada

    # Crear una lista de coordenadas para el segundo rectángulo
    rect2_coords = [(5, -long/2), (8,-long/2), (8, long/2), (5, long/2)]

    # Crear el segundo rectángulo usando la lista de coordenadas
    rect2 = Polygon(rect2_coords, facecolor='blue', edgecolor='black')   # Crear un objeto Polygon con las coordenadas y los colores especificados
    ax.add_patch(rect2)                        # Añadir el objeto Polygon al gráfico

    # Añadir el símbolo de carga negativa dentro del segundo rectángulo
    ax.text(6.5, 0, '-', fontsize=20, horizontalalignment='right', verticalalignment='center')  # Añadir texto en la posición indicada

    # Configurar los vectores del campo eléctrico
    X, Y = np.meshgrid(np.linspace(-20, 20, 20), np.linspace(-10-(long/2), 10+(long/2), 20))   # Crear una malla de puntos
    Ex = np.zeros_like(X)                    # Crear un array con ceros con la misma forma que X
    Ey = np.zeros_like(Y)                    # Crear un array con ceros con la misma forma que Y


    # Calculate the electric field vectors
    # Formula distancia Eucladiana: r = sqrt((x-x0)^2 + (y-y0)^2)
    for i in range(20):
        for j in range(20):
            x = X[i][j]
            y = Y[i][j]
            r1 = np.sqrt((x+6.5)**2 + y**2)
            r2 = np.sqrt((x-6.5)**2 + y**2)
            #Formula para calcular el campo electrico entre ambas cargas  Ex = x+6.5/r1^3 - x - 6.5/ r2^3
            Ex[i][j] = (x+6.5)/r1**3 - (x-6.5)/r2**3
            #Ey​=​y/r1^3​-y/r2^3
            Ey[i][j] = y/r1**3 - y/r2**3

    # Normalize the electric field vectors
    E = np.sqrt(Ex**2 + Ey**2)
    Ex_norm = Ex/E
    Ey_norm = Ey/E

    # Draw the electric field vectors
    plt.quiver(X, Y, Ex_norm, Ey_norm, color="yellow")

    # Show the plot
    plt.show()

# Prompt the user to input the length of the plates
long = float(input("Enter the length of the plates: "))

# Draw the electric field
draw_field(long)
