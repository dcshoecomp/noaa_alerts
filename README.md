Version | Changes
:--- | :---
v0.0.8 | merged concept of claytonjn's idea of unlimited alerts. Sensor now will dump all alerts in (alerts_string)
v0.0.7 | added "unit_of_measurement" HA property<br>changed add_devices to add_entities to avoid future issues<br>added throttle aka scan_interval config option
v0.0.6 | manifest.json is now working<br>added __init__.py<br>entity_id is now noaa_alerts_(your zone id)

# noaa_alerts
HomeAssistant Noaa Alerts Custom Sensor

Custom sensor using pypi(https://pypi.org/project/noaa-sdk/) noaa-sdk to get an alert sensor

To add noaa_alerts to your installation, download the latest release zip and copy noaa_alerts folder to `<config directory>/custom_components/` and add the following to your configuration.yaml file:

**Example configuration.yaml entry**
```yaml
sensor:
  - platform: noaa_alerts
    zoneid: YOUR_ZONE_ID
    zoneid: ANOTHER_ZONE_ID
```
**Configuration variables:**  

key | description  
:--- | :---  
**zoneid (Optional)** | Go to https://alerts.weather.gov/ scroll down to the states and click zone id. By default latitude/longitude will be taken from the Home Assistant configuration. Mulitple Zones accepted. 
scan_interval (Optional) |  Minimum time interval between updates. Default is 1 minute. Supported formats:<br>scan_interval: 'HH:MM:SS'<br>scan_interval: 'HH:MM'


**states:** sensor will return the number of current alerts, attributes will be the 1st most severe alert, with exception of alerts_string. Naming format is noaa_alerts_<your zoneid here>.

attribute | description  
:--- | :---  
urgency | (Immediate, Expected, Future, Unknown) sorted in that order
event | event type
severity | severity level(minor, moderate, severe, extreme)
headline | summary headline of event
instruction | noaa recommended instructions for possible evacuation
description | full description of event
alerts_string | full json dump of all alerts in zone
