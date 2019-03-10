"""
A componenet which allow you to get information from noaa weather.gov
For more details about this component, please refer to the documentation at

https://github.com/dcshoecomp/HA_noaa_alerts
"""

import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)

__version_ = '0.0.1'

REQUIREMENTS = ['noaa_sdk']

CONF_ZONEID="zoneid"

ATTR_DESCRIPTION = 'description'

SCAN_INTERVAL = timedelta(seconds=300)

ICON = 'mdi:weather-hurricane'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ZONEID): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    zoneid = str(config.get(CONF_ZONEID))
    add_devices([ha_noaa_alertsSensor(zoneid)])

class ha_noaa_alertsSensor(Entity):
    def __init__(self, zoneid):
        self._zoneid = zoneid
        self.update()

    def update(self):
        from noaa_sdk import noaa
        nws = noaa.NOAA().alerts(active=1,zone=self._zoneid)
        nwsalerts = nws['features']
        if len(nwsalerts) > 0:
            self._description = nwsalerts[0].get('properties').get('description')
            self._state = nwsalerts[0].get('properties').get('event')
        else:
            self._description = 'none'
            self._state = 'none'
            
    @property
    def name(self):
        return 'noaa'

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        return {
            ATTR_DESCRIPTION: self._description,
        }
