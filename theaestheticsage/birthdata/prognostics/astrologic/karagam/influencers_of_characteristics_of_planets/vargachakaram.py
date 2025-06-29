from birthdata.prognostics.astrologic.bavagam.base import bavahelpers

bavas=["mesham","rishabam","midhunam","kadagam","simmam","kanni","thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
aanrasi=["mesham","midhunam","simmam","thulam","dhanusu","kumbam"]
penrasi=["rishabam","kadagam","kanni","viruchigam","magaram","meenam"]
navamsahelper={"mesham":["chandhiran","guru","kethu"],"simmam":["sevvaai","sukiran","shani"],"dhanusu":["budhan","rahu","suriyan"]}
varkkamdata={}
trimsamsamhelper={"sevvaai":5,"shani":5,"guru":8,"budhan":7,"sukiran":5}
#raasivarkkam
def raasi(data):
    raasi={}
    for classplanets in data:
            raasi[classplanets]=bavas[data[classplanets]["kaalapurushan"]-1]
    return raasi.copy()
def horai(data):
    horai={}
    for classplanets in data:
        entry=data[classplanets]["kaalapurushan"]-1
        vikalvalues=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*108000
        if 0<vikalvalues<=54000 and entry%2==0:
            horai[classplanets]="simmam"
        elif 54000<vikalvalues<=108000 and entry%2==0:
            horai[classplanets]="kadagam"
        if 54000<vikalvalues<=108000 and entry%2!=0:
            horai[classplanets]="simmam"
        elif 0<vikalvalues<=108000 and entry%2!=0:
            horai[classplanets]="kadagam"
    return horai.copy()
#drekaanam
def drekaanam(data):
    drekaanam={}
    for classplanets in data:
        vikalvalues=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*108000
        for i in range(3):
            if (36000*i)<vikalvalues<=(36000*(i+1)):
                entry=data[classplanets]["kaalapurushan"]+(4*i)
                if entry>12:
                    entry=entry-12
                drekaanam[classplanets]=bavas[entry-1]
    return drekaanam.copy()
#sapdhaamsam
def sapdhamasam(data):
    sapdhamasam={}
    for classplanets in data:
        vikalvalues=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*108000
        for i in range(7):
            if (15428.57*i)<vikalvalues<=(15428.57*(i+1)):
                entry=i+data[classplanets]["kaalapurushan"]
                if (data[classplanets]["kaalapurushan"]%2)!=0:
                    if entry>12:
                        entry=entry-12
                    sapdhamasam[classplanets]=bavas[entry-1]
                    break
                elif (data[classplanets]["kaalapurushan"]%2)==0:
                    take=data[classplanets]["kaalapurushan"]+6+i
                    if take>12:
                        take=take-12
                    sapdhamasam[classplanets]=bavas[take-1]
                    break
    return sapdhamasam.copy()
#navamsam
def navamsam(data):
    navamsam={}
    for classplanets in data:
        for nh in navamsahelper:
            if data[classplanets]["chaaram"]["charanadhan"] in navamsahelper[nh]:
                entry=data[classplanets]["chaaram"]["paadham"]+bavas.index(nh)-1
                navamsam[classplanets]=bavas[entry]
                break
    return navamsam.copy()
#dasamsam
def dasamsam(data):
    dasamsam={}
    for classplanets in data:
        vikalvalues=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*108000
        for i in range(10):
            if (10800*i)<vikalvalues<=(10800*(i+1)):
                entry=i+data[classplanets]["kaalapurushan"]
                if bavas[(data[classplanets]["kaalapurushan"]-1)] in aanrasi:
                    if entry>12:
                        entry=entry-12
                    dasamsam[classplanets]=bavas[entry-1]
                    break
                elif bavas[(data[classplanets]["kaalapurushan"]-1)] in penrasi:
                    """
                    ex=int(input("traditional or new(0/1):"))
                    if ex==0:
                        take=data[classplanets]["kaalapurushan"]+6+i
                    if ex==1:
                        take=data[classplanets]["kaalapurushan"]+8+i"""
                    take=data[classplanets]["kaalapurushan"]+8+i
                    if take>12:
                        take=take-int(take/12)*12
                    dasamsam[classplanets]=bavas[take-1]
                    break
    return dasamsam.copy()
#dhuvadasamsam
def dhuvadasamsam(data):
    dhuvadasamsam={}
    for classplanets in data:
        vikalvalues=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*108000
        for i in range(12):
            if (9000*i)<vikalvalues<=(9000*(i+1)):
                entry=i+data[classplanets]["kaalapurushan"]
                if entry>12:
                    entry=entry-12
                dhuvadasamsam[classplanets]=bavas[entry-1]
    return dhuvadasamsam.copy()
#shastiamsam
def shastiamsam(data):
    shastiamsam={}
    for classplanets in data:
        vikalvalues=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*108000
        pos=(int(vikalvalues/1800)+1)%12
        if bavas[(data[classplanets]["kaalapurushan"]-1)] in aanrasi:
            entry=data[classplanets]["kaalapurushan"]+pos
            if entry>12:
                entry=entry-int(entry/12)*12
            shastiamsam[classplanets]=bavas[entry-2]
        if bavas[(data[classplanets]["kaalapurushan"]-1)] in penrasi:
            entry=data[classplanets]["kaalapurushan"]+pos-1
            if entry>12:
                entry=entry-int(entry/12)*12
            shastiamsam[classplanets]=bavas[entry-1] 
    return shastiamsam.copy()
def trimsamsam(data):
    trimsamdic={}
    for classplanets in data:
        degpl=data[classplanets]["paagai"]*3600+data[classplanets]["kalai"]*60+data[classplanets]["vikalai"]-(data[classplanets]["kaalapurushan"]-1)*3600*30
        if (data[classplanets]["kaalapurushan"]%2==0):
            cdrrasi=penrasi
            trimsam={list(trimsamsamhelper.keys())[i]:list(trimsamsamhelper.values())[i]*3600 for i in range(len(trimsamsamhelper)-1,-1,-1)}
        else:
            cdrrasi=aanrasi
            trimsam={list(trimsamsamhelper.keys())[i]:list(trimsamsamhelper.values())[i]*3600 for i in range(len(trimsamsamhelper))}
        amt=0
        for val in trimsam:
            amt=amt+trimsam[val]
            if degpl<=amt:
                amt=0
                for bv in cdrrasi:
                    if bavahelpers.ownership(bv)==val:
                        trimsamdic[classplanets]=bv  
                break
    return trimsamdic.copy()   


