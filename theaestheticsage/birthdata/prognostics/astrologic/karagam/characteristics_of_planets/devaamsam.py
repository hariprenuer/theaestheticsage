from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import ashtakamsam
from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
class devaamsam(basic):
    vargas=["horai","drekaanam","navamsam","shastiamsam","dhuvadasamsam","dasamsam","trimsamsam","sapdhamsam"]
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.subathuvam=ashtakamsam.ashtakamsam(self.name,self.passer).ashtakamsam
        self.chakras=self.aux.varkkam
        repetition={}
        suba={}
        for pl in planetonly:
            count=0
            pos=self.chakras["raasi"][pl]
            for vrg in self.vargas:
                if self.chakras[vrg][pl]==pos:
                    count=count+1
            repetition[pl]=count
        self.repetition=repetition.copy()
        for pl in planetonly:
            suba[pl]=self.subathuvam[pl]+self.subathuvam[pl]*(self.repetition[pl]/len(self.vargas))
        self.devaamsam=suba.copy()