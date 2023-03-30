from Calc.Fundamentos import nuevoTema

import pickle

nuevoTema("Modulo Pickle y serialización binaria.")

info = [35,88,3.14,16]

with open("ArchivoSerial","wb") as binfile:
    pickle.dump(info, binfile)

print("Archivo binario escrito.")

with open("ArchivoSerial","rb") as binfile:
    lista = pickle.load(binfile)
    print(lista)

print("Archivo binario leido y reconstruido.")