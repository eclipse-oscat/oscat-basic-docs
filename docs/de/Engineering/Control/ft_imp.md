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
| **Input	IN** | REAL (Eingangssignal) |
| **T** | TIME (Zeitkonstante) |
| **K** | REAL (Multiplikator) |
| **Output	OUT** | REAL (Hochpass Mit Zeitkonstante T) |
| | FT_IMP Ist ein Hochpass-Filter mit Zeitkonstante T und Multiplikator K. Eine sprunghafte Änderung am Eingang wird am Ausgang sichtbar, kling aber nach der Zeit T bereits um 63% und nach 3 * T um 95% ab. Somit ist nach einer sprunghaften Änderung des Eingangssignals von 0 auf 10 der Ausgang zum Zeitpunkt der Eingangsänderung 10 und kling nach 1 * T auf 3,7 und nach 3 * T auf 0,5 ab und wird dann allmählich wieder 0. |
| **Strukturbild** |  |

![ft_imp](ft_imp.gif)

![ft_imp_diag](ft_imp_diag.gif)
