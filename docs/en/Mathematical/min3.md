<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MIN3

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input	IN1** | REAL (input 1) |
| **IN2** | REAL (input 2) |
| **IN3** | REAL (input 3) |
| **Output** | REAL (Minimum 3 inputs) |
| | The function  MIN3 returns the minimum value of 3 inputs. Basically, the function MIN in standard functionality IEC61131-3 should have a variable number of inputs. However, since in some systems   the function MIN supportes only two inputs, the function MIN3 is available. |

![min3](min3.gif)

**Example:**

```iecst
MIN3(1,3,2) = 1.
```
