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
| **Input	STR** | STRING (Eingabe STRING) |
| **Output** | STRING (Ergebnis STRING) |
| | Die Funktion EXEC arbeitet Mathematische Ausdrücke ab und liefert das Ergebnis als STRING zurück. Der Ausdruck darf nur ein einfacher Ausdruck mit einem Operator und ohne Klammern sein. Bei Fehlern, wie zum Beispiel einem Teilen durch Null liefert EXEC den Rückgabestring 'ERROR'. |
| **Die zulässigen Operatoren sind** | +, - *, /, ^, SIN, COS, TAN, SQRT. |
| | Als Zahlen sind REAL und Integer-Zahlen zulässig. |

![exec](exec.gif)

**Beispiel:**

Beispiel:	EXEC('3^2') = '9' EXEC('4-2') = '2'
