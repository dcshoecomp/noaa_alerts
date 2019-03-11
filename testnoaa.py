#!/usr/bin/env python
from noaa_sdk import noaa
#CONF_ZONEID="LAC121"
latitude=41.477509
longitude=-81.813951
#place with current alert https://api.weather.gov/alerts?zone=TNZ097
#place with no current alert https://api.weather.gov/alerts?zone=OHZ011
#https://api.weather.gov/alerts/active
#nws = noaa.NOAA().alerts(active=1,zone=CONF_ZONEID)
#follow format of https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/components/weather/darksky.py
try:
    CONF_ZONEID
except NameError:
    params={'point': '{0},{1}'.format(latitude,longitude)}
    print('latlong')
else:
    params={'zone': CONF_ZONEID}
    print('zoneid')

print(params)

nws = noaa.NOAA().alerts(active=1, **params)
nwsalerts = nws['features']

if len(nwsalerts) > 0:
    description = nwsalerts[0].get('properties').get('description')
    event_type = nwsalerts[0].get('properties').get('event')
    event_urgency = nwsalerts[0].get('properties').get('urgency')
    event_severity = nwsalerts[0].get('properties').get('severity')
else:
    description = 'none'
    state = 'none'

print("****description: **** ", description)
print("****event: ***** ", event_type)
print("****urgency: ***** ", event_urgency)
print("****severity: ***** ", event_severity)
lengthkeys = len(nwsalerts)
print("****count of alerts: ****", lengthkeys)
print("\n\n\n\n\n\n\n")

#for alert in nwsalerts:
#    print(alert.get('properties').get('description'))
