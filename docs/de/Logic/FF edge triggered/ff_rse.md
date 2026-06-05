<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktionsbaustein

| | |
|:---|:---|
| **Input	CS** | BOOL (flankensensitiver Set) |
| **CR** | BOOL (flankensensitiver Reset) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q** | BOOL (Ausgang) |
| | FF_RSE ist ein flankengetriggertes RS Flip-Flop. Der Ausgang Q wird durch eine steigende Flanke an CS gesetzt und durch eine steigende Flanke an CR gelöscht. Treten beide Flanken (CS und CR) gleichzeitig auf, so wird der Ausgang auf FALSE gesetzt. Ein Asynchroner Reset Eingang RST setzt den Ausgang jederzeit auf FALSE. |

![ff_rse](ff_rse.gif)
