<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BOOL

| | |
|:---|:---|
| **Input	TD** | TOD(time of day) |
| **TD** | TOD(time of day) |
| **STOP** | TOD(stop time) |
| **Output** | BOOL (  Return Value  ) |
| | TIME CHECK checks whether the daily time TD is between the START and STOP time. TIME CHECK returns TRUE if TD > = START and TD < STOP. IF START and STOP are defined in a way that START > STOP, the output with the start set to TRUE and remains by midnight TRUE until at the next day STOP is reached. |
| **The function has the following definition** |  |
| **START < STOP** | TD >= START AND TD < STOP |
| **START > STOP** | TD >= START OR TD < STOP |

![timecheck](timecheck.gif)
