<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	D** | BOOL (input bit) |
| **A0** | BOOL (address bit0) |
| **A1** | BOOL (address bit1) |
| **A2** | BOOL (address bit 2) |
| **Output	Q0** | BOOL (TRUE with A0 = 0 and A1 = 0 and A2 = 0) |
| **Q1** | BOOL (TRUE = 1 with A0 and A1 = 0 and A2 = 0) |
| **Q2** | BOOL (true when A0 = 0 and A1 = 1 and A2 = 0) |
| **Q3** | BOOL (TRUE with A0 = 1 and A1 = 1 and A2 = 0) |
| **Q4** | BOOL (TRUE with A0 = 0 and A1 = 0 and A2 = 1) |
| **Q5** | BOOL (TRUE with A0 = 1 and A1 = 0 and A2 = 1) |
| **Q6** | BOOL (TRUE with A0 = 0 and A1 = 1 and A2 = 1) |
| **Q7** | BOOL (TRUE with A0 = 1 and A1 =1 and A2 = 1) |
| | DEC_8 is an 8-bit decoder module If A0 = 0 and A1 = 0 and A2 = 0, the D input is pased to output Q0, if A0 = 1 and A1 = 1 and A2 = 1 the D is connected to Q3. In other words, Q0 = 1 if D = 1 and A0 = 0 and A1 = 0 A2 = 0. |
| **The following diagram illustrates the logic of the module** |  |
| **Logical connection** |  |
| **Q0 = D & /A0 & /A1 & /A2** | Q1 = D & A0 & /A1 & /A2 |
| **Q2 = D & /A0 & A1 & /A2** | Q3 = D & A0 & A1 & /A |
| **Q4 = D & /A0 & /A1 & A2** | Q5 = D & A0 & /A1 & A2 |
| **Q6 = D & /A0 & A1 & A2** | Q7 = D & A0 & A1 & A2 |

![dec_8](dec_8.gif)

![dec_8_trace](dec_8_trace.gif)
