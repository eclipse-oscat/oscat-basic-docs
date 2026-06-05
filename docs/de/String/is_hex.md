<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IS_HEX

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	STR** | STRING (Eingabestring) |
| **Output** | BOOL (TRUE wenn STR nur Hexadezimalzeichen enthält) |
| | IS_HEX testet ob in der Zeichenkette STR nur Hexadezimalzeichen enthalten sind. Wird ein anderes Zeichen gefunden gibt die Funktion FALSE zurück. Sind in STR nur Hexadezimalzeichen enthalten gibt die Funktion TRUE zurück. Hexadezimalzeichen sind die Zeichen mit dem Dezimalcode 0..9, a..f und A..F. |

![is_hex](is_hex.gif)
