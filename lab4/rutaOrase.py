class RutaOrase:
    def __init__(self,o1,o2,d):
        self._oras1=o1
        self._oras2=o2
        self._distanta=d

    def getOras1(self):
        return self._oras1
    def setOras1(self,o1):
        self._oras1=o1

    def getOras2(self):
        return self._oras2
    def setOras2(self,o2):
        self._oras2=o2

    def getDistanta(self):
        return self._distanta
    def setDistanta(self,d):
        self._distanta=d

    def __str__(self):
        return str(self._oras1)+"->"+str(self._oras2)+":"+str(self._distanta)