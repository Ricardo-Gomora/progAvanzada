interes=0.4
deposito=float(input('deposito del ano:'))
ano1=deposito*interes
ano1t=ano1+deposito
print('total del primer anho',ano1t)


ano2=ano1t*interes
ano2t=ano1t+ano2
print('total del segundo anho',ano2t)

ano3=ano2t*interes
ano3t=ano2t+ano3
print('total del tercer anho',ano3t)
