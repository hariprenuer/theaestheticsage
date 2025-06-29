from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.base import bavahelpers as bh
from birthdata.prognostics.astrologic.karagam.strength_of_planets import planetaryconditons as pc # type: ignore
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import planetaryaspectations as pas

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
kendiram=[1,4,7,10]
thirikonam=[1,5,9]
panabaram=[2,5,8,11]
dhurthasthanam=[3,6,8,12]
def assigner(bavas,data):
    dict={}
    for ind in data:
        dict[ind]=bavas[ind]
    return dict.copy()
def adhibathgiver(data):
    lst=[]
    for ind in data:
        if bh.ownership(data[ind]) not in lst:
            lst.append(bh.ownership(data[ind]))
    return lst
class aadhibathiyam:
    def __init__(self,data,wrt="lagnam"):
        self.birthdata=data
        print(self.birthdata)
        self.aux=ax.auxillarydata(self.birthdata)
        self.data=self.aux.data
        if wrt in planetonly:
            self.wrt=wrt
        else:
            self.wrt="lagnam"
        pos=self.data[self.wrt]["kaalapurushan"]-1
        bathiyam={}
        kendiras={}
        thirikonas={}
        maraivu={}
        normpos={}
        for ord in range(1,13):
            index=pos+ord
            if index>12:
                index=index-12*int(index/12)
            bathiyam[ord]=bavaslist[index-1]
        self.aadhibathiyam=bathiyam.copy()
        self.kendiram=assigner(self.aadhibathiyam,kendiram)
        self.thirikonam=assigner(self.aadhibathiyam,thirikonam)
        self.panabaram=assigner(self.aadhibathiyam,panabaram)
        self.dhurthasthanam=assigner(self.aadhibathiyam,dhurthasthanam)
        self.kendhiradhibathi=adhibathgiver(self.kendiram)
        self.thirikonadhibathi=adhibathgiver(self.thirikonam)
        self.avayogadhibathi=adhibathgiver(self.dhurthasthanam)
        for pl in planetonly:
            for ind in kendiram:
                if self.kendiram[ind]==bavaslist[self.data[pl]["kaalapurushan"]-1]:
                    kendiras[pl]=[ind,self.kendiram[ind]]+pc.planetarycondition(self.birthdata).planetcondition(pl)[:-1]+self.aux.grahapaarvai.planetasp(pl)
            for ind in thirikonam:
                if self.thirikonam[ind]==bavaslist[self.data[pl]["kaalapurushan"]-1]:
                    thirikonas[pl]=[ind,self.thirikonam[ind]]+pc.planetarycondition(self.birthdata).planetcondition(pl)[:-1]+self.aux.grahapaarvai.planetasp(pl)
            for ind in dhurthasthanam:
                if self.dhurthasthanam[ind]==bavaslist[self.data[pl]["kaalapurushan"]-1]:
                    maraivu[pl]=[ind,self.dhurthasthanam[ind]]+pc.planetarycondition(self.birthdata).planetcondition(pl)[:-1]+self.aux.grahapaarvai.planetasp(pl)
            for ind in panabaram:
                if self.panabaram[ind]==bavaslist[self.data[pl]["kaalapurushan"]-1]:
                    normpos[pl]=[ind,self.panabaram[ind]]+pc.planetarycondition(self.birthdata).planetcondition(pl)[:-1]+self.aux.grahapaarvai.planetasp(pl)
        self.kendiraplanets=kendiras.copy()
        self.thirikonaplanets=thirikonas.copy()
        self.maraivusthanaplanets=maraivu.copy()
        self.elsepos=normpos.copy()
        natdic={}
        for pl in planetonly:
            if pl in self.kendiraplanets:
                natdic[pl]=self.kendiraplanets[pl]
            if pl in self.thirikonaplanets:
                natdic[pl]=self.thirikonaplanets[pl]
            if pl in self.maraivusthanaplanets:
                natdic[pl]=self.maraivusthanaplanets[pl]
            if pl in self.elsepos:
                natdic[pl]=self.elsepos[pl]
        self.natural=natdic.copy()
            
            
                                                                                           