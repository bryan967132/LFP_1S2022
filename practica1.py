from parseData import parse

pr = parse()
info = pr.parseData("informacion.data")
año = pr.getYear(info)
mes = pr.getMonth(info)
cuerpo = pr.getBody(info)

print("Reporte de Ventas")
print(f"Año: {año}")
print(f"Mes: {mes}")

for i in cuerpo:
    i = i.__dict__
    print(f"Producto: {i['nombre']}")
    print(f"\tPrecio: $ {i['precio']}")
    print(f"\tCantidad Vendida: {i['cantidad']}")
    print(f"\tTotal: $ {float(i['precio'])*int(i['cantidad'])}")