#!/usr/bin/env python
from noaa_sdk import noaa
CONF_ZONEID="TNZ097"
#https://api.weather.gov/alerts?zone=TNZ097
#https://api.weather.gov/alerts/active
nws = noaa.NOAA().alerts(active=1,zone=CONF_ZONEID)
nwsalerts = nws['features']

if len(nwsalerts) > 0:
    description = nwsalerts[0].get('properties').get('description')
    state = nwsalerts[0].get('properties').get('event')
else:
    description = 'none'
    state = 'none'

print("****description: **** ", description)
print("****event: ***** ", state)
lengthkeys = len(nwsalerts)
print("****count of alerts: ****", lengthkeys)
print("\n\n\n\n\n\n\n")

for alert in nwsalerts:
    print(alert.get('properties').get('description'))