<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : STRING

| | |
|:---|:---|
| **Input	IN** | STRING (Eingangswert) |
| **CX** | STRING (Alle Zeichen die gelöscht werden sollen) |
| **Output** | STRING (Ergebnis STRING) |
| | DEL_CHARS löscht alle Zeichen aus einer Zeichenkette die in der Zeichenkette CX enthalten sind. |
| | CLEAN('Nr.1 23#', ' #ABCDEFG') = 'Nr.123' |

![del_chars](del_chars.gif)
