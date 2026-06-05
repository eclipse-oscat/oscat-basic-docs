<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ESR_MON_X8

| | |
|:---|:---|
| **Type** | Function module |
| **Input	S0..7** | Byte  (  status Inputs  ) |
| **DT_IN** | DATE_TIME (time-date-time stamp for input) |
| **Mode** | Byte (designate the type of processing of messages) |
| **Output	ESR_FLAG** | BOOL (TRUE when messages are present) |
| **IN/OUT	 ESR_OUT** | array [0..7]  of  ESR_DATA (collected messages) |
| **Setup	A0..7** | STRING  (10) (signal address of the inputs) |
| | ESR_MON_X8 collects status messages of up to 8 ESR compatible modules, provides them with a  Timestamp  ,  date stamp  ,  input number and a module address. The collected messages are buffered and passed to a protocol module. If messages for transmission are present, this is indicated by the signal ESR_FLAG. At input DT_IN the current time, which is used for the timestamp of the messages should be provided. The MODE input determines which status messages should be passed. |
| | When the MODE input is not wired, automatically all messages are processed. |
| **The ESR data at the output consist of the following items** | .TYP	1 = error, 2 = State, 3 = Debug 
 . ADRESS	Byte address of ESR data recording 
.LINE	Line number (input) of the ESR data recording 
.DS	Date stamp of type DATE_TIME 
.DT	Timestamp of type TIME (PLC  Timer  ) 
.Data	Data Byte 0 contains the status message |

| | An application example for the module is in the description of ESR_COLLECT. |

![esr_mon_X8](esr_mon_X8.gif)
