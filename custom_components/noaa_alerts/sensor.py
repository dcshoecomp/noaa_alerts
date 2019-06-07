"""
A component which allows you to get information from noaa weather.gov
For more details about this component, please refer to the documentation at
https://github.com/dcshoecomp/noaa_alerts
"""

import logging
import json

import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import (PLATFORM_SCHEMA)
from homeassistant.const import (CONF_LATITUDE, CONF_LONGITUDE, CONF_SCAN_INTERVAL)
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

__version_ = 'pre-release'

REQUIREMENTS = ['noaa_sdk']

CONF_ZONEID="zoneid"
CONF_URGENCY="urgency"
CONF_SEVERITY="severity"

DEFAULT_ZONEID="LAT,LONG"

ATTR_EVENT = 'event'
ATTR_SEVERITY = 'severity'
ATTR_HEADLINE = 'headline'
ATTR_INSTRUCTION = 'instruction'
ATTR_DESCRIPTION = 'description'

SCAN_INTERVAL = timedelta(seconds=60)

ICON = 'mdi:weather-hurricane'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_ZONEID, default=DEFAULT_ZONEID): cv.string,
    vol.Optional(CONF_LATITUDE): cv.latitude,
    vol.Optional(CONF_LONGITUDE): cv.longitude,
    vol.Optional(CONF_URGENCY): cv.string,
    vol.Optional(CONF_SEVERITY): cv.string,
    vol.Optional(CONF_SCAN_INTERVAL): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    zoneid = str(config.get(CONF_ZONEID))
    latitude = config.get(CONF_LATITUDE, hass.config.latitude)
    longitude = config.get(CONF_LONGITUDE, hass.config.longitude)
    event_urgency = str(config.get(CONF_URGENCY))
    event_severity = str(config.get(CONF_SEVERITY))
    update_interval = config.get(CONF_SCAN_INTERVAL, SCAN_INTERVAL)
    add_entities([noaa_alertsSensor(zoneid, event_urgency, event_severity, latitude, longitude,update_interval)], True)

def sortedbyurgencyandseverity(prop):
    if (prop['urgency']).lower() == 'immediate':
        sortedvalue = 1
    elif (prop['urgency']).lower() == 'expected':
        sortedvalue = 10
    elif (prop['urgency']).lower() == 'future':
        sortedvalue = 100
    else:
        sortedvalue = 1000
    if (prop['severity']).lower() == 'extreme':
        sortedvalue = sortedvalue * 1
    elif (prop['severity']).lower() == 'severe':
        sortedvalue = sortedvalue * 2
    elif (prop['severity']).lower() == 'moderate':
        sortedvalue = sortedvalue * 3
    else:
        sortedvalue = sortedvalue * 4
    return sortedvalue

class noaa_alertsSensor(Entity):
    def __init__(self, zoneid, event_urgency, event_severity, latitude, longitude, interval):
        self._zoneid = zoneid
        self.latitude = latitude
        self.longitude = longitude
        self._event_urgency = event_urgency
        self._event_severity = event_severity
        self.update = Throttle(interval)(self._update)

    def _update(self):
        from noaa_sdk import noaa
        if self._zoneid != 'LAT,LONG':
            params={'zone': self._zoneid}
        else:
            params={'point': '{0},{1}'.format(self.latitude,self.longitude)}
        try:
            nws = noaa.NOAA().alerts(active=1, **params)
            nwsalerts = nws['features']
            if len(nwsalerts) > 1:
                nwsalerts = sorted(nwsalerts, key=sortedbyurgencyandseverity)
                self._state = nwsalerts[0]['properties']['urgency']
                self._event_type = nwsalerts[0]['properties']['event']
                self._event_severity = nwsalerts[0]['properties']['severity']
                self._description = nwsalerts[0]['properties']['description']
                self._headline = nwsalerts[0]['properties']['headline']
                self._instruction = nwsalerts[0]['properties']['instruction']
                #second set of events
                self._state2 = nwsalerts[0]['properties']['urgency']
                self._event_type2 = nwsalerts[0]['properties']['event']
                self._event_severity2 = nwsalerts[0]['properties']['severity']
                self._description2 = nwsalerts[0]['properties']['description']
                self._headline2 = nwsalerts[0]['properties']['headline']
                self._instruction2 = nwsalerts[0]['properties']['instruction']
            elif len(nwsalerts) == 1:
                self._state = nwsalerts[0]['properties']['urgency']
                self._event_type = nwsalerts[0]['properties']['event']
                self._event_severity = nwsalerts[0]['properties']['severity']
                self._description = nwsalerts[0]['properties']['description']
                self._headline = nwsalerts[0]['properties']['headline']
                self._instruction = nwsalerts[0]['properties']['instruction']
                self._state2 = 'none'
            else:
                self._state = 'none'
                self._event_type = 'none'
                self._event_severity = 'none'
                self._headline = 'none'
                self._instruction = 'none'
                self._description = 'none'
                self._state2 = 'none'
        except Exception as err:
            self._state = 'Error'
            self._event_type = 'none'
            self._event_severity = 'none'
            self._headline = 'none'
            self._instruction = 'none'
            self._description = err

    @property
    def name(self):
        name = "NOAA Alerts"
        if self._zoneid != 'LAT,LONG':
            name += ' (' + self._zoneid + ')'
        return name

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        if self._state2 == 'none':
            return {
                ATTR_EVENT: self._event_type,
                ATTR_SEVERITY: self._event_severity,
                ATTR_HEADLINE: self._headline,
                ATTR_INSTRUCTION: self._instruction,
                ATTR_DESCRIPTION: self._description,
            }
        else:
            return {
                ATTR_EVENT: self._event_type,
                ATTR_SEVERITY: self._event_severity,
                ATTR_HEADLINE: self._headline,
                ATTR_INSTRUCTION: self._instruction,
                ATTR_DESCRIPTION: self._description,
                'urgency2': self._state2,
                'event2': self._event_type2,
                'severity2': self._event_severity2,
                'headline2': self._headline2,
                'instruction2': self._instruction2,
                'description2': self._description2,
            }

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return None
