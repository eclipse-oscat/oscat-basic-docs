<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Diese Struktur definiert Ortsabhängige Konstanten. Die Variable SETUP der Globalen Variablenliste stellt diese in der Bibliothek zur Verfügung.

| | | |
|:---|:---|:---|
| ***.EXTENDED_ASCII** | BOOL := TRUE erweitert den ASCII Zeichensatz um | Umlaute z.B. ÄÖÜ |
| ***.CHARNAMES[1..4]** | STRING(253) speichert Unicode Zeichennamen | |
| ***.MTH_OFS** | ARRAY[1..12] OF INT := 0, 31, 59, 90, 120, 151, 181, 212, | 243, 273, 304, 334; |
| ***.DECADES** | ARRAY[0..8] OF REAL := 1,10,100,1000,10000,100000, | |

MTH_OFS wird in verschiedenen Datumsfunktionen verwendet, im Array steht der jeweilige Tagesoffset für die Monate des Jahres. Der 1. Februar eines Jahre ist z.B. der Tag 31 + 1.

1000000,10000000,100000000;
