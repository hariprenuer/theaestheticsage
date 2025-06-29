from birthdata.prognostics.astrologic.karagam import auxillarydata as ax

suriyan={"suriyan":[1,2,4,7,8,9,10,11],"chandhiran":[3,6,10,11],"sevvaai":[1,2,4,7,8,9,10,11],
         "budhan":[3,5,6,9,10,11,12],"guru":[5,6,9,11],"sukiran":[6,7,12],"shani":[1,2,4,7,8,9,10,11],
         "lagnam":[3,4,6,10,11,12]}
chandhiran={"suriyan":[3,6,7,8,10,11],"chandhiran":[1,3,6,7,10,11],"sevvaai":[2,3,5,6,9,10,11],
         "budhan":[1,3,4,5,7,8,10,11],"guru":[1,4,7,8,10,11,12],"sukiran":[3,4,5,7,9,10,11],
         "shani":[3,5,6,11],"lagnam":[3,6,10,11]}
sevvaai={"suriyan":[3,5,6,10,11],"chandhiran":[3,6,11],"sevvaai":[1,2,4,7,8,10,11],
         "budhan":[3,5,6,11],"guru":[6,10,11,12],"sukiran":[6,8,11,12],
         "shani":[1,4,7,8,9,10,11],"lagnam":[1,3,6,10,11]}
budhan={"suriyan":[5,6,9,11,12],"chandhiran":[2,4,6,8,10,11],"sevvaai":[1,2,4,7,8,9,10,11],
         "budhan":[1,3,5,6,9,10,11,12],"guru":[6,8,11,12],"sukiran":[1,2,3,4,5,8,9,11],
         "shani":[1,2,4,7,8,9,10,11],"lagnam":[1,2,4,6,8,10,11]}
guru={"suriyan":[1,2,3,4,7,8,9,10,11],"chandhiran":[2,5,7,9,11],"sevvaai":[1,2,4,7,8,10,11],
         "budhan":[1,2,4,5,6,9,10,11],"guru":[1,2,3,4,7,8,10,11],"sukiran":[2,5,6,9,10,11],
         "shani":[3,5,6,12],"lagnam":[1,2,4,5,6,7,9,10,11]}
sukiran={"suriyan":[8,11,12],"chandhiran":[1,2,3,4,5,8,9,11,12],"sevvaai":[3,5,6,9,11,12],
         "budhan":[3,5,6,9,11],"guru":[5,8,9,10,11],"sukiran":[1,2,3,4,5,8,9,10,11],
         "shani":[3,4,5,8,9,10,11],"lagnam":[1,2,3,4,5,8,9,11]}
shani={"suriyan":[1,2,4,7,8,10,11],"chandhiran":[3,6,11],"sevvaai":[3,5,6,10,11,12],
         "budhan":[6,8,9,10,11,12],"guru":[5,6,11,12],"sukiran":[6,11,12],
         "shani":[3,5,6,11],"lagnam":[1,3,4,6,10,11]}
pinnatavarkalst=[suriyan,chandhiran,sevvaai,budhan,guru,sukiran,shani]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","lagnam"]
class pinnatavarkam:
    #objects are pinnaatavarkam
    def __init__(self,birthdata,pinnatavarkam):
        parals={}
        self.data=ax.auxillarydata(birthdata).data
        for classbavas in bavaslist:
            parals[classbavas]=0
        for element in pinnatavarkam:
            influenced=[]
            for ele in range(len(pinnatavarkam[element])):
                take=self.data[element]["kaalapurushan"]-1+pinnatavarkam[element][ele]
                if take>12:
                    take=take-12*int(take/12)
                influenced.append(bavaslist[take-1])
            for bava in influenced:
                parals[bava]=parals[bava]+1
        self.parals=parals.copy()
def ashtavarkamgiver(name):
    objects=[]
    for i in pinnatavarkalst:
        objects.append(pinnatavarkam(name,i).parals)
    samudhayaparal={}
    for bv in bavaslist:
        samudhayaparal[bv]=0
    for i in range(len(objects)):
        for bv in bavaslist:
            samudhayaparal[bv]=samudhayaparal[bv]+objects[i][bv]
    return samudhayaparal.copy()
class ashtavarkam:
    def __init__(self,name=None):
        if name!=None:
            self.name=name       
            self.ashtavarakam=ashtavarkamgiver(name)
    def pinnatavarkam(self,pinnatavarkas):
        if type(pinnatavarkas)==type("  "):
            if pinnatavarkas in planets:
                return pinnatavarkam(self.name,pinnatavarkalst[planets.index(pinnatavarkas)]).parals            
        else:
            return pinnatavarkam(self.name,pinnatavarkas).parals
    @staticmethod
    def pinnatavarkaparal(pinnatavarkas):
        if type(pinnatavarkas)==type("  "):
            if pinnatavarkas in planets:
                pinnatavarkas=pinnatavarkalst[planets.index(pinnatavarkas)]
        if pinnatavarkas in pinnatavarkalst:
            return pinnatavarkas    