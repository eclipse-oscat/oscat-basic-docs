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
| **Input	PT** | TIME (Periodendauer) |
| **AM** | REAL (Signal Amplitude) |
| **OS** | REAL (Signal Offset) |
| **Output	Q** | BOOL (Binäres Ausgangssignal) |
| **OUT** | REAL (Analoges Ausgangssignal) |
| | GEN_RDM ist ein Zufalls-Signalgenerator. Er erzeugt am Ausgang OUT einen neuen Wert in PT Zeitabständen. Der Ausgang Q wird für genau einen Zyklus TRUE, wenn sich der Ausgang OUT verändert hat. Der Eingang AM und OS legen die Amplitude und den Offset für den Ausgang OUT fest. Wenn die Eingänge OS und AM nicht beschaltet werden sind die Vorgabewerte 0 und 1. |
| | Das folgende Beispiel zeigt eine Traceaufzeichnung für die Eingangswerte PT=100ms, AM=10 und OS=5. Der Ausgang erzeugt Werte alle 100ms im Bereich von 0 .. 10. |

![gen_rdm](gen_rdm.gif)

![gen_rdm_trace](gen_rdm_trace.gif)
