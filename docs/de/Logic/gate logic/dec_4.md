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
| **A0** | BOOL (Adresse Bit0) |
| **A1** | BOOL (Adresse Bit1) |
| **Output	Q0** | BOOL (TRUE bei A0=0 und A1=0) |
| **Q1** | BOOL (TRUE bei A0=1 und A1=0) |
| **Q2** | BOOL (TRUE bei A0=0 und A1=1) |
| **Q3** | BOOL (TRUE bei A0=1 und A1=1) |
| **DEC_4 ist ein 4-Bit Dekodierbaustein. Ist A0=0 und A1=0 wird der Eingang D auf Ausgang Q0 geschaltet. Wenn A0=1 und A1=1 wird D auf Q3 geschaltet. Mit anderen Worten** | Q0=1, wenn D=1 und A0=0 und A1=0. |
| **Logische Verknüpfung** | Q0 = D & /A0 & /A1 |
| | Q1 = D & A0 & /A1 |
| | Q2 = D & /A0 & A1 |
| | Q3 = D & A0 & A1 |

![dec_4](dec_4.gif)

![dec_4_trace](dec_4_trace.gif)
