<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktionsbaustein

| | |
|:---|:---|
| **Input	RES** | BOOL (Reset) |
| **Output	CT_MIN** | TIME (minimale gemessene Zykluszeit) |
| **CT_MAX** | TIME (maximale gemessene Zykluszeit) |
| **CT_LAST** | TIME (zuletzt gemessene Zykluszeit) |
| **SYSTIME** | TIME (Laufzeit seit dem letzten 	Start) |
| **SYSDAYS** | INT (Anzahl der Tage seit dem letzten Start) |
| **CYCLES** | DWORD (Anzahl der Zyklen seit dem letzten Start) |
| | CYCLE_TIME überwacht die Zykluszeiten einer SPS und stellt dem Anwender eine Reihe von Informationen über Zykluszeiten und Laufzeiten zur Verfügung. Die Gesamtzahl der Zyklen wird ebenfalls gemessen. Hiermit kann der Anwender zum Beispiel. sicherstellen, dass eine Funktion alle 100 Zyklen aufgerufen wird. Regelbausteine können Fehler melden, wenn die Zykluszeit zu lange wird und deshalb die Regelparameter nicht mehr garantiert werden können. |

![cycle_time](cycle_time.gif)
