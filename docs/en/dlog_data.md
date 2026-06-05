<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DLOG_DATA

The  Structure  DLOG_DATA is used for communication of the DLOG_ * modules. DLOG_DATA:

| Data field | Data Type | Description |
| --- | --- | --- |
| STORE_TYPE | BYTE | Typ of DLOG_STORE module |
| ADD_HEADER | BOOL | Header data store |
| ADD_DATA | BOOL | Cyclic data store |
| ADD_DATA_REQ | BOOL | Store data from external |
| CLOCK_TRIG | BOOL | DTI (  Date-Time  ) New value |
| ID_MAX | USINT | Number of blocks DLOG_* modules |
| DTI | DT | current  Date-Time  Value |
| UCB | UNI_CIRCULAR_BUFFER_DATA | Data Storage |
| NEW_FILE_STRING | STRING | New file name |
| NEW_FILE_RTRIG | BOOL | Edge new file was created |
