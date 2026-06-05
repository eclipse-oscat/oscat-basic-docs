<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _ARRAY_ADD

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	PT** | Pointer (Zeiger auf das Array) |
| **SIZE** | UINT (Größe des Arrays) |
| **X** | REAL (zu addierender Wert) |
| **Output** | BOOL (TRUE) |
| **Die Funktion _ARRAY_ADD addiert zu jedem Element eines beliebigen Array of REAL den Wert X. Beim Aufruf wird der Funktion ein Pointer auf das zu initialisierende Array und dessen Größe in Bytes übergeben. Unter CoDeSys lautet der Aufruf** | _ARRAY_ADD(ADR(Array), SIZEOF(Array), X), wobei Array der Name des zu manipulierenden Arrays ist. ADR ist eine Standardfunktion, die den Pointer auf das Array ermittelt und SIZEOF ist eine Standardfunktion, die die Größe des Arrays ermittelt. Die Funktion liefert nur TRUE zurück. Das durch den Pointer angegebene Array wird direkt im Speicher manipuliert. |
| | Diese Art der Bearbeitung von Arrays ist äußerst effizient, da kein zusätzlicher Speicher benötigt wird und keine Übergabewerte kopiert werden müssen. |
| **Aufruf** | _ARRAY_ADD(ADR(bigarray), SIZEOF(bigarray), X) |
| **Beipiel** | [0,-2,3,-1-5]	 ; X = 3 wird umgewandelt in [3,1,6,2,-2] |

![_array_add](_array_add.gif)
