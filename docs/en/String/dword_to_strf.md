<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: STRING

| | |
|:---|:---|
| **Input	IN** | DWORD (input value) |
| **N** | Int (length of the result string) |
| **Output** | STRING (result STRING) |
| | DWORD_TO_STRF converts a DWORD, Word or byte in a STRING of fixed length. The output string is exactly N digits, with leading zeros inserted or leading digits truncated. The maximum permitted length N is 20 digits. |

![dword_to_strf](dword_to_strf.gif)

**Example:**

```iecst
DWORD_TO_STRF(5123, 6) = '005123'
```
```iecst
DWORD_TO_STRF(5123, 3) = '123'
```
