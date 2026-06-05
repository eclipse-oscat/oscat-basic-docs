<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : BOOL

| | |
|:---|:---|
| **Input	IN** | BYTE (Zeichen) |
| **Output** | BOOL (TRUE IN ein Zeichen 0..9 ist) |
| | ISC_LOWER testet ob ein Zeichen IN ein Kleinbuchstabe ist, Ist IN ein Kleinbuchstabe gibt die Funktion TRUE zurück, wenn nicht gibt die Funktion FALSE zurück. Bei der Prüfung wird die Globale Setup Konstante EXTENDED_ASCII berücksichtigt. Wenn EXTENDED_ASCII = TRUE ist werden Zeichen des erweiterten ASCII Zeichensatzes nach ISO 8859-1 ausgewertet. |
| **Die folgende Tabelle Erläutert die Zeichencodes** |  |

![isc_lower](isc_lower.gif)

| Code | EXTENDED_ASCII = TRUE | EXTENDED_ASCII = FASLE |
| --- | --- | --- |
| 0..96, 123..223, 247, 255 | FALSE | FALSE |
| 97..122 | TRUE | TRUE |
| 224..246 | TRUE | FALSE |
| 248..254 | TRUE | FALSE |
