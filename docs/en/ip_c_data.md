<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IP_C

IP_C data structure:

| Data field | Data Type | Description |
| --- | --- | --- |
| C_MODE | BYTE | Type of connection |
| C_PORT | WORD | Port Number |
| C_IP | DWORD | coded IP v4 address |
| C_STATE | BYTE | Status of the connection |
| C_ENABLE | BOOL | Connection release |
| R_OBSERVE | BOOL | Receive data monitor |
| TIME_RESET | BOOL | Reset the monitoring times |
| ERROR | DWORD | Error Code |
| FIFO | IP_FIFO_DATA | Data structure of the access management(No user access required) |
| MAILBOX | ARRAY [1..16] OF BYTE | Mailbox: data area for module data exchange |
