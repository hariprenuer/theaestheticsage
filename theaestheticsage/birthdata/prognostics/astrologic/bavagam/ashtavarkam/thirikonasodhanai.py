from birthdata.prognostics.astrologic.bavagam.ashtavarkam import ashtavarkam as asht

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
def sodhanaispecialcaes(data):
    if data[0]==data[1] and data[0]==data[2] and data[2]==data[1]:
        for ind in range(len(data)):
            data[ind]=0
        return data
    if data.count(0)==1:
        return data
    if data.count(0)==2:
        for ind in range(len(data)):
            if data[ind]!=0:
                data[ind]=0
        return data
    else:
        for ind in range(len(data)):
            data[ind]=min(data)
        return data
class ashtathirikonasodhanai:
    def __init__(self,attavarkam):
        sample={}
        ashtathirikonasodhanai={}
        for i in range(4):
            sodhanai=[]
            for subin in range(3):
                sodhanai.append(attavarkam[bavaslist[subin*4+i]])
            data=sodhanaispecialcaes(sodhanai)
            for subin in range(3):
                for ind in range(len(data)):
                    sample[bavaslist[subin*4+i]]=data[subin]
        for ele in bavaslist:
            ashtathirikonasodhanai[ele]=sample[ele]
        self.ashtathirikonasodhanai=ashtathirikonasodhanai.copy()
class thirikonaodhanai:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        ashtavarkam=asht.ashtavarkam(self.birthdata).ashtavarakam
        for ele in bavaslist:
            ashtavarkam[ele]=ashtavarkam[ele]%12
        self.thirikonasodhanai=ashtathirikonasodhanai(ashtavarkam).ashtathirikonasodhanai
    def pinnatavarkathirikonasodhanai(self,pinnatavarkas):
        pinnatavarkas=asht.ashtavarkam(self.birthdata).pinnatavarkam(pinnatavarkas)
        if pinnatavarkas is not None:
            return ashtathirikonasodhanai(pinnatavarkas).ashtathirikonasodhanai