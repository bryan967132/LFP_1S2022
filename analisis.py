import matplotlib.pyplot as plotpy
from matplotlib import cm
from matplotlib import colors
from pData import parseData
from pLFP import parseLFP
from PIL import Image
class graph:
    def graphs(self,info,inst):
        data = parseData()
        lfp = parseLFP()
        año = data.getYear(info)
        mes = data.getMonth(info)
        productos = data.getBody(info)
        instrucciones = lfp.getBody(inst)
        titulo = ""
        try:
            titulo = instrucciones['TITULO']
        except:
            titulo = "Reporte de Ventas " + mes + " - " + año

        if instrucciones['GRAFICA'].upper() == "BARRAS":
            nombre = []
            vend = []

            for i in productos:
                precio = float(i['precio'])
                cantidad = int(i['cantidad'])
                nombre.append(i['nombre'])
                vend.append(precio*cantidad)

            fig, ax = plotpy.subplots()
            fig.canvas.manager.set_window_title(instrucciones['NOMBRE']) 
            ax.bar(nombre,vend)
            ax.set_title(titulo)

            try:
                ax.set_ylabel(instrucciones['TITULOY'])
            except:
                pass
            try:
                ax.set_xlabel(instrucciones['TITULOX'])
            except:
                pass
            plotpy.savefig(instrucciones['NOMBRE'])

        elif instrucciones['GRAFICA'].upper() == "PIE":
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
            fig.canvas.manager.set_window_title(instrucciones['NOMBRE']) 
            ax.pie(vend,labels=nombre,autopct="%0.1f %%",colors=colores)
            ax.set_title(titulo)
            plotpy.savefig(instrucciones['NOMBRE'])

        elif instrucciones['GRAFICA'].upper() == "LÍNEAS" or instrucciones['GRAFICA'].upper() == "LINEAS":
            nombre = []
            vend = []

            for i in productos:
                precio = float(i['precio'])
                cantidad = int(i['cantidad'])
                nombre.append(i['nombre'])
                vend.append(precio*cantidad)
                
            fig, ax = plotpy.subplots()
            fig.canvas.manager.set_window_title(instrucciones['NOMBRE']) 
            ax.plot(nombre,vend)
            ax.set_title(titulo)
            try:
                ax.set_ylabel(instrucciones['TITULOY'])
            except:
                pass
            try:
                ax.set_xlabel(instrucciones['TITULOX'])
            except:
                pass
            plotpy.savefig(instrucciones['NOMBRE'])
        img = Image.open(instrucciones['NOMBRE']+'.png')
        img.show()