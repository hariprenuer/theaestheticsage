from birthdata.prognostics.astrologic.karagam import auxillarydata as ax
from birthdata.prognostics.astrologic.bavagam.base import bavahelpers
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import postiongrade

import math
#sthana balam
#ucchabalam
kendiram=[1,4,7,10]
panabaram=[2,5,8,11]
abokliyam=[3,6,9,12]
digbala1=["guru","budhan"]
digbala4=["chandhiran","sukiran"]
digbala7=["shani"]
digbala10=["suriyan","sevvaai"]
bavas=["mesham","rishabam","midhunam","kadagam","simmam","kanni","thulam","viruchigam",
"dhanush","magaram","kumbam","meenam"]
benefics=["chandhiran","budhan","sukiran","guru"]
malefics=["shani","suriyan","sevvaai"]
moolatrikonam={"suriyan":["simmam",(0,20)],"chandhiran":["rishabam",(3,27)],"sevvaai":["mesham",(0,12)],
               "budhan":["kanni",(15,25)],"guru":["dhanusu",(0,20)],"sukiran":["thulam",(0,20)],
               "shani":["kumbam",(0,20)]}
planetonly=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
uchapaagai={"suriyan":10,"chandhiran":33,"sevvaai":298,"budhan":165,"guru":95,"sukiran":357,"shani":200}
saptvargabala={"moolatirikonam":45,"aatchi":30,"adhimithru":22.5,"mithru":15,"samam":7.5,"chathru":3.75,"adhichathru":1.875}
malepl=["suriyan","sevvaai"]
femalepl=["chandhiran","sukiran"]
bipl=["budhan","shani"]
def roundoff(val,to):
    if val>to:
        val=val-int(val/to)*to
        return val
    else:
        return val
def sumbala(lstdata):
    returner={}
    for pl in planetonly:
        plamt=0
        for bala in lstdata:
            plamt+=bala[pl]
        returner[pl]=plamt
    return returner
def uchabalam(data):
    degs=[(int(data[pl]["paagai"])+(int(data[pl]["kalai"])+int(data[pl]["vikalai"])/60)/60) for pl in planetonly]
    for i in range(len(degs)):
        if degs[i]>uchapaagai[planetonly[i]]:
            val=(roundoff(uchapaagai[planetonly[i]]+180,360)-degs[i])/3
            if val<0:
                val=math.fabs(val)
                val=val-int(val/60)*60
                val=60-val
            else:
                val=val-int(val/60)*60
            degs[i]=val
        else:
            val=(degs[i]-roundoff(uchapaagai[planetonly[i]]+180,360))/3
            if val<0:
                val=math.fabs(val)
                if degs[i]<uchapaagai[planetonly[i]] and val>60:
                    val=val-int(val/60)*60
                    val=60-val
            else:
                val=val-int(val/60)*60
            degs[i]=val
    return {planetonly[i]:degs[i] for i in range(len(planetonly))}.copy()
def saptavargiyabala(data,relation,raasidata):
    chakaras=["raasi","horai","drekaanam","dhuvadasamsam","navamsam","trimsamsam","sapdhamsam"]
    bala={pl:0 for pl in planetonly}
    for chak in chakaras:
        consch=data[chak]
        for pl in planetonly:
            relpl=bavahelpers.ownership(consch[pl])
            if pl==relpl and chak=="raasi":
                degpl=(int(raasidata[pl]["paagai"])-(raasidata[pl]["kaalapurushan"]-1)*30+(int(raasidata[pl]["kalai"])+int(raasidata[pl]["vikalai"])/60)/60)
                if int(degpl) in range(moolatrikonam[pl][1][0],moolatrikonam[pl][1][1]):
                    bala[pl]=bala[pl]+saptvargabala["moolatirikonam"]  
            if pl==relpl:
                bala[pl]=bala[pl]+saptvargabala["aatchi"]
            else:
                for typrel in relation[pl]:
                    if relpl in relation[pl][typrel]:
                        bala[pl]=bala[pl]+saptvargabala[typrel]    
    return bala
def ojayugmabala(chakra):
    ojabala={}
    for pl in planetonly:
        plamt=0
        for ch in ["raasi","navamsam"]:
            if pl in ["chandhiran","sukiran"]:
                if (bavas.index(chakra[ch][pl])+1)%2==0:
                    plamt+=15
            else:
                if (bavas.index(chakra[ch][pl])+1)%2!=0:
                    plamt+=15
        ojabala[pl]=plamt
    return ojabala.copy()
def kendirabala(raasidata):
    kendirabala={}
    for pl in planetonly:
        plamt=0
        if raasidata[pl]["lagnam"] in kendiram:
            plamt+=60
        if raasidata[pl]["lagnam"] in panabaram:
            plamt+=30
        if raasidata[pl]["lagnam"] in abokliyam:
            plamt+=15
        kendirabala[pl]=plamt
    return kendirabala
def drekaanabala(raasidata):
    drekaanabala={}
    for pl in planetonly:
        plamt=0
        degs=int(raasidata[pl]["paagai"])*3600-(raasidata[pl]["kaalapurushan"]-1)*30*3600+(int(raasidata[pl]["kalai"])*60+int(raasidata[pl]["vikalai"]))
        for i in range(3):
            if 36000*i<degs<=36000*(i+1):
                if i==0 and pl in malepl:
                    plamt=15
                elif i==1 and pl in bipl:
                    plamt=15
                elif i==2 and pl in femalepl:
                    plamt=15 
        drekaanabala[pl]=plamt
    return drekaanabala
def dighelper(deg,wrt):
    res=math.fabs(deg-wrt)
    if res>180*3600:
        res=360*3600-res
    return 180*3600-math.fabs(deg-wrt)
def digbala(raasidata):
    digbala={}
    lagna=int(raasidata["lagnam"]["paagai"])*3600+(int(raasidata["lagnam"]["kalai"])*60+int(raasidata["lagnam"]["vikalai"]))
    fourth=roundoff(lagna+30*3*3600,3600*30*12)
    seventh=roundoff(lagna+30*6*3600,3600*30*12)
    tenth=roundoff(lagna+30*9*3600,3600*30*12)
    for pl in planetonly:
        degpl=int(raasidata[pl]["paagai"])*3600+(int(raasidata[pl]["kalai"])*60+int(raasidata[pl]["vikalai"]))
        if pl in digbala10:
            digbala[pl]=math.fabs(dighelper(degpl,tenth))/(3*3600)
        if pl in digbala1:
            digbala[pl]=math.fabs(dighelper(degpl,lagna))/(3*3600)
        if pl in digbala4:
            digbala[pl]=math.fabs(dighelper(degpl,fourth))/(3*3600)
        if pl in digbala7:
            digbala[pl]=math.fabs(dighelper(degpl,seventh))/(3*3600)
    return digbala
def pakshabala(raasidata):
    pakshabala={}
    sunpos=int(raasidata["suriyan"]["paagai"])*3600+(int(raasidata["suriyan"]["kalai"])*60+int(raasidata["suriyan"]["vikalai"]))
    moonpos=int(raasidata["chandhiran"]["paagai"])*3600+(int(raasidata["chandhiran"]["kalai"])*60+int(raasidata["chandhiran"]["vikalai"]))
    diff=math.fabs(sunpos-moonpos)
    if diff>648000:
        diff=diff-int(diff/648000)*648000
    paksha=math.fabs(diff/(3*3600))
    for pl in planetonly:
        if pl in ["chandhiran","budhan"]:
            pakshabala[pl]=paksha*2
            continue
        if pl in benefics:
            pakshabala[pl]=paksha
        if pl in malefics:
            pakshabala[pl]=60-paksha
    return pakshabala
class shadbalam:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        aux=ax.auxillarydata(self.birthdata)
        self.data=aux.data
        self.uchabalam=uchabalam(self.data)
        self.positongrade=postiongrade.positionalrelation(self.data).positionalrelation
        self.chakaram=aux.varkkam
        self.saptavargabala=saptavargiyabala(self.chakaram,self.positongrade,self.data)
        self.ojayugmabala=ojayugmabala(self.chakaram)
        self.kendirabala=kendirabala(self.data)
        self.drekaana=drekaanabala(self.data)
        self.sthanabalam=sumbala([self.uchabalam,self.saptavargabala,self.kendirabala,self.drekaana,self.ojayugmabala])
        self.digbala=digbala(self.data)
        self.pakshabala=pakshabala(self.data)
        self.total=[val/60 for val in list(sumbala([self.sthanabalam,self.digbala,self.pakshabala]).values())]
        print(self.total)
shadbalam("hari prasath")
#risetrans