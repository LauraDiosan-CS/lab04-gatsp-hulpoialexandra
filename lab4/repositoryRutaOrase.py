from rutaOrase import *
class RepositoryRutaOrase:
    def __init__(self,fileNamei):
        self._harta=[]
        self._fileNameIn=fileNamei
        self.loadFromFile()

    def loadFromFile(self):
        f=open(self._fileNameIn)
        n=int(f.readline())
        i=1
        while i<=n:
            infos=f.readline().split(",")
            o1=i
            j=1
            while j<=n:
                o2=j
                d=int(infos[j-1])
                ruta=RutaOrase(o1,o2,d)
                self._harta.append(ruta)
                j += 1
            i=i+1
        f.close()

    def search(self,oras1):
        list=[]
        for r in self._harta:
            if(r.getOras1()==oras1):
                list.append(r)
        return list

    def getHarta(self):
        return self._harta

    def getFileNameIn(self):
        return self._fileNameIn

    def getSource(self):
        return self._source

    def getDest(self):
        return self._dest