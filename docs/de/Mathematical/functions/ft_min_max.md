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
| **RST** | BOOL (Reset Eingang) |
| **Output	MX** | REAL (Maximalwert des Eingangssignal) |
| **MN** | REAL (Minimalwert des Eingangssignal) |
| | FT_MIN_MAX Speichert den Minimal- und Maximalwert eines Eingangssignals IN und stellt diese beiden Werte an den Ausgängen MN und MX zur Verfügung bis er durch einen Reset wieder gelöscht wird. Ein Reset setzt MN und MX auf den zum Zeitpunkt des Resets anliegenden Eingangswert zurück. |

![ft_min_max](ft_min_max.gif)
