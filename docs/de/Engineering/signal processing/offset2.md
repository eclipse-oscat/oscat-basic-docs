<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## OFFSET2

| | |
|:---|:---|
| **Type** | Funktion |
| **Input	X** | REAL (Eingangssignal) |
| **O1** | REAL (Enable Offset 1) |
| **O2** | REAL (Enable Offset 2) |
| **O3** | REAL (Enable Offset 3) |
| **D** | BOOL (EnableDefault) |
| **Output** | REAL (Ausgangswert mit Offset) |
| **Setup	Offset_1** | REAL (Offset der addiert wird, wenn O1=TRUE) |
| **Offset_2** | REAL (Offset der addiert wird, wenn O2=TRUE) |
| **Offset_3** | REAL (Offset der addiert wird, wenn O3=TRUE) |
| **Offset_4** | REAL (Offset der addiert wird, wenn O4=TRUE) |
| **DEFAULT** | REAL (Wird anstelle von X verwendet, wenn TRUE) |
| | Die Funktion OFFSET2 addiert einen Offset zu einem Eingangssignal abhängig vom Binären Wert an O1 .. O4.  Werden mehrere Offsets gleichzeitig selektiert, so wird der Offset mit der höchsten Nummer addiert und die anderen ignoriert. Werden O1 und O3 gleichzeitig TRUE, so wird nur Offset_3 addiert und nicht Offset_1. Mit dem Eingang D kann ein Default-Wert anstelle des Eingangs X auf den Addierer geschaltet werden. Die Offsets und der Defaultwert werden über Setup-Variablen definiert. |
| | Weitere Erläuterungen und ein Beispiel finden Sie unter Offset, welches sehr ähnliche Funktion aufweist. Offset2 addiert nur jeweils einen (den mit der höchsten Nummer) Offset, während Offset alle selektierten gleichzeitig addiert. |

![offset2](offset2.gif)
