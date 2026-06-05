<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## NET_VAR_X8

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	X** | NET_VAR_DATA (NET_VAR data structure) |
| **INPUT	IN_REAL1** | REAL (input) |
| **IN_REAL2** | REAL (input) |
| **IN_DINT1** | DINT (input) |
| **IN_DINT2** | DINT (input) |
| **IN_UDINT1** | DINT (input) |
| **IN_UDINT2** | DINT (input) |
| **IN_DWORD1** | DINT (input) |
| **IN_DWORD2** | DINT (input) |
| **OUTPUT	OUT_REAL1** | REAL (ouput) |
| **OUT_REAL2** | REAL (output) |
| **OUT_DINT1** | DINT (output) |
| **OUT_DINT2** | DINT (output) |
| **OUT_UDINT1** | DINT (output) |
| **OUT_UDINT2** | DINT (output) |
| **OUT_DWORD1** | DINT (output) |
| **OUT_DWORD2** | DINT (output) |
| **ID** | BYTE (ID) |
| | The module NET_VAR_X8 is used for bidirectional transmission of each two REAL, DINT, UINT, DWORD values ​​from the master to slave and vice versa. The  signals IN1..8 are collected and passed to the other side (control) on the same module at the same position as OUT1..8 again. |
| | Simultaneously, the input data on the opposite side (other control) is passed here as BUF_OUT again. |
| | ID parameter indicates the current identification number of the module instance. If the configuration of the master and the slave program is differently (incorrectly) that ID number is passed as a fault in the module NET_VAR_CONTROL. |

![net_var_x8](net_var_x8.gif)
