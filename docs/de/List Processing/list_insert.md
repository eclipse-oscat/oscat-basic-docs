<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_INSERT

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	SEP** | BYTE (Separationszeichen der Liste) |
| **POS** | INT (Position des Listenelements) |
| **INS** | STRING (Neues Element) |
| **I/O	LIST** | STRING(LIST_LENGTH) (Eingangsliste) |
| **Output** | BOOL (TRUE) |
| | LIST_INSERT setzt ein Element an der Stelle POS in eine Liste ein. Die Liste besteht aus  Zeichenketten (Elementen) die mit dem Separationszeichen SEP beginnen. Das erste Element der Liste hat die Position 1. Wird eine Position größer als das letzte Element der Liste angegeben werden leere Elemente an die Liste angehängt bis INS an seiner vorgesehenen Position am Ende der Liste steht. Ist POS = 0 wird das neue Element an den Anfang der Liste gestellt. |

![list_insert](list_insert.gif)

**Beispiel:**

```iecst
LIST_INSERT('&ABC&23&&NEXT',38,0,'NEW')= '&NEW&ABC&23&&NEXT' LIST_INSERT('&ABC&23&&NEXT',38,1,'NEW')= '&NEW&ABC&23&&NEXT' LIST_INSERT('&ABC&23&&NEXT',38,3,'NEW')= '&ABC&23&NEW&&NEXT' LIST_INSERT('&ABC&23&&NEXT',38,6,'NEW')= '&ABC&23&&NEXT&&NEW'
```
