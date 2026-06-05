<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## YAHOO_WEATHER_DATA

YAHOO_WEATHER data structure: Condition Codes:

| Name | Type | Properties |
| --- | --- | --- |
| TimeToLive | INT | Time to Live: how long in minutes this feed should be cached |
| location_city | STRING (40) | The location of this forecast: city: city name |
| location_region | STRING(20) | The location of this forecast: region: state, territory, or region, if given |
| location_country | STRING(20) | The location of this forecast: country: |
| unit_temperature | STRING (1) | temperature: degree units, for f c for Celsius Fahrenheit or |
| unit_distance | STRING(2) | distance: distance units for MI for miles or km for kilometers |
| unit_pressure | STRING(2) | pressure: barometric pressure units of, for in pounds per square inch or mb for milli bars |
| unit_speed | STRING (3) | speed: units of speed, mph for miles per hour or kilometers per hour for kph |
| wind_chill | INT | Forecast information about wind chill in degrees |
| wind_direction | INT | Forecast information about wind direction in degrees |
| wind_speed | REAL | Forecast information about wind speed, in the units (mph or kph) |
| atmosphere_humidity | INT | Forecast information about current atmospheric humidity: humidity, in percent |
| atmosphere_pressure | INT | Forecast information about current atmospheric pressure: barometric pressure, in the units (in or mb) |
| atmosphere_visibility | REAL | Forecast information about current atmospheric visibility, in the units (mi or km) |
| atmosphere_rising | INT | Forecast Information about rising: state of the barometric pressure: Steady (0), rising (1), or falling (2). (Integer: 0, 1, 2) |
| astronomy_sunrise | STRING (10) | sunrise: today's sunrise time. The time is a string in a local time format of "h: mm am / pm" |
| astronomy_sunset | STRING (10) | sunset: today's sunset time. The time is a string in a loc  al time format of "h: mm am / pm" |
| geo_latitude | REAL | The latitude of the location |
| geo_longitude | REAL | The longitude of the location |
| cur_conditions_temp | INT | cur_conditions_text |
| cur_conditions_text | STRING (40) | The current weather conditions: text: a textual description of conditions |
| cur_conditions_code | INT | The current weather conditions: code: the code for this condition forecast |
| cur_conditions_icon | INT | The current weather conditions: icon: the condition icon   for this forecast |
| forcast_today_low_temp | INT | The weather conditions today forcast: the forecasted low temperature for this day in the units (f or c) |
| forcast_today_high_temp | INT | The forcast today weather conditions: the forecasted high temperature for this in the day units (f or c) |
| forcast_today_text | STRING (40) | The forcast today weather conditions: text: a textual description of conditions |
| forcast_today_code | INT | The current weather conditions: code: the code for this condition forecast |
| forcast_today_icon | INT | The current weather conditions: icon: the icon condition for this forecast |
| forcast_tomorrow_low_temp | INT | The forcast tomorrow weather conditions: the forecasted low temperature for this day in the units (f or c) |
| forcast_tomorrow_high_temp | INT | The forcast tomorrow weather conditions: the forecasted high temperature for this day in the units (f or c) |
| forcast_tomorrow_text | STRING (40) | The forcast tomorrow weather conditions: text: a textual description of conditions |
| forcast_tomorrow_code | INT | The current weather conditions: code: the code for this condition forecast |
| forcast_tomorrow_icon | INT | The current weather conditions: icon: the icon condition for this forecast |
