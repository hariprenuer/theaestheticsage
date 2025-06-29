from birthdatfrom birthdata.prognostics.astrologic.planetary_positions.PyHora_main.hora.horoscope.charta.prognostics.astrologic.planetary_positions.PyHora_main.hora.horoscope.dhasa.modules import *
.house import *

""" Also called Lagna Kendradi Rasi Dhasa """
def moola_dhasa(chart,dob):
    """
        calculate Lagna Kendraadhi dhasa aka Moola Dhasa
        @param chart: house_to_planet_list
          Example: ['','','','','2','7','1/5','0','3/4','L','','6/8'] 1st element is Aries and last is Pisces
        @param dob: Date of birth as a tuple e.g. (1999,12,31)  
        @return: 2D list of [dhasa_lord,dhasa_start,[Bhukthi_lord1,bhukthi_lord2,], dhasa_duraation
          Example: [ [7, '1993-6-1', '1996-6-1', [7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6], 3], ...]
    """
    dob_year = dob[0]
    dob_month = dob[1]
    dob_day = dob[2]
    h_to_p = chart[:]
    #print(h_to_p)
    p_to_h = utils.get_planet_to_house_dict_from_chart(h_to_p)    
    print(p_to_h)
    asc_house = p_to_h['L']
    seventh_house = (asc_house+7-1)%12
    print("Finding which house",asc_house,seventh_house,'is stronger')
    dhasa_seed_sign = stronger_rasi(h_to_p,asc_house,seventh_house)
    print('dhasa_seed_sign',dhasa_seed_sign)
    direction = 0
    if p_to_h[6]==dhasa_seed_sign:
        direction = 1
    elif p_to_h[8]==dhasa_seed_sign:
        direction = -1
    elif dhasa_seed_sign in const.odd_signs:  # Forward
        direction = 1
    elif dhasa_seed_sign in const.even_signs:  # backward
        direction = -1
    ks = sum(kendras()[:3],[])
    print('ks',ks)
    dhasa_progression = [(dhasa_seed_sign+direction*(k-1))%12 for k in ks]
    print(dhasa_progression)
    dhasa_periods = []
    dhasa_start = dob_year
    for sign in dhasa_progression:
        dhasa_duration = narayana._dhasa_duration(p_to_h,sign)
        dhasa_end = dhasa_start+dhasa_duration
        andtardhasa = _antardhasa(sign,p_to_h)#)+' '+str(dhasa_duration)+' months each'
        dhasa_period_suffix = '-'+str(dob_month)+'-'+str(dob_day)
        dhasa_periods.append([sign,str(dhasa_start)+dhasa_period_suffix,str(dhasa_end)+dhasa_period_suffix,andtardhasa,dhasa_duration])
        dhasa_start = dhasa_end
    # Second cycle
    dhasa_start = dhasa_end
    total_dhasa_duration = sum([row[-1] for row in dhasa_periods ])
    for c,sign in enumerate(dhasa_progression):
        dhasa_duration = 12 - dhasa_periods[c][-1]
        total_dhasa_duration += dhasa_duration
        if dhasa_duration <=0: # no need for second cycle as first cycle had 12 years
            #dhasa_duration = 12
            continue
        dhasa_end = dhasa_start+dhasa_duration
        #print(sign,_narayana_antardhasa(sign))
        andtardhasa = _antardhasa(sign,p_to_h)#)+' '+str(dhasa_duration)+' months each'
        dhasa_period_suffix = '-'+str(dob_month)+'-'+str(dob_day)
        dhasa_periods.append([sign,str(dhasa_start)+dhasa_period_suffix,str(dhasa_end)+dhasa_period_suffix,andtardhasa,dhasa_duration])
        dhasa_start = dhasa_end
        #print('total_dhasa_duration',total_dhasa_duration,dhasa_end)
        if total_dhasa_duration >= const.human_life_span_for_narayana_dhasa:
            break
    return dhasa_periods
def _antardhasa(antardhasa_seed_rasi,p_to_h):
    direction = -1
    if p_to_h[6]==antardhasa_seed_rasi or antardhasa_seed_rasi in const.odd_signs: # Forward
        direction = 1
    if p_to_h[8]==antardhasa_seed_rasi:
        direction *= -1
    return [(antardhasa_seed_rasi+direction*i)%12 for i in range(12)]
if __name__ == "__main__":
    pass