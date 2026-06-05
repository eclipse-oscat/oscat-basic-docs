<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## WORLD_WEATHER_ICON_OSCAT

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	WW** | WORLD_WEATHER_DATA   (Weather data) |
| **INPUT	ACTIVATE** | BOOL (positive edge starts the query) |
| | The module replaces the original vendor-specific numbers on the weather icons by OSCAT standard icon numbers. Following a positive edge at ACTIVATE the elements (icon numbers) in the WORLD_WEATHER_DATA data structure is replaced. After querying the weather data using WORLD_WEATHER this module should be called subsequently. It is simply the parameter DONE from the module WORLD_WEATHER that is interconnected with ACTIVATE. |
| **The following elements will be adapted** |  |
| | WW.WORLD_WEATHER_CUR.WEATHER_ICON |
| | WW.WORLD_WEATHER_DAY[0..4].WEATHER_ICON |

![world_weather_icon_oscat](world_weather_icon_oscat.gif)
