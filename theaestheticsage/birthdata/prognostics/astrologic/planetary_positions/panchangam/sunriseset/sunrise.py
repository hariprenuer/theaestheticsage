# import datetime
# from suntime import Sun, SunTimeException
# import pytz
# latitude =  11.664325
# longitude = 78.146011
# sun = Sun(latitude, longitude)
# # Get today's sunrise and sunset in UTC
# today_sr = sun.get_sunrise_time()
# today_ss = sun.get_sunset_time()
# for pl in pytz.all_timezones:
#     if "India" in pl:
#         print(pl)
# print(today_sr,today_ss)
# print('Today at Warsaw the sun raised at {} and get down at {} UTC'.
#       format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))
# # On a special date in your machine's local time zone
# abd = datetime.date(2014, 10, 3)
# abd_sr = sun.get_local_sunrise_time(abd)
# abd_ss = sun.get_local_sunset_time(abd)
# print('On {} the sun at Warsaw raised at {} and get down at {}.'.
#       format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))