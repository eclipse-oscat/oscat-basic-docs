<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	 Function  : BYTE

| | |
|:---|:---|
| **Input	STR** | STRING(10) (String input) |
| **Output** | BYTE (character code) |
| | CHARCODE returns the byte code of a  Named Characters.  A  List  the  Codes  with  Name  located under the function charName. If no character known, for the name in STR  0 is returned. If STR consists of only one character, then the code of this character   returned. CHARCODE uses the global variables SETUP.CHARNAMES which include the list of names with codes. |

![charcode](charcode.gif)

**Beispiel:**

Example:	CHARCODE('euro') = 128 and corresponds to the character € CHARCODE(',') = 44
