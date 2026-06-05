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
| **Input	STR** | STRING (Eingabestring) |
| **Output** | BOOL (TRUE wenn STR nur Kontrollzeichen enthält) |
| | IS_CTRL testet ob in der Zeichenkette STR nur Kontrollzeichen enthalten sind. Wird ein anderes Zeichen gefunden gibt die Funktion FALSE zurück. Sind in STR nur Kontrollzeichen enthalten gibt die Funktion TRUE zurück. Kontrollzeichen sind die Zeichen mit dem Dezimalcode 0..31 und 127. |

![is_ctrl](is_ctrl.gif)
