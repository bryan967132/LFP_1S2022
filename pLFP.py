class parseLFP:
    def getBody(self,info):
        info = info.replace("<","").replace(">","")
        info = info.replace("¿","").replace("?","")
        info = info.replace("\"","")
        info = info.split(",")
        instrucciones = {}
        for i in info:
            i = i.split(":")
            instrucciones[i[0]] = i[1]
        return instrucciones

    def datadec(self,archivo):
        file = open(archivo)
        info = file.read()
        file.close()
        info = info.replace(" ","").replace("Â","").replace("\n","").replace("\t","")
        return info