# HA_noaa_alerts
HomeAssistant Noaa Alerts Custom Sensor

initial test for custom sensor using pypi(https://pypi.org/project/noaa-sdk/) noaa-sdk to get an alert sensor


To add HA_noaa_alerts to your installation, copy HA_noaa_alerts to /config/custom_components and add the following to your configuration.yaml file:

# Example configuration.yaml entry
sensor:
  - platform: HA_noaa_alerts
    zoneid: YOUR_ZONE_ID

# Description
zoneid: Go to https://alerts.weather.gov/ scroll down to the states and click zone id. required: true type: string 
