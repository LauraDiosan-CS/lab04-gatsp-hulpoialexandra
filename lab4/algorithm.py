import random
from math import sqrt
from chromozome import Chromozome
from evaluation import Evaluation

class Algoritm:
    def __init__(self,repository):
        self.__repository=repository
        self.__nrOfNodes=int(sqrt(len(repository.getHarta())))
        self.__pop=[]
        self.__fit=[]
        self.__evalFunc=Evaluation(repository.getHarta(),self.__nrOfNodes)
        self.__minFit=0
        self.__nrConsMinFit=0
        self.__lastFit=0
        self.__fitEvol=[]

    def __initialize(self):
        self.__pop.append(Chromozome(self.__nrOfNodes))
        self.__pop.append(Chromozome(self.__nrOfNodes))
        self.__pop.append(Chromozome(self.__nrOfNodes))
        self.__pop.append(Chromozome(self.__nrOfNodes))

    def __evaluate(self):
        for chromozome in self.__pop:
            self.__fit.append(self.__evalFunc.evaluate(chromozome.getRepres()))
            chromozome.setFitness(self.__evalFunc.evaluate(chromozome.getRepres()))
        self.__minFit=min(self.__fit)
        self.__nrConsMinFit=1
        self.__lastFit=self.__fit[3]

    def __selection(self):
        fitSum=sum(self.__fit)
        proportions=[]
        roulette=[]
        aux=0
        for fit in self.__fit:
            proportions.append(fit/fitSum)
            roulette.append(aux+(fit/fitSum))
            aux=aux+(fit/fitSum)
        p1=random.random()
        for i in range(4):
            if(p1<roulette[i]):
                parent1=self.__pop[i]
                break
        parent2=parent1
        while(parent2==parent1):
            p2 = random.random()
            for i in range(4):
                if (p2 < roulette[i]):
                    parent2 = self.__pop[i]
                    break
        return parent1,parent2

    def __crossover(self,parent1,parent2):
        return parent1.crossover(parent2), parent2.crossover(parent1)

    def _mutation(self,o1,o2):
        return o1.mutation(),o2.mutation()

    def __best(self,o1,o2):
        if(o1.getFitness()<o2.getFitness()):
            return o1
        return o2

    def __worst(self):
        maxFit=max(self.__fit)
        for chromo in self.__pop:
            if(chromo.getFitness()==maxFit):
                return chromo

    def __getFinalResult(self):
        for i in range(len(self.__fit)):
            if(self.__fit[i]==self.__minFit):
                return (self.__pop[i])

    def __writeToFile(self,result):
        reprResult=result.getRepres()
        f=(self.__repository.getFileNameIn().split(".txt"))[0]
        f=open(f+"_solution.txt","w")
        f.write(str(len(reprResult)))
        f.write('\n')
        f.write(str(reprResult[0]))
        for i in range(1,len(reprResult)):
            f.write(","+str(reprResult[i]))
        f.write('\n')
        f.write(str(self.__fitEvol[0]))
        for i in range(1,len(self.__fitEvol)):
            f.write(","+str(self.__fitEvol[i]))
        f.write('\n')
        f.write(str(result.getFitness()))

    def execute(self):
        #initialize
        self.__initialize()
        self.__evaluate()
        self.__fitEvol.append(self.__minFit)

        while(self.__nrConsMinFit<300):
            for i in range(4):
                #selection
                selection=self.__selection()
                parent1=selection[0]
                parent2=selection[1]

                #crossover
                crossover=self.__crossover(parent1,parent2)
                o1=crossover[0]
                o2=crossover[1]

                #mutation
                mutation=self._mutation(o1,o2)
                o1=mutation[0]
                o2=mutation[1]

                #evaluation
                fit1=self.__evalFunc.evaluate(o1.getRepres())
                o1.setFitness(fit1)
                fit2=self.__evalFunc.evaluate(o2.getRepres())
                o2.setFitness(fit2)

                #modify generation
                b=self.__best(o1,o2)
                w=self.__worst()
                self.__pop.remove(w)
                self.__fit.remove(w.getFitness())
                self.__pop.append(b)
                self.__fit.append(b.getFitness())
                self.__minFit=min(self.__fit)
                if(self.__fitEvol[len(self.__fitEvol)-1]==self.__minFit):
                    self.__nrConsMinFit+=1
                else:
                    self.__nrConsMinFit=1
                self.__fitEvol.append(self.__minFit)
                # self.__lastFit=b.getFitness()
        self.__writeToFile(self.__getFinalResult())