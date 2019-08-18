a=int(input("ingrese el numero del primer termino: "))
b=int(input("ingrese el numero del segundo termino: "))
c=int(input("ingrese el numero del tercer termino: "))
d=((b*b)-(4*a*c))
doble=a*2
if d<0:
    x1=(-(b)+(d**0.5))/doble
    x2=(-(b)-(d**0.5))/doble
    print("la solucion para x1= ", x1, "la solucion para x2= ", x2)
