<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : REAL

| | |
|:---|:---|
| **Input	FLT** | STRING(20) (Gleitkommazahl) |
| **Output** | REAL (REAL Wert der Gleitkommazahl) |
| | FLOAT_TO_REAL wandelt eine als STRING vorliegende Gleitpunktzahl in einen Datentyp REAL um. Bei Der Umwandlung werden '.' oder ',' als Komma interpretiert und 'E' oder 'e' als Trennzeichen des Exponenten. Die Zeichen '-0123456789' werden Ausgewertet und alle anderen in FLT vorkommenden Zeichen werden ignoriert. |

![float_to_real](float_to_real.gif)
