<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCALE_R

| | |
|:---|:---|
| **Type	Funktion** | REAL |
| **Input	X** | REAL (Eingangswert) |
| **I_LO** | REAL (Eingangswert min) |
| **I_HI** | REAL (Eingangswert max) |
| **O_LO** | REAL (Ausgangswert min) |
| **O_HI** | REAL (Ausgangswert max) |
| **Output** | REAL (Ausgangswert) |
| | SCALE_R skaliert einen Eingangswert REAL und errechnet einen Ausgangswert in REAL. Der Eingangswert X wird dabei auf I_LO und I_HI begrenzt. SCALE_D(IN, 4, 20, 0, 100) skaliert einen Eingang mit 4 .. 20 mA auf den Ausgang 0..100. SCALE_R kann auch mit negativen Ausgangswerten und negativer Steigung arbeiten, die Werte I_LO und I_HI müssen aber immer so spezifiziert werden, dass ILO < I_HI ist. |

![scale_r](scale_r.gif)
