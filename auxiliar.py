import matplotlib.pyplot as plotpy
from matplotlib import cm
from matplotlib import colors
from pData import parseData
from pLFP import parseLFP

data = parseData()
lfp = parseLFP()

info = data.datadec('informacion.data').upper()
año = data.getYear(info)
mes = data.getMonth(info)
productos = data.getBody(info)

inst = lfp.datadec('instrucciones.lfp').upper()
instrucciones = lfp.getBody(inst)

arrProd = []
for i in productos:
    arrProd.append(i)

for i in range(len(arrProd)-1):
    for j in range(len(arrProd)-i-1):
        if int(arrProd[j]['cantidad'])*float(arrProd[j]['precio']) < int(arrProd[j+1]['cantidad'])*float(arrProd[j+1]['precio']):
            arrProd[j],arrProd[j+1] = arrProd[j+1],arrProd[j]

reporte = "201908355 - Danny Hugo Bryan Tejaxun Pichiya<br>\n"


for i in arrProd:
    reporte += str(i['nombre'])+" "+str(i['precio'])+" "+str(i['cantidad'])+" "+str(float(i['precio'])*int(i['cantidad']))+"<br>\n"

file = open("Reporte.html","w")

amount_written = file.write(reporte)

file.close()

"""if instrucciones['GRAFICA'] == "BARRAS":
    eje_x = []
    eje_y = []

    for i in productos:
        precio = float(i['precio'])
        cantidad = int(i['cantidad'])
        eje_x.append(i['nombre'])
        eje_y.append(precio*cantidad)

    fig, ax = plotpy.subplots()
    ax.bar(eje_x,eje_y)
    ax.set_title(instrucciones['TITULO'])
    ax.set_ylabel(instrucciones['TITULOY'])
    ax.set_xlabel(instrucciones['TITULOX'])
    plotpy.show()

elif instrucciones['GRAFICA'] == "PIE":
    nombre = []
    vend = []

    for i in productos:
        precio = float(i['precio'])
        cantidad = int(i['cantidad'])
        nombre.append(i['nombre'])
        vend.append(precio*cantidad)

    normdata = colors.Normalize(min(vend), max(vend))
    colormap = cm.get_cmap("Oranges")
    colores = colormap(normdata(vend))

    fig, ax = plotpy.subplots()
    ax.pie(vend,labels=nombre,autopct="%0.1f %%",colors=colores)
    ax.set_title(instrucciones['TITULO'])
    plotpy.show()

elif instrucciones['GRAFICA'] == "LÍNEAS" or instrucciones['GRAFICA'] == "LINEAS":
    nombre = []
    vend = []

    for i in productos:
        precio = float(i['precio'])
        cantidad = int(i['cantidad'])
        nombre.append(i['nombre'])
        vend.append(precio*cantidad)

    fig, ax = plotpy.subplots()
    ax.plot(nombre,vend)
    ax.set_title(instrucciones['TITULO'])
    ax.set_ylabel(instrucciones['TITULOY'])
    ax.set_xlabel(instrucciones['TITULOX'])
    plotpy.show()"""