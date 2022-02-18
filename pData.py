class parseData:
    def getMonth(self,info):
        return info.split("=")[0].split(":")[0]
    
    def getYear(self,info):
        return info.split("=")[0].split(":")[0]
        
    def getBody(self,info):
        info = info.split("=")[1]
        caracteres = "()[]\""
        for caracter in caracteres:
            info = info.replace(caracter,"")
        info = info.split(";")

        body = []

        for i in info:
            prod = {}
            i = i.split(",")
            prod.update({'nombre':i[0],'precio':i[1],'cantidad':i[2]})
            body.append(prod)
        return body

    def datadec(self,archivo):
        file = open(archivo)
        info = file.read()
        file.close()
        caracteres = "\n\t"
        for caracter in caracteres:
            info = info.replace(caracter,"")
        info = info.replace(" ","")
        return info