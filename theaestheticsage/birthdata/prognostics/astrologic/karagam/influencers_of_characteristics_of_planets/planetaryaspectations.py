aspectations={"suriyan":[7],"chandhiran":[7],"sevvaai":[4,7,8],"budhan":[7],
              "guru":[5,7,9],"sukiran":[7],"shani":[3,7,10],"rahu":[],"kethu":[],"lagnam":[]}
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
planetaries=["lagnam",'suriyan','chandhiran','sevvaai','budhan','guru','sukiran','shani','rahu','kethu']
def aspgiver(data,exas=None,excond=None):
    asps={}
    for bv in bavaslist:
        asps[bv]=[]
    if exas is None:
        for pl in planetaries:
            for asp in aspectations[pl]:
                index=data[pl]["kaalapurushan"]+asp-1
                if index>12:
                    index=index-12*int(index/12)
                if pl not in ["lagnam","rahu","kethu"]:
                    asps[bavaslist[index-1]].append(pl)
    elif exas is not None and excond is not None:
        for pl in planetaries:
            for asp in exas:
                index=data[pl]["kaalapurushan"]+asp-1
                if index>12:
                    index=index-12*int(index/12)
                if pl!=excond and (pl not in ["lagnam","rahu","kethu"]):
                    asps[bavaslist[index-1]].append(pl)
    return asps.copy()
def plaspgiver(data,bava):
    plass={}
    for pl in planetaries:
        plass[pl]=[]
    for pl in planetaries:
        for bv in bava:
            if bavaslist[data[pl]["kaalapurushan"]-1]==bv:
                plass[pl]=bava[bv]
                break 
    return plass.copy()
class grahapaaravai:
    def __init__(self,data):
        #self.name=name
        self.data=data
        bavas=aspgiver(self.data).copy()
        plas=plaspgiver(self.data,bavas).copy()
        bavas14=aspgiver(self.data,[3,10],"shani").copy()
        bavas12=aspgiver(self.data,[5,9],"guru").copy()
        bavas34=aspgiver(self.data,[4,8],"sevvaai").copy()
        kaalpaarvai=plaspgiver(self.data,bavas14).copy()
        araipaarvai=plaspgiver(self.data,bavas14).copy()
        mukaalpaarvai=plaspgiver(self.data,bavas34).copy()
        allbavas={"mullupaarvai":bavas.copy(),"kaalpaarvai":bavas14.copy(),"araipaarvai":bavas12.copy(),"mukaalpaarvai":bavas34.copy()}
        allgrahas={"mullupaarvai":plas.copy(),"kaalpaarvai":kaalpaarvai.copy(),"araipaarvai":araipaarvai.copy(),"mukaalpaarvai":mukaalpaarvai.copy()}
        self.baavapaarvai=allbavas.copy()
        self.grahapaarvai=allgrahas.copy()
        self.plasdata={"baavapaarvai":self.baavapaarvai,"grahapaarvai":self.grahapaarvai}
    def planetasp(self,planet,normaliser="mullupaarvai"):
        return self.grahapaarvai[normaliser][planet]