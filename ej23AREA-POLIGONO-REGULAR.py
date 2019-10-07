import math

S=float(input('longitud de los lados'))
N=int(input('numero de lados'))

area=(N)*(S*S)/4*math.tan(3.146/N)

print('el area del poligono es:', area)