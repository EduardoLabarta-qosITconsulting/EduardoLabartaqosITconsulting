



""""EJERCICIOS OPCIONALES PROPUESTOS POR UN COMPAÑERO EN EL TABLON DE CLASSROOM"""





""" Ejercicio 1: Calculadora Mejorada
Crea un programa que pida al usuario dos números y una operación (+, -, *, /).
Luego, usa una estructura if-elif-else para realizar la operación correspondiente.
Si el usuario introduce una operación no válida, muestra un mensaje de error. """




"""
num1 = float(input("Introduce un numero: "))
num2 = float(input("Introduce otro numero: "))
operacionInvalida= True


while operacionInvalida:
    operacion = str(input("Introduce una operacion: "))
    operacionInvalida = False 
    if(operacion=="+"):
        print(f"La suma de {num1} y {num2} es {num1+num2}")
        
    elif(operacion=="-"):
        print(f"La resta de {num1} y {num2} es {num1-num2}")
        
    elif(operacion=="*"):
        print(f"La multiplicacion de {num1} y {num2} es {num1*num2}")
       
    elif(operacion=="/"):
        print(f"La division de {num1} entre {num2} es {num1/num2}")
       
    else:
        print("Error: Operación no valida")
        operacionInvalida = True
 """
 
 
 
 
 
 
 
 
 
 
"""  Ejercicio 2: Contador de Vocales
Pide al usuario una palabra y cuenta cuántas vocales (a, e, i, o, u) tiene. Usa un
bucle for y una lista para almacenar las vocales. """



""" vocales = ["a","e","i","o","u"]
cantidadVocales = []
contador = 0

palabra = input("Introduce una palabra: ").lower()

for letra in palabra:
    if letra in vocales:
        contador +=1
        
print(f"La palabra contiene {contador} vocales") """











""" Ejercicio 3: Manipulación de Listas
Crea una lista con al menos 10 números. Luego:
● Muestra la lista original.
● Muestra solo los números pares.
● Muestra la suma de todos los números de la lista.
● Reemplaza todos los números impares por 0 y muestra la lista modificada. """




""" numeros = [2,4,1,9,6,14,25,74,21,17]
print("\n")
print(numeros)
print("\n")
print("NUMEROS PARES: ")
for x in numeros:
    if(x%2==0):
        print(x)
        
sumaTotal = sum(numeros)
print(f"La suma total es {sumaTotal}")

for y,num in enumerate(numeros):
    if(num%2 != 0):
        numeros[y] = 0
        
print(numeros) """
        
        
        
      
      
       
      
      
      
      
      
        
        
""" Ejercicio 4: Simulación de Login
Crea un programa que simule un inicio de sesión. Define un usuario y una contraseña
predefinidos. Luego, pide al usuario que ingrese su usuario y contraseña. Si son
correctos, muestra "Acceso concedido", de lo contrario, "Acceso denegado". Dale al
usuario 3 intentos antes de bloquear el acceso.    """    




""" usuarioDef = "usuario123"
contraseñaDef = "contraseña123"
credencialesIncorrectas = True
intentos = 3

while credencialesIncorrectas:
    if(intentos>0):
        usuarioUsuario = str(input("Introduce el usuario: "))
        contraseñaUsuario = str(input("Introduce la contraseña: "))
        
        if(usuarioUsuario == usuarioDef and contraseñaUsuario == contraseñaDef):
            print("Acceso concedido")
            credencialesIncorrectas = False
        else:
            intentos -= 1
            print("Acceso denegado")
            print(f"Te quedan {intentos} intentos")
        
    else:
        break """
        
     
     
     
     
     
     
     
     
     
     
     
        
        
        
        
""" Ejercicio 5: Números Primos
Crea una función que reciba un número y determine si es primo o no. Luego, pide un
número al usuario y usa la función para decirle si es primo. """
""" 



def esPrimo(num):
    contador = 2
    esPrimo = True
    while contador != num:
        if(num%contador == 0):
            esPrimo=False
            break
        contador += 1
    return esPrimo

num = int(input("Introduce un numero para saber si es primo: "))    

print(esPrimo(num))
     """
     
     
     
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
""" Ejercicio 6: Ordenando una Lista
Pide al usuario 5 números, guárdalos en una lista y luego muestra:
● La lista ordenada de menor a mayor.
● La lista ordenada de mayor a menor.
● El número más grande y el más pequeño de la lista. """



""" numeros=[]
numerosDesc= []

for x in range(5):
    num = int(input("Introduce un numero: "))
    numeros.append(num)
    
numeros.sort()
print(numeros)

for x in range(5,0,-1):
    numerosDesc.append(x)
    
print(numerosDesc)

print(f"El numero mas grande la lista es {numeros[4]} y el mas pequeño es {numeros[0]}") """
















""" Ejercicio 7: Adivina el Número
Crea un programa que genere un número aleatorio entre 1 y 20 y pida al usuario que
lo adivine.
● Si el usuario adivina, muestra un mensaje de felicitaciones.
● Si el número es menor, dile "El número es mayor".
● Si el número es mayor, dile "El número es menor".
● El usuario tiene 5 intentos. """




""" import random

numAleatorio = random.randint (0,20)
intentos = 5
while intentos>0:
    numUsuario = int(input("Intenta adivinar el numero secreto: "))
    if (numUsuario==numAleatorio):
        print("Felicidades has conseguido acertar el numero secreto")
        break
    else:
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
        if(numAleatorio>numUsuario):
            print("El numero secreto es mas grande")
        else:
            print("El numero secreto es mas pequeño")
    print("\n")
    if(intentos== 0):
        print(f"El numero secreto era {numAleatorio}")
 
 
  """
 
 
 
 
 
 
 
 
 
 
 
 
"""  Ejercicio 8: Convertidor de Temperaturas
Crea una función que convierta grados Celsius a Fahrenheit y otra que convierta
grados Fahrenheit a Celsius. Luego, pide al usuario un valor y la conversión que
quiere realizar.
💡 Fórmulas:
● °F = (°C × 9/5) + 32
● °C = (°F − 32) × 5/9 """



""" opcionInvalida = True

while opcionInvalida:
    print("¿Que conversion de temperaturas quieres hacer?")
    print("1.Celsius a Fahrenheit")
    print("2.Fahrenheit a Celsius")
    opcionUsuario=int(input())
    print("Introduzca la temperatura")
    temperaturaUsuario = float(input())

    if(opcionUsuario==1):
        temperaturaFahr = (temperaturaUsuario * 9/5) + 32
        print(f"{temperaturaUsuario} en Celsius son {temperaturaFahr} Fahrenheit")
        opcionInvalida = False
    elif(opcionUsuario==2):
        temperaturaCels= (temperaturaUsuario - 32) * 5/9
        print(f"{temperaturaUsuario} Fahrenheit son {temperaturaCels} Celsius")
        opcionInvalida = False
    else:
        print("Error: Conversion elegida invalida, intentelo de nuevo") """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
""" Ejercicio 9: Conteo de Palabras en un Texto
Pide al usuario que introduzca un texto y luego:
● Cuenta cuántas palabras tiene.
● Cuenta cuántas veces aparece la palabra "Python".
● Muestra el texto en mayúsculas y en minúsculas.
💡 Pista: Usa .split() para contar palabras. """






""" palabras=[]

texto = str(input("Introduce un texto\n"))
print("\n")

palabras= texto.split(" ")

print(f"El texto tiene {len(palabras)} palabras")

contadorPython= 0
for x in palabras:
     if( x.lower()=="python"):
        contadorPython += 1 

print(f"La palabra Python se repite {contadorPython} veces")
print("Texto en minuscula\n")

for x in palabras:  
    print(f"{x.lower()} ", end="" )


print("\n")
print("Texto en mayuscula\n")

for x in palabras:  
    print(f"{x.upper()} ", end="" ) """
    
    
















""" Ejercicio 10: Pirámide de Números
Pide al usuario un número n y genera una pirámide numérica de n niveles como esta:
Si n = 5: """
    
    
    
    
    
""" n = int(input("Introduce un numero: "))
contador = 0

for x in range(0,n):
    contador += 1
    print("")
    
    for y in range(0,n-x):
        print(" ",end="")
    
    for z in range(0,contador):
        if(x==0):
             print("n", end="")
        else:
            print("n ", end="") """
    
    
        


    