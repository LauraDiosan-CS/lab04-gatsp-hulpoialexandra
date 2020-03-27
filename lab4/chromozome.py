from random import*
class Chromozome:
    def __init__(self,nrOfNodes):
        self.__nrOfNodes=nrOfNodes
        self.__fitness=0
        nodes=self.__initialize()
        self.__repres=[1]
        for i in range(nrOfNodes-1):
            gene = choice(nodes)
            nodes.remove(gene)
            self.__repres.append(gene)

    def __initialize(self):
        result=[]
        for i in range(2,self.__nrOfNodes+1):
            result.append(i)
        return result

    def getFitness(self):
        return self.__fitness

    def setFitness(self,fit):
        self.__fitness=fit

    def getRepres(self):
        return self.__repres

    def setRepres(self,rep):
        self.__repres=rep

    def __createRepr_Cross(self,substr,cuttingPoint1,cuttingPoint2):
        result=[]
        for i in range(self.__nrOfNodes):
            result.append(0)
        c=0
        for i in range(self.__nrOfNodes):
            if(i>=cuttingPoint1 and i<cuttingPoint2):
                result[i]=substr[c]
                c+=1
        return result


    def crossover(self,chromozome):
        cuttingPoin1=randint(0,self.__nrOfNodes)
        cuttingPoin2=randint(0,self.__nrOfNodes)
        while(cuttingPoin2==cuttingPoin1):
            cuttingPoin2 = randint(0, self.__nrOfNodes)
        if(cuttingPoin2<cuttingPoin1):
            aux=cuttingPoin1
            cuttingPoin1=cuttingPoin2
            cuttingPoin2=aux
        substr=self.__repres[cuttingPoin1:cuttingPoin2]
        newChromozomeRepr=self.__createRepr_Cross(substr,cuttingPoin1,cuttingPoin2)
        ich=cuttingPoin2
        inewch=cuttingPoin2
        while(inewch<self.__nrOfNodes):
            if(chromozome.getRepres()[ich] not in newChromozomeRepr):
                newChromozomeRepr[inewch]=chromozome.getRepres()[ich]
                inewch+=1
            ich+=1
            if(ich==self.__nrOfNodes):
                ich=0
        inewch=0
        if(ich==self.__nrOfNodes):
            ich=0
        while(inewch<cuttingPoin1):
            if(chromozome.getRepres()[ich] not in newChromozomeRepr):
                newChromozomeRepr[inewch]=chromozome.getRepres()[ich]
                inewch+=1
            ich+=1
        newChromozome=Chromozome(self.__nrOfNodes)
        newChromozome.setRepres(newChromozomeRepr)
        return newChromozome

    def mutation(self):
        gene1=randint(0,self.__nrOfNodes-1)
        gene2=randint(0,self.__nrOfNodes-1)
        aux=self.__repres[gene1]
        self.__repres[gene1]=self.__repres[gene2]
        self.__repres[gene2]=aux
        return self
