<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IP_FIFO_DATA

IP_FIFO_DATA data structure:

| Data field | Data Type | Description |
| --- | --- | --- |
| X | ARRAY [1..128] OF BYTE | FIFO memory with registered ID's |
| Y | ARRAY [1..128] OF BYTE | Number of entries per ID's |
| ID | BYTE | Last assigned ID (highest ID) |
| MAX_ID | BYTE | Maximum number of applications per ID |
| INIT | BOOL | Initialization performed |
| EMPTY | BOOL | FIFO is empty |
| FULL | BOOL | FIFO is full (should not happen!) |
| TOP | INT | Maximum number of entries in FIFO |
| NW | INT | write-index FIFO |
| NR | INT | read-index FIFO |
