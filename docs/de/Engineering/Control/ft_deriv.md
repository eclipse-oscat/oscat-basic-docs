<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## FT_DERIV

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	IN** | REAL (Eingangssignal) |
| **K** | REAL (Multiplikator) |
| **RUN** | BOOL (Freigabe Eingang) |
| **Output	OUT** | REAL (Ableitung des Eingangssignals K * X / T) |
| | FT_DERIV ist ein D-Glied, oder auch LZI-Übertragungsglied, welches ein differenzierendes Übertragungsverhalten aufweist. Am Ausgang von FT_DERIV steht die Ableitung über die Zeit T in Sekunden zur Verfügung. Wenn das Eingangssignal in einer Sekunde von 3 auf 4 steigt so ist der Ausgang 1*K ( K * X / T = 1 * (4 – 3) / 1 = 1. |
| | Anders ausgedrückt ist die Ableitung des Eingangssignals die momentane Steigung des Eingangssignals. Mit dem Eingang RUN kann FT_DERIV enabled, beziehungsweise disabled werden. FT_DERIV arbeitet intern in Mikrosekunden und wird dadurch auch den Anforderungen  sehr schneller SPS Controller mit Zykluszeiten unter einer Millisekunde gerecht. |
| **Strukturbild** |  |

![ft_deriv](ft_deriv.gif)

![ft_deriv_diag](ft_deriv_diag.gif)
