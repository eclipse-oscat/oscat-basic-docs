<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion

| | |
|:---|:---|
| **Input	BFT** | INT (Windstärke nach der Beaufort Skala) |
| **Output	MS** | REAL (Windstärke in Meter / Sekunde) |
| | BFT_TO_MS rechnet Windgeschwindigkeiten nach der Beaufort Skala in Meter Pro Sekunde um. |
| **Die Berechnung erfolgt nach der Formel** |  |
| | BFT_TO_MS = 0.836m/s * B^3/2 |

![bft_to_ms](bft_to_ms.gif)
