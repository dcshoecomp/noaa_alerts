#!/usr/bin/env python
from noaa_sdk import noaa
CONF_ZONEID="IAZ078"
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
params['limit'] = 3
params={}
print(params)
try:
    nws = noaa.NOAA().alerts(active=1, **params)
    #nws = noaa.NOAA().active_alerts()
    print(nws)
except Exception as err:
    print(err)

nwsalerts = nws['features']

def sortedbyurgencyandseverity(prop):
    if (prop['properties']['urgency']).lower() == 'immediate':
        sortedvalue = 1
    elif (prop['properties']['urgency']).lower() == 'expected':
        sortedvalue = 10
    elif (prop['properties']['urgency']).lower() == 'future':
        sortedvalue = 100
    else:
        sortedvalue = 1000
    if (prop['properties']['severity']).lower() == 'extreme':
        sortedvalue = sortedvalue * 1
    elif (prop['properties']['severity']).lower() == 'severe':
        sortedvalue = sortedvalue * 2
    elif (prop['properties']['severity']).lower() == 'moderate':
        sortedvalue = sortedvalue * 3
    else:
        sortedvalue = sortedvalue * 4
    return sortedvalue

nwsalerts = sorted(nwsalerts, key=sortedbyurgencyandseverity)
for d in sortedalerts: d['properties']['severity']

if len(nwsalerts) > 1:
    nwsalerts = sorted(nwsalerts, key=sortedbyurgencyandseverity)
    for d in sortedalerts: d['properties']['severity']
elif len(nwsalerts) == 1:
    description = nwsalerts[0].['properties']['description']
    event_type = nwsalerts[0].['properties']['event']
    event_urgency = nwsalerts[0].['properties']['urgency']
    event_severity = nwsalerts[0].['properties']['severity']
else:
    description = 'none'
    state = 'none'
nwsalerts[0]['properties']['description']
print("****description: **** ", description]
print("****event: ***** ", event_type]
print("****urgency: ***** ", event_urgency]
print("****severity: ***** ", event_severity]
lengthkeys = len(nwsalerts)
print("****count of alerts: ****", lengthkeys)
print("\n\n\n\n\n\n\n")

for alert in nwsalerts:
    #print(alert.['properties']['description'])
    (alert['properties']['description']).lower()
any(d['properties']['urgency'] == 'Immediate' for d in nwsalerts)