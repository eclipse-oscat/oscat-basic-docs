<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CHK_REAL

| | |
|:---|:---|
| **Type	Funktion** | BYTE |
| **Input	X** | REAL (Zu testender Wert) |
| **Output** | BYTE (Rückgabewert) |
| | CHK_REAL prüft X auf gültigen Wertebereich. |
| **Die Rückgabewerte sind** |  |
| **#00** | gültige Gleitpunktzahl |
| **#20** | + unendlich |
| **#40** | - unendlich |
| **#80** | NAN |
| | für weitere Informationen siehe auch die Floating Point Spezifikation IEEE754. |

![chk_real](chk_real.gif)
