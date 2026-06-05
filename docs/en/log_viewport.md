<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LOG_VIEWPORT

| | |
|:---|:---|
| **Type** | Function module |
| **IN_OUT	LC** | LOG_CONTROL |
| **LV** | us_LOG_VIEWPORT |
| **The module LOG_VIEWPORT is used to index a list of LOG_CONTROL messages, which are currently in the virtual view. To move around within the message list (scroll), a scroll offset can be specified by LV.MOVE_TO_X. A positive value   scroll in direction of newer reports and a negative value in the direction of the earlier messages. The number of lines in the message list of the virtual view is given by LV.COUNT. The current messages in the virtual view are stored in LV.LINE_ARRAY [x], and are available for further processing. A change in the message list is always announced with LV.UPDATE** | = TRUE, and the user has to reset. |
| | The following LV.MOVE_TO_X values produce a special behavior. |
| | +30000 = display previous Messages (beginning of the ring buffer) |
| | +30001 = display latest messages (end of the ring buffer) |
| | +30002 = one full page in direction of recent messages. |
| | +30003 = One full page in direction of older messages |

![log_viewport](log_viewport.gif)
