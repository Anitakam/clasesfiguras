class Poligono(object):
    __slots__ = ('dim1', 'dim2')
 
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
 
    def area(self):
        print(('VALORES'))
 
 
 
class Triangulo(Poligono):
    def __init__(self, dim1, dim2, base, altura):
        super().__init__(dim1, dim2)
        self.base = base
        self.altura = altura
 
    def area(self):
        print(('El área del triángulo es:'))
        return((self.base * self.altura) / 2.)
 
    def perimetro(self):
        print(('El perímetro del triángulo es: '))
        return(self.dim1 + self.dim2 + self.base)

class cuadrado(Poligono):
    def __init__(self, dim1, dim2, base, altura):
        super().__init__(dim1, dim2)
        self.base = base
        self.altura = altura
        
        
 
    def area(self):
        print(('El área del cuadrado es es:'))
        return((self.base * self.altura))

      
    def perimetro(self):
        print(('El perímetro del cuadrado es: '))
        return(self.dim1 * 4)
 
def main():
    F =  Poligono(10, 10)
    T = Triangulo(10, 8, 5, 6)
    C = cuadrado(3, 3, 3, 3)
    
    F.area()
    print((T.area()))
    print((T.perimetro()))
    print((C.area()))
    print((C.perimetro()))
 
    
  
 
if __name__ == '__main__':
    main()
