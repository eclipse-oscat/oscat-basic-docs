<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : DWORD

| | |
|:---|:---|
| **Input	IN** | DWORD (Eingangsdaten) |
| **N** | INT (Anzahl der zu schiebenden Bits) |
| **Output** | DWORD (Ergebnis) |
| | SHR1 schiebt das Eingangs DWORD um N Bits nach Rechts und füllt die N linken Bits mit 1en auf. Im Gegensatz zur IEC Standard Funktion SHL die beim Schieben mit Nullen aufgefüllt wird bei SHR1 mit Einsen Aufgefüllt. |

![shr1](shr1.gif)

**Beispiel:**

Beispiel:	SHR1(11110000,2) ergibt 11111100
