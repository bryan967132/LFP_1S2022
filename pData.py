class parseData:
    def getMonth(self,info):
        return info.split(":")[0]
    
    def getYear(self,info):
        return info.split(":")[1][:4]
        
    def getBody(self,info):
        info = info.split(":")[1][4:]
        info = info.replace("(","").replace(")","")
        info = info.replace("[","").replace("]","")
        info = info.replace("\"","").split(";")

        body = []

        for i in info:
            prod = {}
            i = i.split(",")
            prod['nombre'] = i[0]
            prod['precio'] = i[1]
            prod['cantidad'] = i[2]
            body.append(prod)
        return body

    def datadec(self,archivo):
        file = open(archivo)
        info = file.read()
        file.close()
        info = info.replace(" ","").replace("\n","").replace("\t","")
        return info