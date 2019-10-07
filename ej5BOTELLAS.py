b1=int(input('cantidad de botellas de 1L o menos:'))
b2=int(input('cantidad de botellas mayores a 1L:'))

r1=float(b1*0.10)
r2=float(b2*0.25)
d=int(1)

rembolso=r1+r2+d

print('su rembolso total es:', rembolso)