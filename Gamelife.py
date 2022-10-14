#Juego de la vida Mikebarrsan 23/08/22
"""
#GAMELIFE
Contexto:
El juego de la vida de John Conway es un programa que se conoce como autómata celular, tiene varias "células" que consisten en varias casillas en una rejilla que están vivas o muertas
dependiendo si están "rellenas" o no, así como el número de vecinos vivos/muertos que tengan.
Este programa simula las 3 reglas que estableció John Conway:
- Nacimiento: si una célula muerta está rodeada por exactamente 3 células vivas, esta nacerá.
- Supervivencia: si una célula viva está rodeada por 2 o 3 células vivas, esta sobrevive.
- Muerte: si una célula viva tiene menos de 2 o más de 3 células vecinas vivas, esta muere.

Asimismo, el juego de la vida es un programa increíble que puede ser comparado con procesos físicos, biológicos e incluso sociales, etc... aparte de ser muy atractivo visualmente.
Este programa tiene varias reglas definidas que demostrarán los comportamientos peculiares de las "células" de John Conway, como resultado se puede esperar que la población:
- Se estabilice: todas las células vivas se queden quietas
- Se extinga: todas la células mueran
- Sea indefinida: nunca deje de haber nacimientos y muertes

**En este caso, se trató de ejecutar el programa en un sistema MacOS pero la librería pygame no se ejecutaba correctamente por lo que las siguientes instrucciones de instalación de
los prerrequisitos son solo para Windows.

Prerrequisitos (Windows):
- Instalar python:
    - Descargar la versión más reciente en el sitio oficial de python: https://www.python.org/downloads/
- Instalar pip (extensión de pygame para instalar librerías)
    - De acuerdo a la versión de su python, descargue los siguientes enlaces como archivos en su pc (moverlo en donde tiene el programa):
        - Instalador: instalador get-pip.py
        - Python 3.2: get-pip.py
        - Python 3.3 o 3.4: get-pip.py o Python 3.4 get-pip.py
    - Ahora ir a la terminal y localizarse en la ubicación del archivo anterior y ejecutar el siguiente comando: ‘python get-pip.py’
- Instalar librería pygame y numpy:
    - Instalarlas desde la terminal con el comando -pip install “nombre de la librería”- (encontrarse en la misma ubicación que el programa)
"""
#Bibliotecas
import pygame#Para la interfaz gráfica
import numpy as np#Para asignarle los valores de 1 y 0 a las células y guardar una copia del nuevo estado de estas
import time#Para poner un time sleep entre cada animación y sea más cómodo percibibir la "animación"
import random#Para pponer números aleatorios en la creación de status y crear un inicioo aleatorio de células vivas y muertas
pygame.init()
"""
==================================================================================Funciones secundarias========================================================================================
"""
#Datos para la creación de la rejilla
Rejilla = ancho, largo = 800, 800
color_fondo = 30, 30, 30
filas = 40
columnas = 40
pantalla = pygame.display.set_mode(Rejilla)#Indica las proporciones de la pantalla
pantalla.fill(color_fondo)#Colorea con el color de fondo (negro)
def creac_rejilla(pantalla):
"""
(funciones, ciclos y ciclos anidados)
recibe: pantalla
Esta función se encarga de crear y mostrar una rejilla en "blanco"
gris muy oscuro en la escala RGB
"""
    for num_filas in range (0, 800, 20):
        for contador in range (0, 800, 20):
            celula = pygame.rect.Rect(contador, num_filas, 20, 20)#Da las proporciones y posición de la célula
            pantalla.fill(color_fondo)
            pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)#Rellena la célula de color negro
            pygame.display.flip()#Muestra lo anterior en pantalla
def creacion_estatus(filas, columnas):
"""
(operadores, funciones, listas, listas anidadas, ciclos y ciclos anidados)
recibe: filas, columnas
Esta función crea una matriz con células vivas/muertas al azar, asimismo, la muestra en pantalla
devuelve: status
"""
    status = np.zeros((filas, columnas))
    for num_filas in range (filas):
        for contador in range (columnas):
            status[num_filas, contador] = int(random.randint(0, 1))
    for num_filas in range (filas):
        for contador in range (columnas):
            if status[num_filas, contador] == 0:
                celula = pygame.rect.Rect(contador*20, num_filas*20, 20, 20)
                pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)
            if status[num_filas, contador] == 1:
                celula = pygame.rect.Rect(contador*20, num_filas*20, 20, 20)
                pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
    pygame.display.flip()
    return status
"""
===========================================================================Parte principal del programa========================================================================================
"""
def juego(status, filas, columnas):
"""
(operadores, funciones, listas, listas anidadas, ciclos y ciclos anidados)
recibe: status, filas y columnas
Esta función evalúa el estado aleatorio generado anteriormente de las células y evalúa a sus vecinos y acuerdo a las reglas de el juego de la vida,
genera una matriz diferente y por ende muestra en pantalla una rejilla acorde a las reglas, refresca con un ritmo de .1 segundos y genera el "GIF" de el juego de la vida.
"""
    new_Status = np.copy(status)#Aquí creamos un nuevo status para el juego, porque si no guardamos los cambios en otro status durante su ejecución, tomará en cuenta las nuevas asignaciones
    #de valor miientras calculas los siguientes estadoos de las células y eso no es lo que queremos. Lo que queremos es que evalue el nuevo estado de la célula de acuerdo a los status anteriores
    while True:
        #COLOREADO Y ASIGNACIÓN DE VALOR
        for y in range (filas):
            for x in range (columnas):
                #Suma de vecinos, tiene un "%" para que cuando se encuentre en las esquinas y haya una célula que exceda los límites de la rejilla, tome la célula del lado opuesto
                #de la rejilla
                vecinos = 0
                izq_up_y = (y-1)%40
                izq_up_x = (x-1)%40
                vecinos+=status[izq_up_y, izq_up_x]
                m_up_y = (y-1)%40
                m_up_x = x%40
                vecinos+=status[m_up_y, m_up_x]
                der_up_y = (y-1)%40
                der_up_x = (x+1)%40
                vecinos+=status[der_up_y, der_up_x]
                izq_m_y = y%40
                izq_m_x = (x-1)%40
                vecinos+=status[izq_m_y, izq_m_x]
                der_m_y = y%40
                der_m_x = (x+1)%40
                vecinos+=status[der_m_y, der_m_x]
                izq_d_y = (y+1)%40
                izq_d_x = (x-1)%40
                vecinos+=status[izq_d_y, izq_d_x]
                m_d_y = (y+1)%40
                m_d_x = x%40
                vecinos+=status[m_d_y, m_d_x]
                der_d_y = (y+1)%40
                der_d_x = (x+1)%40
                vecinos+=status[der_d_y, der_d_x]
                #Aquí es donde se les asigna el valor al nuevo estatus del juego (el cual sserá dibujado en la parte de abajo)
                if status[y, x] == 0:
                    if vecinos == 3:
                        new_Status[y, x] = 1
                    else:
                        new_Status[y, x] = 0
                elif status[y, x] == 1:
                    if vecinos==2:
                        new_Status[y, x] = 1
                    elif vecinos==3:
                        new_Status[y, x] = 1
                    else:
                        new_Status[y, x] = 0
                #Aquí es donde de acuerdo al estado anterior, dibuja el nuevo status
                if new_Status[y, x] == 0:
                    if vecinos == 3:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
                    else:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (30, 30, 30), celula, 0)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)
                elif new_Status[y, x] == 1:
                    if vecinos==2:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
                    elif vecinos==3:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
                    else:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (30, 30, 30), celula, 0)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)
                if y==39 and x==39:
                    status = np.copy(new_Status) #Aquí se guarda el nuevo estatus en el status anterior para la siguiente evaluación de los vecinos en el siguiente nuevo status
                    pygame.display.flip()#Esto despliega en pantalla los cambios realizados de nacimientos, muertes o supervivencias
                    time.sleep(.1)#Realentiza la animación a .1 segundos para que sea más fácil seguir la animación, este parámetro se puede cambiar
"""
================================================================================================Main=========================================================================================
"""
def main(pantalla, filas, columnas):
    creac_rejilla(pantalla)#Llama a la función creación rejilla para que ponga la rejilla en "blanco"
    status = creacion_estatus(filas, columnas)#Llama esta función para que nos de estado de células (vivas/muertas) de manera aleatoria
    juego(status, filas, columnas)#De acuerdo al estado anterior generado, esta función evaluará de manera infinita a las células y hará los cambios pertinentes
main(pantalla, filas, columnas)#Llama al main
