<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IP2GEO

IP2GEO data structure:

| Name | Type | Properties |
| --- | --- | --- |
| STATE | BOOL | Data is valid |
| Data is valid | DWORD | IP address of the geographical data |
| COUNTRY_CODE | STRING(2) | Country code   (ISO format)   eg AT = Austria |
| COUNTY_NAME | STRING(20) | Name of the country |
| REGION_CODE | STRING(2) | Region Code (FIPS format) eg 09 = Vienna |
| REGION_NAME | STRING(20) | Name of region |
| CITY | STRING(20) | Name of the city |
| GEO_LATITUDE | REAL | Latitude of the place |
| GEO_LONGITUDE | REAL | Longitude of the place |
| TIME_ZONE_NAME | STRING(20) | Time zone name |
| GMT_OFFSET | INT | Offset from Universal Time in minutes |
| IS_DST | BOOL | DST active |
