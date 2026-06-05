<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ISC_HEX

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	IN** | BYTE (Zeichen) |
| **Output** | BOOL (TRUE IN ein Zeichen 0..9 ist)) |
| | ISC_HEX testet ob ein Zeichen IN ein Hexadezimales Zeichen ist, Ist IN ein Zeichen 0..9, A..F, a..f gibt die Funktion TRUE zurück, wenn nicht gibt die Funktion FALSE zurück. |
| | Die Zeichen 0..9 haben die Codes (48..57) |
| | Die Zeichen A..F haben die Codes (65..70) |
| | Die Zeichen a..f haben die Codes (97..102) |

![isc_hex](isc_hex.gif)
