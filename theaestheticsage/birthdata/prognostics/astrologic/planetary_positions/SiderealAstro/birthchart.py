# coding: utf-8
# from globalinit import *
from birthdata.prognostics.astrologic.planetary_positions.SiderealAstro.globalinit import *


class Birthchart:

	def __init__(self, name: str, dt: datetime, lat: float, lng: float, hsys='W', sidereal=True):
		""" Birthchart constructor: name (string), datetime object (UT), latitude, longitude, 
			house system for house cusps, sidereal mode (default) """
		self.name = name
		self.birthTime = dt
		self.lat, self.lng, self.sid = lat, lng, sidereal
		finalpos={}
		timedifftup = dt.timetuple()[:6] #year, month, day, hour, minute, second
		jt = swe.utc_to_jd(*timedifftup, swe.GREG_CAL) #convert to Julian time
		
		#planetpos = list(swe.calc_ut(jt[1], i, flag=int(sidereal)*swe.FLG_SIDEREAL+swe.FLG_SPEED) for i in range(len(PLANETKEY)))
		planetpos = list(swe.calc_ut(jt[1], i, (int(sidereal)*swe.FLG_SIDEREAL+swe.FLG_SPEED)) for i in range(len(PLANETKEY)))
		
		#nodepos = [swe.nod_aps_ut(jt[1], i, flag=int(sidereal)*swe.FLG_SIDEREAL) for i in range(len(NODES))]
		nodepos = [swe.nod_aps_ut(jt[1], i, (int(sidereal)*swe.FLG_SIDEREAL)) for i in range(len(NODES))]
		
		speed={PLANETKEY[i]:planetpos[i][0][3] for i in range(len(PLANETKEY))}
		#print("#####@@@@@",speed)
		self.planetspeed=speed.copy()
		
		#self.planets = {planetName: (planetpos[i], swe.split_deg(planetpos[i][0],8)) for i, planetName in enumerate(PLANETKEY)}
		self.planets = {planetName: (planetpos[i], swe.split_deg(planetpos[i][0][0],8)) for i, planetName in enumerate(PLANETKEY)}
		
		#cuspdegs, angledegs = swe.houses_ex(jt[1], lat, lng, hsys=hsys.encode(), flag=int(sidereal)*swe.FLG_SIDEREAL)
		cuspdegs, angledegs = swe.houses_ex(jt[1], lat, lng, hsys.encode(), (int(sidereal)*swe.FLG_SIDEREAL))
		
		self.houseCusps = tuple((cuspdegs[i], swe.split_deg(cuspdegs[i],8)) for i in range(len(cuspdegs)))
		self.angles = {angleName: (angledegs[i], swe.split_deg(angledegs[i],8)) for i, angleName in enumerate(ANGLEKEY)}
		#self.sect = 'Day' if (self.angles['Ascendant'][0] - self.planets['Sun'][0][0]) % 360 <= 180 else 'Night'
		self.sect = 'Day' if (self.angles['Ascendant'][0] - self.planets['Sun'][0][0][0]) % 360 <= 180 else 'Night'
		self.lots = {}
		self.ZR = {}
		self.nodepos=nodepos.copy()
		finalpos["lagnam"]=self.angles["Ascendant"][0]
		for pl in PLANETKEY:
			finalpos[pl]=self.planets[pl][0][0][0]
		finalpos["Rahu"]=nodepos[1][0][0]
		finalpos["Kethu"]=nodepos[1][1][0]
		self.planetaryposition=finalpos.copy()


	def calculateLots(self):
		""" Calculates Hellenistic lots. Sources: Carmen Astrologicum trans. Ben Dykes, Hellenistic Astrology by Chris Brennan """
		asc = self.angles['Ascendant'][0]
		print(self.planets)
		self.lots = { 'Fortune': (asc + self.planets['Moon'][0][0][0] - self.planets['Sun'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Sun'][0][0][0] - self.planets['Moon'][0][0][0]) % 360,
					'Spirit': (asc + self.planets['Sun'][0][0][0] - self.planets['Moon'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Moon'][0][0][0]- self.planets['Sun'][0][0][0]) % 360,

					# Father: use alternate calculation (for either sect) if Saturn is under the beams
					'Father': (asc + self.planets['Saturn'][0][0][0] - self.planets['Sun'][0][0][0]) % 360 if self.sect == 'Day' \
								and abs(self.planets['Sun'][0][0][0] - self.planets['Saturn'][0][0][0]) > 15.0 \
								else (asc + self.planets['Jupiter'][0][0][0] - self.planets['Mars'][0][0][0]) % 360 if abs(self.planets['Sun'][0][0][0] - self.planets['Saturn'][0][0][0]) <= 15.0 \
								else (asc + self.planets['Sun'][0][0][0] - self.planets['Saturn'][0][0][0]) % 360,
					'Mother': (asc + self.planets['Moon'][0][0][0] - self.planets['Venus'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Venus'][0][0][0] - self.planets['Moon'][0][0][0]) % 360,
					'Siblings_Valens': (asc + self.planets['Jupiter'][0][0][0] - self.planets['Saturn'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Saturn'][0][0][0] - self.planets['Jupiter'][0][0][0]) % 360,
					'Siblings_Paulus': (asc + self.planets['Jupiter'][0][0][0] - self.planets['Saturn'][0][0][0]) % 360,

					'Marriage_Firmicus': (asc + self.planets['Venus'][0][0][0] - self.planets['Saturn'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Saturn'][0][0][0] - self.planets['Venus'][0][0][0]) % 360,
					'Husband_Firmicus': (asc + self.planets['Venus'][0][0][0] - self.planets['Mars'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Mars'][0][0][0] - self.planets['Venus'][0][0][0]) % 360,
					'Marriage_M_Paulus': (asc + self.planets['Venus'][0][0][0] - self.planets['Saturn'][0][0][0]) % 360,
					'Marriage_F_Paulus': (asc + self.planets['Saturn'][0][0][0] - self.planets['Venus'][0][0][0]) % 360,
					'Marriage_Valens': (asc + self.planets['Venus'][0][0][0] - self.planets['Jupiter'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Jupiter'][0][0][0] - self.planets['Venus'][0][0][0]) % 360,
					'Marriage_M_Valens': (asc + self.planets['Venus'][0][0][0] - self.planets['Sun'][0][0][0]) % 360,
					'Marriage_F_Valens': (asc + self.planets['Mars'][0][0][0] - self.planets['Moon'][0][0][0]) % 360,
					'Pleasure_and_wedding': (asc + self.houseCusps[6][0] - self.planets['Venus'][0][0][0]) % 360,
					'Wedding_M': (self.planets['Venus'][0][0][0] + self.planets['Moon'][0][0][0] - self.planets['Sun'][0][0][0]) % 360,
					'Wedding_F': (self.planets['Mars'][0][0][0] + self.planets['Moon'][0][0][0] - self.planets['Sun'][0][0][0]) % 360,
					
					'Children_Paulus': (asc + self.planets['Saturn'][0][0][0] - self.planets['Jupiter'][0][0][0]) % 360, # not reversed by night (Brennan)
					'Children_Valens_M': (asc + self.planets['Mercury'][0][0][0] - self.planets['Jupiter'][0][0][0]) % 360,
					'Children_Valens_F': (asc + self.planets['Venus'][0][0][0] - self.planets['Jupiter'][0][0][0]) % 360,

					'Friendship': (asc + self.planets['Mercury'][0][0][0] - self.planets['Moon'][0][0][0]) % 360,
					# Exaltation: from Sun to Aries = 0.0 - Sun; from Moon to Taurus = 30.0 - Moon
					'Exaltation': (asc - self.planets['Sun'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + 30.0 - self.planets['Moon'][0][0][0]) % 360
					 }
		self.lots['Foundation'] = (asc + min(abs(self.lots['Spirit'] - self.lots['Fortune']), abs(self.lots['Fortune'] - self.lots['Spirit']))) % 360
		self.lots['Eros_Paulus'] = (asc + self.planets['Venus'][0][0][0] - self.lots['Spirit']) % 360 if self.sect == 'Day' \
							else (asc + self.lots['Spirit'] - self.planets['Venus'][0][0][0]) % 360
		self.lots['Eros_Valens'] = (asc + self.lots['Spirit'] - self.lots['Fortune']) % 360 if self.sect == 'Day' \
							else (asc + self.lots['Fortune'] - self.lots['Spirit']) % 360
		self.lots['Necessity_Paulus'] = (asc + self.lots['Fortune'] - self.planets['Mercury'][0][0][0]) % 360 if self.sect == 'Day' \
							else (asc + self.planets['Mercury'][0][0][0] - self.lots['Fortune']) % 360
		self.lots['Necessity_Valens'] = (asc + self.lots['Fortune'] - self.lots['Spirit']) % 360 if self.sect == 'Day' \
							else (asc + self.lots['Spirit'] - self.lots['Fortune']) % 360
		self.lots['Courage'] = (asc + self.lots['Fortune'] - self.planets['Mars'][0][0][0]) % 360 if self.sect == 'Day' \
							else (asc + self.planets['Mars'][0][0][0] - self.lots['Fortune']) % 360
		self.lots['Victory'] = (asc + self.planets['Jupiter'][0][0][0] - self.lots['Spirit']) % 360 if self.sect == 'Day' \
							else (asc + self.lots['Spirit'] - self.planets['Jupiter'][0][0][0]) % 360
		self.lots['Nemesis'] = (asc + self.lots['Fortune'] - self.planets['Saturn'][0][0][0]) % 360 if self.sect == 'Day' \
							else (asc + self.planets['Saturn'][0][0][0] - self.lots['Fortune']) % 360
		house2sign = SIGNKEY[swe.split_deg(self.houseCusps[1][0],8)[4]]
		house2ruler = RULERS[house2sign]
		self.lots['Assets'] = (asc + self.houseCusps[1][0] - self.planets[house2ruler][0][0][0]) % 360
		self.lots['Death'] = (self.planets['Saturn'][0][0][0] + self.houseCusps[7][0] - self.planets['Moon'][0][0][0]) % 360
		self.lots['Illness'] = (asc + self.planets['Mars'][0][0][0] - self.planets['Saturn'][0][0][0]) % 360 if self.sect == 'Day' \
								else (asc + self.planets['Saturn'][0][0][0] - self.planets['Mars'][0][0][0]) % 360

		for lot in self.lots:
			split_deg = swe.split_deg(self.lots[lot],8)
			self.lots[lot] = { 'exact': self.lots[lot], 
								'deg': split_deg[0],
								'min': split_deg[1],
								'sec': split_deg[2],
								'sign': SIGNKEY[split_deg[4]] }
		

	def calculateZR(self, lotname: str, maxage=100, valens_rule=True):
		""" Calculates all zodiacal releasing periods and subperiods (L1 = longest to L4 = shortest)
			for a particular lot from birth to maxage """
		if not self.lots:
			self.calculateLots()
		enddt = self.birthTime + timedelta(days=365.25*maxage)
		l1_start = self.birthTime
		l1_sign = self.lots[lotname]['sign']
		# Valens' rule that if Spirit & Fortune fall in the same sign, start releasing from Spirit from the following sign
		if valens_rule and lotname == 'Spirit' and self.lots[lotname]['sign'] == self.lots['Fortune']['sign']:
			l1_sign = SIGNKEY[(SIGNKEY.index(l1_sign)+1) % 12]
		l1 = []
		l2 = []
		l3 = []
		l4 = []
		note1 = ""
		while l1_start < enddt:
			l1_period = ZR_PERIODS[l1_sign]
			l1.append((l1_start, l1_sign, note1))
			l2_start = l1_start
			l1_start += timedelta(days=360*l1_period)
			l2_startsign = l2_sign = l1_sign
			lb2 = False
			note2 = ""
			while l2_start < l1_start and l2_start < enddt:
				l2_period = ZR_PERIODS[l2_sign]
				l2.append((l2_start, l2_sign, note2))
				note2 = ""
				l3_start = l2_start
				l2_start += timedelta(days=30*l2_period)
				l3_startsign = l3_sign = l2_sign
				lb3 = False
				note3 = ""
				while l3_start < l2_start and l3_start < l1_start and l3_start < enddt:
					l3_period = ZR_PERIODS[l3_sign]
					l3.append((l3_start, l3_sign, note3))
					note3 = ""
					l4_start = l3_start
					l3_start += timedelta(days=2.5*l3_period)
					l4_startsign = l4_sign = l3_sign
					lb4 = False
					note4 = ""
					while l4_start < l3_start and l4_start < l2_start and l4_start < l1_start and l4_start < enddt:
						l4_period = ZR_PERIODS[l4_sign]
						l4.append((l4_start, l4_sign, note4))
						note4 = ""
						l4_start += timedelta(hours=5*l4_period)
						l4_sign = SIGNKEY[(SIGNKEY.index(l4_sign)+1) % 12]
						if l4_sign == l4_startsign and not lb4:	#loosing of the bond
							l4_sign = SIGNKEY[(SIGNKEY.index(l4_sign)+6) % 12]
							lb4 = True
							note4 = "LB"
					l3_sign = SIGNKEY[(SIGNKEY.index(l3_sign)+1) % 12]
					if l3_sign == l3_startsign and not lb3:	#loosing of the bond
						l3_sign = SIGNKEY[(SIGNKEY.index(l3_sign)+6) % 12]
						lb3 = True
						note3 = "LB"
				l2_sign = SIGNKEY[(SIGNKEY.index(l2_sign)+1) % 12]
				if l2_sign == l2_startsign and not lb2:	#loosing of the bond
					l2_sign = SIGNKEY[(SIGNKEY.index(l2_sign)+6) % 12]
					lb2 = True
					note2 = "LB"
			l1_sign = SIGNKEY[(SIGNKEY.index(l1_sign)+1) % 12]
		self.ZR[lotname] = {'L1': l1, 'L2': l2, 'L3': l3, 'L4': l4}