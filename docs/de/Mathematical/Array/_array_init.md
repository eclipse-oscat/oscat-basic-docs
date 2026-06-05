<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _ARRAY_INIT

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	PT** | Pointer (Zeiger auf das Array) |
| **SIZE** | UINT (Größe des Arrays) |
| **INIT** | REAL (Initialwert) |
| **Output** | BOOL (TRUE) |
| **Die Funktion _ARRAY_INIT initialisiert ein beliebiges Array of REAL mit einem Initialwert. Beim Aufruf wird der Funktion ein Pointer auf das zu initialisierende Array und dessen Größe in Bytes übergeben. Unter CoDeSys lautet der Aufruf** | _ARRAY_INIT(ADR(Array), SIZEOF(Array), INIT), wobei Array der Name des zu manipulierenden Arrays ist. ADR ist eine Standardfunktion, die den Pointer auf das Array ermittelt und SIZEOF ist eine Standardfunktion, die die Größe des Arrays ermittelt. Die Funktion liefert nur TRUE zurück. Das durch den Pointer angegebene Array wird direkt im Speicher manipuliert. |
| | Diese Art der Bearbeitung von Arrays ist äußerst effizient, da kein zusätzlicher Speicher benötigt wird und keine Übergabewerte kopiert werden müssen. |

![_array_init](_array_init.gif)

**Beispiel:**

```iecst
_ARRAY_INIT(ADR(bigarray), SIZEOF(bigarray), 0) initialisiert bigarray mit 0.
```
