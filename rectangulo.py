"""from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    #def __str__(self):
    #    return  super(Rectangulo, self).__str__() + "ancho:" + str(self.get_ancho) + "alto:" + str(self.get_alto) +"color:" + self.__get_color

#rectangulo = Rectangulo(4, 5, "verde")
#print(rectangulo)

    def area(self):
        return self.__ancho * self.__alto """

from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        #hace referencia a FiguraGeometrica por la prioridad
        #super().__init__(lado, lado) 
        Color.__init__(self, color)
    
    def area(self):
        return self.__alto * self.__ancho



