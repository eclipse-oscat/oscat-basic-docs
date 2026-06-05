<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DLOG_REAL

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	X** | DLOG_DATA (DLOG data structure) |
| **INPUT	VALUE** | REAL (process value) |
| **N** | INT (number of decimal places) |
| **D** | STRING(1) (decimal punctuation character) |
| **COLUMN** | STRING (40) (process value name) |
| **DELTA** | REAL (difference value) |
| | The module DLOG_REAL is for logging (recording) of a process value of type REAL, and can only be used in combination with a DLOG_STORE_* module, as this coordinates of the data structure X to record the data. Using parameter N defines the number of desired decimal places. See documentation on the module REAL_TO_STRF.  The D input determines which character represents the decimal point. Passed with no sign of parameter D, automatically ',' is used. 
At recording formats that support a process value name, such as at DLOG_STORE_FILE_CSV a name can be provided at COLUMN". If with DELTA parameter a value not equal 0.0 is specified, the automatic data logging is enabled via differential monitoring. Changing the value of VALUE to + / - DELTA automatically stores a record. This feature can be applied in parallel to the central trigger on the DLOG_STORE_ * module. |

![dlog_real](dlog_real.gif)
