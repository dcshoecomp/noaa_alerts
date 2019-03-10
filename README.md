# noaa_alerts
HomeAssistant Noaa Alerts Custom Sensor

initial test for custom sensor using pypi(https://pypi.org/project/noaa-sdk/) noaa-sdk to get an alert sensor

To add HA_noaa_alerts to your installation, copy noaa_alerts folder to `<config directory>/custom_components/` and add the following to your configuration.yaml file:

**Example configuration.yaml entry**
```yaml
sensor:
  - platform: noaa_alerts
    zoneid: YOUR_ZONE_ID
```
**Configuration variables:**  

key | description  
:--- | :---  
**zoneid (Required)** | Go to https://alerts.weather.gov/ scroll down to the states and click zone id. 

**states:**
sensor will return the event type of the current alert

**limitations:**
Currently it can only return the first active alert reported by noaa

