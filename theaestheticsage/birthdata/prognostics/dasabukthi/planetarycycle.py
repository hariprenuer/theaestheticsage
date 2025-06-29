from birthdata.prognostics.dasabukthi import dasahelpers as dh
import datetime as dt
from birthdata.prognostics.dasabukthi import iruppudasaentry
from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import sqlhelpers

dasaplanetaries=['suriyan','chandhiran','sevvaai','rahu','guru','shani','budhan','kethu','sukiran']
dasaduration={"suriyan":6,"chandhiran":10,"sevvaai":7,"rahu":18,"guru":16,"shani":19,"budhan":17,"kethu":7,"sukiran":20}


#---------------------------------------------------------------------------------------------------------
# print(type(sqlhelpers.dasadata(name)[0][3]),sqlhelpers.dasadata(name)[0][4])
# self.age=dh.agecal(sqlhelpers.dasadata(name)[0][3],sqlhelpers.dasadata(name)[0][4])
# self.iruppu=dh.listtodate(dh.dasahelper(sqlhelpers.dasadata(name)[0][2]))
#  # iruppuplanet=sqlhelpers.dasadata(name)[0][1]
#---------------------------------------------------------------------------------------------------------


def recall(name):
    return planetaryinfluencers(name)
def canipass(agestr,timestr,iruppu,iruppupl):
    age=dh.agecal(agestr,timestr)
    iruppu=dh.listtodate(dh.dasahelper(iruppu))
    return [age,iruppu,iruppupl]
class planetaryinfluencers:
    order=10
    def __init__(self,data=None): 
            # if sqlhelpers.dasachecker(data):
            if False:
                self.age,self.iruppu,self.iruppuplanet=canipass(sqlhelpers.dasadata(data)[0][3],sqlhelpers.dasadata(data)[0][4],sqlhelpers.dasadata(data)[0][2],sqlhelpers.dasadata(data)[0][1])
            else:
                self.age,self.iruppu,self.iruppuplanet=canipass(data["dob"],data["tob"],data["iruppu"],data["iruppuplanet"])
            # print(data)
            # print("age:",self.age)
            datalist=[]
            if type(self.age)==type(dt.datetime(2022,6,9)) and type(self.iruppu)==type(dt.datetime(2022,6,9)):
                if self.age<self.iruppu:
                    self.planetaryinfluencers=[self.iruppuplanet]
                else:
                    ind=dasaplanetaries.index(self.iruppuplanet)
                    if ind==len(dasaplanetaries):
                        ind=-1
                    if ind==len(dasaplanetaries)-1:
                        ind=-1
                    amt=0
                    remfactor=self.age-self.iruppu
                    days=dh.actualdiff(dh.dasahelper(str(self.age.date())),dh.dasahelper(str(self.iruppu.date())))
                    sep=str(remfactor).replace(" ","").replace("days","").split(",")[1].split(":")
                    remfactor=days*86400000+int(sep[0])*3600000+int(sep[1])*60000+int(sep[2].split(".")[0])*1000
                    datalist=[]
                    #print("age after iruppudasa in milliseconds:",remfactor)
                    for pl in dh.listchanger(dasaplanetaries[ind+1]):
                        amt=amt+dh.influenceduration([pl])
                        if amt>remfactor:
                            datalist.append(pl)
                            amt=amt-dh.influenceduration([pl])
                            break
                    for i in range(self.order-1):
                        datalist.append(None)
                    for count in range(1,self.order):
                        notinclude=0
                        for pl in dh.listchanger(datalist[count-1]):
                            datalist[count]=pl
                            amt=amt+dh.influenceduration(datalist)
                            if amt>remfactor:
                                datalist[count]=(pl)
                                amt=amt-dh.influenceduration(datalist)
                                #print(f"order:{count}",pl)
                                break
                            else:
                                notinclude+=1
                                if notinclude==9:
                                    print("WARNING not included!",datalist[count-1])
                        if notinclude==9:
                            print("WARNING not included!",datalist[count-1])
                    self.planetaryinfluencers=datalist  
        # else:
        #     if data.isalpha():
        #         iruppudasaentry.dasaentry(data)
        #         #recall(name)
    @classmethod
    def changeorder(cls,order):
        cls.order=order
# print(planetaryinfluencers({"dob":"9-6-2005","tob":"14-03","iruppu":"13-6-2","iruppuplanet":"guru"}))