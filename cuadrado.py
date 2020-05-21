from figura_geometrica import FiguraGeometrica
# from color import Color

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        #hace referencia a FiguraGeometrica por la prioridad
        #super().__init__(lado, lado) 
        self.color = color


