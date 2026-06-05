<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Die Struktur ESR_DATA wir für Error- und Status- Reporting Bausteine verwendet.

| | | |
|:---|:---|:---|
| ***.TYP** | BYTE | Datentyp |
| ***.ADRESS** | STRING(10) | Adressbezeichnung |
| ***.DS** | DT | Datums- Zeit- Stempel |
| ***.TS** | TIME | Zeitstempel in Millisekunden |
| ***.DATA** | ARRAY[0..7] OF BYTE | Datenpaket |
