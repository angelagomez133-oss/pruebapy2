import numpy as np

#Se establece la temperatura en grados celcius del mes de 
# setiembre en una ciudad de la selva del Perú
x=np.random.randint(22,35,size=30)
print("Temperatura del mes",x)
print("Temperatura promedio:",np.mean(x),"°")
print("Temperatura mínima;",np.min(x),"°")
print("Temperatura máxima:",np.max(x),"°")
print("Temperatura desv estandar:",np.max(x),"°")

#Se establece la probabilidad de lluvias durante el mes
y=np.random.randint(20,100,size=30)
temperatura=np.random.randint(x)
print("Probabilidad de lluvia del mes",(y))
print("Probabilidad lluvia maxima:",np.max(y),"%")
print("Probabilidad lluvia maxima:",np.min(y),"%")


print("Temperatura 01/09: ",x[0],"°")
print("Prob. lluvia 01/09: ",y[0],"%")
print("Temperatura Semana 01: ",x[0:6],"°")
print("Prob. lluvia Semana 01: ",y[0:6],"%")
print("Promedio temperatura semana 01:",round(np.mean(x[0:6]),2),"°")
print("Probabilidad lluvia semana 01:",round(np.mean(y[0:6]),2),"%")
