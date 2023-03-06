# Se comienza con una imagen basada en Archlinux
FROM archlinux  
#actualizamos los repositorios
RUN pacman -Sy
#instala python dentro de la imagen  
RUN pacman -S python --noconfirm
#instala pip dentro de la imagen 
RUN pacman -S python-pip --noconfirm
#instala la libreria numpy 
RUN pip install numpy
#Generamos artesanalmente un ejemplo de python con numpy
RUN echo "import numpy as np"  > numpy_test.py
RUN echo "print(np.zeros((2,2)))" >> numpy_test.py
#se define que al instanciar la imagen en un contenedor se corra por defecto python numpy_test.py
CMD ["python","numpy_test.py"]