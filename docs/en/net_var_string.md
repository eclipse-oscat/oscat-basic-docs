<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## NET_VAR_STRING

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	X** | NET_VAR_DATA (NET_VAR data structure) |
| **IN** | STRING(string_length) (input string) |
| **OUT** | STRING (string_length) (output-string) |
| **OUTPUT		ID** | BYTE (ID) |
| | The module NET_VAR_STRING is used for bidirectional transmission of STRING from the master to slave and vice versa. The STRING in the parameters IN will be recorded and passed on the other side (control) on the same module at the same position as OUT parameter. |
| | At the same time the input String on the opposite side of the (other control) is passed here as a OUT value again. |
| | ID parameter indicates the current identification number of the module instance. If the configuration of the master and the slave program is differently (incorrectly) that ID number is passed as a fault in the module NET_VAR_CONTROL. |

![net_var_string](net_var_string.gif)
