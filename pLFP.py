import easygui as eg
class parseLFP:
    def getBody(self,info):
        caracteres = "Â<>¿?\""
        for caracter in caracteres:
            info = info.replace(caracter,"")
        info = info.split(",")
        instrucciones = {}
        for i in info:
            i = i.split(":")
            instrucciones.update({i[0].upper():i[1]})
        return instrucciones

    def datadec(self):
        archivo = eg.fileopenbox()
        file = open(archivo)
        info = file.read()
        file.close()
        caracteres = "\n\t"
        for caracter in caracteres:
            info = info.replace(caracter,"")
        info = info.replace(" ","")
        return info