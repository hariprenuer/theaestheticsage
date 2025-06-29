from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import houselordinfluence as hl
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
class avasthai(basic):
    plavasthai={4:["shani","rhau","kethu"],2:["sukiran"],5:planetonly,1:["chandhiran"]}
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=self.aux.data
        self.subathuvam=hl.lordinfluence(self.name,self.passer).houseinfl
        avasth={}
        shub={}
        for pl in planetonly:
            degpl=self.data[pl]["paagai"]*3600+self.data[pl]["kalai"]*60+self.data[pl]["vikalai"]-(self.data[pl]["kaalapurushan"]-1)*30*3600
            for ind in range(0,5):
                if ind*21600<degpl<(ind+1)*21600:
                    if self.data[pl]["kaalapurushan"]%2==0:
                        avasth[pl]=5-ind
                    else:
                        avasth[pl]=ind+1
        self.avas=avasth
        for ind in self.avas:
            for pl in planetonly:
                if self.avas[pl] in self.plavasthai:
                    if pl in self.plavasthai[self.avas[pl]]:
                        shub[pl]=self.subathuvam[pl]-(self.subathuvam[pl])*0.1
                    else:
                        shub[pl]=self.subathuvam[pl]
                else:
                    shub[pl]=self.subathuvam[pl]
        self.avasthai=shub.copy()