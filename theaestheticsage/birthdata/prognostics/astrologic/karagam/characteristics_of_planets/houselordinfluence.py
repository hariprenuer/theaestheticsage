from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import angisaminfluence
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
class lordinfluence(basic):
    houseinfl=0.5
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.positions=self.aux.data
        self.data=angisaminfluence.angisaminfluence(self.name,self.passer).angisaminfluence
        hl={}
        for pl in planetonly:
            hl[pl]=self.data[pl]+self.data[self.bh.ownership(bavaslist[self.positions[pl]["kaalapurushan"]-1])]*self.houseinfl
        self.houseinfl=hl.copy()