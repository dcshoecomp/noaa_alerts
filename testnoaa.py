#!/usr/bin/env python
from noaa_sdk import noaa
CONF_ZONEID="TXZ338"
n = noaa.NOAA()
res = n.alerts(active=0,zone=CONF_ZONEID)
alerts = res['features']
for alert in alerts:
    print(alert.get('properties').get('description'))
