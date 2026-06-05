<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : STRING

| | |
|:---|:---|
| **Input	IN** | BYTE (Eingangswert) |
| **Output** | STRING(8) (Ergebnis STRING) |
| | BYTE_TO_STRB konvertiert ein Byte in einen STRING fester Länge. Der Ausgangsstring ist exakt 8 Stellen lang und entspricht der bitweisen Schreibweise des Wertes IN. Der Ausgangsstring besteht aus den Zeichen '0' und '1'. Das  niederwertigste Bit ist rechts im STRING. Falls ein STRING mit weniger als 8 Zeichen benötigt wird kann dieser mit der Standardfunktion RIGHT() entsprechend abgeschnitten werden. Der Aufruf RIGHT(BYTE_TO_STRB(X),4) ergibt einen STRING mit 4 Zeichen, die dem Inhalt der untersten 4 Bit von X entspricht. |

![byte_to_strb](byte_to_strb.gif)

**Beispiel:**

```iecst
BYTE_TO_STRB(3) = '00000011'
```
