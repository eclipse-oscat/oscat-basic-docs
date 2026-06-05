<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## WORLD_WEATHER_DATA

WORLD_WEATHER_DATA data structure: WORLD_WEATHER_CUR data structure: WORLD_WEATHER_DAY data structure:

| Name | Type | Properties |
| --- | --- | --- |
| CUR | WORLD_WEATHER_CUR | Current weather conditions |
| DAY | ARRAY [0..4] OF WORLD_WEATHER_DAY | Next 5 days of weather forecast |

| Name | Type | Properties |
| --- | --- | --- |
| OBSERVATION_TIME | STRING(8) | Observation time (UTC) |
| TEMP_C | INT | Temperature (°C) |
| WEATHER_CODE | INT | Unique Weather Code |
| WEATHER_DESC | STRING(60) | Weather description text |
| WEATHER_ICON | INT | Weather Icon |
| WIND_SPEED_MILES | INT | Wind speed in miles per hour |
| WIND_SPEED_KMPH | INT | Wind speed in kilometre per hour |
| WIND_DIR_DEGREE | INT | Wind direction in degree |
| WIND_DIR16POINT | STRING (3) | 16-Point wind direction compass |
| PRECIPMM | REAL | Precipitation amount in millimetre |
| HUMIDITY | INT | Humidity (%) |
| VISIBILITY | INT | Visibility (km) |
| PRESSURE | INT | Atmospheric pressure in milibars |
| CLOUDOVER | INT | Cloud cover (%) |

| Name | Type | Properties |
| --- | --- | --- |
| DATE_OF_DAY | STRING (10) | Date for which the weather is forecasted |
| TEMP_MAX_C | INT | Day temperature in °C(Celcius) |
| TEMP_MAX_F | INT | Day temperature in °F(Fahrenheit) |
| TEMP_MIN_C | INT | Night temperature in °C(Celcius) |
| TEMP_MIN_F | INT | Night temperature in °F(Fahrenheit) |
| WIND_SPEED_MILES | INT | Wind Speed in mph (miles per hour) |
| WIND_SPEED_KMPH | INT | Wind Speed in kmph (Kilometer per hour) |
| WIND_DIR_DEGREE | INT | Wind direction in degree |
| WIND_DIR16POINT | STRING (3) | 16-Point wind direction compass |
| WEATHER_CODE | INT | A unique weather condition code |
| WEATHER_DESC | STRING(60) | Weather description text |
| WEATHER_ICON | INT | Weather Icon |
| PRECIPMM | REAL | Precipitation Amount (millimetre) |
