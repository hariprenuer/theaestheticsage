import math
bavas=["mesham","rishabam","midhunam","kadagam","simmam","kanni","thulam","viruchigam",
"dhanush","magaram","kumbam","meenam"]
lords={
"kethu":["ashwini","magam","moolam"],
"sukiran":["bharani","pooram","pooradam"],
"suriyan":["kiruthigai","uthiram","uthiradam"],
"chandhiran":["rohini","hastham","thiruvonam"],
"sevvaai":["mirugasirisham","chithirai","avittam"],
"rahu":["thiruvadhirai","swathi","sadhayam"],
"guru":["punarpoosam","visagam","pooratadhi"],
"shani":["poosam","anusham","uthiratadhi"],
"budhan":["ayilyam","kettai","revathi"]}
nakshatras={1:["ashwini","bharani","kiruthigai"],2:["kiruthigai","rohini","mirugasirisham"],
3:["mirugasirisham","thiruvadhirai","punarpoosam"],4:["punarpoosam","poosam","ayilyam"],
5:["magam","pooram","uthiram"],6:["uthiram","hastham","chithirai"],
7:["chithirai","swathi","visagam"],8:["visagam","anusham","kettai"],
9:["moolam","pooradam","uthiradam"],10:["uthiradam","thiruvonam","avittam"],
11:["avittam","sadhayam","pooratadhi"],12:["pooratadhi","uthiratadhi","revathi"]}
ref={1:[4,4,1],2:[3,4,2],3:[2,4,3],4:[1,4,4]}
def charanakshathra(data):   
    test={}
    chardict={}
    for i in data:
        accpos=data[i]["paagai"]*3600+data[i]["kalai"]*60+data[i]["vikalai"]-((data[i]["kaalapurushan"]-1)*108000)
        accpos=int(math.fabs(accpos))
        for j in range(9):
            if (12000)*j<accpos<=(12000)*(j+1):
                cpos=j+1
                posfour=int(data[i]["kaalapurushan"]%4)
                if posfour==0:
                    posfour=4
                sub=ref[(posfour)]
                count=-1
                for k in sub:
                    count=count+1
                    cpos=cpos-k
                    if cpos<=0:
                        chardict["charanakshathra"]=nakshatras[data[i]["kaalapurushan"]][count]
                        if count==1 or count==2:
                            chardict["paadham"]=cpos+k
                            break
                        elif count==0:
                            startcpos=posfour-1
                            if startcpos==0:
                                startcpos=4
                            ned=ref[startcpos][2]+cpos+k
                            if ned>4:
                                ned=ned-4*(int(ned/4))
                            if ned==0:
                                ned=4
                            chardict["paadham"]=ned
                            break
        for m in lords:
            if chardict["charanakshathra"] in lords[m]:
                chardict["charanadhan"]=m
                test=chardict.copy()
                data[i]["chaaram"]=test
    return data
