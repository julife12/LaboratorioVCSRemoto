print("hola bienvenido a el software para solucionar ecuaciones de tipo, ax2+bx+c")
a=int(input("ingrese el numero del primer termino: "))
b=int(input("ingrese el numero del segundo termino: "))
c=int(input("ingrese el numero del tercer termino: "))
cuadrado=b*b
ac4=a*c*4
d= (cuadrado-ac4)
if d>0:
    import math
    x1=(((-b)+(math.sqrt(d))/a*2))
    x2=(((-b)-(math.sqrt(d))/a*2))
    print("la solucion para x1= ", x1, "la solucion para x2= ", x2)
else:
    if d==0:
        
        x=(-(b))/a*2
        print("la solucion es x= ", x)
    else:
        print("no existe solucion en los numeros")


