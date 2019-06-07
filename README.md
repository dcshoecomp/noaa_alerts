Version | Changes
:--- | :---
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
```
**Configuration variables:**  

key | description  
:--- | :---  
**zoneid (Optional)** | Go to https://alerts.weather.gov/ scroll down to the states and click zone id. By default latitude/longitude will be taken from the Home Assistant configuration

**states:** sensor will return the urgency of the current alert (Immediate, Expected, Future, Unknown), if multiple events exist will take most urgent state, then most severe and return 2 events.

attribute | description  
:--- | :---  
event | event type
severity | severity level(minor, moderate, severe, extreme)
headline | summary headline of event
instruction | noaa recommended instructions for possible evacuation
description | full description of event

hidden attributes | Until second alert event exists
:--- | :---
urgency2 | second urgency state
event2 | event type
severity2 | severity level(minor, moderate, severe, extreme)
headline2 | summary headline of event
instruction2 | noaa recommended instructions for possible evacuation
description2 | full description of event
