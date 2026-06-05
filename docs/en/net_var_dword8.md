<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## NET_VAR_DWORD8

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	X** | NET_VAR_DATA (NET_VAR data structure) |
| **INPUT	IN 1..8** | DWORD (input DWORD) |
| **OUTPUT	OUT 1..8** | DWORD (output DWORD) |
| **ID** | BYTE (ID) |
| | The module NET_VAR_DWORD8 is used for bidirectional transmission of eight DWORD from the master to slave and vice versa. The signals DWORD IN1..8 are collected and passed to the other side (control) on the same module at the same position as OUT1..8 again. |
| | Simultaneously, the on the opposite side (other control) passed input datawords passed here as a OUT1..8 again. |
| | ID parameter indicates the current identification number of the module instance. If the configuration of the master and the slave program is differently (incorrectly) that ID number is passed as a fault in the module NET_VAR_CONTROL. |

![net_var_dword8](net_var_dword8.gif)
