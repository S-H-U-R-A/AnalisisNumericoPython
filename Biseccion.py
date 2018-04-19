import matplotlib.pyplot as plt
import numpy as np

#Función que se va a analizar
def f(x):
    return ( 230*(pow(x,4)) + 18*(pow(x,3)) + 9*(pow(x,2)) - (221*x) - 9 )

#Programa principal
print (" ")
print ("METODO DE BISECCION")
print (" ")

x0 = float(input('Introduce el valor de x0: '))

x1 = float(input('Introduce el valor de x1: '))

error=float((input('Introduce el valor para la tolerancia: ')))

x2 = (x0+x1)/2.0

i=0

print (" ")

#Se dibuja en la grafica la funcion y donde esta su raiz
x = np.linspace(3, -3, (error*10000000000000000) )

print ('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Iteraciones','X0','X1','X2','F(X0)','F(X1)','F(X2)'))

print (" ")

while abs( f(x2) ) > error:

    i = i + 1

    x2 = (x0+x1)/2.0

    print ('{:^14}{:^10.14f}{:^10.14f}{:^10.14f}{:^10.14f}{:^10.14f}{:^10.14f}'.format(i,float(x0),float(x1),float(x2),float(f(x0)),float(f(x1)),float(f(x2))))

    if f(x0)*f(x2) < 0:

        x1=x2

    else :

        x0=x2

    #Se imprime en cada vuelta la posible raiz
    plt.plot(x, f(x), 'g-', x2, f(x2), 'b:o')

#Se imprime por pantalla la raiz
print (" ")
print ("La raíz es: ",x2)

plt.plot(x, f(x), 'g-', x2, f(x2), 'r:o')

plt.xlabel('X')
plt.ylabel('Y')

plt.title("BISECCIÓN CON RAIZ:("+str(x2)+")")

plt.grid()
plt.show()

#Evita el cierre de la ventana
input()
