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
| ***.TYP** | BYTE | Event Type |
| ***.CHANNEL** | BYTE | Channel |
| ***.DAY** | BYTE | Day or days |
| ***.START** | TOD | Start time |
| ***.DURATION** | TIME | Duration |
| ***.LAND** | BYTE | Logical AND |
| ***.LOR** | BYTE | Logical OR |
| ***.LAST** | DT | last activity of the event |

The structure TIMER_EVENT defines and stores defaults for timers and events.
