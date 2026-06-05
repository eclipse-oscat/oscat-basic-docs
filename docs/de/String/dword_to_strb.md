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
| **Input	IN** | DWORD (Eingangswert) |
| **Output** | STRING(32) (Ergebnis String) |
| | DWORD_TO_STRB konvertiert ein DWORD, Word oder Byte in einen STRING fester Länge. Der Ausgangsstring ist exakt 32 Stellen lang und entspricht der bitweisen Schreibweise des Wertes IN. Der Ausgangsstring besteht aus den Zeichen '0' und '1'. Das  niederwertigste Bit steht links im STRING. DWORD_TO_STRB kann Eingangsformate Byte, Word und DWORD Typen verarbeiten. Der Ausgang ist aber unabhängig vom Eingangstyp immer ein STRING mit 32 Zeichen. Falls ein kürzerer STRING benötigt wird, kann dieser mit der Standard Funktion RIGHT() entsprechend abgeschnitten werden. Der Aufruf RIGHT(DWORD_TO_STRB(X),8) ergibt einen STRING mit 8 Zeichen die dem Inhalt des untersten Bytes von X entsprechen. |

![dword_to_strb](dword_to_strb.gif)

**Beispiel:**

Beispiel: DWORD_TO_STRB(127) = '00000000000000000000000001111111'
