from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import andhakamsam
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
class pushkaramsam(basic):
    def __init__(self,name,passer):
        super().__init__(name,passer)
        self.data=self.aux.data
        self.subathuvam=andhakamsam.andhakamsam(self.name,self.passer).andhakamsam
        suba={}
        pushkarpaagai={i:[] for i in [21,14,24,7]}
        for i in range(4):
            for j in range(0,3):
                ind=i+j*4
                if i==0:
                    pushkarpaagai[21].append(bavaslist[ind])
                if i==1:
                    pushkarpaagai[14].append(bavaslist[ind])
                if i==2:
                    pushkarpaagai[24].append(bavaslist[ind])
                if i==3:
                    pushkarpaagai[7].append(bavaslist[ind])
        self.pushkarpaagai=pushkarpaagai.copy()
        for ind in pushkarpaagai:
            for pl in planetonly:
                if bavaslist[self.data[pl]["kaalapurushan"]-1] in pushkarpaagai[ind] and self.data[pl]["paagai"]==ind:
                    suba[pl]=self.subathuvam[pl]+(self.subathuvam)*0.2
                else:
                    suba[pl]=self.subathuvam[pl]
        self.pushakaramsam=suba.copy()