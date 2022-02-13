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

ventas = []
for i in productos:
    ventas.append(i)

for i in range(len(ventas)-1):
    for j in range(len(ventas)-i-1):
        if int(ventas[j]['cantidad']) < int(ventas[j+1]['cantidad']):
            ventas[j],ventas[j+1] = ventas[j+1],ventas[j]

reporte = """<!DOCTYPE html>
<html lang="en">
<head>
	<title>Reporte</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100">
					<table style="margin-bottom: 50px;">
						<thead>
							<tr class="table100-head">
								<th class="column1">
									201908355 - DANNY HUGO BRYAN TEJAXUN PICHIYA
								</th>
							</tr>
						</thead>
					</table>
					<table style="margin-bottom: 50px;">
						<thead>
							<tr class="table100-head">
								<th class="column1">PRODUCTO</th>
								<th class="column2">PRECIO</th>
								<th class="column3">UNIDADES VENDIDAS</th>
								<th class="column6">TOTAL</th>
							</tr>
						</thead>
						<tbody>"""

for i in arrProd:
    reporte += """<tr>
									<td class="column1">"""+str(i['nombre'])+"""</td>
									<td class="column2">"""+str(i['precio'])+"""</td>
									<td class="column3">"""+str(i['cantidad'])+"""</td>
									<td class="column6">"""+str(float(i['precio'])*int(i['cantidad']))+"""</td>
								</tr>"""

reporte += """</tbody>
					</table>
                    <table style="margin-bottom: 50px;">
						<thead>
							<tr class="table100-head">
								<th class="column1">PRODUCTO</th>
								<th class="column2">PRECIO</th>
								<th class="column6">UNIDADES VENDIDAS</th>
							</tr>
						</thead>
						<tbody>
                        <tr>
									<td class="column1">"""+str(ventas[0]['nombre'])+"""</td>
									<td class="column2">"""+str(ventas[0]['precio'])+"""</td>
									<td class="column6">"""+str(ventas[0]['cantidad'])+"""</td>
								</tr>
                        </tbody>
					</table>
                    </tbody>
					</table>
                    <table style="margin-bottom: 50px;">
						<thead>
							<tr class="table100-head">
								<th class="column1">PRODUCTO</th>
								<th class="column2">PRECIO</th>
								<th class="column6">UNIDADES VENDIDAS</th>
							</tr>
						</thead>
						<tbody>
                        <tr>
									<td class="column1">"""+str(ventas[len(ventas)-1]['nombre'])+"""</td>
									<td class="column2">"""+str(ventas[len(ventas)-1]['precio'])+"""</td>
									<td class="column6">"""+str(ventas[len(ventas)-1]['cantidad'])+"""</td>
								</tr>
                        </tbody>
					</table>
                </div>
			</div>
		</div>
	</div>


	

<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>"""

file = open("Reporte/Reporte.html","w")

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