<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CONSTANTS_LOCATION

| | | |
|:---|:---|:---|
| ***.DEFAULT** | INT:= 1 | |
| ***.LMAX** | INT:= 3 | indicates how many places are defined. |
| ***.LANGUAGE** | ARRAY[1..5] of INT := 2,2,3,2,2; | |

This structure defines location-dependent constants. The variable LOCATION of the global variable list places it in the library.

(1 = Germany, 2 = Austria, France 3 =, 4 = Belgium-German,

5 = Italy, South Tyrol).

for each location, the language is defined.
