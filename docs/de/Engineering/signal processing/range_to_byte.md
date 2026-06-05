<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RANGE_TO_BYTE

| | |
|:---|:---|
| **Type** | Funktion |
| **Input	X** | REAL (Eingangswert) |
| **LOW** | REAL (untere Bereichsgrenze) |
| **HIGH** | REAL (Obere Bereichsgrenze) |
| **Output** | BYTE (Ausgangswert) |
| | RANGE_TO_BYTE wandelt einen REAL Wert in einen BYTE Wert. Ein Eingangswert X der dem Wert LOW entspricht wird dabei in einen Ausgangswert von 0 gewandelt und ein Eingangswert X der dem Eingangswert HIGH entspricht wird in einen Ausgangswert von 255 gewandelt. Der Eingang X wird auf den Bereich von LOW bis HIGH begrenzt, ein Überlauf des BYTE Ausgangs kann  deshalb nicht stattfinden. |

![range_to_byte](range_to_byte.gif)
