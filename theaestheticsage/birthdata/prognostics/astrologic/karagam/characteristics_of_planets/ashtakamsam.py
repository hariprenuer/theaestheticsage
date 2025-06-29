from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import vainasiyanakshatra
from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
class ashtakamsam(basic):
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=self.aux.varkkam
        self.subathuvam=vainasiyanakshatra.vainasiyanakshtra(self.name,self.passer).vainasiyanakshatra
        suba={}
        bava8=bavaslist.index(self.data["raasi"]["lagnam"])+7
        if bava8>12:
            bava8-=12
        for pl in planetonly:
            index=bavaslist.index(self.data["raasi"][pl])+8
            if index>12:
                index-=12
            if bavaslist[index-1]==self.data["navamsam"][pl] or bavaslist[bava8-1]==self.data["navamsam"][pl]:
                suba[pl]=self.subathuvam[pl]-(self.subathuvam[pl])*0.2
            else:
                suba[pl]=self.subathuvam[pl]
        self.ashtakamsam=suba.copy()