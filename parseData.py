from producto import producto
class parse:
    def getMonth(self,info):
        return info.split(":")[0]
    
    def getYear(self,info):
        return info.split(":")[1][:4]
        
    def getBody(self,info):
        info = info.split(":")[1][4:]
        info = info.replace("(","").replace(")","")
        info = info.replace("[","").replace("]","")
        info = info.replace("\"","")[:-1].split(";")

        body = []

        for i in info:
            i = i.split(",")
            body.append(producto(i[0],i[1],i[2]))
        return body

    def parseData(self,archivo):
        file = open(archivo)
        info = file.read()
        file.close()
        info = info.replace(" ","").replace("\n","")
        return info