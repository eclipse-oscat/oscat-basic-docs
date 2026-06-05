<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## The structure ESR_DATA is used for  Error  and Status  Reporting  modules.

| | | |
|:---|:---|:---|
| ***.TYP** | BYTE | Data Type |
| ***.ADRESS** | STRING(10) | Adress designation |
| ***.DS** | DT | Date / time stamp |
| ***.TS** | TIME | Timestamp in milliseconds |
| ***.DATA** | ARRAY[0..7] OF BYTE | Data packet |
