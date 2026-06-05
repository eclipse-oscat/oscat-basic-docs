<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LENGTH

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	M** | REAL (Meter) |
| **P** | REAL (Typographischer Punkt) |
| **IN** | REAL (Inch) |
| **FT** | REAL (Foot) |
| **YD** | REAL (Yard) |
| **MILE** | REAL (Mile) |
| **SM** | REAL (Internationale Seemeile) |
| **FM** | REAL (Fathom) |
| **Output	YM** | REAL (Meter) |
| **YP** | REAL (Typographischer Punkt) |
| **YIN** | REAL (Inch) |
| **YFT** | REAL (Foot) |
| **YYD** | REAL (Yard) |
| **YMILE** | REAL (Mile) |
| **YSM** | REAL (Internationale Seemeile) |
| **YFM** | REAL (Fathom) |
| | Der Baustein LENGTH konvertiert verschiedene in der Praxis gebräuchliche Einheiten für Längeneinheiten. Normalerweise wird nur der zu konvertierende Eingang belegt und die restlichen Eingänge bleiben frei. Werden jedoch mehrere Eingänge gleichzeitig mit Werten beaufschlagt, so werden die Werte aller Eingänge entsprechend umgewandelt und dann aufsummiert. |
| | 1 P = 0,376065 mm (Einheit aus dem Druckereigewerbe) |
| | 1 IN = 25,4 mm |
| | 1 FT = 0,3048 m |
| | 1 YD = 0,9144 m |
| | 1 MILE = 1609,344 m |
| | 1 SM = 1852 m |
| | 1 FM = 1,829 m |

![length](length.gif)
