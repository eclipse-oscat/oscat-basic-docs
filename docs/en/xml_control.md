<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## XML_CONTROL

XML_CONTROL data structure:

| Data field | Data Type | Description |
| --- | --- | --- |
| COMMAND | WORD | Control commands (binary occupancy) |
| START_POS | UINT | (Buffer index of first character) |
| STOP_POS | UINT | (Buffer-index of the last characters) |
| COUNT | UINT | Element number |
| TYPE | INT | Type code of the current element |
| LEVEL | UINT | Current hierarchy / level |
| PATH | STRING(STRING_LENGTH) | Hierarchy as TEXT (PATH) |
| ELEMENT | STRING(STRING_LENGTH) | current item as TEXT |
| ATTRIBUTE | STRING(STRING_LENGTH) | Current attributes as TEXT |
| VALUE | STRING(STRING_LENGTH) | Current value as TEXT |
| BLOCK1_START | UINT | Start position of block 1 |
| BLOCK1_STOP | UINT | Stop position of Unit 1 |
| BLOCK2_START | UINT | Start position of block 2 |
| BLOCK2_STOP | UINT | Stop position of Unit 2 |
