#from math import *
import matplotlib.pyplot as plt
import numpy as np

def g(x):
  return ( 230*(pow(x,4)) + 18*(pow(x,3)) + 9*(pow(x,2)) - 9 )/221

print (" ")
print ("METODO DEL PUNTO FIJO")
print (" ")

p0  = float(input('Introduce el valor de x0: '))

tol = float((input('Introduce el valor para la tolerancia: ')))

n0  = float((input('Introduce el valor para la cantidad de iteraciones: ')))

#Se dibuja en la grafica la funcion y donde esta su raiz
x = np.linspace( 3, -3, (tol*10000000000000000) )

i=1

while i<=n0:

    p = g(p0)

    if abs(p-p0)<tol:

        print (" ")
        print("El punto fijo es ",p," despues de ",i," iteraciones")

        break

    i=i+1

    p0=p

    #Se imprime en cada vuelta la posible raiz
    plt.plot(x, g(x), 'g-', p, g(p), 'b:o')

#Se imprime por pantalla la raiz
print (" ")

plt.plot(x, g(x), 'g-', p, g(p), 'r:o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title("PUNTO FIJO CON RAIZ:("+str(p)+")")

plt.grid()
plt.show()

if i > n0:

    print("El metodo no converge")



#Evita el cierre de la ventana
input()