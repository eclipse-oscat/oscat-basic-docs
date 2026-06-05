<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MANUAL_4

| | |
|:---|:---|
| **Type** | Function module |
| **Input	I0..I3** | BOOL (inputs) |
| **MAN** | BOOL (manual override) |
| **M0..M3** | BOOL (input signals in manual mode) |
| **STP** | BOOL (Asynchronous  Step  in manual mode) |
| **Output	Q0..Q3** | BOOL (output signals) |
| **STATUS** | BYTE (ESR compliant status output) |
| | MANUAL_4 can override 4 digital signal in manual mode. As long as MAN = FALSE the outputs Q follows direct the input I. As soon as the inputs MAN = TRUE, the outputs follow the states of the inputs M. The STP input follow   is in manual mode, a rotating set of outputs are generated. STP is active only during manual operation. When in manual operation of STP registered a rising edge, then  the outputs follow not the inputs MX but are switched cyclically with STP. At the first rising edge of STP, only the output Q0 gets active and the next  edge of STP the module switch to the output Q1 and so on. Once the input MAN goes back to FALSE the outputs Q follows again the input I. The ESR compliant status output passes the switching states. |

![manual_4](manual_4.gif)

| STATUS | Condition |
| --- | --- |
| 100 | Automatic Mode MAN = FALSE, Q0 = I0, Q1 = I1, Q2 = I2, Q3 = I3 |
| 101 | Manual Mode MAN = TRUE, Q0 = M0, Q1 = M1, Q2 = M2, Q3 = M3 |
| 110,111,112,113 | Step Mode for Output Q0, Q1, Q2, Q3 |
