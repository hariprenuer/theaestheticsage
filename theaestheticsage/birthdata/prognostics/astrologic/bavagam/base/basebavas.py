from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.base import bavahelpers as bh

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni","thulam","viruchigam",
           "dhanusu","magaram","kumbam","meenam"]
class featuresofbavas:
    def __init__(self,bava):
        self.bava=bava
        self.owner=bh.ownership(bava)
        self.ismoolathirikonam=bh.ismoolathirikonam(bava)
        self.type=bh.aanpenrasi(bava)
class bavas:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        self.data=ax.auxillarydata(birthdata).data
        contentdic={}
        for bv in bavaslist:
            contentdic[bv]=bh.contents(bv,self.data)
        self.holdings=contentdic.copy()
        self.rasi=bavaslist[self.data["chandhiran"]["kaalapurushan"]-1]
        self.lagnam=bavaslist[self.data["lagnam"]["kaalapurushan"]-1]
        self.lagnaadhibadhi=bh.ownership(bavaslist[self.data["lagnam"]["kaalapurushan"]-1])
        self.raasiadhibadhi=bh.ownership(self.rasi)
        self.indhulagnam=bh.indhulagnam(self.data)
        self.aarudalagnam=bh.aarudalagnam(self.data)
