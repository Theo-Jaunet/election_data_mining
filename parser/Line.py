class Line:

    def __init__(self, id, Commune, Candidats):
        self.id = id
        self.Commune = Commune
        self.Candidats = Candidats
        self.nbCand = 0

    def __str__(self):
        return "{id:"+str(self.id)+",Commune: "+str(self.Commune)+",Candidats:["+self.printCand()+"]}"


    def printCand(self):
        mes=""
        for cand in self.Candidats:
            mes += str(cand)+","
        return mes[:-1]