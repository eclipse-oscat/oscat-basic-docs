<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CHARNAME

| | |
|:---|:---|
| **Type	 Function** | STRING(10) |
| **Input	C** | BYTE (character code) |
| **Output** | STRING (character name) |
| | CHARNAME determines the character name for a character code. |

![charname](charname.gif)

![Object 1](Object 1)

**Beispiel:**

Example: CHARNAME(128) = 'euro' If no name is known for a code, the code is returned as a single character. For the Code 0 an empty string is returned. CHARNAME uses the global variables SETUP.CHARNAMES which includes the list of names with codes.
