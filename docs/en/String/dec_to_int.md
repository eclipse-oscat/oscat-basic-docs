<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: INT

| | |
|:---|:---|
| **Input	DEC** | STRING(10) (decimal-encoded string) |
| **Output** | INT (output value) |
| | The function DEC_TO_INT converts a decimal encoded string into a byte value. Here only decimal characters '0 '.. '9' and '-' are interpreted, others in DEC occurring characters are ignored . |

![dec_to_int](dec_to_int.gif)

**Beispiel:**

Example:	DEC_TO_INT ('-34') is -34.
