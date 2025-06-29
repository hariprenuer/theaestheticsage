import sys
import lifechart as lc
import relationalindex
import positionsdasainvolved
import chart as ch
import csv
from birthdata.prognostics.dasabukthi import dasahelpers as dh

birthdata={'dob': '9-6-2005', 'tob': '14-3', 'latitude': 11.6643, 'longitude': 78.146}
planets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
tomillisecond=31556952000
toms=31104000000
def returnerint(data,option=True):
    data=[int(item) for item in data.split("-")]
    if option:
        return data
    else:
        return [data[2]]+[data[1]]+[data[0]]
def tomilliseconds(data):
    forconv=[1,12,365.2425]
    val=0
    for i in range(0,3):
        val=val+data[i]*tomillisecond/forconv[i]
    return val

def convreturn(dur):
    returner=[]
    value=dur/toms
    for i in range(len(dh.multipliers)):
        returner.append(int(value))
        value=(value-int(value))*dh.multipliers[i]
    return returner

def listadder(ini,data):
    returnit=[ini[index]+data[index] for index in range(len(data))]
    for i in range(1,len(returnit)):
        if returnit[i]>dh.multipliers[i-1]:
            returnit[i]=returnit[i]-dh.multipliers[i-1]
            returnit[i-1]+=1
    return returnit
class lifevalue(lc.lifechartvalue):
    def __init__(self,birthdata):
        super().__init__(birthdata)
        #for 100 years
        dob=returnerint(self.aux.date,False)
        iruppudasa=tomilliseconds(self.aux.iruppudasa)
        age=tomilliseconds([int(item) if len(item)<=4 else int(item[0:2]) for item in str(self.aux.age).split("-")])
        if age>iruppudasa:
            startdate=[int(item) for item in str(self.aux.startdate).split("-")]
            startdate.extend([int(item) for item in str(self.aux.time).split("-")])
            startdate.extend([0 for i in range(7-len(startdate))])
            print(startdate)
        starter=dh.listchanger(dh.listchanger(self.aux.iruppuplanet)[1])
        
        giveout=[]
        count=0
        # with open("C://Users//91770//OneDrive//Desktop//WEBAPP//theaestheticsage//birthdata//prognostics//data","w") as f:
        #     fieldnames=["start","end","value"]
        # print(starter)
        src=startdate
        count=0
        for pl1 in starter:
            for pl2 in dh.listchanger(pl1):
                for pl3 in dh.listchanger(pl2):
                    count+=1
                    src=listadder(src,convreturn(dh.influenceduration([pl1,pl2,pl3])))
                    pq=relationalindex.relationalindex(self.posgrade,[pl1,pl2,pl3]).relationalindex
        print(src)
        print(count)
        print(pq)
lifevalue(birthdata)
