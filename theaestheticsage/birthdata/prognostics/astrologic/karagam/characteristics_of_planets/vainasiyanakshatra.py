from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import pushkaramsam
nakshatras=["ashwini","bharani","kiruthigai","rohini","mirugasirisham","thiruvadhirai","punarpoosam",
            "poosam","ayilyam","magam","pooram","uthiram","hastham","chithirai","swathi","visagam",
            "anusham","kettai","moolam","pooradam","uthiradam","thiruvonam","avittam","sadhayam",
            "pooratadhi","uthiratadhi","revathi"]
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
class vainasiyanakshtra(basic):
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.chaaram=self.aux.chaaram
        suba={}
        self.subathuvam=pushkaramsam.pushkaramsam(self.name,self.passer).pushakaramsam
        moonpos=[self.chaaram["chandhiran"]["charanakshathra"],self.chaaram["chandhiran"]["paadham"]]
        index=nakshatras.index(moonpos[0])+22
        if index>27:
            index=index-27
        self.vainasiya=nakshatras[index-1]
        for pl in planetonly:
            if self.chaaram[pl]["charanakshathra"]==self.vainasiya:
                if self.chaaram[pl]["paadham"]==moonpos[1]:
                    suba[pl]=self.subathuvam[pl]-(self.subathuvam[pl])*0.4
                else:
                    suba[pl]=self.subathuvam[pl]-(self.subathuvam[pl])*0.2
            else:
                suba[pl]=self.subathuvam[pl]
        self.vainasiyanakshatra=suba.copy()