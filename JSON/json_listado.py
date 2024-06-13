import json

archivo = open("json_socios.json", "r")
mijson = json.load(archivo)
archivo.close()
print("\nLISTADO DE SOCIOS Y COMPRAS")
print("Socio\tNombre")
for socio in mijson["socios"]:
    num = socio["num socio"]
    nombre = socio["nombre"]
    print("%s\t%s" % (num, nombre))
    print("\t\tCódigo\tCantidad")
    for compra in socio["compras"]:
        print("\t\t%s\t%s" % (compra["codigo"], compra["cantidad"]))
