<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion

| | |
|:---|:---|
| **Input	A** | [VECTOR_3](../../Data Types/vector_3.md) (Vektor mit den Koordinaten X, Y, Z) |
| **B** | [VECTOR_3](../../Data Types/vector_3.md) (Vektor mit den Koordinaten X, Y, Z) |
| **Output** | BOOL (TRUE wenn die beiden Vektoren parallel sind) |
| | V3_PAR wird dann TRUE wenn die beiden Vektoren A und B Parallel sind. Ein Nullvektor ist Parallel zu jedem Vektor da er keine Richtung hat. Zwei Vektoren A und B die in Gegensätzliche Richtung zeigen sind Parallel. |
| | V3_PAR([1,1,1],[2,2,2]) = TRUE |
| | V3_PAR([1,1,1],[-1,-1,-1]) = TRUE |
| | V3_PAR([1,2,3],[0,0,0]) = TRUE |
| | V3_PAR([1,2,3],[1,0,0]) = FALSE |

![v3_par](v3_par.gif)
