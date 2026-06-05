<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CALENDAR

A variable type CALENDAR can be used for to provide modul wide calendar data. In the section date and time functions are various functions to update the calendar continuously. *.UTC: DT	Universal world time *.LDT: DT	Local time *.LDate: DATE	Local date *.LTOD: TOD	Local time of day *.YEAR: INT	Local year *.MONTH: INT	Local months *.DAY: INT	Local days *.WEEKDAY: INT	Local weekday *.OFFSET: INT	Offset of local time to universal time in minutes *.DST_EN: BOOL	Daylight saving time Enable *.DST_ON: BOOL	Daylight saving time is On *.NAME: STRING (5)	Time zone name *.LANGUAGE : INT	Language (See  Language  Setup) *.LONGITUDE: REAL	Longitude of the place *.LATITUDE: REAL	Latitude of the place *.SUN_RISE: TOD	Time of sunrise (LTC) *.SUN_SET: TOD	Time of sunset (LTC) *.SUN_MIDDAY: TOD	World time when the Sun stands in the south (LTC) *.SUN_HEIGTH: REAL	the highest altitude of the sun on the horizon *.SUN_HOR: REAL	Horizontal solar altitude in degrees from north *.SUN_VER: REAL	Vertical position of the sun above the horizon *.NIGHT: BOOL	TRUE if night *.HOLIDAY: BOOL	TRUE if holiday *.HOLY_NAME : STRING (30)	Name of the holiday *.WORK_WEEK: _ INT	current work week
