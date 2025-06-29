from birthdata.prognostics.astrologic.bavagam.ashtavarkam import ekadhibathiyasodhanai as ek
from birthdata.prognostics.astrologic.karagam import auxillarydata as ax

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
crasipindam=[7,10,8,4,10,5,7,8,9,5,11,12]
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
plgrahapindam=[5,5,8,5,10,7,5]
class raasipindam:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        allpinda={}
        for pl in planetonly:
            afpindam=0
            data=ek.ekadhibathiyasodhanai(self.birthdata).pinnatavarkaekadhibathiyaodhanai(pl)
            for bv in bavaslist:
                afpindam=afpindam+data[bv]*crasipindam[bavaslist.index(bv)]
            allpinda[pl]=afpindam
        self.raasipindam=allpinda.copy()
class grahapindam:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        gallpinda={}
        for pl in planetonly:
            value=0            
            data=ek.ekadhibathiyasodhanai(self.birthdata).pinnatavarkaekadhibathiyaodhanai(pl)
            for planet in planetonly:
                pos=bavaslist[ax.auxillarydata(self.name).data[planet]["kaalapurushan"]-1]
                value=value+data[pos]*plgrahapindam[planetonly.index(planet)]
            gallpinda[pl]=value
        self.grahapindam=gallpinda.copy()
class sorthiyapindam:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        sorthiya={}
        gpinda=grahapindam(self.birthdata).grahapindam
        rpinda=raasipindam(self.birthdata).raasipindam
        for planet in planetonly:
            sorthiya[planet]=gpinda[planet]+rpinda[planet]
        print(sorthiya)
        self.sorthiyapindam=sorthiya.copy()
class gunakaarangal:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        self.grahapindam=grahapindam(self.birthdata).grahapindam
        self.raasipindam=raasipindam(self.birthdata).raasipindam
        self.sorthiyapindam=sorthiyapindam(self.birthdata).sorthiyapindam
