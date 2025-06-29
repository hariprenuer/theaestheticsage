from birthdata.prognostics.astrologic.bavagam.base import bavahelpers as bh

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
shubascale={"suriyan":50,"sevvaai":25,"sukiran":75,"guru":100,"rahu":10,"kethu":10,"shani":0}
class lagnaadhibathiyam:
    def __init__(self,data):
        self.data=data
        lagnaadhibathiyam={}
        for pl in planetonly:
            lagnaadhibathiyam[pl]=[]
        wrtlagna=bavaslist[self.data["lagnam"]["kaalapurushan"]-1:]+bavaslist[0:self.data["lagnam"]["kaalapurushan"]-1]
        for spot in range(len(wrtlagna)):
            lagnaadhibathiyam[bh.ownership(wrtlagna[spot])].append(spot+1)
        self.lagnaadhibathiyam=lagnaadhibathiyam.copy()
        self.bavaadhibathiyam=wrtlagna.copy()