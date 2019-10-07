a=int (input("Inserte su primer numero:"))
b=int (input("Inserte su segundo numero:"))
c=int (input("Inserte su tercer numero"))
MIN = min (a,b,c)
MAX = max (a,b,c)
MED= a+b+c -MIN-MAX

print(" Los numeros en orden son:")
print("",MIN)
print("",MED)
print("",MAX)