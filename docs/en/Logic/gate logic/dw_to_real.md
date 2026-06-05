<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: REAL

| | |
|:---|:---|
| **Input	X** | DWORD (input) |
| **Output** | REAL (output value) |
| | DW_TO_REAL copies the bit pattern of a DWORD (IN) to a REAL. These bits are copied without regard to their meaning. The function REAL_TO_DW is the inverse so that the conversion of REAL_TO_DW and then DW_TO_REAL result in the output value. The IEC standard DWORD_TO_REAL function converts the value of the DWORD to a REAL value. |

![dw_to_real](dw_to_real.gif)
