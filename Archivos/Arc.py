file = open ("EjemploArchivo.txt","w")
file.write("Este es el contenido del archivo\n")
file.close()

lista = ["Fresa","Mango","Papaya"]

with open("EjemploArchivo.txt","a") as file:
    for e in lista:
        file.write(e + "\n")

print("Lista escrita en el archivo")

lista2 = ["Honda","Suzuki","BMW"]
with open("EjemploArchivo.txt","a") as file:
    file.writelines(lista2)

print("Lista escrita en el archivo con writelines")

print("imprimir todo el contenido del archivo")
with open("EjemploArchivo.txt","r") as file:
    print(file.read())

print("Leer dos lineas y posteriomente 5 caracteres.")
with open("EjemploArchivo.txt","r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("Almacenar el contenido en una lista y mostrar el ultimo")
with open("EjemploArchivo.txt","r") as file:
    contenido = file.readlines()
    print(contenido[-1])
