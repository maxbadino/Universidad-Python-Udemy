from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

rectangulo = Rectangulo(5, 4, "azul")
print(rectangulo.area())
print(rectangulo.color)
# el orden de busqueda es:
# Cuadrado, FiguraGeometrica(izquierda), Color(derecha), Object(Clase Abuela) 
# print(Cuadrado.mro())
# print(Rectangulo.mro())

