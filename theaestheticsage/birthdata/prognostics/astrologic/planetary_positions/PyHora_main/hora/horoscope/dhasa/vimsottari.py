# -*- coding: UTF-8 -*-

# vimsottari.py -- routines for computing time periods of vimsottari dhasa bhukthi
#
# Copyright by Sundar Sundaresan, USA. carnaticmusicguru2015@comcast.net
# Downloaded from https://github.com/naturalstupid
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Calculates Vimshottari (=120) Dasha-bhukthi-antara-sukshma-prana
"""
import datetime
from collections import OrderedDict as Dict
from birthdata.prognostics.astrologic.planetary_positions.PyHora_main.hora.horoscope.dhasa.modules import *
import swisseph as swe
from birthdata.prognostics.astrologic.planetary_positions.PyHora_main.hora.panchanga import panchanga  # if __init__.py files are present

sidereal_year = const.sidereal_year  # some say 360 days, others 365.25 or 365.2563 etc
vimsottari_adhipati = lambda nak: const.vimsottari_adhipati_list[nak % (len(const.vimsottari_adhipati_list))]

indices={"L":"lagnam",0:"suriyan",1:"chandhiran",2:"sevvaai",3:"budhan",4:"guru",5:"sukiran",6:"shani",7:"rahu",8:"kethu"}

### --- Vimoshatari functions
def vimsottari_next_adhipati(lord):
    """Returns next guy after `lord` in the adhipati_list"""
    current = const.vimsottari_adhipati_list.index(lord)
    next_index = (current + 1) % len(const.vimsottari_adhipati_list)
    return const.vimsottari_adhipati_list[next_index]

def vimsottari_dasha_start_date(jd):
    """Returns the start date of the mahadasa which occured on or before `jd`"""
    nak, rem = panchanga.nakshatra_position(jd)
    one_star = (360 / 27.)        # 27 nakshatras span 360°
    lord = vimsottari_adhipati(nak)          # ruler of current nakshatra
    period = const.vimsottari_dict[lord]       # total years of nakshatra lord
    period_elapsed = rem / one_star * period # years
    period_elapsed *= sidereal_year        # days
    start_date = jd - period_elapsed      # so many days before current day
    return [lord, start_date]

def vimsottari_mahadasa(jdut1):
    """List all mahadashas and their start dates"""
    lord, start_date = vimsottari_dasha_start_date(jdut1)
    retval = Dict()
    for i in range(9):
        retval[lord] = start_date
        start_date += const.vimsottari_dict[lord] * sidereal_year
        lord = vimsottari_next_adhipati(lord)

    return retval

def vimsottari_bhukti(maha_lord, start_date):
    """Compute all bhuktis of given nakshatra-lord of Mahadasa
    and its start date"""
    lord = maha_lord
    retval = Dict()
    for i in range(9):
        retval[lord] = start_date
        factor = const.vimsottari_dict[lord] * const.vimsottari_dict[maha_lord] / const.human_life_span_for_vimsottari_dhasa
        start_date += factor * sidereal_year
        lord = vimsottari_next_adhipati(lord)

    return retval

# North Indian tradition: dasa-antardasa-pratyantardasa
# South Indian tradition: dasa-bhukti-antara-sukshma
def vimsottari_antara(maha_lord, bhukti_lord, start_date):
    """Compute all antaradasas from given bhukit's start date.
    The bhukti's lord and its lord (mahadasa lord) must be given"""
    lord = bhukti_lord
    retval = Dict()
    for i in range(9):
        retval[lord] = start_date
        factor = const.vimsottari_dict[lord] * (const.vimsottari_dict[maha_lord] / const.human_life_span_for_vimsottari_dhasa)
        factor *= (const.vimsottari_dict[bhukti_lord] / const.human_life_span_for_vimsottari_dhasa)
        start_date += factor * sidereal_year
        lord = vimsottari_next_adhipati(lord)

    return retval


def where_occurs(jd, some_dict):
    """Returns minimum key such that some_dict[key] < jd"""
    # It is assumed that the dict is sorted in ascending order
    # i.e. some_dict[i] < some_dict[j]  where i < j
    for key in reversed(some_dict.keys()):
        if some_dict[key] < jd: return key


def compute_vimsottari_antara_from(jd, mahadashas):
    """Returns antaradasha within which given `jd` falls"""
    # Find mahadasa where this JD falls
    i = where_occurs(jd, mahadashas)
    # Compute all bhuktis of that mahadasa
    bhuktis = vimsottari_bhukti(i, mahadashas[i])
    # Find bhukti where this JD falls
    j = where_occurs(jd, bhuktis)
    # JD falls in i-th dasa / j-th bhukti
    # Compute all antaras of that bhukti
    antara = vimsottari_antara(i, j, bhuktis[j])
    return (i, j, antara)

def get_vimsottari_dhasa_bhukthi(jd,place):
    """
        provides Vimsottari dhasa bhukthi for a given date in julian day (includes birth time)
        @param jd: Julian day for birthdate and birth time
        @return: a list of [dhasa_lord,bhukthi_lord,bhukthi_start]
          Example: [ [7, 5, '1915-02-09'], [7, 0, '1917-06-10'], [7, 1, '1918-02-08'],...]
    """
    # jd is julian date with birth time included
    city,lat,long,tz = place
    jdut1 = jd - tz/24
    dashas = vimsottari_mahadasa(jdut1)
    dhasa_bukthi=[]
    for i in dashas:
        #print(' ---------- ' + get_dhasa_name(i) + ' ---------- ')
        bhuktis = vimsottari_bhukti(i, dashas[i])
        dhasa_lord = i
        for j in bhuktis:
            bhukthi_lord = j
            jd1 = bhuktis[j]
            y, m, d, h = swe.revjul(round(jd1 + tz))
            date_str = '%04d-%02d-%02d' %(y,m,d)
            bhukthi_start = date_str
            dhasa_bukthi.append([dhasa_lord,bhukthi_lord,bhukthi_start]) 
            #dhasa_bukthi[i][j] = [dhasa_lord,bhukthi_lord,bhukthi_start]
    return dhasa_bukthi

def subractorforiruppu(dob,enddata):
    enddata=[int(item) for item in enddata.split("-")]
    dob=[dob[2]]+[dob[1]]+[dob[0]]
    iruppu=[]
    if dob[0]<enddata[0]:
        iruppu.append(enddata[0]-dob[0])
    if dob[1]<enddata[1]:
        iruppu.append(enddata[1]-dob[1])
    else:
        if iruppu[0]!=0:
            iruppu[0]=iruppu[0]-1
        iruppu.append((12+enddata[1])-dob[1])
    if dob[2]<enddata[2]:
        iruppu.append(enddata[2]-dob[2])
    else:
        if iruppu[1]!=0:
            iruppu[1]=iruppu[1]-1
        iruppu.append((30+enddata[2])-dob[2])
    if len(iruppu)==3:
        return tuple(iruppu)
    else:
        print("ERROR")

class dasabukthi:
    def __init__(self,dob,tob,lat=11.664325,lon=78.146011,tz=+5.5) -> None:
        self.latitude=lat
        self.longitude=lon
        self.timezone=tz
        self.dob=[int(val) for val in dob.split("-")]
        self.tob=[int(val) for val in tob.split("-")]+[0,]
        ayanamsa_mode="Lahiri"
        panchanga.set_ayanamsa_mode('LAHIRI')
        place = panchanga.Place('salem',self.latitude,self.longitude,self.timezone)
        jd_at_dob = utils.julian_day_number((self.dob[2],self.dob[1],self.dob[0]),(self.tob[0],self.tob[1],self.tob[2]))
        asc = panchanga.ascendant(jd_at_dob, place)
        planetaryposition = charts.divisional_chart(jd_at_dob, place, ayanamsa_mode, divisional_chart_factor=1)
        self.planetaryposition={indices[item[0]]:(item[1][0]*30+item[1][1]) for item in planetaryposition}
        db=get_vimsottari_dhasa_bhukthi(jd_at_dob, place)#,years)#, ayanamsa_mode, divisional_chart_factor)
        #print(db)
        rep=db[0][0]
        for d,b,s in db:
            if rep!=d:
                iruppu=s
                break
        self.startdate=iruppu
        self.iruppudasa=subractorforiruppu(self.dob,iruppu)

# print(dasabukthi("9-6-2005","14-3").iruppudasa)
'------ main -----------'
# if __name__ == "__main__":
#     from modules import *
#     import charts
#     """ SET AYANAMSA MODE FIRST """
#     panchanga.set_ayanamsa_mode('LAHIRI')
#     jd_at_dob = utils.julian_day_number((2005,6,9),(14,3,0))
#     years = 21
#     place = panchanga.Place('salem',16+15.0/60,81+12.0/60,5.5)
#     divisional_chart_factor = 1
#     ayanamsa_mode = 'Lahiri'
#     asc = panchanga.ascendant(jd_at_dob, place)
#     print('ascendat',asc)
#     chart_67_pp = charts.divisional_chart(jd_at_dob, place, ayanamsa_mode, divisional_chart_factor=1)
#     print(chart_67_pp)
#     db=get_vimsottari_dhasa_bhukthi(jd_at_dob, place)#,years)#, ayanamsa_mode, divisional_chart_factor)
#     print('vimsottari_dhasa bhukthi')
#     print(db)
#     rep=db[0][0]
#     for d,b,s in db:
#         if rep!=d:
#             print(s)
#             break
#     exit()

