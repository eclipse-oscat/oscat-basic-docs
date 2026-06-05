<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## OVERRIDE

| | |
|:---|:---|
| **Type** | Function |
| **Input	X1** | REAL (input signal 1) |
| **X2** | REAL  (Input signal 2) |
| **X3** | REAL (input signal 3) |
| **E1** | BOOL (  Enable  Signal 1) |
| **E2** | BOOL (  Enable  Signal 2) |
| **E2** | BOOL (  Enable  Signal 3) |
| **Output** | REAL (output value |
| | OVERRIDE supplies at the output Y the input value (X1, X2, X3), whose absolute value is the largest of all. The inputs X1, X2 and X3 may each individually be enabled with the inputs E1, E2 and E3. if one of the input signals E1, E2 or E3 to FALSE, the corresponding input X1, X2 or X3 is not considered. One of many possible applications of OVERRIDE is for example, the query of three sensors with the highest value overrides the others. With the inputs of E in the diagnosis case, each sensor can be queried individually, or a defective sensor can be switched off. |

![override](override.gif)

**Beispiel:**

Example: OVERRIDE(10,-12,11, TRUE, TRUE, TRUE) = -12 OVERRIDE(10,-12,11, TRUE, FALSE, TRUE) = 11 OVERRIDE(10,-12,11, FALSE, FALSE, FALSE) = 0
