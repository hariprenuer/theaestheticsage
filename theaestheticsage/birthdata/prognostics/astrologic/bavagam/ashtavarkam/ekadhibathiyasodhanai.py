from birthdata.prognostics.astrologic.karagam import auxillarydata as ax

from birthdata.prognostics.astrologic.bavagam.ashtavarkam import thirikonasodhanai
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
ownersoftwo={"sevvaai":["mesham","viruchigam"],"budhan":["midhunam","kanni"],"guru":["dhanusu","meenam"],
             "sukiran":["rishabam","thulam"],"shani":["magaram","kumbam"]}
class ashtaekadhibathiyasodhanai:
    def __init__(self,birthdata,pinnatavarka):
        planetarypositions=[]
        sodhanai=[]
        data=ax.auxillarydata(birthdata).data
        sample=pinnatavarka.copy()
        for pl in planetonly:
            planetarypositions.append(bavaslist[data[pl]["kaalapurushan"]-1])
        for pl in planetonly:
            for bv in planetarypositions:
                if pl in ownersoftwo:
                   if bv in list(ownersoftwo[pl]):
                        if bv not in sodhanai:
                            sodhanai.append(bv)
        for ele in planetonly:
            if ele in ownersoftwo:
                if sample[ownersoftwo[ele][0]]==0 or sample[ownersoftwo[ele][1]]==0:
                    continue
                else:
                    count=0
                    caseablst=[]
                    caseplst=[]
                    for plhouse in ownersoftwo[ele]:
                        if plhouse in sodhanai:
                            count=count+1
                            caseplst.append(plhouse)
                        else:
                            caseablst.append(plhouse)
                    if count==2:
                        sample=sample
                    if count==1:
                        if sample[caseablst[0]]<=sample[caseplst[0]]:
                            sample[caseablst[0]]=0
                        else:
                            sample[caseablst[0]]=sample[caseplst[0]]
                    if count==0:
                        if sample[caseablst[0]]==sample[caseablst[1]]:
                            sample[caseablst[0]]=0
                            sample[caseablst[1]]=0
                        else:
                            lstsamp=[sample[caseablst[0]],sample[caseablst[1]]]
                            sample[caseablst[0]]=min(lstsamp)
                            sample[caseablst[1]]=min(lstsamp)
        self.ashtaekadhibathiyasodhanai=sample.copy()
class ekadhibathiyasodhanai:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        ashtavarkam=thirikonasodhanai.thirikonaodhanai(self.birthdata).thirikonasodhanai
        self.ekadhibathiyasodhanai=ashtaekadhibathiyasodhanai(self.birthdata,ashtavarkam).ashtaekadhibathiyasodhanai
    def pinnatavarkaekadhibathiyaodhanai(self,pinnatavarkas):
        pinnatavarkas=thirikonasodhanai.thirikonaodhanai(self.birthdata).pinnatavarkathirikonasodhanai(pinnatavarkas)
        if pinnatavarkas is not None:
            return ashtaekadhibathiyasodhanai(self.birthdata,pinnatavarkas).ashtaekadhibathiyasodhanai