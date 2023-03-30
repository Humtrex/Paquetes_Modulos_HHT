def nuevoTema(tema):
    print("\n========",tema, "========\n")

#Este es un comentario de una linea
nuevoTema("Operadores aritmeticos")
print("Operador división entera (10//3): ", 10//3)
print("Operador potencia (5 ** 3): ",5 ** 3 ) #Operador **
'''Este es un 
comentario de 
varias lineas'''

nuevoTema("Operadores lógicos")
print("Operador and (True and False): ", True and False)
#Actividad: Imprimir la tabla de verdad de los operadores logicos
print("==== Tabla operador and ======")
print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)
print(" ")
print("==== Tabla operador not =======")
print("not True: ", not True )
print("not False: ", not False)
print(" ")
print("===== Tabla operador or ======")
print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)

nuevoTema("Operadores de comparación")
print("Ej : 2 == 3" , 2 == 3)
#Actividad: Agregar los demas operadores de comparación
print("Operador ==  (2==3): ", 2==3 )
print("Operador != (2!=3)", 2!=3)
print("Operador < (4<9) : ", 4<9)
print("Operador <= (7<=4) : ", 7<=4)
print("Operrador >  (6>2)", 6>2)
print("Operador >= (3>=2)", 3>=2)

nuevoTema("Variables")
#Variables validas
variable1 = 10
variable2 = 6.2456
variable3 = "Juancho"
dosPalabras = "Hola"
dos_Palabras = "Hello"
print(variable1,variable2, variable3, dosPalabras, dos_Palabras)
a,b,c = 5,10.09,"Welcome"
print(a,b,c)

nuevoTema("Enteros")
w=105
x=764238743243
y=-234
z=0b00110011
h=0xffa
print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))

nuevoTema("Flotantes")
x=1297.50
print(x,type(x))
y=0.5637939
print(y,type(y))

nuevoTema("Numeros complejos")
x=-46j
y=12+45j
z=2j
print(x,type(x))
print(y,type(y))
print(z,type(z))

nuevoTema("Booleanos")
lis=[8]
print(lis,"is",bool(lis))
t=()
print(t, "is", bool(t))
new = "Hello"
print(new, "is ", bool(new))
num = 99
print(num,"is",bool(num))
comp = 1 + 0j
print(comp,"is",bool(comp))
val = None #None equivale a null
print(val,"is", bool(val))

nuevoTema("Listas")#No son arreglos
a=[10, 20.5, "Python List"]
print(a)
print(a[1])
a[0]= "Hola"
print(a)

nuevoTema("Tuplas")
t=(25,"tupla",1+10j,3.1416)
print(t)
print("t[2] = ",t[2])
print("t[1:4] = ",t[1:4])
#t[1]= 34 Operación no validas en las tuplas

nuevoTema("Sets o conjuntos")
s=set([5,4,6,8,8,1])
print("s = ",s)
print(type(s))
#s[0] = 3 da error
for ss in s:
    print(ss) #iteracion

nuevoTema("Diccionarios")
d = {1:"Valor1", "Valor2":2j}
print(d,type(d))
print("d[Valor2]:",d["Valor2"])
print("")
import random
clientes = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
dic_desc = {cliente:random.randint(1, 100) for cliente in clientes}
print(dic_desc)

nuevoTema("Cadenas")
q = "Esto es una cadena"
print(q)
print(type(q))
w = "Esto es una comilla doble \" de ejemplo"
print(w, type(w))
r = '''Esta es una cadena
de varias lineas    con tabulares  y
        saltos
de
linea'''
print(r,type(r))
print("Segmentacion de cadenas")
print(q[5:11])
print(q[:5])
print(q[7:])
print(q[-8:-1])
print(q[0:18:1])
print(q[0:18:2])
print(q[0:18:3])
cadena1 ="Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.upper()
print(cadena5)

nuevoTema("Objetos mutables e inmutables")
print("Inmutables")
print("Son numeros, cadenas, tuplas y conjuntos estaticos")
print("")
print("Mutables")
print("Son listas, diccionarios, conjuntos, bytearray")
print("")
