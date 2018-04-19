import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return ( 230*(pow(x,4)) + 18*(pow(x,3)) + 9*(pow(x,2)) - (221*x) - 9 )

def fprima(x):
    return ( 920*(pow(x,3)) + 54*(pow(x,2)) + 18*x - 221)

#Programa principal
print (" ")
print ("MÉTODO DE NEWTON-RAPHSON")
print (" ")

#Valor digitado por el usuario
x = float(input('Ingresa el valor de x: '))

#Error digitado por el usuario
tolerancia=float(input('Introduce el valor para la tolerancia: '))

raiz = []

raiz.insert(0,0)

i = 0

#Error por defecto para que el programa inicie
error = 1

print (" ")

xD = np.linspace(3, -3, ( tolerancia*10000000000000000 ) )

print ('{:^10}{:^10}{:^10}{:^15}{:^15}{:^15}'.format('Iteraciones','x0','x1','F(x0)','F\'(x0)','f(x1)'))

print (" ")

while abs(error) > tolerancia:

    x1 = x - (f(x)/fprima(x))

    raiz.append( x1 )

    print ('{:^10}{:^10.6f}{:^10.6f}{:^15.6f}{:^15.6f}{:^15.6f}'.format(i,float(x),float(x1),float(f(x)),float(fprima(x)),float(f(x1))))

    i = i + 1

    x = x1
    error = ( raiz[i] - raiz[i-1] ) / raiz[i]

    plt.plot(xD, f(xD), 'b-', x, f(x), 'g:o')

print (" ")
print ("La raíz es: ", x )

plt.plot(xD, f(xD), 'b-', x, f(x), 'r:o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title("NEWTON-RAPHSON CON RAIZ:("+str(x)+")")
plt.grid()

plt.show()

#Evita el cierre de la ventana
input()





















