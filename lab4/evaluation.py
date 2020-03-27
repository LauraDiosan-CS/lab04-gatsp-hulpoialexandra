class Evaluation:
    def __init__(self,harta,nrOfNodes):
        self.__harta=harta
        self.__nrOfNodes=nrOfNodes

    def __existaRuta(self,a,b):
        for ruta in self.__harta:
            if ruta.getOras1()==a and ruta.getOras2()==b:
                return ruta.getDistanta()
        return 0

    def evaluate(self,chromozomeRep):
        fit=self.__existaRuta(chromozomeRep[self.__nrOfNodes-1],chromozomeRep[0])
        if fit ==0:
            return 0
        for i in range(self.__nrOfNodes-1):
            aux=self.__existaRuta(chromozomeRep[i],chromozomeRep[i+1])
            if(aux==0):
                return 0
            fit+=aux
        return fit