from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import aspectationsinfluence as ai
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
class chaaraminfluence(basic):
    influencingrate=0.50
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=ai.aspectationinfluence(self.name,self.passer).aspinfluence
        self.chaaram=self.aux.chaaram
        char={}
        for pl in planetonly:
            char[pl]=self.data[pl]+self.data[self.chaaram[pl]["charanadhan"]]*self.influencingrate
        self.chaaraminfluence=char.copy()
    @classmethod
    def changerate(cls,rate):
        cls.influencingrate=rate
#print(chaaraminfluence("hari prasath").chaaraminfluence)