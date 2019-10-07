D=float(input('ingresa los dias:'))
H=float(input('ingresa las horas:'))
M=float(input('ingresa los minutos:'))
S=float(input('ingresa los segundos:'))

dias=D*86400
horas=H*3600
minutos=M*60
segundos=S

totaldesegundos=dias+horas+minutos+segundos
print('el total de segundos es:', totaldesegundos)

