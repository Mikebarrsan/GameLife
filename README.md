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
