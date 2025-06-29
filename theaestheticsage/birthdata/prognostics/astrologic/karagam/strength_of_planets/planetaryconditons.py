from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.base import bavahelpers as bh

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
utchaveedu={"suriyan":"mesham","chandhiran":"rishabam","guru":"kadagam","budhan":"kanni","shani":"thulam",
            "sevvaai":"magaram","sukiran":"meenam","rahu":"something","kethu":"something"}
neetchaveedu={"suriyan":"thulam","chandhiran":"viruchigam","guru":"magaram","budhan":"meenam","shani":"mesham",
            "sevvaai":"kadagam","sukiran":"kanni","rahu":"something","kethu":"something"}
natpuveedu={"suriyan":["viruchigam","kadagam","dhanusu","meenam"],"chandhiran":["midhunam","simmam","kanni"],
            "guru":["mesham","simmam","viruchigam"],"budhan":["rishabam","simmam","thulam"],
            "shani":["rishabam","midhunam","kanni"],"sevvaai":["simmam","dhanusu","meenam"],
            "sukiran":["midhunam","dhanusu","magaram","kumbam"],"rahu":["midhunam","kanni","rishabam","thulam","magaram","kumbam"],
            "kethu":["midhunam","kanni","rishabam","thulam","magaram","kumbam"]}
pagaiveedu={"suriyan":["rishabam","magaram","kumbam"],"chandhiran":[],"guru":["rishabam","midhunam","kanni","thulam"],"budhan":["kadagam"],
            "shani":["mesham","kadagam","simmam","viruchigam"],"sevvaai":["midhunam","kanni"],"sukiran":["kadagam","simmam"],"rahu":["kadagam","simmam","dhanusu","meenam"],
            "kethu":["kadagam","simmam","dhanusu","meenam"]}
class planetarycondition:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        self.data=ax.auxillarydata(self.birthdata).data
        plcond={}
        for pl in planetonly:
            if utchaveedu[pl]==bavaslist[self.data[pl]["kaalapurushan"]-1]:
                plcond[pl]=[100,"utcham",bavaslist[self.data[pl]["kaalapurushan"]-1]]
            elif neetchaveedu[pl]==bavaslist[self.data[pl]["kaalapurushan"]-1]:
                plcond[pl]=[10,"neetcham",bavaslist[self.data[pl]["kaalapurushan"]-1]]
            elif bh.ownership(bavaslist[self.data[pl]["kaalapurushan"]-1])==pl:
                plcond[pl]=[90,"aatchi",bavaslist[self.data[pl]["kaalapurushan"]-1]]
            elif bavaslist[self.data[pl]["kaalapurushan"]-1] in natpuveedu[pl]:
                plcond[pl]=[75,"natpu",bavaslist[self.data[pl]["kaalapurushan"]-1]]
            elif bavaslist[self.data[pl]["kaalapurushan"]-1] in pagaiveedu[pl]:
                plcond[pl]=[25,"pagai",bavaslist[self.data[pl]["kaalapurushan"]-1]]
            else:
                plcond[pl]=[50,"samam",bavaslist[self.data[pl]["kaalapurushan"]-1]]            
        self.planetarycondition=plcond.copy()
    def planetcondition(self,planet):
        return self.planetarycondition[planet]
