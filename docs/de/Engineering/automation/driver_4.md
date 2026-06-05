<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DRIVER_4

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	SET** | BOOL (asynchroner Set Eingang) |
| **IN0..IN3** | BOOL (Schalteingänge) |
| **RST** | BOOL (asynchroner Reset Eingang) |
| **Output	Q0 .. Q3** | BOOL (Schaltausgänge) |
| | DRIVER_1 ist ein Treiberbaustein dessen Ausgänge Q durch die Eingänge IN geschaltet werden. eine detaillierte Beschreibung des Bausteins befindet sich unter DRIVER_1. DRIVER_4 stellt im Gegensatz zu DRIVER_1 4 Schaltausgänge zur Verfügung, hat aber ansonsten die gleiche Funktionalität. |
| **Setup	TOGGLE_MODE** | BOOL (Mode des Eingangs IN) |
| **TIMEOUT** | TIME (Maximale Ontime der Ausgänge) |

![driver_4](driver_4.gif)
