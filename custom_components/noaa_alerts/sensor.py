"""
A componenet which allows you to get information from noaa weather.gov
For more details about this component, please refer to the documentation at

https://github.com/dcshoecomp/noaa_alerts
"""

import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)
from homeassistant.const import (CONF_LATITUDE, CONF_LONGITUDE)

__version_ = '0.0.2'

REQUIREMENTS = ['noaa_sdk']

CONF_ZONEID="zoneid"
CONF_URGENCY="urgency"
CONF_SEVERITY="severity"

ATTR_DESCRIPTION = 'description'
ATTR_EVENT = 'event'
ATTR_SEVERITY = 'severity'

SCAN_INTERVAL = timedelta(seconds=60)

ICON = 'mdi:weather-hurricane'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_ZONEID): cv.string,
    vol.Optional(CONF_LATITUDE): cv.latitude,
    vol.Optional(CONF_LONGITUDE): cv.longitude,
    vol.Optional(CONF_URGENCY): cv.string,
    vol.Optional(CONF_SEVERITY): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    zoneid = str(config.get(CONF_ZONEID))
    latitude = config.get(CONF_LATITUDE, hass.config.latitude)
    longitude = config.get(CONF_LONGITUDE, hass.config.longitude)
    event_urgency = str(config.get(CONF_URGENCY))
    event_severity = str(config.get(CONF_SEVERITY))
    add_devices([noaa_alertsSensor(zoneid, event_urgency, event_severity, latitude, longitude)])

class noaa_alertsSensor(Entity):
    def __init__(self, zoneid, event_urgency, event_severity, latitude, longitude):
        self._zoneid = zoneid
        self.latitude = latitude
        self.longitude = longitude
        self._event_urgency = event_urgency
        self._event_severity = event_severity
        self.update()

    def update(self):
        from noaa_sdk import noaa
        if self._zoneid is not None:
            params={'zone': self._zoneid}
        else:
            params={'point': '{0},{1}'.format(self.latitude,self.longitude)}
        nws = noaa.NOAA().alerts(active=1, **params)
        nwsalerts = nws['features']
        if len(nwsalerts) > 0:
            self._state = nwsalerts[0].get('properties').get('urgency')
            self._event_type = nwsalerts[0].get('properties').get('event')
            self._event_severity = nwsalerts[0].get('properties').get('severity')
            self._description = nwsalerts[0].get('properties').get('description')
        else:
            self._state = 'none'
            self._event_type = 'none'
            self._event_severity = 'none'
            self._description = 'none'

    @property
    def name(self):
        return 'noaa_alerts'

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        return {
            ATTR_EVENT: self._event_type,
            ATTR_SEVERITY: self._event_severity,
            ATTR_DESCRIPTION: self._description,
        }
