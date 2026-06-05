<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IS_LOWER

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	STR** | STRING (Eingabestring) |
| **Output** | BOOL (TRUE wenn STR nur Kleinbuchstaben enthält) |
| | IS_LOWER testet ob in der Zeichenkette STR nur Kleinbuchstaben enthalten sind. Wird etwas anderes als ein Kleinbuchstabe gefunden gibt die Funktion FALSE zurück. Sind in STR nur Kleinbuchstaben enthalten gibt die Funktion TRUE zurück. Bei der Prüfung wird die Globale Setup Konstante EXTENDED_ASCII berücksichtigt. Wenn EXTENDED_ASCII = TRUE ist werden Zeichen des erweiterten ASCII Zeichensatzes nach ISO 8859-1 berücksichtigt. Umlaute wie Ä,Ö,Ü werden nur dann berücksichtigt wenn die Globale Konstante  EXTENDED_ASCII = TRUE ist. |

![is_lower](is_lower.gif)
