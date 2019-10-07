agua=4.186
ele= 8.9
J= 2.7777e-7

Volumen =float(input("inserte los mililitros de agua:"))
Dtemperatura=float(input( "inserte la temperatura en grados celcius:"))
q= Volumen * Dtemperatura * agua
print (" usted requiere %d joules de energia" % q )
kilovatios= q*J
costo =kilovatios * ele
print ( "la energia del costo  es en  centavos  : ", costo)