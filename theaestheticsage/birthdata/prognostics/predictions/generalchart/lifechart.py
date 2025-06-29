from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.karagam.characteristics_of_planets import subathuvam
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import relationalindex, postiongrade

from birthdata.prognostics.astrologic.bavagam.ashtavarkam import ashtavarkam, ekadhibathiyasodhanai, thirikonasodhanai
from birthdata.prognostics.astrologic.bavagam.aadibathiyam import positionsdasainvolved, baseaadhibathiyam

from birthdata.prognostics.astrologic.planetary_positions.panchangam.kochaaram import currentpositon

shadbalaplanets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
planets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
ashtavarka=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
def makeitreturn(inidic,toupdate):
    dic=inidic
    dic.update(toupdate)
    return dic.copy()

class lifechartvalue:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        self.aux=ax.auxillarydata(self.birthdata)
        self.data=ax.auxillarydata(self.birthdata).data
        self.positionsinvloved=positionsdasainvolved.postionsinvolved(self.birthdata)
        self.dasa=positionsdasainvolved.postionsinvolved(self.birthdata).dasa
        self.subathuvam=subathuvam.characteristics(self.birthdata).characteristics
        # self.shadbalam=shadbalahelper.datacollector("hari prasath")
        self.posgrade=postiongrade.positionalrelation(self.data).positionalrelation
        self.dasacooperation=relationalindex.relationalindex(self.posgrade,self.dasa).relationalindex
        self.kochaaram=currentpositon.kocharam().data
        self.ashtavarkam=ashtavarkam.ashtavarkam(self.birthdata)
        self.thirikonasodhanai=thirikonasodhanai.thirikonaodhanai(self.birthdata)
        self.ekadhibathiyasodhanai=ekadhibathiyasodhanai.ekadhibathiyasodhanai(self.birthdata)
        #self.baseaadhibathiyam=baseaadhibathiyam.aadhibathiyam(self.birthdata)
        # value=0
        # divider=0
        # totalsubsum=sum(list(self.subathuvam.values()))/len(self.subathuvam)
        # for pl in self.dasacooperation:
        #     value=value+self.positionsinvloved[pl]*self.subathuvam[pl]*self.shadbalam[pl]*self.dasacooperation[pl]
        #     divider=divider+self.positionsinvloved[pl]*self.shadbalam[pl]*self.dasacooperation[pl]
        # birthvalue=100*(value/divider)/totalsubsum
        # koacharamvalue=0
        # koachradivider=0
        # # print(100*(value/divider)/totalsubsum)
        # for pl in ashtavarka:
        #     asht=self.ashtavarkam.pinnatavarkam(pl)[bavaslist[self.kochaaram[pl]["kaalapurushan"]-1]]
        #     koacharamvalue=koacharamvalue+(self.subathuvam[pl])/8-(asht-1)
        #     koachradivider=koachradivider+self.subathuvam[pl]
        # self.kocharamvalue=koacharamvalue
        # self.birthvalue=birthvalue
        tosubmit={
            "dob":self.aux.date,
            "tob":self.aux.time,
            "latitude":self.aux.latitude,
            "longitude":self.aux.longitude,
            "postionalgrader":self.posgrade,
            # "planetaryposition":self.data,
            # "angisanadhan":self.aux.angisanadhan,
            # "varkkam":self.aux.varkkam,
            # # "shadbalam":self.shadbalam,
            # "subathuvam":self.subathuvam,
            # "kocharam":self.kochaaram,
            # "ashtavarkam":makeitreturn({"samudhayam":self.ashtavarkam.ashtavarakam},{pl:self.ashtavarkam.pinnatavarkam(pl) for pl in shadbalaplanets}),
            # "sodhanai":{"thirikonasodhanai":makeitreturn({"samudhayam":self.thirikonasodhanai.thirikonasodhanai}, {pl:self.thirikonasodhanai.pinnatavarkathirikonasodhanai(pl) for pl in shadbalaplanets}),
            #             "ekadhibathiyasodhanai":makeitreturn({"samudhayam":self.ekadhibathiyasodhanai.ekadhibathiyasodhanai},{pl:self.ekadhibathiyasodhanai.pinnatavarkaekadhibathiyaodhanai(pl) for pl in shadbalaplanets})},
            # "lagnaadhibathiyam":self.positionsinvloved.aadhibathiyam,
            # "paarvai":self.aux.plas,
            # "dasa":self.dasa,
            # "yogi":self.aux.yogiavayogi,
            # "dasauravu":self.aux.relationalindex,
            # "tharkalauravu":self.posgrade,
            # "dasabavainvloved":self.positionsinvloved.positionsinvolved,
            # "dasagrahinvolved":self.positionsinvloved.planetinvolvement,
            "iruppudasa":self.aux.iruppudasa,
            "iruppuplanet":self.aux.iruppuplanet,
        }
        self.horoscope=tosubmit.copy()
        # print(tosubmit)
# print(lifechartvalue({'dob': '9-6-2005', 'tob': '14-3', 'latitude': 11.6643, 'longitude': 78.146}).dasacooperation)
