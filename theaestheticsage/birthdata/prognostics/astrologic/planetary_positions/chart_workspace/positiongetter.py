from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import positionentry
from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import sqlhelpers
planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","maandhi"]
planetdict={}
plots=["paagai","kalai","vikalai","kaalapurushan","lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","maandhi"]
newdata={}
class horoscopeblueprint:
    global newdata
    def __init__(self,name):
        global newdata
        if sqlhelpers.namechecker(name):
            data=sqlhelpers.dataofname(name)
            data=data[0][1:]
            for i in range(len(planets)):
                planetdict[planets[i]]=data[i]
            newdata=planetdict
            for i in planets:
                planetposition=[]
                for j in newdata[i].split("-"):
                    planetposition.append(int(j))
                if planetposition[2]>=60:
                    planetposition[1]=planetposition[1]+int(planetposition[2]/60)
                    planetposition[2]=planetposition[2]-(int(planetposition[2]/60))*60
                if planetposition[1]>=60:
                    planetposition[0]=planetposition[0]+int(planetposition[1]/60)
                    planetposition[1]=planetposition[1]-(int(planetposition[1]/60))*60
                for m in range(13):
                    if (30*m)<(((planetposition[0]*3600)+(planetposition[1]*60)+planetposition[2])/3600)<=(30*(m+1)): 
                        planetposition.append(m+1)            
                newdata[i]=planetposition
            for i in planets:
                for j in planets:
                    wrtpos=13+newdata[i][3]-newdata[j][3]
                    if wrtpos>12:
                        wrtpos=wrtpos-12
                    newdata[i].append(wrtpos)
            for i in planets:
                dict1={}
                for j in range(len(plots)):
                    dict1[plots[j]]=newdata[i][j]
                newdata[i]=dict1
        else:
            if (input("do you want to newly enter now:")) in ["yes","YES","y","Y"]:
                positionentry.postionentry(name)
            else:
                print("thankyou")
                self.data=None
                self.name=None
        self.data=newdata.copy()
        self.name=name 