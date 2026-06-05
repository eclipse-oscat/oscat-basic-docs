<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MS_TO_BFT

| | |
|:---|:---|
| **Type** | Funktion |
| **Input	MS** | INT (Windstärke nach der Beaufort Skala) |
| **Output	MS** | REAL (Windstärke in Meter / Sekunde) |
| | MS_TO_BFT rechnet Windgeschwindigkeiten von Meter / Sekunde in die Beaufort Skala um. |
| **Die Berechnung erfolgt nach der Formel** |  |
| | MS_TO_BFT = (MS * 1.196172)^2/3 |

![ms_to_bft](ms_to_bft.gif)
