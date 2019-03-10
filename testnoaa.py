#!/usr/bin/env python
from noaa_sdk import noaa
CONF_ZONEID="TNZ097"
#https://api.weather.gov/alerts?zone=TNZ097
#https://api.weather.gov/alerts/active
n = noaa.NOAA()
res = n.alerts(active=1,zone=CONF_ZONEID)
alerts = res['features']
description = alerts[0].get('properties').get('description')
print("****description: **** ", description)
state = alerts[0].get('properties').get('event')
print("****event: ***** ", state)
lengthkeys = len(alerts)
print("****count of alerts: ****", lengthkeys)
print("\n\n\n\n\n\n\n")
for alert in alerts:
    print(alert.get('properties').get('description'))