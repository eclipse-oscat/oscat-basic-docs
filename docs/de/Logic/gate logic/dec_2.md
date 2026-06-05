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
| **Input	D** | BOOL (Eingangs Bit) |
| **A** | BOOL (Adresse) |
| **Output	Q0** | BOOL (TRUE bei A=0) |
| **Q1** | BOOL (TRUE bei A=1) |
| **DEC_2 ist ein 2-Bit Dekodierbaustein. Ist A=0, so wird der Eingang D auf Ausgang Q0 geschaltet. Ist A=1, so wird D auf Q1 geschaltet. Mit anderen Worten** | Q0=1 wenn D=1 und A=0. |
| **Logische Verknüpfung** | Q0 = D & /A; Q1 = D & A |

![dec_2](dec_2.gif)

![dec_2_trace](dec_2_trace.gif)
