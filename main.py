print("hola bienvenido a el software para solucionar ecuaciones de tipo, ax^2+bx+c")
a=int(input("ingrese el termino a: "))
b=int(input("ingrese el termino b: "))
c=int(input("ingrese el termino c: "))
cuadrado= b*b
multiplicacion=a*c
import math
d=math.sqrt(cuadrado-4*multiplicacion)
doble=2*a
if d>0:
    x1=((-b)+d)
    x1_1=x1/doble
    x2=((-b)-(d))
    x2_1=x2/doble
    print("la solucion para x1= ", x1_1, "la solucion para x2= ", x2_1)
else:
    if d==0:
        
        x=(-b)/doble
        print("la solucion es x= ", x)
    else:
        print("no existe solucion en los terminos descritos")

        