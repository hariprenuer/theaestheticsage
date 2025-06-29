from birthdata.prognostics.astrologic.karagam.characteristics_of_planets.basic import basic

import math
planetonly=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
class degreeofcloseness(basic):
    def __init__(self,name,data):
        super().__init__(name)
        self.subathuvam=data
        self.positions=self.aux.data
        degreeofcloseness={}
        decision=True
        for pl in planetonly:
            degreeofcloseness[pl]=self.subathuvam[pl]
        entries=[]
        for pl1 in planetonly:
            for pl2 in planetonly:
                if pl1!=pl2:
                    for ex in range(len(entries)):
                        if [pl1,pl2]==entries[ex] or [pl2,pl1]==entries[ex]:
                            decision=False
                    if decision==True:
                        planetpos1=self.positions[pl1]["paagai"]*3600+self.positions[pl1]["kalai"]*60+self.positions[pl1]["vikalai"]#-(self.positions[pl1]["kaalapurushan"]-1)*108000
                        planetpos2=self.positions[pl2]["paagai"]*3600+self.positions[pl2]["kalai"]*60+self.positions[pl2]["vikalai"]#-(self.positions[pl2]["kaalapurushan"]-1)*108000
                        diff=math.fabs(planetpos1-planetpos2)
                        if diff<108000:
                            entries.append([pl1,pl2])
                            degreeofcloseness[pl1]=degreeofcloseness[pl1]+self.subathuvam[pl2]*((108000-diff)/108000)
                            degreeofcloseness[pl2]=degreeofcloseness[pl2]+self.subathuvam[pl1]*((108000-diff)/108000)
                    else:
                        degreeofcloseness[pl1]=degreeofcloseness[pl1]
                        degreeofcloseness[pl2]=degreeofcloseness[pl2]
                    decision=True
        if degreeofcloseness["budhan"]==0:
            degreeofcloseness["budhan"]=70
        self.closeness=degreeofcloseness.copy()