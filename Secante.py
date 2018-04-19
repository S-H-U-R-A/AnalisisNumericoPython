import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return ( 230*(pow(x,4)) + 18*(pow(x,3)) + 9*(pow(x,2)) - (221*x) - 9 )

print (" ")
print ("MÉTODO DE LA SECANTE")
print (" ")

#Valor digitado por el usuario
x0 = float(input('Introduce el valor de inicio x0: '))

#Valor digitado por el usuario
x1 = float(input('Introduce el valor de inicio x1: '))

#Error digitado por el usuario
tolerancia =float(input('Introduce el valor para la tolerancia: '))

raiz = []

raiz.insert(0,0)

i = 0

#Error por defecto para que el programa inicie
error = 1

print (" ")

#Se dibuja en la grafica la funcion y donde esta su raiz
x = np.linspace(3, -3, ( tolerancia*10000000000000000 ) )

print ('{:^14}{:^14}{:^14}{:^14}{:^14}{:^14}{:^14}'.format('Iteraciones','x0','x1','x0','f(x0)','f(x1)','f(x2)'))

print (" ")

while abs(error) > tolerancia:

    x2 = x1 - ( f(x1)*(x0-x1))/(f(x0)-f(x1))
    
    raiz.append(x2)

    plt.plot(x, f(x), 'b-', x2, f(x2), 'g:o')

    print ('{:^10}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}{:^10.5f}'.format(i,float(x0),float(x1),float(x2),float(f(x0)),float(f(x1)),float(f(x2))))

    x0 = x1
    x1 = x2

    i  = i + 1

    error = ( raiz[i]-raiz[i-1] ) / raiz[i]
    
print (" ")
print ("La raíz es: ",x2)

plt.plot(x, f(x), 'b-', x2, f(x2), 'r:o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("SECANTE CON RAIZ:("+str(x2)+")")
plt.grid()
plt.show()

#Evita el cierre de la ventana
input()






















