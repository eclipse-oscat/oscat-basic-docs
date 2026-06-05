<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IP_FIFO

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	FIFO** | IP_FIFO_DATA   (IP-FIFO management data) |
| **ID** | BYTE (current ID assigned by IP_FIFO module) |
| **STATE** | BYTE (control commands and status messages) |
| | This module is used in combination with IP_CONTROL for resource management. This makes it possible that client applications request exclusive access permissions and   can also give back. By the FIFO is ensured that each participant equally often gets the resource access assigned. |
| | In the first call of the module automatically a new unique application ID is assigned, which one the administration in FIFO is managed. The STATE parameter is changed by the application as well as from IP_FIFO module. Each application may register by default only once in the FIFO. |
| **STATE** |  |
| **Procedure** |  |
| | 1. application set the STATE to 1 |
| | 2. Access permission are required as is the STATE = 2 |
| | 3. if resource is free,   and access rights are present, then 
 STATE=3 |

| | 4. If the application has the resource resp. the access needs
 not anymore the application sets STATE to 4. Thereafter 
  IP_FIFO releases the resource again and set STATE to 0. |

| | 5. Process is repeated (same or other application) |

![ip_fifo](ip_fifo.gif)

**Beispiel:**

Example is found in the module IP_CONTROL!

| Value | State Message |
| --- | --- |
| 0 | no action |
| 1 | Privilege request |
| 2 | Privilege request has been accepted in FIFO |
| 3 | Privilege obtained (allowing resource access) |
| 4 | Privilege remove |
| 5 | Privilege was again removed from FIFO |
