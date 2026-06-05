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
| **E** | BOOL (Freigabe Eingang) |
| **N** | INT (Anzahl der Werte über die der Mittelwert gebildet wird) |
| **RST** | BOOL (Reset Eingang) |
| **Output** | REAL (Gleitender Mittelwert über die letzten N Werte) |
| | Der Funktionsbaustein FT_AVG berechnet einen gleitenden Mittelwert jeweils über die letzten N Werte. Durch den Eingang RST können die gespeicherten Werte gelöscht werden. N ist definiert von 0 .. 32. N=0 bedeutet das Ausgangssignal = Eingangssignal ist. N=5 bildet den Mittelwert über die letzten 5 Werte. Der Mittelwert wird maximal über 32 Werte gebildet. Durch den Eingang E kann kontrolliert werden, wann der Eingang gelesen wird. Hierdurch kann auf einfache Weise ein Sample und Hold Baustein wie zum Beispiel SH_1 mit FT_AVG verknüpft werden. Beim ersten Aufruf von FT_AVG wird der Puffer mit dem Eingangssignal geladen, um zu vermeiden dass ein Ramp-up stattfindet. |
| | Im folgenden Beispiel liest SH_1 einmal pro Sekunde den Eingangswert Signal_in und gibt diese Werte einmal pro Sekunde an FT_AVG weiter, welcher dann aus den letzten 8 Werten den Mittelwert bildet. |

![ft_avg](ft_avg.gif)

![ft_avg_sample](ft_avg_sample.gif)
