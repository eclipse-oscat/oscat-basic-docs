<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## STATUS_TO_ESR

| | |
|:---|:---|
| **Type	Function** | [ESR_DATA](../Data Types/esr_data.md) |
| **Input	 STATUS** | BYTE (status byte) |
| **ADRESS** | Byte (address, bytes) |
| **LINE** | Byte (input number) |
| **DT_IN** | DATE_TIME (time-date-input) |
| **TS** | TIME (time for timestamp) |
| **Output** | [ESR_DATA](../Data Types/esr_data.md) (ESR data block) |
| | STATUS_TO_ESR  generates a record from the input values. |
| | A STATUS in the range between 1.. 99 is an error message and will be marked as Type 1.  Status 100 .. 199 is characterized as type 2 and 200 .. 255 is marked as Type 3 (  Debug I  nformation). |
| **The ESR data at the output consist of the following items** |  |
| **.TYPE** | 1 = error, 2 = State, 3 = Debug |
| **.ADRESS** | Byte address of ISR data recording |
| **.LINE** | Line number (input) of the ESR data recording |
| **.DS** | Date stamp of type DATE_TIME |
| **.DT** | Timestamp of type TIME (PLC-timer) |
| **.Data** | Data block of 8 bytes |

![status_to_esr](status_to_esr.gif)
