from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import chart

import datetime
plots=["paagai","kalai","vikalai","kaalapurushan","lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
class kocharam:
    def __init__(self,data=None):
        if data is None:
            date=[int(i) for i in str(datetime.datetime.now().date()).split("-")]
            time=[int(float(i)) for i in str(datetime.datetime.now().time()).split(":")]
            if time[1]>60:
                time[1]=time[1]-60
                time[0]+=1
            #print("################# KOCHARAM:",time,sep="\n")
            self.data=chart.positions(str(date[2])+"-"+str(date[1])+"-"+str(date[0]),str(time[0])+"-"+str(time[1])).planetaryposition
        else:
            self.data=chart.positions(str(data["date"][2])+"-"+str(data["date"][1])+"-"+str(data["date"][0]),str(data["time"][0])+"-"+str(data["time"][1])+"-"+str(data["time"][2])).planetaryposition
