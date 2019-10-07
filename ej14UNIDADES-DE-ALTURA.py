pies=float(input('inserte el total de pies:'))
pulgadas=float(input('inserte el total de pulgadas:'))

ft=pies*12
IN=ft+pulgadas

cm=IN*2.54

print('total de pulgadas',IN)
print('la equivalencia es:',cm,'cm')