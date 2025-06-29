from birthdata.prognostics.astrologic.planetary_positions.SiderealAstro import birthchart as bc
from birthdata.prognostics.astrologic.planetary_positions.panchangam.baavam import baavam
from birthdata.prognostics.astrologic.karagam.influencers_of_characteristics_of_planets import nakshatrachaaram
import datetime
from birthdata.prognostics.astrologic.planetary_positions.PyHora_main.hora.horoscope.dhasa import vimsottari

plots=["paagai","kalai","vikalai","kaalapurushan","lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
dasaduration={"suriyan":6,"chandhiran":10,"sevvaai":7,"rahu":18,"guru":16,"shani":19,"budhan":17,"kethu":7,"sukiran":20}
dividings=[12,30,24,60,60,1000]
def toreadable(datadic,opt=False):
	planetdict={}
	data=list(datadic.values())
	for i in range(len(planets)):
		planetdict[planets[i]]=data[i]
	newdata=planetdict.copy()
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
	if opt:
		return newdata.copy()
	return nakshatrachaaram.charanakshathra(newdata.copy()).copy()
def iruppudasa(moonspeed,moondata):
	iruppudasa=[]
	speedpervikalai=24/(moonspeed*3600)
	#print("speedpervikalai:",speedpervikalai)
	ttlspdvik=speedpervikalai*48000
	iruppuown=dasaduration[moondata["chaaram"]["charanadhan"]]
	#print(moondata)
	moonpos=moondata["paagai"]*3600+moondata["kalai"]*60+moondata["vikalai"]
	comp=((48000-((moonpos-int(moonpos/12000)*12000)+(moondata["chaaram"]["paadham"]-1)*12000))/48000)*iruppuown
	for i in dividings:
		iruppudasa.append(int(comp))
		comp=(comp-int(comp))*i
	#print("!!!!!!!!!!!!!!!!!!",iruppudasa)
	return (moonspeed,iruppudasa)
def converter(pos):
	data=""
	count=0
	while True:
		data=data+"-"+str(int(str(pos).split(".")[0]))
		pos=pos-int(pos)
		pos=pos*60
		count=count+1
		if pos==0 or count==3:
			return data[1:]
		
class positions:
	planetaries=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
	tamilspped=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
	inthere=["lagnam","Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Rahu","Kethu"]
	forspeed=["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn"]
	def __init__(self,date="9-6-2005",time="14-3",lat=11.6643,long=78.1460,timezone=+5.5,option=True):
		self.planetpos=vimsottari.dasabukthi(date,time,lat,long,timezone)
		self.startdate=self.planetpos.startdate
		self.lat=lat
		self.long=long
		if not option:
			if type(date)==str:
				date=date.split("-")
				date=[int(i) for i in date]
			if type(time)==str:
				time=time.split("-")
				time=[int(i) for i in time]
			if time[0]>5 or (time[0]==5 and time[1]>30):
				time[0]=time[0]-5
				if time[1]<30:
					time[1]=time[1]+60
					time[0]=time[0]-1
				time[1]=time[1]-29
			self.time=time
			self.date=date
			self.object=bc.Birthchart("narayanan",datetime.datetime(self.date[2],self.date[1],self.date[0],self.time[0],self.time[1],38,55),self.lat,self.long)
			self.infloat=self.object.planetaryposition
			bavagam=self.object.angles
			bavadic={}
			posforconv={}
			bavadic["lagnaspudam"]=converter(bavagam["Ascendant"][0])
			bavadic["dasamalagnaspudam"]=converter(bavagam["Midheaven"][0])
			for pl in self.inthere:
				posforconv[self.planetaries[self.inthere.index(pl)]]=converter(self.infloat[pl])
			self.speed={ self.tamilspped[i]:self.object.planetspeed[self.forspeed[i]] for i in range(len(self.forspeed))}
			planetaryposition=posforconv.copy()
			self.spudam=bavadic.copy()
			self.baavagachakaram=baavam.bavagachakaram(self.spudam).bavagacharam
			self.iruppudasa=iruppudasa(self.speed["chandhiran"],toreadable(planetaryposition)["chandhiran"])

######################################################################################################################################
		
		planetaryposition={pl:converter(self.planetpos.planetaryposition[pl]) for pl in self.planetaries}.copy()
		self.iruppudasa=self.planetpos.iruppudasa
		self.planetaryposition=toreadable(planetaryposition,True)
		self.spudam={"lagnaspudam":planetaryposition["lagnam"]}
		self.baavagachakaram=baavam.bavagachakaram(self.spudam).bavagacharam
		self.iruppuplanet=toreadable(planetaryposition)["chandhiran"]["chaaram"]["charanadhan"]
