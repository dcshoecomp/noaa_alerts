#!/usr/bin/env python
from noaa_sdk import noaa
n = noaa.NOAA()
res = n.alerts(active=0,zone="OHZ011")
alerts = res['features']
for alert in alerts:
    print(alert.get('properties').get('description'))