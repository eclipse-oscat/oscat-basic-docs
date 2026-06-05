<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ESR_MON_R4

| | |
|:---|:---|
| **Type** | Function module |
| **Input	R0.. 3** | REAL (signal input) |
| **DT_IN** | DATE_TIME (time-date-input stamp for time-stamp) |
| **Output	ESR_FLAG** | BOOL (TRUE, if ESR data are available) |
| **IN/OUT	ESR_OUT** | ESR_Data (ESR_data ouput) |
| **Setup	A0..3** | STRING(10) (signal address of the inputs) |
| **A0..3** | STRING(10) (signal address of the inputs) |
| | ESR_MON_R4 monitors up to 4 analog signals for changes and provides them with a  time  s  stamp  and the address of the input signal. The collected messages are buffered and passed to a protocol module on ESR_OUT. The output ESR_FLAG is set to TRUE when messages are present. A change of an input is recorded only when the input has changed more than the in threshold S predetermined value. |
| **.TYPE** | 20  Floating point |
| **.ADRESS** | Byte address of ISR data recording |
| **.LINE** | Line number (input) of the ESR data recording |
| **.DS** | Date stamp of type DATE_TIME |
| **.DT** | Timestamp of type TIME (PLC- Timer  ) |
| **.Data** | Data Block 4 byte real value |
| | An application example for the module is in the description of ESR_COLLECT. |

![esr_mon_r4](esr_mon_r4.gif)
