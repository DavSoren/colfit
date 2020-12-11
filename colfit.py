cantidad = int(input("Cantidad de columnas: "))
print("""Los nombres de archivo tendran el siguiente formato nombre#.txt solo debe reemplazar nombre,
y tener en la misma carpeta archivos nombre1.txt, nombre2.txt, ... nombrecantidad.txt""")
nom = input("Nombre de archivo: ")

delimitador = input("delimitador: ")

res = {}
out = []

for i in range(cantidad):
    file = open("%s%d.txt" % (nom, i+1), "r")
    res[i+1] = []
    for l in file:
        res[i+1].append(l[:-1])
    file.close()

for x in range(len(res[1])):
    cad = ""
    for y in range(cantidad):
        cad += res[y+1][x]+delimitador
    out.append(cad[:-len(delimitador)])

file = open("res.csv", "w")
for o in out:
    file.write(o)
    file.write("\n")
file.close()

input()
