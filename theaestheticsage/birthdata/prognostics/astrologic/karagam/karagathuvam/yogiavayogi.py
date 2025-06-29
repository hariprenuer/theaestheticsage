from birthdata.prognostics.astrologic.karagam import auxillarydata as ax

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
dictavayogi={"chandhiran":"budhan","budhan":"sevvaai","ketu":"rahu",
                 "suriyan":"shani","sevvaai":"kethu","sukiran":"guru",
                 "guru":"suriyan","shani":"chandhiran","rahu":"sukiran"}
nakshatras=["ashwini","bharani","kiruthigai","rohini","mirugasirisham","thiruvadhirai","punarpoosam","poosam",
            "ayilyam","magam","pooram","uthiram","hastham","chithirai","swathi","visagam","anusham","kettai",
            "moolam","pooradam","uthiradam","thiruvonam","avittam","sadhayam","pooratadhi","uthiratadhi",
            "revathi"]
class yogiavayogi:
    def __init__(self,birthdata):
        self.birthdata=birthdata
        self.data=ax.auxillarydata(self.birthdata).data
        suryapos=self.data["suriyan"]["paagai"]*3600+self.data["suriyan"]["kalai"]*60+self.data["suriyan"]["vikalai"]        
        chandhirapos=self.data["chandhiran"]["paagai"]*3600+self.data["chandhiran"]["kalai"]*60+self.data["chandhiran"]["vikalai"] 
        closer=suryapos+chandhirapos+93*3600
        if closer>(360*3600):
            closer=closer-(3600*360)*int(closer/(360*3600))
        for ord in range(0,27):
            if (ord*48000)<closer<=(ord+1)*48000:
                yoginakshatra=nakshatras[ord]
                break
        for pl in lords:
            if yoginakshatra in lords[pl]:
                yogi=pl
                avayogi=dictavayogi[yogi]
                break
        self.yogi=yogi
        self.avayogi=avayogi