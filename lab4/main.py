from repositoryRutaOrase import *
from algorithm import *


fis=input("Dati numele fisierului de intrare(fara extensie): ")
input_files=fis.split(".txt")
input_file=input_files[0]
rep=RepositoryRutaOrase(input_file+".txt")

algorithm=Algoritm(rep)
algorithm.execute()