import swisseph as swe
from math import ceil
from collections import namedtuple as struct
maasa_names = [ "Chaitra", "Vaisakha", "Jyestha", "Ashadha", "Sravana", "Bhadrapada", 
                "Ashwayuja", "Kartika", "Margashira", "Pushya", "Magha", "Phalguna"]

vaara_names = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
tithi_names = [ "shukla padyami", "shukla dwitiya", "shukla tritiya", "shukla chauti", "shukla panchami",
                "shukla shashti", "shukla sapthami", "shukla ashtami", "shukla navami", "shukla dashami",
                "shukla ekadashi", "shukla dwadashi", "shukla trayodashi", "shukla chaturdashi", "poornima",
                "krishna padyami", "krishna dwitiya", "krishna tritiya", "krishna chauti", "krishna panchami",
                "krishna shashti", "krishna sapthami", "krishna ashtami", "krishna navami", "krishna dashami",
                "krishna ekadashi", "krishna dwadashi", "krishna trayodashi", "krishna chaturdashi", "amavasya"]
planets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","uran","nept"]
bavaslist=["mesham","rishabam","midhunam","kadagam","simmam","kanni",
           "thulam","viruchigam","dhanusu","magaram","kumbam","meenam"]
swe.KETU = swe.PLUTO
swe.RAHU=swe.MEAN_NODE
planet_list = [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER,
               swe.VENUS, swe.SATURN, swe.MEAN_NODE, # Rahu = MEAN_NODE
               swe.KETU, swe.URANUS, swe.NEPTUNE ]
Date = struct('Date', ['year', 'month', 'day'])
Place = struct('Place', ['latitude', 'longitude', 'timezone'])
swe.set_ephe_path("C://Users//91770//Desktop//astronomy//ephe")
gregorian_to_jd = lambda date: swe.julday(date.year, date.month, date.day, 0.0)
ketu = lambda rahu: (rahu + 180) % 360

def nakshatra_pada(longitude):
  """Gives nakshatra (1..27) and paada (1..4) in which given longitude lies"""
  # 27 nakshatras span 360°
  one_star = (360 / 27)  # = 13°20'
  # Each nakshatra has 4 padas, so 27 x 4 = 108 padas in 360°
  one_pada = (360 / 108) # = 3°20'
  quotient = int(longitude / one_star)
  reminder = (longitude - quotient * one_star)
  pada = int(reminder / one_pada)
  # convert 0..26 to 1..27 and 0..3 to 1..4
  return [1 + quotient, 1 + pada]
def unwrap_angles(angles):
  """Add 360 to those elements in the input list so that
     all elements are sorted in ascending order."""
  result = angles
  for i in range(1, len(angles)):
    if result[i] < result[i-1]: result[i] += 360

  assert(result == sorted(result))
  return result
def new_moon(jd, tithi_, opt = -1):
    """Returns JDN, where
        opt = -1:  JDN < jd such that lunar_phase(JDN) = 360 degrees
        opt = +1:  JDN >= jd such that lunar_phase(JDN) = 360 degrees
    """
    if opt == -1:  start = jd - tithi_         # previous new moon
    if opt == +1:  start = jd + (30 - tithi_)  # next new moon
    # Search within a span of (start +- 2) days
    x = [ -2 + offset/4 for offset in range(17) ]
    y = [lunar_phase(start + i) for i in x]
    y = unwrap_angles(y)
    y0 = inverse_lagrange(x, y, 360)
    return start + y0

def raasi(jd):
  """Zodiac of given jd. 1 = Mesha, ... 12 = Meena"""
  s = solar_longitude(jd)
  solar_nirayana = solar_longitude(jd)
  # 12 rasis occupy 360 degrees, so each one is 30 degrees
  return ceil(solar_nirayana / 30.)
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
def yoga(jd, place):
    """Yoga at given jd and place.
        1 = Vishkambha, 2 = Priti, ..., 27 = Vaidhrti
    """
    # 1. Find time of sunrise
    lat, lon, tz = place
    rise = sunrise(jd, place)[0] - tz / 24.  # Sunrise at UT 00:00

    # 2. Find the Nirayana longitudes and add them
    lunar_long = lunar_longitude(rise)
    solar_long = solar_longitude(rise)
    total = (lunar_long + solar_long) % 360
    # There are 27 Yogas spanning 360 degrees
    yog = ceil(total * 27 / 360)

    # 3. Find how many longitudes is there left to be swept
    degrees_left = yog * (360 / 27) - total

    # 3. Compute longitudinal sums at intervals of 0.25 days from sunrise
    offsets = [0.25, 0.5, 0.75, 1.0]
    lunar_long_diff = [ (lunar_longitude(rise + t) - lunar_longitude(rise)) % 360 for t in offsets ]
    solar_long_diff = [ (solar_longitude(rise + t) - solar_longitude(rise)) % 360 for t in offsets ]
    total_motion = [ moon + sun for (moon, sun) in zip(lunar_long_diff, solar_long_diff) ]

    # 4. Find end time by 4-point inverse Lagrange interpolation
    y = total_motion
    x = offsets
    # compute fraction of day (after sunrise) needed to traverse 'degrees_left'
    approx_end = inverse_lagrange(x, y, degrees_left)
    ends = (rise + approx_end - jd) * 24 + tz
    answer = [int(yog), to_dms(ends)]

    # 5. Check for skipped yoga
    lunar_long_tmrw = lunar_longitude(rise + 1)
    solar_long_tmrw = solar_longitude(rise + 1)
    total_tmrw = (lunar_long_tmrw + solar_long_tmrw) % 360
    tomorrow = ceil(total_tmrw * 27 / 360)
    isSkipped = (tomorrow - yog) % 27 > 1
    if isSkipped:
        # interpolate again with same (x,y)
        leap_yog = yog + 1
        degrees_left = leap_yog * (360 / 27) - total
        approx_end = inverse_lagrange(x, y, degrees_left)
        ends = (rise + approx_end - jd) * 24 + tz
        leap_yog = 1 if yog == 27 else leap_yog
        answer += [int(leap_yog), to_dms(ends)]

    return answer


def karana(jd, place):
    """Returns the karana and their ending times. (from 1 to 60)"""
    # 1. Find time of sunrise
    rise = sunrise(jd, place)[0]

    # 2. Find karana at this JDN
    solar_long = solar_longitude(rise)
    lunar_long = lunar_longitude(rise)
    moon_phase = (lunar_long - solar_long) % 360
    today = ceil(moon_phase / 6)
    degrees_left = today * 6 - moon_phase

    return [int(today)]
def vaara(jd):
    """Weekday for given Julian day. 0 = Sunday, 1 = Monday,..., 6 = Saturday"""
    return int(ceil(jd + 1) % 7)

def masa(jd, place):
    """Returns lunar month and if it is adhika or not.
        1 = Chaitra, 2 = Vaisakha, ..., 12 = Phalguna"""
    ti = tithi(jd, place)[0]
    critical = sunrise(jd, place)[0]  # - tz/24 ?
    last_new_moon = new_moon(critical, ti, -1)
    next_new_moon = new_moon(critical, ti, +1)
    this_solar_month = raasi(last_new_moon)
    next_solar_month = raasi(next_new_moon)
    is_leap_month = (this_solar_month == next_solar_month)
    maasa = this_solar_month + 1
    if maasa > 12: maasa = (maasa % 12)
    return [int(maasa), is_leap_month]

# def planetary_positions(jd, place):
#   """Computes instantaneous planetary positions
#      (i.e., which celestial object lies in which constellation)

#      Also gives the nakshatra-pada division
#    """
#   jd_ut = jd - place.timezone / 24.

#   positions = []
#   for planet in planet_list:
#     if planet != swe.KETU:
#       nirayana_long = sidereal_longitude(jd_ut, planet)
#     else: # Ketu
#       nirayana_long = ketu(sidereal_longitude(jd_ut, swe.RAHU))

#     # 12 zodiac signs span 360°, so each one takes 30°
#     # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
#     constellation = int(nirayana_long / 30)
#     coordinates = to_dms(nirayana_long % 30)
#     positions.append([planet, constellation, coordinates, nakshatra_pada(nirayana_long)])

#   return positions

# def ascendant(jd, place):
#     """Lagna (=ascendant) calculation at any given time & place"""
#     lat, lon, tz = place
#     jd_utc = jd - (tz / 24.)
#     set_ayanamsa_mode() # needed for swe.houses_ex()

#     # returns two arrays, cusps and ascmc, where ascmc[0] = Ascendant
#     nirayana_lagna = swe.houses_ex(jd_utc, lat, lon, flag = swe.FLG_SIDEREAL)[1][0]
#     # 12 zodiac signs span 360°, so each one takes 30°
#     # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
#     constellation = int(nirayana_lagna / 30)
#     coordinates = to_dms(nirayana_lagna % 30)

#     reset_ayanamsa_mode()
#     return [constellation, coordinates, nakshatra_pada(nirayana_lagna)]

class dateattributes:
    def __init__(self,date=[9,6,2005],place=[11.664325, 78.146011, +5.30]):
        self.date=date
        self.place=place
        dob=gregorian_to_jd(Date(self.date[2],self.date[1],self.date[0]))
        location=Place(self.place[0],self.place[1],self.place[2])
        self.yogam=yoga(dob,location)
        self.karanam=karana(dob,location)
        self.vaara=vaara_names[vaara(dob)]
        self.masa=maasa_names[masa(dob,location)[0]]
        self.thithi=tithi_names[tithi(dob,location)[0]]
        self.sunrise=sunrise(dob,location)
dateattributes()