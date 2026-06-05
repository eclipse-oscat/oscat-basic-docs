<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DEG

| | |
|:---|:---|
| **Type	Funktion** | REAL |
| **Input	Rad** | REAL (Winkel in Bogenmaß) |
| **Output** | REAL (Winkel in Grad) |
| | Die Funktion DEG konvertiert einen Winkelwert von Bogenmaß in Grad. Dabei wird berücksichtigt das der Eingang nicht größer als 2π sein darf. Wenn RAD größer als 2π ist wird entsprechend 2π abgezogen bis der Eingang RAD zwischen 0 und 2π liegt. |
| **DEG(π) = 180 Grad,** | DEG(3π) = 180 Grad |
| **DEG(0) = 0 Grad,** | DEG(2π) = 0 Grad |

![deg](deg.gif)
