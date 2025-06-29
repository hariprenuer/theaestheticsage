from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.aadibathiyam import lagnaadhibathiyam as lg
# from birthdata.prognostics.dasabukthi import planetarycycle as pc

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
class postionsinvolved:
    def __init__(self,data,dasagiven=None):
        self.birthdata=data
        self.data=ax.auxillarydata(self.birthdata).data
        self.charam=ax.auxillarydata(self.birthdata).chaaram
        self.angisam=ax.auxillarydata(self.birthdata).angisanadhan
        # self.dasa=pc.planetaryinfluencers(self.name).planetaryinfluencers
        if dasagiven is None:
            self.dasa=ax.auxillarydata(self.birthdata).dasa
        else:
            self.dasa=dasagiven
        self.aadhibathiyam=lg.lagnaadhibathiyam(self.data).lagnaadhibathiyam
        self.wrt=lg.lagnaadhibathiyam(self.data).bavaadhibathiyam
        involved=[]
        reps={}
        planetwise={pl:0 for pl in planets}
        for pl in self.dasa:
            involved=involved+[self.data[pl]["lagnam"]]+self.aadhibathiyam[pl]+[self.data[self.charam[pl]["charanadhan"]]["lagnam"]]+self.aadhibathiyam[self.charam[pl]["charanadhan"]]+[self.data[self.angisam[pl]["angisanadhan"]]["lagnam"]]+self.aadhibathiyam[self.angisam[pl]["angisanadhan"]]+[self.data[self.angisam[pl]["thunaiangisandhan"]]["lagnam"]]+self.aadhibathiyam[self.angisam[pl]["thunaiangisandhan"]]
        for ind in range(1,13):
            if ind in involved:
                reps[ind]=involved.count(ind)
            else:
                reps[ind]=0
        self.positionsinvolved=reps.copy()
        for i in range(1,13):
            for pl in planets:
                if i in self.aadhibathiyam[pl]:
                    planetwise[pl]=planetwise[pl]+self.positionsinvolved[i]
        planetwise["rahu"]=self.positionsinvolved[self.data["rahu"]["lagnam"]]
        planetwise["kethu"]=self.positionsinvolved[self.data["kethu"]["lagnam"]]
        self.planetinvolvement=planetwise.copy()
