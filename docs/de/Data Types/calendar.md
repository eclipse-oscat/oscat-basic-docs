<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CALENDAR

| | | |
|:---|:---|:---|
| ***.UTC** | DT | Universelle Weltzeit |
| ***.LDT** | DT | Lokalzeit |
| ***.LDATE** | DATE | Lokales Datum |
| ***.LTOD** | TOD | Lokale Tageszeit |
| ***.YEAR** | INT | Lokales Jahr |
| ***.MONTH** | INT | Lokales Monat |
| ***.DAY** | INT | Lokaler Tag |
| ***.WEEKDAY** | INT | Lokaler Wochentag |
| ***.OFFSET** | INT | Offset der Lokalzeit zur Weltzeit in Minuten |
| ***.DST_EN** | BOOL | Sommerzeit Enable |
| ***.DST_ON** | BOOL | Sommerzeit ist Aktiv |
| ***.NAME** | STRING(5) | Name der Zeitzone |
| ***.LANGUAGE** | INT | Sprache (Siehe Language Setup) |
| ***.LONGITUDE** | REAL | Längengrad des Ortes |
| ***.LATITUDE** | REAL | Breitengrad des Ortes |
| ***.SUN_RISE** | TOD | Zeitpunkt des Sonnenaufgangs (LTC) |
| ***.SUN_SET** | TOD | Zeitpunkt des Sonnenuntergangs (LTC) |
| ***.SUN_MIDDAY** | TOD | Weltzeit wenn Sonne im Süden Steht (LTC) |
| ***.SUN_HEIGTH** | REAL | höchster Sonnenstand über Horizont |
| ***.SUN_HOR** | REAL | Horizontaler Sonnenstand in Grad von Nord |
| ***.SUN_VER** | REAL | Vertikaler Sonnenstand über den Horizont |
| ***.NIGHT** | BOOL | TRUE wenn Nacht |
| ***.HOLIDAY** | BOOL | TRUE wenn Feiertag |
| ***.HOLY_NAME** | STRING(30) | Name des Feiertages |
| ***.WORK_WEEK** | _ INT | aktuelle Arbeitswoche |

Eine Variable vom Typ CALENDAR kann benutzt werden um Programmweite Kalenderdaten zur Verfügung zu stellen. Im Abschnitt Datums und Zeitfunktionen finden sich diverse Funktionen um den Kalender fortlaufend zu aktualisieren.
