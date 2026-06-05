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
| **Input	IN** | REAL (input signal) |
| **RES** | REAL (input change) |
| **Output	Q** | BOOL (output) |
| **D** | REAL (last change of the input signal) |
| | A_TRIG monitors an input value on change and every time when the input value changes by more than RES, the module generates an output pulse for a cycle so that the new value can be processed. At the same time, the device remembers the current input value with which it compares with the input IN at the next cycle. At the output D the difference between IN and the stored value is displayed. |

![a_trig](a_trig.gif)
