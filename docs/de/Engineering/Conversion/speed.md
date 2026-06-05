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
| **Input	MS** | REAL (Meter / Sekunde) |
| **KMH** | REAL (Kilometer / Stunde) |
| **KN** | REAL (Knoten = Seemeilen / Stunde) |
| **MH** | REAL (Meilen / Stunde) |
| **Output	YMS** | REAL (Meter / Sekunde) |
| **YKMH** | REAL (Kilometer / Stunde) |
| **YKN** | REAL (Knoten = Seemeilen / Stunde) |
| **YMH** | REAL (Meilen / Stunde) |
| | Der Baustein SPEED konvertiert verschiedene in der Praxis gebräuchliche Einheiten für Geschwindigkeiten. Normalerweise wird nur der zu konvertierende Eingang belegt und die restlichen Eingänge bleiben frei. Werden jedoch mehrere Eingänge gleichzeitig mit Werten beaufschlagt, so werden die Werte aller Eingänge entsprechend umgewandelt und dann aufsummiert. |
| | 1 ms = Meter / Sekunde = 3,6 km/h |
| | 1 kmh = Kilometer / Stunde = 1/3,6 m/s |
| | 1 kn = Knoten = 1 Seemeile / Stunde = 0,5144 m/s |
| | 1 mh = Meilen / Stunde = 0,44704 m/s |

![speed](speed.gif)
