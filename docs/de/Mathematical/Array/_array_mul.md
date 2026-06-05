<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _ARRAY_MUL

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	PT** | Pointer (Zeiger auf das Array) |
| **SIZE** | UINT (Größe des Arrays) |
| **X** | REAL (Multiplikator) |
| **Output** | BOOL (TRUE) |
| **Die Funktion _ARRAY_MUL multipliziert jedes Element eines beliebigen Array of REAL mit den Wert X. Beim Aufruf wird der Funktion ein Pointer auf das zu initialisierende Array und dessen Größe in Bytes übergeben. Unter CoDeSys lautet der Aufruf** | _ARRAY_MUL(ADR(Array), SIZEOF(Array), X), wobei Array der Name des zu manipulierenden Arrays ist. ADR ist eine Standardfunktion, die den Pointer auf das Array ermittelt und SIZEOF ist eine Standardfunktion, die die Größe des Arrays ermittelt. Die Funktion liefert nur TRUE zurück. Das durch den Pointer angegebene Array wird direkt im Speicher manipuliert. |
| | Diese Art der Bearbeitung von Arrays ist äußerst effizient, da kein zusätzlicher Speicher benötigt wird und keine Übergabewerte kopiert werden müssen. |
| **Aufruf** | _ARRAY_MUL(ADR(bigarray), SIZEOF(bigarray), X) |

![_array_mul](_array_mul.gif)

**Beispiel:**

```iecst
[0,-2,3,-1-5]; X = 3 wird umgewandelt in [0,-6,9,-3,-15]
```
