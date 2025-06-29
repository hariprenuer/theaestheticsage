from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import nakshatrachaaram
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import vargachakaram
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import angisam
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import planetaryaspectations as plas
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import postiongrade
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import relationalindex
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import yogiavayogi

from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import chart
from birthdata.prognostics.dasabukthi import planetarycycle
from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import positiongetter
from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import sqlhelpers

planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","maandhi"]
class auxillarydata:
    def __init__(self,data):
        othertype=False
        # if sqlhelpers.namechecker(data):
        if False:
            self.data=data
            obj=positiongetter.horoscopeblueprint(data)
            maindata=obj.data
        else:
            #print(data)
            othertype=True
            obj=chart.positions(data["dob"],data["tob"],data["latitude"],data["longitude"])
            self.startdate=obj.startdate
            iruppu=str(obj.iruppudasa[0])+"-"+str(obj.iruppudasa[1])+"-"+str(obj.iruppudasa[2])
            maindata=obj.planetaryposition
            self.data=maindata.copy()
            self.date=data["dob"]
            self.time=data["tob"]
            self.longitude=data["longitude"]
            self.latitude=data["latitude"]
            self.iruppudasa=obj.iruppudasa
            self.iruppuplanet=obj.iruppuplanet
        chardtreq={}
        for i in planets:
            if othertype:
                if i!="maandhi":
                    chardtreq[i]=nakshatrachaaram.charanakshathra(maindata)[i]["chaaram"]
            else:
                chardtreq[i]=nakshatrachaaram.charanakshathra(maindata)[i]["chaaram"]
        self.chaaram=chardtreq.copy()
        self.angisanadhan=(angisam.angisam(nakshatrachaaram.charanakshathra(maindata))[0]).copy()
        self.varkkam={"raasi":vargachakaram.raasi(maindata),"horai":vargachakaram.horai(maindata),"sapdhamsam":vargachakaram.sapdhamasam(maindata),
        "dasamsam":vargachakaram.dasamsam(maindata),"dhuvadasamsam":vargachakaram.dhuvadasamsam(maindata),"navamsam":vargachakaram.navamsam(maindata),            
        "shastiamsam":vargachakaram.shastiamsam(maindata),"drekaanam":vargachakaram.drekaanam(maindata),"trimsamsam":vargachakaram.trimsamsam(maindata)}.copy()
        self.data=maindata.copy()
        self.grahapaarvai=plas.grahapaaravai(self.data)
        self.plas=plas.grahapaaravai(self.data).plasdata.copy()
        self.tharakalauravu=postiongrade.positionalrelation(self.data).positionalrelation.copy()
        self.yogiavayogi=yogiavayogi.yogiavayogi(self.data).yogiavayogi.copy()
        if othertype:
            self.pcobj=planetarycycle.planetaryinfluencers({"dob":data["dob"],"tob":data["tob"],"iruppu":iruppu,"iruppuplanet":self.chaaram["chandhiran"]["charanadhan"]})
            self.dasa=self.pcobj.planetaryinfluencers
            self.age=self.pcobj.age
        else:
            self.pcobj=planetarycycle.planetaryinfluencers(self.data)
            self.dasa=self.pcobj.planetaryinfluencers
        self.relationalindex=relationalindex.relationalindex(self.tharakalauravu,self.dasa).relationalindex.copy()
 
