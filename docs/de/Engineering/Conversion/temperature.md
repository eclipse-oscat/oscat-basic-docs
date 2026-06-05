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
| **Input	K** | REAL (Temperatur nach Kelvin Skala) |
| **C** | REAL (Temperatur nach Celsius Skala) |
| **F** | REAL (Temperatur nach Fahrenheit Skala) |
| **RE** | REAL (Temperatur nach Reaumur Skala) |
| **RA** | Real (Temperatur nach Rankine Skala) |
| **Output	YK** | REAL (Temperatur nach Kelvin Skala) |
| **YC** | REAL (Temperatur nach Celsius Skala) |
| **YF** | REAL (Temperatur nach Fahrenheit Skala) |
| **YRE** | REAL (Temperatur nach Reaumur Skala) |
| **YRA** | Real (Temperatur nach Rankine Skala) |
| | Der Baustein TEMP konvertiert verschiedene in der Praxis gebräuchliche Einheiten für Temperatur. Normalerweise wird nur der zu konvertierende Eingang belegt und die restlichen Eingänge bleiben frei. Werden jedoch mehrere Eingänge gleichzeitig mit Werten beaufschlagt, so werden die Werte aller Eingänge entsprechend umgewandelt und dann aufsummiert. |
| | 1 K = 273.15 °C |
| | 1 °C = 273.15 K |
| | 1 °F = °C * 1.8 + 32 |
| | 1 Re = °C * 0.8 |
| | 1 Ra = K * 1.8 |

![temperature](temperature.gif)
