# import sys
from birthdata.prognostics.predictions.generalchart import lifechart
hariprasath={"dob":"9-6-2005","tob":"14-3","latitude":11.6643,"longitude":78.1460}
format=["latitude","longitude","date","month","year","hour","minutes"]
actualformat=["dob","tob","latitude","longitude"]
class horoscope:
    def __init__(self,detials=hariprasath):
        if type(detials)==list:
            detials=detials[0]
        if "date" in detials:
            datadic={}
            datadic["dob"]=str(detials["date"])+"-"+str(detials["month"])+"-"+str(detials["year"])
            datadic["tob"]=str(detials["hour"])+"-"+str(detials["minutes"])
            datadic["latitude"]=float(str(detials["latitude"]).replace("Decimal","").replace("(","").replace(")",""))
            datadic["longitude"]=float(str(detials["longitude"]).replace("Decimal","").replace("(","").replace(")",""))
            self.detials=datadic
        else:
            self.detials=detials
        print({'dob':'9-6-2005','tob':'14-3','latitude':11.6643,'longitude':78.146}==self.detials and self.detials==hariprasath)
        self.horoscope=lifechart.lifechartvalue(self.detials).horoscope