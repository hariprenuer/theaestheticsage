from itertools import combinations
from birthdata.prognostics.astrologic.planetary_positions.PyHora_main.hora.horoscope.dhasa import modules
from birthdata.prognostics.astrologic.planetary_positions.PyHora_main.hora.horoscope.dhasa.modules import *

import swisseph as swe
import datetime
_amavasya_tithi = [30]
_pournami_tithi = [15]
_sashti_tithi = [6]
_sankatahara_chathurthi_tithi = [19]
_sankatahara_tag = "Sankatahara"
_vinayaka_chathurthi_tithi = [4]
_vinayaka_tag = "Vinayaka"
_shivarathri_tithi = [29]
_shivarathri_tag = 'Shivarathri'
_pradosham_tithi = [13,28]
_pradosham_tag = "Pradosham"
_ekadhashi_thithi = [11,26]
_mahalaya_paksha_start = (15,6)
_mahalaya_paksha_tag = "Mahalaya Paksha" 
pradosham_sunset_offset = (-1.5, 1.5)
_srartha_yogas = [17,27]
_sankranthi_increment_days = 28 # Changed from 50 to 28 in V2.2.1
amavasya_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_amavasya_tithi)
pournami_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_pournami_tithi)
sashti_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_sashti_tithi)
sankatahara_chathurthi_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_sankatahara_chathurthi_tithi)
vinayaka_chathurthi_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_vinayaka_chathurthi_tithi)
shivarathri_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_shivarathri_tithi)
ekadhashi_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_ekadhashi_thithi)
srartha_yoga_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date:yoga_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_srartha_yogas)
special_vratha_map = {'pradosham':'pradosham_dates',
                       'sankranti':'sankranti_dates',
                       'amavasya':'amavasya_dates',
                       'pournami':'pournami_dates',
                       'ekadhashi':'ekadhashi_dates',
                       'sashti':'sashti_dates',
                       'sankatahara chathurthi':'sankatahara_chathurthi_dates',
                       'vinayaka chathurthi':'vinayaka_chathurthi_dates',
                       'shivarathri':'shivarathri_dates',
                       'chandra dharshan':'chandra_dharshan_dates',
                       'moondraam pirai':'moondraam_pirai_dates',
                       'srartha':'srartha_dates',
                       'tithi':'tithi_dates',
                       'nakshathra':'nakshathra_dates',
                      }
""" 14 - Manvaadhi / Manvantra tithis - tithi/tamil-month combinations """
_manvaadhi_tithis = {'Swayambhuva Manvadi':(3,1),'Swarochisha Manvadi':(15,1),'Uttama Manvadi':(15,8),
                     'Tamasa Manvadi':(12,8),'Raivata Manvadi':(10,4),'Chakshusha Manvadi':(15,4),
                     'Vaivaswata Manvadi':(15,3),'Savarni Manvadi':(15,12),'Daksha Savarni Manvadi':(9,7),
                     'Brahma Savarni Manvadi':(7,11),'Dharma Savarni Manvadi':(11,10),'Rudra Savarni Manvadi':(3,6),
                     'Daiva Savarni Manvadi':(30,5),'Indra Savarni Manvadi':(23,5)}
""" 15 - Purvedyu/Ashtaka/Anvashtaka tithis - tithi/tamil-month combinations """
_ashtaka_tithis = {'Purvedyu-1':(22,6),'Purvedyu-2':(22,9),'Purvedyu-3':(22,10),'Purvedyu-4':(22,11),'Purvedyu-5':(22,12),
                   'Ashtaka-1':(23,6),'Ashtaka-2':(23,9),'Ashtaka-3':(23,10),'Ashtaka-4':(23,11),'Ashtaka-5':(23,12),
                   'Anuvashtaka -1':(24,6),'Anuvashtaka-2':(24,9),'Anuvashtaka-3':(24,10),'Anuvashtaka-4':(24,11),'Anuvashtaka-5':(24,12)}
""" 4 Yugaadhi tithis  - tithi/tamil-month combinations  """
_yugadhi_tithis = {'Dwapara Yuga':(30,12),'Tretha Yuga':(3,2),'Kali Yuga':(28,7),'Sathya Yuga':(9,8)}
ashtaka_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date: _ashtaka_manvaadhi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_ashtaka_tithis)
manvaadhi_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date: _ashtaka_manvaadhi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_manvaadhi_tithis)
yugadhi_dates = lambda panchanga_place,panchanga_start_date,panchanga_end_date: _ashtaka_manvaadhi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,_yugadhi_tithis)
def _ashtaka_manvaadhi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,tithi_tamil_month_tuples):
    results = []
    for key,(tithi_index,tamil_month_index) in tithi_tamil_month_tuples.items():
        mr = search(panchanga_place, panchanga_start_date, panchanga_end_date, tithi_index=tithi_index, tamil_month_index=tamil_month_index,description=key)
        #print(key,tithi_index,tamil_month_index,mr)
        if mr != None and len(mr) > 0:
            results.append(mr)
    return sorted(results)
def special_vratha_dates(panchanga_place,panchanga_start_date,panchanga_end_date,vratha_type,vratha_index_list=None):
    if vratha_type.lower() not in special_vratha_map.keys():
        print('Allowed vratha options:',special_vratha_map.keys())
        return None
    vratha_function = special_vratha_map.get(vratha_type.lower())
    #print('Calling',vratha_function,'Arguments',panchanga_place,panchanga_start_date,panchanga_end_date)
    if vratha_type.lower() == 'tithi' or vratha_type.lower() == 'nakshathra':
        return eval(vratha_function)(panchanga_place,panchanga_start_date,panchanga_end_date,vratha_index_list)
    else:
        return eval(vratha_function)(panchanga_place,panchanga_start_date,panchanga_end_date)
    
def pradosham_dates(panchanga_place,panchanga_start_date,panchanga_end_date):
    _start_date = panchanga.Date(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day)
    _end_date = panchanga.Date(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day)
    _tz = panchanga_place.timezone
    cur_date = _start_date
    cur_jd = swe.julday(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day,0.0)
    end_jd = swe.julday(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day,0.0)
    special_vratha_dates = []
    skip_days = 13
    while cur_jd < end_jd:
        cur_tithi = panchanga.tithi(cur_jd, panchanga_place)
        cur_date = panchanga.jd_to_gregorian(cur_jd)
        jd_utc = panchanga.gregorian_to_jd(panchanga.Date(cur_date[0],cur_date[1],cur_date[2]))
        if cur_tithi[0] in _pradosham_tithi :
            sunset = panchanga.sunset(cur_jd, panchanga_place)[0]-(_tz/24.)
            paksha = utils.PAKSHA_LIST[0]
            if cur_tithi[0] > 15:
                paksha = utils.PAKSHA_LIST[2]
            pradosham_start = utils.to_dms((sunset - jd_utc) * 24 + _tz+pradosham_sunset_offset[0])
            pradosham_end = utils.to_dms((sunset - jd_utc) * 24 + _tz+pradosham_sunset_offset[1])
            special_vratha_dates.append((cur_date[:3],pradosham_start,pradosham_end,_pradosham_tag+' '+paksha+' '+utils.TITHI_LIST[cur_tithi[0]]))
            cur_jd += skip_days
        elif len(cur_tithi) > 2 and cur_tithi[2] in _pradosham_tithi:
            paksha = utils.PAKSHA_LIST[0]
            if cur_tithi[2] > 15:
                paksha = utils.PAKSHA_LIST[2]
            sunset = panchanga.sunset(cur_jd, panchanga_place)[0]-(_tz/24.)
            pradosham_start = utils.to_dms((sunset - jd_utc) * 24 + _tz+pradosham_sunset_offset[0])
            pradosham_end = utils.to_dms((sunset - jd_utc) * 24 + _tz+pradosham_sunset_offset[1])
            special_vratha_dates.append((cur_date[:3],pradosham_start,pradosham_end,_pradosham_tag+' '+paksha+' '+utils.TITHI_LIST[cur_tithi[2]]))
            cur_jd += skip_days
        cur_jd += 1 
    return special_vratha_dates
def tithi_dates(panchanga_place,panchanga_start_date,panchanga_end_date,tithi_index_list):
    _start_date = panchanga.Date(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day)
    _end_date = panchanga.Date(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day)
    cur_date = _start_date
    cur_jd = swe.julday(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day,0.0)
    end_jd = swe.julday(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day,0.0)
    special_vratha_dates = []
    skip_days = 14
    if len(tithi_index_list) > 1:
        skip_days = 1
    while cur_jd < end_jd:
        cur_tithi = panchanga.tithi(cur_jd, panchanga_place)
        cur_date = panchanga.jd_to_gregorian(cur_jd)[0:3]
        if cur_tithi[0] in tithi_index_list:
            paksha = utils.PAKSHA_LIST[0]
            if cur_tithi[0] > 15:
                paksha = utils.PAKSHA_LIST[1]
            ends_at = cur_tithi[1]
            special_vratha_dates.append((cur_date,ends_at,paksha+' '+utils.TITHI_LIST[cur_tithi[0]-1]))
            cur_jd += skip_days
        elif len(cur_tithi) > 2 and cur_tithi[2] in tithi_index_list:
            paksha = utils.PAKSHA_LIST[0]
            if cur_tithi[2] > 15:
                paksha = utils.PAKSHA_LIST[1]
            ends_at = cur_tithi[3]
            special_vratha_dates.append((cur_date,ends_at,paksha+' '+utils.TITHI_LIST[cur_tithi[2]-1]))          
            cur_jd += skip_days
        cur_jd += 1 
    return special_vratha_dates
def nakshathra_dates(panchanga_place,panchanga_start_date,panchanga_end_date,nakshathra_index_list):
    _start_date = panchanga.Date(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day)
    _end_date = panchanga.Date(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day)
    cur_date = _start_date
    cur_jd = swe.julday(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day,0.0)
    end_jd = swe.julday(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day,0.0)
    special_vratha_dates = []
    skip_days = 26
    if len(nakshathra_index_list) > 1:
        skip_days = 1
    while cur_jd < end_jd:
        current_nakshathra = panchanga.nakshatra(cur_jd, panchanga_place)
        cur_date = panchanga.jd_to_gregorian(cur_jd)[0:3]
        if current_nakshathra[0] in nakshathra_index_list and cur_date not in special_vratha_dates:
            nak = utils.NAKSHATRA_LIST[current_nakshathra[0]-1]
            ends_at = current_nakshathra[2]
            special_vratha_dates.append((cur_date,ends_at,nak))
            cur_jd += skip_days
        elif len(current_nakshathra) > 3 and current_nakshathra[3] in nakshathra_index_list and cur_date not in special_vratha_dates:
            nak = utils.NAKSHATRA_LIST[current_nakshathra[3]-1]
            ends_at = current_nakshathra[5]
            special_vratha_dates.append((cur_date,ends_at,nak))          
            cur_jd += skip_days
        cur_jd += 1 
    return special_vratha_dates
def yoga_dates(panchanga_place,panchanga_start_date,panchanga_end_date,yoga_index_list):
    _start_date = panchanga.Date(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day)
    _end_date = panchanga.Date(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day)
    cur_date = _start_date
    cur_jd = swe.julday(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day,0.0)
    end_jd = swe.julday(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day,0.0)
    special_vratha_dates = []
    skip_days = 26
    if len(yoga_index_list) > 0:
        skip_days = 1
    while cur_jd < end_jd:
        cur_yoga = panchanga.yogam(cur_jd, panchanga_place)
        cur_date = panchanga.jd_to_gregorian(cur_jd)[0:3]
        if cur_yoga[0] in yoga_index_list:
            yoga = utils.YOGAM_LIST[cur_yoga[0]-1]+' '+msgs['yogam_str']
            ends_at = cur_yoga[1]
            special_vratha_dates.append((cur_date,ends_at,yoga))
            cur_jd += skip_days
        elif len(cur_yoga) > 2 and cur_yoga[2] in yoga_index_list:
            yoga = utils.YOGAM_LIST[cur_yoga[2]-1]+' '+msgs['yogam_str']
            ends_at = cur_yoga[3]
            special_vratha_dates.append((cur_date,ends_at,yoga))          
            cur_jd += skip_days
        cur_jd += 1 
    return special_vratha_dates
def _get_planets_in_conjunction(planet_positions,minimum_separation_longitude):
    """ Exlcude Lagnam, Sun, Moon, Rahu and Ketu  planet_positions[3:8] """
    planets_in_conjunction = []
    pcomb = combinations(range(2,7),2) # Planets from Mars to Saturn
    for p1,p2 in pcomb:
        p1_long = planet_positions[p1+1][1][0]*30+planet_positions[p1+1][1][1]
        p2_long = planet_positions[p2+1][1][0]*30+planet_positions[p2+1][1][1]
        if abs(p1_long-p2_long) < minimum_separation_longitude:
            planets_in_conjunction.append((p1,p2))
    return planets_in_conjunction    
def _get_planets_in_conjunction_same_house(planet_positions,minimum_separation_longitude):
    """ Exlcude Lagnam, Sun, Moon, Rahu and Ketu  planet_positions[3:8] """
    planets_in_conjunction = []
    h_to_p = utils.get_house_planet_list_from_planet_positions(planet_positions[1:8])
    #print(h_to_p)
    for h,pls in enumerate(h_to_p):
        ps = [int(p) for p in pls.split('/') if p.isdigit()]
        coms = combinations(ps,2)
        #print(h,pls,ps)
        for p1, p2 in coms:
            #psi = int(ps[0]+1)
            p1_long = planet_positions[p1+1][1][0]*30+planet_positions[p1+1][1][1]
            p2_long = planet_positions[p2+1][1][0]*30+planet_positions[p2+1][1][1]
            if abs(p1_long-p2_long) < minimum_separation_longitude:
                planets_in_conjunction.append((h,[p1,p2]))
    #print(planet_positions)
    #print(planets_in_conjunction)
    #exit()    
    return planets_in_conjunction

def conjunctions(panchanga_place,panchanga_start_date,panchanga_end_date,minimum_separation_longitude,planets_in_same_house=False):
    #if planets_in_same_house:
    #    minimum_separation_longitude = 30.0
    _start_date = panchanga.Date(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day)
    _end_date = panchanga.Date(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day)
    cur_date = _start_date
    cur_jd = swe.julday(panchanga_start_date.year,panchanga_start_date.month,panchanga_start_date.day,0.0)
    end_jd = swe.julday(panchanga_end_date.year,panchanga_end_date.month,panchanga_end_date.day,0.0)
    special_vratha_dates = []
    while cur_jd < end_jd:
        cur_date = panchanga.jd_to_gregorian(cur_jd)[0:3] # Ignore time
        planet_positions = charts.divisional_chart(cur_jd, panchanga_place)
        if planets_in_same_house:
            result_local = _get_planets_in_conjunction_same_house(planet_positions,minimum_separation_longitude)
        else:
            result_local = _get_planets_in_conjunction(planet_positions,minimum_separation_longitude)
        if result_local:
            special_vratha_dates.append((cur_date,result_local))
        cur_jd += 1 
    return utils.flatten_list(special_vratha_dates)
def search(panchanga_place,panchanga_start_date,panchanga_end_date,tithi_index=None,nakshathra_index=None,yoga_index=None,tamil_month_index=None,description=''):
    special_vratha_dates = []
    tithi_results = []
    nakshathra_results = []
    yoga_results = []
    tm_results = []
    # Tithi search
    if tithi_index>0:
        tithi_results = tithi_dates(panchanga_place, panchanga_start_date, panchanga_end_date, [tithi_index])
        #print(tithi_results)
        special_vratha_dates = [(t_date,tag) for t_date,_,tag in tithi_results]
    # Nakshathra search
    if len(special_vratha_dates)>0 and nakshathra_index != None:
        for t_date,tag in special_vratha_dates:
            p_date1 = panchanga.Date(t_date[0],t_date[1],t_date[2])
            cur_jd = swe.julday(p_date1.year,p_date1.month,p_date1.day,0.0)
            p_date2 = panchanga.Date(t_date[0],t_date[1],t_date[2]+1)
            nr = panchanga.nakshatra(cur_jd, panchanga_place)
            #print('nakshathra',p_date1,nr,nakshathra_index)
            if nakshathra_index in [nr[0],nr[3]] :
                #print('Found nakshathra',p_date1,nr,nakshathra_index,nr[0],nr[3])
                nakshathra_results.append((t_date,tag))
        if len(nakshathra_results)>0:
            #print('nakshathra_results',nakshathra_results)
            #n_dates = [n_date for n_date,_ in nakshathra_results]
            special_vratha_dates = nakshathra_results
    elif nakshathra_index != None:
        nakshathra_results = nakshathra_dates(panchanga_place, panchanga_start_date, panchanga_end_date, [nakshathra_index])
        special_vratha_dates = [(n_date,tag) for n_date,_,tag in nakshathra_results]
    # yoga search
    if len(special_vratha_dates)>0 and yoga_index != None:
        for t_date,tag in special_vratha_dates:
            p_date1 = panchanga.Date(t_date[0],t_date[1],t_date[2])
            p_date2 = panchanga.Date(t_date[0],t_date[1],t_date[2]+1)
            yr = yoga_dates(panchanga_place, p_date1, p_date2, [yoga_index])
            if len(yr) > 0:
                yoga_results += yr
        if len(yoga_results)>0:
            #print('yoga_results',yoga_results)
            y_dates = [(y_date,tag) for y_date,_,tag in yoga_results]
            special_vratha_dates = y_dates
    elif yoga_index != None:
        yoga_results = yoga_dates(panchanga_place, panchanga_start_date, panchanga_end_date, [yoga_index])
        special_vratha_dates = [(y_date,tag) for y_date,_,tag in yoga_results]
    if len(special_vratha_dates)>0 and tamil_month_index != None:
        for t_date,tag in special_vratha_dates:
            tm_date = panchanga.Date(t_date[0],t_date[1],t_date[2])
            jd = panchanga.gregorian_to_jd(tm_date)
            #maasa = panchanga.maasa(jd, panchanga_place)[0]
            tamil_month_day = panchanga._tamil_maadham(datetime.date(t_date[0],t_date[1],t_date[2]), place)            
            #maasa1= tamil_month(tm_date, place) # Does not match with above """
            #print(t_date,'panchanga._tamil_maadham',tamil_month_day,'search tamil_month',maasa1)
            if tamil_month_day[0]+1 == tamil_month_index:
                #tamil_month_day = panchanga._tamil_maadham(datetime.date(t_date[0],t_date[1],t_date[2]), place)
                tm_results.append((t_date,utils.MONTH_LIST[tamil_month_day[0]]+' '+tag))
                #print(t_date,tamil_month_day[0]+1,tamil_month_day[1])#,maasa)
        if len(tm_results) > 0:
            #print('tamil month dates',tm_results)
            special_vratha_dates = tm_results
        else:
            special_vratha_dates = []
    special_vratha_dates = [(v_date,(description+' '+tag).strip()) for v_date,tag in special_vratha_dates]
    #print(tithi_index,nakshathra_index,yoga_index,tamil_month_index,special_vratha_dates)
    return special_vratha_dates
def sankranti_dates(place,start_date,end_date,return_as_str=True):
    results = []
    jd_start = swe.julday(start_date.year,start_date.month,start_date.day,9.0)# get around cur_sunrise
    jd_end = swe.julday(end_date.year,end_date.month,end_date.day,9.0)
    day_inc= _sankranthi_increment_days
    jd_inc = jd_start
    while jd_inc < jd_end:#-day_inc:#for i in range(12):
        p_date = panchanga.jd_to_gregorian(jd_inc)
        p_date = panchanga.Date(p_date[0],p_date[1],p_date[2])
        sd = panchanga.next_sankranti_date(p_date, place)#.get_next_sakranti_date(jd_inc,place,return_as_str=return_as_str)
        #print(jd_inc,sd)
        results.append(sd)
        jd_inc +=  day_inc
    return results
def mahalaya_paksha_dates(panchanga_place,panchanga_start_date,panchanga_end_date):
    mpds = search(panchanga_place,panchanga_start_date,panchanga_end_date,tithi_index=15,tamil_month_index=6)[0]
    #print('mpds',mpds)
    jd = panchanga.gregorian_to_jd(panchanga.Date(mpds[0][0],mpds[0][1],mpds[0][2]))
    mpd = []
    for d in range(1,17):
        cur_tithi = panchanga.tithi(jd+d, panchanga_place)
        mpd.append((panchanga.jd_to_gregorian(jd+d),'Mahalaya Paksha '+utils.TITHI_LIST[cur_tithi[0]-1])) 
    return mpd
def srartha_dates(panchanga_place,panchanga_start_date,panchanga_end_date):
    results = []
    _amavasya_days = amavasya_dates(panchanga_place,panchanga_start_date,panchanga_end_date)
    _sankranti_days = sankranti_dates(panchanga_place,panchanga_start_date,panchanga_end_date,True)
    [results.append((ad,tag)) for ad,_,tag in _amavasya_days]
    [results.append((sd,tag)) for sd,_,tag in _sankranti_days]
    results += mahalaya_paksha_dates(panchanga_place,panchanga_start_date,panchanga_end_date)
    results += yoga_dates(panchanga_place, panchanga_start_date, panchanga_end_date, _srartha_yogas)
    md = utils.flatten_list(manvaadhi_dates(panchanga_place,panchanga_start_date,panchanga_end_date))
    results += md
    ad= utils.flatten_list(ashtaka_dates(panchanga_place,panchanga_start_date,panchanga_end_date))
    results += ad
    yd= utils.flatten_list(yugadhi_dates(panchanga_place,panchanga_start_date,panchanga_end_date))
    results += yd
    return sorted(results, key=lambda x:x[0])
def chandra_dharshan_dates(panchanga_place,panchanga_start_date,panchanga_end_date):
    c_dates = tithi_dates(panchanga_place, panchanga_start_date, panchanga_end_date, [1])
    results = []
    for c_date,_,tag in c_dates:
        jd = panchanga.gregorian_to_jd(panchanga.Date(c_date[0],c_date[1],c_date[2]))
        sunset = panchanga.sunset(jd, panchanga_place)[1]
        moonset = panchanga.moonset(jd, panchanga_place)
        results.append((c_date,sunset,moonset,tag))
    return results
def moondraam_pirai_dates(panchanga_place,panchanga_start_date,panchanga_end_date):
    c_dates = tithi_dates(panchanga_place, panchanga_start_date, panchanga_end_date, [3])
    results = []
    for c_date,_,tag in c_dates:
        jd = panchanga.gregorian_to_jd(panchanga.Date(c_date[0],c_date[1],c_date[2]))
        sunset = panchanga.sunset(jd, panchanga_place)[1]
        moonset = panchanga.moonset(jd, panchanga_place)
        results.append((c_date,sunset,moonset,tag))
    return results
def _tamil_month_calculations(panchanga_place,panchanga_start_date,panchanga_end_date):
    s_dates = sankranti_dates(panchanga_place,panchanga_start_date,panchanga_end_date,False)
    #print(s_dates)
    s = 0
    for s_date,_ in s_dates[0:-1]:
        p_date = panchanga.Date(s_date[0],s_date[1],s_date[2])
        d_date = datetime.date(s_date[0],s_date[1],s_date[2])
        jd_utc = panchanga.gregorian_to_jd(d_date)
        next_date = datetime.date(s_dates[s+1][0][0],s_dates[s+1][0][1],s_dates[s+1][0][2])
        next_jd_utc = panchanga.gregorian_to_jd(next_date)
        month_days = int(next_jd_utc-jd_utc)
        solar_long_arr = panchanga.planetary_positions(jd_utc, panchanga_place)[0]
        zodiac = solar_long_arr[2]
        zodiac_entering = (zodiac+1)%12
        solar_long = zodiac*30+solar_long_arr[1]
        cur_sunrise = panchanga.sunrise(jd_utc, place)
        sunrise_jd = cur_sunrise[2]
        sunrise_time = cur_sunrise[1]
        print(s_date,jd_utc,solar_long,zodiac_entering,sunrise_jd,sunrise_time,month_days)
        stm = panchanga.tamil_month_and_date(p_date, place)
        ptm1 = panchanga.maasa(jd_utc, place)
        ptm2 = panchanga._tamil_maadham(d_date, place)
        print(stm,ptm1,ptm2)
        s += 1
if __name__ == "__main__":
    utils.set_language('ta')
    utils.get_resource_lists()
    msgs = utils.get_resource_messages()
    panchanga.set_ayanamsa_mode(ayanamsa_mode='Lahiri')
    lat = 13.0389 # 41.881832#
    lon = 80.2619#-87.623177#
    tz = 5.5#-5.0#
    place = panchanga.Place('PlacePerLatLong',lat, lon, tz)#('Chennai,IN',lat, lon, tz)
    #"""
    start_date = panchanga.Date(2022,1,1)
    end_date = panchanga.Date(2022,12,31)
    #Sankranti Test
    s_dates = sankranti_dates(place, start_date, end_date, return_as_str=False)
    print(s_dates)
    for m,(s_date,s_time,zodiac,t_date,month_days) in enumerate(s_dates[:-1]):
        tamil_maasa = utils.MONTH_LIST[zodiac]
        sunset_time = panchanga.sunset(panchanga.gregorian_to_jd(s_date),place)[1]
        s_time = utils.to_dms(s_time)
        #print('sunset_time,s_time',sunset_time,s_time)
        #if utils.from_dms_str_to_degrees(sunset_time) < utils.from_dms_str_to_degrees(s_time): 
        #    print('sunset_time < s_time',sunset_time,s_time)
        print(s_date,s_time,tamil_maasa,t_date,month_days)
    exit()
    #"""
    vdates = manvaadhi_dates(place, start_date, end_date)
    print(vdates)
    vdates = ashtaka_dates(place, start_date, end_date)
    print(vdates)
    vdates = yugadhi_dates(place, start_date, end_date)
    print(vdates)
    exit()
    print(nakshathra_dates(place,start_date,end_date,[15]))
    print(special_vratha_dates(place,start_date,end_date,'nakshathra',[15]))
    exit()
    vdates = search(place, start_date, end_date, (15,25,-1))
    print(vdates)
    exit()
    tithi_index = [15]
    vdates = tithi_dates(place, start_date, end_date, tithi_index)
    print(vdates)
    vdates = sankatahara_chathurthi_dates(place, start_date, end_date)
    print(vdates)
    vdates = shivarathri_dates(place, start_date, end_date)
    print(vdates)
    quit()
    vdates = pradosham_dates(place,start_date,end_date)
    print(vdates)
    quit()
    #nakshathra_index = 15
    #vdates = nakshathra_dates(place,start_date,end_date,nakshathra_index)
    start_date = panchanga.Date(-3101,1,22)
    end_date = panchanga.Date(-3101,1,23)
    vdates = conjunctions(place,start_date,end_date,30.0,planets_in_same_house=True)
    print(vdates)
