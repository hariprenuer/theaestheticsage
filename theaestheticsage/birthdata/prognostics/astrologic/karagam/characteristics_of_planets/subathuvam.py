from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic
from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import chandhirasubathuvam as chandhiran
from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import devaamsam

planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
mesham={"suriyan":100,"chandhiran":100,"sevvaai":75,"budhan":0,"guru":100,"sukiran":0,
        "shani":0,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
rishabam={"suriyan":100,"chandhiran":0,"sevvaai":0,"budhan":100,"guru":0,"sukiran":75,
        "shani":100,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
midhunam={"suriyan":25,"chandhiran":50,"sevvaai":0,"budhan":100,"guru":50,"sukiran":100,
        "shani":100,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
kadagam={"suriyan":50,"chandhiran":100,"sevvaai":100,"budhan":0,"guru":100,"sukiran":50,
        "shani":25,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
simmam={"suriyan":100,"chandhiran":50,"sevvaai":100,"budhan":0,"guru":100,"sukiran":25,
        "shani":0,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
kanni={"suriyan":25,"chandhiran":0,"sevvaai":0,"budhan":100,"guru":0,"sukiran":100,
        "shani":75,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
thulam={"suriyan":25,"chandhiran":100,"sevvaai":0,"budhan":100,"guru":0,"sukiran":100,
        "shani":100,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
viruchigam={"suriyan":100,"chandhiran":100,"sevvaai":75,"budhan":0,"guru":100,"sukiran":0,
        "shani":50,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
dhanusu={"suriyan":100,"chandhiran":50,"sevvaai":100,"budhan":0,"guru":100,"sukiran":0,
        "shani":0,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
magaram={"suriyan":0,"chandhiran":25,"sevvaai":75,"budhan":100,"guru":0,"sukiran":100,
        "shani":75,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
kumbam={"suriyan":25,"chandhiran":0,"sevvaai":50,"budhan":100,"guru":0,"sukiran":100,
        "shani":100,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
meenam={"suriyan":25,"chandhiran":100,"sevvaai":100,"budhan":0,"guru":100,"sukiran":0,
        "shani":0,"rahu":0,"kethu":0,"maandhi":0,"lagnam":0}
lagnas=[mesham,rishabam,midhunam,kadagam,simmam,kanni,thulam,viruchigam,dhanusu,magaram,
        kumbam,meenam]
class characteristics(basic):
    def __init__(self,name):
        super().__init__(name)
        end={}
        iyarkaippabar={"suriyan":-50,"chandhiran":0,
            "sevvaai":-75,"budhan":0,"guru":0,"sukiran":0,"shani":-100,"rahu":-100,
            "kethu":-100,"maandhi":-100,"lagnam":0}
        iyarkaisubar={"suriyan":50,"chandhiran":chandhiran.chanhdirasubathuvam(self.name).chandhirasubathuvam,
            "sevvaai":25,"budhan":0,"guru":100,"sukiran":75,"shani":0,"rahu":0,
            "kethu":0,"maandhi":0,"lagnam":0}
        aadhibathiyam=lagnas[self.aux.data["lagnam"]["kaalapurushan"]-1]
        self.iyarkaisubar=devaamsam.devaamsam(self.name,iyarkaisubar).devaamsam
        self.iyarkaipaabar=devaamsam.devaamsam(self.name,iyarkaippabar).devaamsam
        self.aadhibathiyam=devaamsam.devaamsam(self.name,aadhibathiyam).devaamsam
        for pl in planetonly:
            end[pl]=(self.iyarkaisubar[pl])*0.33+(self.aadhibathiyam[pl])*0.33+(self.iyarkaipaabar[pl])*0.33
        self.characteristics=end.copy()
        self.least=list(self.characteristics.values())[list(self.characteristics.values()).index(min(self.characteristics.values()))]
        self.percent={pl:(self.characteristics[pl]/(sum(list(self.characteristics.values()))/len(self.characteristics)))*100 for pl in self.characteristics}
# print(characteristics("hari prasath").characteristics)