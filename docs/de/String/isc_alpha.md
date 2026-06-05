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
| **Output** | BOOL (TRUE IN ein Zeichen a..z, A..Z oder Umlaut ist) |
| | ISC_ALPHA testet ob das Zeichen IN ein alphabetisches Zeichen ist, Ist IN ein Zeichen A..Z, a..z oder ein beliebiger Umlaut gibt die Funktion TRUE zurück, wenn nicht gibt die Funktion FALSE zurück. Bei der Prüfung wird die Globale Setup Konstante EXTENDED_ASCII berücksichtigt. Wenn EXTENDED_ASCII = TRUE ist werden Zeichen des erweiterten ASCII Zeichensatzes nach ISO 8859-1 ausgewertet. Umlaute wie Ä,Ö,Ü werden nur dann berücksichtigt wenn die Globale Konstante  EXTENDED_ASCII = TRUE ist. |
| **Die folgende Tabelle Erläutert die Codes** |  |

![is_alpha](is_alpha.gif)

| Code | EXTENDED_ASCII = TRUE | EXTENDED_ASCII = FASLE |
| --- | --- | --- |
| 0..64 | FALSE | FALSE |
| 65..90 | TRUE | TRUE |
| 91..96 | FALSE | FALSE |
| 97..122 | TRUE | TRUE |
| 123..191 | FALSE | FALSE |
| 192..214 | TRUE | FALSE |
| 215 | FALSE | FALSE |
| 216..246 | TRUE | FALSE |
| 247 | FALSE | FALSE |
| 248..255 | TRUE | FALSE |
