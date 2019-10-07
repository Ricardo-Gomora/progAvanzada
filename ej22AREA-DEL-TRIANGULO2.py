A= float (input("ingrese el primer lado del trangulo;")) 
B= float (input ("ingrese el segundo lado del triangulo:"))
C= float (input ("ingrese el tercer lado del triangulo:"))

if (A+B)>C and (A+C)>B and (B+C)>A:
   print("Los lados corresponden a un triangulo")    
else:
    print ("Los lados no corrsponden a un triangulo")

S=(A+B+C)/2
area =(S*(S-A)*(S-B)*(S-C))**0.5
print ("El area del triangulo es:" ,area)
