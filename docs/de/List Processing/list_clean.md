<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_CLEAN

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	SEP** | BYTE (Separationszeichen der Liste) |
| **I/O	LIST** | STRING(LIST_LENGTH) (Eingangsliste) |
| **Output** | BOOL (TRUE) |
| | LIST_CLEAN bereinigt eine Liste von leeren Elementen. Die Liste besteht aus  Zeichenketten (Elementen) die mit dem Separationszeichen SEP beginnen. |
| | LIST_CLEAN('&ABC$23&&NEXT', 38) = '&ABC&23&NEXT' |
| | LIST_CLEAN('&&23&&NEXT&', 38) = '&23&NEXT' |
| | LIST_CLEAN('&&&&', 38) = '' |

![list_clean](list_clean.gif)
