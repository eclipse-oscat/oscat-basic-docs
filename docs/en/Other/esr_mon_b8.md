<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ESR_MON_B8

| | |
|:---|:---|
| **Type** | Function module |
| **Input	S0..7** | BOOL (signal input) |
| **DT_IN** | DATE_TIME (time-date-input stamp for time-stamp) |
| **Output	ESR_FLAG** | BOOL (TRUE, if ESR data are available) |
| **IN/OUT	ESR_OUT** | ESR_Data (ESR_data ouput) |
| **Setup	A0..7** | STRING(10) (designation of the inputs) |
| | ESR_MON_B8 monitors up to 8 binary signals to change, and provides them with a  timestamp  and a name. The collected messages are buffered and passed to a protocol module on ESR_OUT. The output ESR_FLAG is set to TRUE when messages are present. |
| **The ESR data at the output consist of the following items** |  |
| **.TYPE** | 11  rising  edge , 10  falling  edge |
| **.ADRESS** | Byte address of ISR data recording |
| **.LINE** | Line number (input) of the ESR data recording |
| **.DS** | Date stamp of type DATE_TIME |
| **.DT** | Timestamp of type TIME (PLC- Timer  ) |
| **.Data** | Data block blank of 8 bytes |
| | An application example for the module is in the description of ESR_COLLECT. |

![esr_mon_b8](esr_mon_b8.gif)
