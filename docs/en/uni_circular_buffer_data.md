<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## UNI_CIRCULAR_BUFFER_DATA

The  Structure  UNI_CIRCULAR_BUFFER_DATA is used for data management for the module UNI_CIRCULAR_BUFFER UNI_CIRCULAR_BUFFER_DATA:

| Data field | Data Type | Description |
| --- | --- | --- |
| D_MODE | INT | MODE (command number) |
| D_HEAD | WORD | Header information Read / Write |
| D_STRING | STRING(STRING_LENGTH) | STRING Read / Write |
| D_REAL | REAL | REAL Read / Write |
| D_DWORD | DWORD | DWORD Read / Write |
| BUF_SIZE | UINT | Number of bytes in the buffer |
| BUF_COUNT | UINT | Number of elements in the buffer |
| BUF_USED | USINT | Level (0-100%) |
| BUF | NW_BUF_LONG | Data BUFFER |
| _GetStart | UINT | Internal: read pointer |
| _GetEnd | UINT | Internal: read pointer |
| _Last | UINT | Intern: Data pointer |
| _First | UINT | Intern: Data pointer |
