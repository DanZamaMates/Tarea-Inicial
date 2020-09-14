#matricula y nombre 1
#matricula y nombre 2
#proposito del programa

#funcion1  calcular área del rectángulo
def calcularArea(a,b):
    return print(str(a*b))

#funcion2  calcular perímetro del rectángulo
def calcularPerimetro(a,b):
    return print(str(2*a + 2*b))

#instrucciones de accion
#pedir datos

print("medida de un lado del rectángulo")
l1 = float(input())

print("medida de un lado del rectángulo")
l2 = float(input())

#desplegar calculo funcion1
calcularArea(l1,l2)
#desplegar calculo funcion 2
calcularPerimetro(l1,l2)

