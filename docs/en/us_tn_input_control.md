<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## us_TN_INPUT_CONTROL

A variable of type us_TN_INPUT_CONTROL can be used to parameterize and manage various INPUT_CONTROL elements, and as well as to represent the  ToolTip information. us_TN_INPUT_CONTROL:

| Data field | Data Type | Description |
| --- | --- | --- |
| bo_Enable | BOOL | Processing enable / disable |
| bo_Update_all | BOOL | All elements redraw |
| bo_Reset_Fokus | BOOL | set Focus on first Element |
| in_Fokus_at | INT | Element with an active focus |
| in_Count | INT | Number of INPUT_CONTROL elements |
| in_ToolTip_X | INT | ToolTip Text X Offset |
| in_ToolTip_Y | INT | ToolTip Text Y Offset |
| by_ToolTip_Attr | BYTE | ToolTip text attributes (color) |
| in_ToolTip_Size | INT | ToolTip text length |
| usa_TN_INPUT_CONTROL_DATA | ARRAY [1..20] OFus_TN_INPUT_CONTROL_DATA |  |
