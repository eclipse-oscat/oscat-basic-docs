<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : REAL

| | |
|:---|:---|
| **Input	T** | REAL (Temperatur in °C) |
| **RS** | REAL (Widerstand bei TS °C) |
| **TS** | REAL (Temperatur bei RS) |
| **Output** | REAL (Widerstandswert) |
| | RES_SI berechnet den Widerstand eines SI-Widerstandsfühlers aus den Eingangswerten T (Temperatur in °C) und RS, Widerstand bei TS in °C. Im Gegensatz zu den Bausteinen RES_NI und RES_PT deren R0 bei 0°C angegeben wird ist die Widerstandsangabe RS bei SI Fühler bei unterschiedlichen Temperaturen (z.B. 25°C bei KTY10). Deshalb hat der Baustein einen Eingang für RS und einen weiteren für TS. |
| **Die Berechnung erfolgt nach der Formel** |  |
| | RES_SI = RS + A*(T-TS) + B*(T-TS)² |
| | A = 7.64E-3 |
| | B = 1.66E-5 |
| | Die Berechnung ist geeignet für einen Temperaturbereich von -50..+150°C. |

![res_si](res_si.gif)
