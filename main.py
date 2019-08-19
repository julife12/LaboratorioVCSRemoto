print("hola bienvenido a el software para solucionar ecuaciones de tipo, ax2+bx+c")
a=int(input("ingrese el numero del primer termino: "))
b=int(input("ingrese el numero del segundo termino: "))
c=int(input("ingrese el numero del tercer termino: "))
cuadrado= b*b
multiplicacion=a*c
d= cuadrado-4*multiplicacion
doble=2*a
if d>0:
    import math
    x1=((-b)+(math.sqrt(d)))
    x1_1=x1/doble
    x2=((-b)-(math.sqrt(d)))
    x2_1=x2/doble
    print("la solucion para x1= ", x1, "la solucion para x2= ", x2)
else:
    if d==0:
        
        x=(-b)/doble
        print("la solucion es x= ", x)
    else:
        print("no existe solucion en los numeros")


