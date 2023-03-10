import turtle as tt 
import math as m
import random as r 


def main():
    
    cantRectangulos = int(input("Ingrese la cantidad de rectangulos: "))
    cantTriangulos = int(input("Ingrese la cantidad de triangulos: "))

    while cantRectangulos < 5 or cantRectangulos > 20 and cantTriangulos < 5 or cantTriangulos > 20:
        print ("Error, ingrese un numero entre 5 y 20")
        cantRectangulos = int(input("Ingrese la cantidad de rectangulos: "))
        cantTriangulos = int(input("Ingrese la cantidad de triangulos: "))

    lienzoTrasero()
    contador = 1
    while contador < cantTriangulos + 1 : 
        x = r.randint(-250, 250)
        y = r.randint(-250, 250)
        tamanio = r.randint(1, 250)
        cambioDeGrad = r.randint(1, 360)
        if (x + tamanio < 250 and y + tamanio < 250 and x - tamanio > -250 and y - tamanio > -250):
            pintarTrinagulo(x, y, contador, tamanio, cambioDeGrad)
            contador += 1
            
    contador = 1
    while contador < cantRectangulos + 1 : 
        x = r.randint(-250, 250)
        y = r.randint(-250, 250)
        tamanio = r.randint(1, 250)
        cambioDeGrad = r.randint(1, 360)
        if (x + tamanio < 250 and y + tamanio < 250 and x - tamanio > -250 and y - tamanio > -250):
            pintarRectangulo(x, y, contador, tamanio, cambioDeGrad)
            contador += 1
            
    tt.done()
    
    

def lienzoTrasero():
    tt.penup()
    tt.goto(-250, -250)
    tt.pendown()
    tt.begin_fill()
    tt.fillcolor("violet")
    for i in range(4):
        tt.forward(500)
        tt.left(90)
        
    tt.end_fill()
    
    
def pintarTrinagulo(x, y, id, tamanio, cambioDeGrad):
    if (id % 3 == 0):
        tt.fillcolor("red")
    elif (id % 5 == 0):
        tt.fillcolor("yellow")
    else:
        tt.fillcolor("blue")
    
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.begin_fill()
    tt.left(cambioDeGrad)
    for i in range(3):
        tt.forward(tamanio)
        tt.left(120)
    
    tt.end_fill()

def pintarRectangulo(x, y, id, tamanio, cambioDeGrad):
    tt.fillcolor("black")
    if (id % 2 == 0):
        tt.fillcolor("green")
        
    
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.begin_fill()
    tt.left(cambioDeGrad)
    for i in range(4):
        if (i % 2 == 0):
            tt.forward(tamanio * 1.5)
        else:
            tt.forward(tamanio)
        tt.left(90)
    
    tt.end_fill()
      
if __name__ == '__main__':
    main()
