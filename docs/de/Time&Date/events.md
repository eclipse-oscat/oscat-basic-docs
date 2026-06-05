<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## EVENTS

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	DATE_IN** | DATE (Eingangsdatum) |
| **ENA** | BOOL (Enable Eingang) |
| **I/O	ELIST** | ARRAY[0..49] of [HOLIDAY_DATA](../Data Types/holiday_data.md) |
| **Output	Y** | BOOL (TRUE, wenn DATE_IN ein Event ist) |
| **Name** | STRING(30) (Name des heutigen Events) |
| | Der Baustein EVENTS zeigt am Ausgang Y mit TRUE besondere Tage an und liefert auch den Namen des entsprechenden Events am Ausgang NAME. EVENTS kann zusätzlich zu einzelnen Tagen auch Events über mehrere Tage berücksichtigen. Im Array ELIST werden Name, Datum und Dauer der Events festgelegt. |
| | Im externen Array ELIST können nach folgendem Muster bis zu 50 solcher Events definiert werden. |
| ***.NAME** | STRING(30)	legt den Namen des Events fest |
| ***.DAY** | SINT 		Monatstag des Events |
| ***.MONTH** | SINT		Monat des Events |
| ***.USE** | SINT		Dauer des Events in Tagen |

![events](events.gif)

**Beispiel:**

```iecst
(NAME := 'Gründungstag', DAY := 13, MONTH := 7, USE := 1) festes Event „Gründungstag“ am 13. Juli für einen Tag. (NAME := 'Gründungstag', DAY := 13, MONTH := 7, USE := 0) Event an einem festen Datum USE=0 bedeutet es ist nicht aktiv. (NAME := 'Betriebsurlaub', DAY := 1, MONTH := 8, USE := 31) legt ein Event mit einer Dauer von 31 Tagen fest.
```
