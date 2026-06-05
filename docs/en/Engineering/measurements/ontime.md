<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	IN** | BOOL (Input) |
| **RST** | BOOL (Reset input) |
| **Output	SECONDS** | UDINT (operating time in seconds) |
| **CYCLES** | UDINT (switch cycles of the input IN) |
| | ONTIME is an hour meter. It is summed up the entire time that the signal IN was since the last RESET to TRUE. Additionally, the number of the total on/off cycles is determined. The output values are of type UDINT. With the input RST, the output values will be reset at any time. The output values are not stored in variables of the module, but are applied externally attached and connected over IO (Pointer). This has the distinct advantage that as desired by the user the variables can be determined as RETAIN or PERSISTENT. It is thus possible to store old operating hours and restore it later, for example, at CPU change. |
| | The declaration of the variables at the inputs SECONDS and CYCLES must be of type UDINT and can either be created as a VAR, VAR RETAIN or VAR RETAIN PERSISTENT. |
| | The declaration of the variables for the operating time and cycles must be UDINT type and can be alternatively RETAIN or PERSISTENT. |
| | VAR RETAIN PERSISTENT |
| **Betriebszeit_in_Sekunden** | UDINT; |
| **Cycles** | UDINT; |
| | END_VAR |
| **The following table explains, RETAIN and PERSISTENT** |  |
| | Type variables  Retain and Persistent  retain their value during download, online change  and reset. In a cold reset or reset source, lose these variables the values. The user can save, but the values in the file system or network, and to restore itself, eg after changing the CPU. |

![ontime](ontime.gif)

![1000000000000244000000B5787DDD96](1000000000000244000000B5787DDD96.png)
![ontime_sample](ontime_sample.gif)
