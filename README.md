# noaa_alerts
HomeAssistant Noaa Alerts Custom Sensor

initial test for custom sensor using pypi(https://pypi.org/project/noaa-sdk/) noaa-sdk to get an alert sensor

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

**states:**
sensor will return the urgency of the current alert (Immediate, Expected, Future, Unknown)

attribute | description  
:--- | :---  
event | event type
severity | severity level(minor, moderate, severe, extreme)
headline | summary headline of event
instruction | noaa recommended instructions for possible evacuation
description | full description of event

**limitations:**
Currently it can only return the first active alert in zone

