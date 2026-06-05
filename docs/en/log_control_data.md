<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LOG_CONTROL

us_LOG_VIEWPORT data structure:

| Name | Type | Properties |
| --- | --- | --- |
| NEW_MSG | STRING(STRING_LENGTH) | New Message - Text |
| NEW_MSG_OPTION | DWORD | New message - Option 
BYTE 3: Reserve
BYTE 2: Level
BYTE 1: Backcolor
BYTE 0: Frontcolor |

| LEVEL | BYTE | Given log level |
| SIZE | INT | Size of the array (maximum index) |
| RESET | BOOL | Reset / delete the entries |
| PRINTF | ARRAY[1.11] OF STRING(STRING_LENGTH) | Parameter data for PRINT_SF block |
| MSG | ARRAY[0.N] OF STRING(STRING_LENGTH) | Array for message - text |
| MSG_OPTION | ARRAY[0.N] OF DWORD | Array ofor messages - Option 
 BYTE 3: Reserve 
BYTE 2: Level 
BYTE 1: Back Color 
BYTE 0: Color front |

| UPDATE_COUNT | UINT | Update-counter (increased with each new message) |
| IDX | INT | Current Issue Index |
| RING_MODE | BOOL | BUFFER enabled overflow / Ringmode enabled |
