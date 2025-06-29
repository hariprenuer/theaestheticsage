from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import avasthai
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
onlypl=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
class karagamsam(basic):
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=self.aux.data
        self.passer=passer
        self.subathuvam=avasthai.avasthai(self.name,self.passer).avasthai
        appender=[self.data[pl]["paagai"]*3600+self.data[pl]["kalai"]*60+self.data[pl]["vikalai"]-(self.data[pl]["kaalapurushan"]-1)*30*3600 for pl in onlypl]
        appender.sort(reverse=True)
        order={}
        subam={}
        for pl in onlypl:
            degpl=self.data[pl]["paagai"]*3600+self.data[pl]["kalai"]*60+self.data[pl]["vikalai"]-(self.data[pl]["kaalapurushan"]-1)*30*3600
            order[pl]=appender.index(degpl)+1
        self.desc=order.copy()
        for pl in planetonly:
            if pl in self.desc:
                subam[pl]=self.subathuvam[pl]+(self.subathuvam[pl])*(0.3/self.desc[pl])
            else:
                subam[pl]=self.subathuvam[pl]
        self.karagamsam=subam.copy()                                                          