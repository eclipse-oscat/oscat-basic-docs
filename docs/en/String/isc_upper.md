<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ISC_UPPER

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	IN** | BYTE (characters) |
| **Output** | Type |
| | ISC_UPPER tests whether a sign IN is a captial letter, if IN is a capital letter, the function returns TRUE, if not the function returns FALSE. In examining the Global Setup EXTENDED_ASCII constant is considered. If EXTENDED_ASCII = TRUE the extended ASCII character-set to be considered in accordance with ISO 8859-1. |
| **The  The following table describes the character codes** |  |

![isc_upper](isc_upper.gif)

| Code | EXTENDED_ASCII=TRUE | EXTENDED_ASCII = FASLE |
| --- | --- | --- |
| 0..64,91..191,215, 223..255 | FALSE | FALSE |
| 65..90 | TRUE | TRUE |
| 192..214 | TRUE | FALSE |
| 216..222 | TRUE | FALSE |
