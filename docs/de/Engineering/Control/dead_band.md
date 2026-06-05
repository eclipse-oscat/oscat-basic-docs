<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DEAD_BAND

| | |
|:---|:---|
| **Type** | Funktion |
| **Input	X** | REAL (Eingangswert) |
| **L** | REAL (Lockout Wert) |
| **Output** | REAL (Ausgangswert) |
| | DEAD_BAND ist eine lineare Übertragungsfunktion mit Totzone. Die Funktion verschiebt den positiven Teil der Kurve um -L und den negativen Teil der Kurve um +L. DEAD_BAND wird benutzt um Quantisierungsrauschen und andere Rauschanteile aus einem Signal zu filtern. DEAD_BAND wird zum Beispiel in Regelkreisen eingesetzt um zu verhindern das der Regler dauernd in kleinen Schritten schaltet und dabei das Stellglied übermäßig belastet und abnutzt. |
| | DEAD_BAND = X - SGN(X)*L wenn ABS(X) > L wenn ABS(X) > L |
| | DEAD_BAND = 0 wenn ABS(X) <= L |

![dead_band](dead_band.gif)

![dead_band1](dead_band1.gif)
