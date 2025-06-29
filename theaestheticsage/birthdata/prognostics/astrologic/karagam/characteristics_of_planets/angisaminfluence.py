from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic
from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import chaaraminfluence as ci

planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
class angisaminfluence(basic):
    angisamrate=0.50
    thunaiangisamrate=0.50
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.chaaram=ci.chaaraminfluence(self.name,self.passer).chaaraminfluence
        self.angisam=self.aux.angisanadhan
        char={}
        for pl in planetonly:
            char[pl]=self.chaaram[pl]+self.chaaram[self.angisam[pl]["angisanadhan"]]*self.angisamrate+self.chaaram[self.angisam[pl]["thunaiangisandhan"]]*self.thunaiangisamrate
        self.angisaminfluence=char.copy()
    @classmethod
    def changerate(cls,rate1,rate2):
        cls.angisamrate=rate1
        cls.thunaiangisamrate=rate2