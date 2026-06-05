<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TIMER_EVENT

| | | |
|:---|:---|:---|
| ***.TYP** | BYTE | Ereignistyp |
| ***.CHANNEL** | BYTE | Kanal |
| ***.DAY** | BYTE | Tag oder Tage |
| ***.START** | TOD | Anfangszeit |
| ***.DURATION** | TIME | Dauer |
| ***.LAND** | BYTE | Logisches AND |
| ***.LOR** | BYTE | Logisches OR |
| ***.LAST** | DT | letzte Aktivität des Ereignisses |

Die Struktur TIMER_EVENT definiert und speichert Vorgaben für Timer und Ereignisse.
