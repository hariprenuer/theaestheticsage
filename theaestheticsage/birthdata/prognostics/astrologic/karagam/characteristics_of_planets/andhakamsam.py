from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import karagamsam
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
andhakams={"mesham":[0,-1],"rishabam":[6,10],"midhunam":[9,15],"kadagam":[18,27],"simmam":[18,27],
             "kanni":[19,21],"thulam":[0,-1],"viruchigam":[27,30],"dhanusu":[20,23],"magaram":[26,29],
             "kumbam":[20,23],"meenam":[0,-1]}
class andhakamsam(basic):
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=self.aux.data
        self.subathuvam=karagamsam.karagamsam(self.name,self.passer).karagamsam
        subam={}
        for pl in planetonly:
            degpl=self.data[pl]["paagai"]*3600+self.data[pl]["kalai"]*60+self.data[pl]["vikalai"]-(self.data[pl]["kaalapurushan"]-1)*30*3600
            val=andhakams[bavaslist[self.data[pl]["kaalapurushan"]-1]]
            if int(degpl/3600) in range(val[0],val[1]):
                subam[pl]=self.subathuvam[pl]-(self.subathuvam[pl])*0.1
            else:
                subam[pl]=self.subathuvam[pl]
        self.andhakamsam=subam.copy()