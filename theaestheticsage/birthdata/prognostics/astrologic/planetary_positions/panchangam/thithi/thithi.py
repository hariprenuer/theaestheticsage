import swisseph as swe
from math import ceil
from collections import namedtuple as struct
tithi_names = [ "shukla padyami", "shukla dwitiya", "shukla tritiya", "shukla chauti", "shukla panchami",
                "shukla shashti", "shukla sapthami", "shukla ashtami", "shukla navami", "shukla dashami",
                "shukla ekadashi", "shukla dwadashi", "shukla trayodashi", "shukla chaturdashi", "poornima",
                "krishna padyami", "krishna dwitiya", "krishna tritiya", "krishna chauti", "krishna panchami",
                "krishna shashti", "krishna sapthami", "krishna ashtami", "krishna navami", "krishna dashami",
                "krishna ekadashi", "krishna dwadashi", "krishna trayodashi", "krishna chaturdashi", "amavasya"]
Date = struct('Date', ['year', 'month', 'day'])
Place = struct('Place', ['latitude', 'longitude', 'timezone'])
swe.set_ephe_path("C://Users//91770//Desktop//astronomy//ephe")
gregorian_to_jd = lambda date: swe.julday(date.year, date.month, date.day, 0.0)
def sidereal_longitude(jd, planet):
    """Computes nirayana (sidereal) longitude of given planet on jd"""
    set_ayanamsa_mode()
    longi, flags = swe.calc_ut(jd, planet, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)
    reset_ayanamsa_mode()
    return norm360(longi[0]) # degrees

_rise_flags = swe.BIT_DISC_CENTER + swe.BIT_NO_REFRACTION
solar_longitude = lambda jd: sidereal_longitude(jd, swe.SUN)
lunar_longitude = lambda jd: sidereal_longitude(jd, swe.MOON)
set_ayanamsa_mode = lambda: swe.set_sid_mode(swe.SIDM_LAHIRI)
reset_ayanamsa_mode = lambda: swe.set_sid_mode(swe.SIDM_FAGAN_BRADLEY)
norm360 = lambda angle: angle % 360


solar_longitude = lambda jd: sidereal_longitude(jd, swe.SUN)
lunar_longitude = lambda jd: sidereal_longitude(jd, swe.MOON)

def to_dms_prec(deg):
    d = int(deg)
    mins = (deg - d) * 60
    m = int(mins)
    s = round((mins - m) * 60, 6)
    return [d, m, s]

def to_dms(deg):
    d, m, s = to_dms_prec(deg)
    return [d, m, int(s)]

def sunrise(jd, place):
    """Sunrise when centre of disc is at horizon for given date and place"""
    lat, lon, tz = place
    result = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)
    rise = result[1][0]  # julian-day number
    # Convert to local time
    return [rise + tz/24., to_dms((rise - jd) * 24 + tz)]

def lunar_phase(jd):
    solar_long = solar_longitude(jd)
    lunar_long = lunar_longitude(jd)
    moon_phase = (lunar_long - solar_long) % 360
    return moon_phase

def inverse_lagrange(x, y, ya):
    """Given two lists x and y, find the value of x = xa when y = ya, i.e., f(xa) = ya"""
    assert(len(x) == len(y))
    total = 0
    for i in range(len(x)):
        numer = 1
        denom = 1
        for j in range(len(x)):
            if j != i:
                numer *= (ya - y[j])
                denom *= (y[i] - y[j])

        total += numer * x[i] / denom

    return total  

def tithi(jd, place):
    """Tithi at sunrise for given date and place. Also returns tithi's end time."""
    tz = place.timezone
    # 1. Find time of sunrise
    rise = sunrise(jd, place)[0] - tz / 24

    # 2. Find tithi at this JDN
    moon_phase = lunar_phase(rise)
    today = ceil(moon_phase / 12)
    degrees_left = today * 12 - moon_phase

    # 3. Compute longitudinal differences at intervals of 0.25 days from sunrise
    offsets = [0.25, 0.5, 0.75, 1.0]
    lunar_long_diff = [ (lunar_longitude(rise + t) - lunar_longitude(rise)) % 360 for t in offsets ]
    solar_long_diff = [ (solar_longitude(rise + t) - solar_longitude(rise)) % 360 for t in offsets ]
    relative_motion = [ moon - sun for (moon, sun) in zip(lunar_long_diff, solar_long_diff) ]

    # 4. Find end time by 4-point inverse Lagrange interpolation
    y = relative_motion
    x = offsets
    # compute fraction of day (after sunrise) needed to traverse 'degrees_left'
    approx_end = inverse_lagrange(x, y, degrees_left)
    ends = (rise + approx_end -jd) * 24 + tz
    answer = [int(today), to_dms(ends)]

    # 5. Check for skipped tithi
    moon_phase_tmrw = lunar_phase(rise + 1)
    tomorrow = ceil(moon_phase_tmrw / 12)
    isSkipped = (tomorrow - today) % 30 > 1
    if isSkipped:
        # interpolate again with same (x,y)
        leap_tithi = today + 1
        degrees_left = leap_tithi * 12 - moon_phase
        approx_end = inverse_lagrange(x, y, degrees_left)
        ends = (rise + approx_end -jd) * 24 + place.timezone
        leap_tithi = 1 if today == 30 else leap_tithi
        answer += [int(leap_tithi), to_dms(ends)]

    return answer
dob=gregorian_to_jd(Date(1976,7,13))
salem=Place ( 11.664325, 78.146011, +5.30)
print(tithi_names[tithi(dob,salem)[0]])