angisanadhan={"suriyan":["ashwini","bharani","kiruthigai"],"chandhiran":["rohini","mirugasirisham","thiruvadhirai"],
"sevvaai":["punarpoosam","poosam","ayilyam"],"budhan":["magam","pooram","uthiram"],
"guru":["hastham","chithirai","swathi"],"sukiran":["visagam","anusham","kettai"],
"shani":["moolam","pooradam","uthiradam"],"rahu":["thiruvonam","avittam","sadhayam"],
"kethu":["pooratadhi","uthiratadhi","revathi"]}
thunaiangisanadhan=[["sevvaai","sukiran","budhan","chandhiran"],
["suriyan","budhan","sukiran","sevvaai"],
["guru","shani","shani","guru"]]
angisanadharass={}
def angisam(data):
    for classplanets in data:
        for ang in angisanadhan:
            if data[classplanets]["chaaram"]["charanakshathra"] in angisanadhan[ang]:
                #data[classplanets]["angisanadhan"]=ang   
                angisanadhanass=ang 
                #data[classplanets]["thunaiangisanadhan"]=thunaiangisanadhan[angisanadhan[ang].index(data[classplanets]["chaaram"]["charanakshathra"])][data[classplanets]["chaaram"]["paadham"]-1]
                thunaiangisanadhanass=thunaiangisanadhan[angisanadhan[ang].index(data[classplanets]["chaaram"]["charanakshathra"])][data[classplanets]["chaaram"]["paadham"]-1]
                data[classplanets]["angisanadhan"]=angisanadhanass
                data[classplanets]["thunaiangisanadhan"]=thunaiangisanadhanass
                angisanadharass[classplanets]={"angisanadhan":angisanadhanass,"thunaiangisandhan":thunaiangisanadhanass}
                break
    angisanadhargal=angisanadharass.copy()
    return [angisanadhargal,data]