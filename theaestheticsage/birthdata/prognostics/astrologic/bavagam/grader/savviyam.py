from birthdata.prognostics.astrologic.karagam import auxillarydata as ax

subagrahas=["guru","sukiran","chandhiran","budhan"]
planetch=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
aanrasi=["mesham","midhunam","simmam","thulam","dhanusu","kumbam"]
penrasi=["rishabam","kadagam","kanni","viruchigam","magaram","meenam"]
class savviyam:
    def __init__(self,name):
        self.name=name
        self.data=ax.auxillarydata(self.name).data
        suriyapaagai=self.data["suriyan"]["paagai"]+180
        if suriyapaagai>360:
            suriyapaagai=suriyapaagai-360*int(suriyapaagai/360)
        suryapos=suriyapaagai*3600+self.data["suriyan"]["kalai"]*60+self.data["suriyan"]["vikalai"]
        chandhirapos=self.data["chandhiran"]["paagai"]*3600+self.data["chandhiran"]["kalai"]*60+self.data["chandhiran"]["vikalai"]
        if chandhirapos<=suryapos:
            self.paksham="sukla-paksham"
        else:
            self.paksham="krishna-paksham"
        print(self.paksham)
        if self.paksham=="sukla-paksham":
            concern=aanrasi
            nonconcern=penrasi
        else:
            nonconcern=aanrasi
            concern=penrasi
        count=0
        elcount=0
        for spl in planetch:
            if spl in subagrahas:
                if bavaslist[self.data[spl]["kaalapurushan"]-1] in concern:
                    count=count+1
                if bavaslist[self.data[spl]["kaalapurushan"]-1] in nonconcern:
                    elcount=elcount+1
            else:
                if bavaslist[self.data[spl]["kaalapurushan"]-1] in nonconcern:
                    elcount=elcount+1
        if count==4 and elcount==len(planetch)-count:
            self.savviyamstatus="savviyam"
            self.grade="A"
        elif count==3 and elcount==len(planetch)-count:
            self.savviyamstatus="abasavviyam"
            self.grade="B"
        elif count==2 and elcount==len(planetch)-count:
            self.savviyamstatus="savviyabasavviyam"
            self.grade="C"
        else:
            self.savviyamstatus="abasavviyabasavviyam"
            self.grade="D"
        print(self.savviyamstatus)
        print(self.grade)