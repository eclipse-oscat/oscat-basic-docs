<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _STRING_TO_BUFFER

| | |
|:---|:---|
| **Type	Funktion** | INT |
| **Input	STR** | STRING (zu kopierender String) |
| **POS** | INT (Position ab der der String in den Puffer kopiert wird) |
| **PT** | POINTER TO BYTE (Adresse des Puffers) |
| **SIZE** | UINT (Größe des Puffers) |
| **Output** | INT (Liefert die nächste Position im Buffer nach dem |
| | eingesetzten String zurück) |
| **Die Funktion _STRING_TO_BUFFER kopiert einen String in ein beliebiges Array of Byte. Der String wird ab einer beliebigen Position POS im Puffer abgelegt. Das erste Element im Array hat die Positionsnummer 0. Beim Aufruf wird der Funktion ein Pointer auf das zu bearbeitende Array und dessen Größe in Bytes übergeben. Unter CoDeSys lautet der Aufruf** | _STRING_TO_BUFFER(STR, POS, ADR(Array), SIZEOF(Array)), wobei Array der Name des zu manipulierenden Arrays ist. ADR ist eine Standardfunktion, die den Pointer auf das Array ermittelt und SIZEOF ist eine Standardfunktion, die die Größe des Arrays ermittelt. Die Funktion liefert die erste Position im Buffer nach dem eingesetzten String zurück. Das durch den Pointer angegebene Array wird direkt im Speicher manipuliert. |
| | Diese Art der Bearbeitung von Arrays ist äußerst effizient, da kein zusätzlicher Speicher benötigt wird und keine Übergabewerte kopiert werden müssen. |

![string_to_buffer](string_to_buffer.gif)

**Beispiel:**

Beispiel: _STRING_TO_BUFFER(STR, POS, ADR(bigarray), SIZEOF(bigarray))
