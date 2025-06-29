from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.aadibathiyam import baseaadhibathiyam as bad
from birthdata.prognostics.astrologic.bavagam.base import basebavas as bb
from birthdata.prognostics.astrologic.bavagam.base import bavahelpers as bh
from birthdata.prognostics.astrologic.karagam.strength_of_planets import planetaryconditons as pc # type: ignore

bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni","thulam","viruchigam",
           "dhanusu","magaram","kumbam","meenam"]
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","lagnam"]
plts=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
aanrasi=["mesham","midhunam","simmam","thulam","dhanusu","kumbam"]
penrasi=["rishabam","kadagam","kanni","viruchigam","magaram","meenam"]
def intherecheck(planet,pos1,pos2=None,val=None):
    if pos2 is None:
        pos2=pos1
    count=0
    if val is not None:
        for pow in val:
            if planet in pos1:
                if pow in pos1[planet]:
                    count=count+1
            elif planet in pos2:
                if pow in pos2[planet]:
                    count=count+1
        if count>0:
            return True
        else:
            return False
def manycheck(planets,pos1,pos2=None):
    if pos2 is None:
        pos2=pos1
    count=0
    for pl in planets:
        if pl in pos1:
            count=count+1
        elif pl in pos2:
            count=count+1
    if count>len(planets)-2:
        return True
def bothsides(surrounder,involved,data,pos1,pos2=None,pos3=None,lim=None):
    if lim is None:
        lim=len(surrounder)
    if pos2 is None:
        pos2=pos1
    if pos3 is None:
        pos3=pos1
    if True:
        count=0
        for ele in plts:
            if ele in surrounder:
                if data[ele][involved]==pos1 or data[ele][involved]==pos2 and data[ele][involved]==pos3:
                    count=count+1
            if count>1 and count<=lim-1:
                return True
class yogas:
    def __init__(self,name):
        #ot bangas
        yogas=[]
        brief={}
        planetarypos={}
        self.name=name
        self.lagnakendiram=bad.aadhibathiyam(self.name,"lagnam").kendiraplanets
        self.chandhirakendiram=bad.aadhibathiyam(self.name,"chandhiran").kendiraplanets
        self.lagnathirikonam=bad.aadhibathiyam(self.name,"lagnam").thirikonaplanets
        self.data=ax.auxillarydata(self.name).data
        for pl in planetonly:
            planetarypos[pl]=bavaslist[self.data[pl]["kaalapurushan"]-1]
        #rusakyogam
        if intherecheck("sevvaai",self.lagnakendiram,self.chandhirakendiram,[100,90]):
            yogas.append("rusakyogam")
            brief["rusakyogam"]=["sevvaai"]
            #effect
        if intherecheck("budhan",self.lagnakendiram,self.chandhirakendiram,[100,90]):
            yogas.append("bathirayogam")
            brief["bathirayogam"]=["budhan"]
            #effect
        if intherecheck("guru",self.lagnakendiram,self.chandhirakendiram,[100,90]):
            yogas.append("hamsayogam")
            brief["hamsayogam"]=["guru"]
            #effect
        if intherecheck("shani",self.lagnakendiram,self.chandhirakendiram,[100,90]):
            yogas.append("sasayogam")
            brief["sasayogam"]=["shani"]
            #effect
        if intherecheck("sukiran",self.lagnakendiram,self.chandhirakendiram,[100,90]):
            yogas.append("malavayogam")
            brief["malavyogam"]=["sukiran"]
            #effect
        if bothsides(["sevvaai","budhan","guru","sukiran","shani"],"chandhiran",self.data,2):
            yogas.append("sunabayogam")
            brief["sunabayogam"]=["chandhiran","sevvaai","budhan","guru","sukiran","shani"]     
        if bothsides(["sevvaai","budhan","guru","sukiran","shani"],"chandhiran",self.data,12):
            yogas.append("anabayogam")
            brief["anabayogam"]=["chandhiran","sevvaai","budhan","guru","sukiran","shani"]     
        if bothsides(["sevvaai","budhan","guru","sukiran","shani"],"chandhiran",self.data,2,12):
            yogas.append("thuruthurayogam")
            brief["thuruthurayogam"]=["chandhiran","sevvaai","budhan","guru","sukiran","shani"]    
        if bothsides(["budhan","sukiran","guru"],"suriyan",self.data,2):
            yogas.append("vesiyogam")
            brief["vesiyogam"]=["suriyan","budhan","sukiran","guru"]
        if bothsides(["budhan","sukiran","guru"],"suriyan",self.data,12):
            yogas.append("vaasiyogam")
            brief["vaasiyogam"]=["suriyan","budhan","sukiran","guru"]
        if bothsides(["budhan","sukiran","guru"],"suriyan",self.data,2,2,12):
            yogas.append("ubayasari")
            brief["ubayasari"]=["suriyan","budhan","sukiran","guru"]
        if bothsides(["budhan","sukiran","guru"],"suriyan",self.data,2,1,12):
            yogas.append("subakarthari")
            brief["subakarthari"]=["suriyan","budhan","sukiran","guru"]
        if bothsides(["budhan","sukiran","guru"],"lagnam",self.data,2):
            yogas.append("susubayogam")
            brief["susubayogam"]=["lagnam","budhan","sukiran","guru"]
        if True:
            count=0
            tcount=0
            for pl in ["chandhiran","suriyan","lagnam"]:
                if planetarypos[pl] in aanrasi:
                    count=count+1
                if planetarypos[pl] in penrasi:
                    tcount=tcount+1
            if count==3 or tcount==3:
                yogas.append("mahabakiyayogam")
                brief["mahabakiyayogam"]=["lagnam","suriyan","chandhiran"]
        if self.data["guru"]["chandhiran"] in [1,4,7,10] and (self.data["guru"]["lagnam"] not in [6,8,12] and self.data["chandhiran"]["lagnam"] not in [6,8,12]):
            yogas.append("gajakesari")
            brief["gajakesari"]=["chandhiran","guru"]
        if bothsides(["budhan","sukiran","guru"],"chandhiran",self.data,10):
            yogas.append("amalayogam")
            brief["amalayogam"]=["chandhiran","budhan","sukiran","guru"]
        if self.data[bb.bavas(self.name).lagnaadhibadhi]["kaalapurushan"]==self.data[bb.bavas(self.name).raasiadhibadhi]["kaalapurushan"]:
            if bb.bavas(self.name).lagnaadhibadhi in self.lagnakendiram or bb.bavas(self.name).lagnaadhibadhi in self.chandhirakendiram:
                yogas.append("pushkalayogam")
                brief["pushkalayogam"]=["chandhiran",bb.bavas(self.name).lagnaadhibadhi,bb.bavas(self.name).raasiadhibadhi,"chandhiran"]
        if bothsides(["sevvaai","budhan","guru","sukiran","shani","suriyan","chandhiran"],"lagnam",self.data,5,6,7,7):
            yogas.append("subamalayogam")
            brief["subamalayogam"]=["lagnam","sevvaai","budhan","guru","sukiran","shani"]  
        if bothsides(["sevvaai","budhan","guru","sukiran","shani","suriyan","chandhiran"],"lagnam",self.data,6,8,12,7):
            yogas.append("asubamalayogam")
            brief["asubamalayogam"]=["lagnam","sevvaai","budhan","guru","sukiran","shani","suriyan","chandhiran"]  
        if intherecheck("sukiran",self.lagnakendiram,[100,90]):
            if bh.ownership(bad.aadhibathiyam(self.name).thirikonadhibathi[9])=="sukiran":
                yogas.append("lakshmiyogam")
                brief["lakshmiyogam"]=["lagnam","sukiran"]
        if self.data["chandhiran"]["guru"] in [1,4,5,7,9,10]:
            guruc=pc.planetarycondition("hari prasath").planetcondition("guru")
            if 100 in guruc or 90 in guruc:
                yogas.append("gowriyogam")
                brief["gowriyogam"]=["chandhiran","lagnam"]
        if manycheck(["sukiran","budhan","guru"],self.lagnakendiram):
            for stre in [100,90]:
                if stre in pc.planetarycondition(name).planetcondition("guru"):
                    yogas.append("saraswatiyogam")
                    brief["saraswatiyogam"]=["sukiran","budhan","guru"]
                    break
        if manycheck(["suriyan","chandhiran"],self.lagnakendiram,self.lagnathirikonam):
            count=0
            for stre in [100,90,75]:
                if stre in pc.planetarycondition(name).planetcondition("suriyan"):
                    count+=1
                elif stre in pc.planetarycondition(name).planetcondition("chandhiran"):
                    count+=1
            if count==2:
                yogas.append("sikandayogam")
                brief["sikandayogam"]=["suriyan","chandhiran","lagnam"]     
        if manycheck(["sukiran","budhan",bad.aadhibathiyam(self.name).thirikonadhibathi[-1]],self.lagnakendiram,self.lagnathirikonam):
            count=0
            for stre in [100,90,75]:
                if stre in pc.planetarycondition(name).planetcondition("sukiran"):
                    count+=1
                elif stre in pc.planetarycondition(name).planetcondition("budhan"):
                    count+=1
            print(count)
            if count==2:
                yogas.append("srinadhayogam")
                brief["srinadhayogam"]=["budhan","sukiran","lagnam"] 
        if manycheck(["guru","shani",bb.bavas(self.name).lagnaadhibadhi],self.lagnakendiram,self.lagnathirikonam):
            for stre in [100,90,75]:
                if stre in pc.planetarycondition(name).planetcondition("guru"):
                    count+=1
                elif stre in pc.planetarycondition(name).planetcondition("shani"):
                    count+=1
            print(count)
            if count==2:
                yogas.append("virunchiyogam")
                brief["virunchiyogam"]=["guru","shani",bb.bavas(self.name).lagnaadhibadhi] 
        if manycheck([bb.bavas(self.name).lagnaadhibadhi,bh.ownership(bad.aadhibathiyam(self.name).kendhiradhibathi[7])],self.lagnakendiram,self.lagnathirikonam):
            for stre in [100,90,75]:
                if stre in pc.planetarycondition(name).planetcondition(bb.bavas(self.name).lagnaadhibadhi):
                    count+=1
                elif stre in pc.planetarycondition(name).planetcondition(bh.ownership(bad.aadhibathiyam(self.name).kendhiradhibathi[7])):
                    count+=1
            print(count)
            if count==2:
                yogas.append("paruvadhayogam")
                brief["paruvadhayogam"]=[bb.bavas(self.name).lagnaadhibadhi,bh.ownership(bad.aadhibathiyam(self.name).kendhiradhibathi[7])] 
        if manycheck([bh.ownership(bad.aadhibathiyam(self.name).thirikonadhibathi[9]),bh.ownership(bad.aadhibathiyam(self.name).kendhiradhibathi[10])],self.lagnakendiram,self.lagnathirikonam):
            for stre in [100,90,75]:
                if stre in pc.planetarycondition(name).planetcondition(bh.ownership(bad.aadhibathiyam(self.name).thirikonadhibathi[9])):
                    count+=1
                elif stre in pc.planetarycondition(name).planetcondition(bh.ownership(bad.aadhibathiyam(self.name).kendhiradhibathi[10])):
                    count+=1
            print(count)
            if count>1:
                yogas.append("rajayogam")
                brief["rajayogam"]=[bh.ownership(bad.aadhibathiyam(self.name).thirikonadhibathi[9]),bh.ownership(bad.aadhibathiyam(self.name).kendhiradhibathi[10])] 
        
        

        print(yogas,brief)
yogas("hari prasath")