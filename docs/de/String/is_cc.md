<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IS_CC

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	STR** | STRING (Eingabestring) |
| **CMP** | STRING (Vergleichszeichen) |
| **Output** | BOOL (TRUE wenn STR nur die im STRING CMP aufgelisteten |
| | Zeichen enthält) |
| | IS_CC testet ob in der Zeichenkette STR nur die in STR aufgelisteten Zeichen enthalten sind. Wird ein anderes Zeichen gefunden gibt die Funktion FALSE zurück. |
| **Beipiele** |  |
| | IS_CC('3.14', '0123456789.') = TRUE |
| | IS_CC('-3.14', '0123456789.') = FALSE |

![is_cc](is_cc.gif)
