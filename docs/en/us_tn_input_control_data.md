<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## us_TN_INPUT_CONTROL_DATA

A variable of type us_TN_INPUT_CONTROL_DATA can use to parameterize a INPUT_CONTROL element and to process element related inputs / events. us_TN_INPUT_CONTROL_DATA:

| Data field | Data Type | Description |
| --- | --- | --- |
| by_Input_Exten_Code | BYTE | Extended Key Code |
| by_Input_ASCII_Code | BYTE | Key Code ASCII |
| bo_Input_ASCII_IsNum | BOOL | Key code is a digit |
| in_Title_X_Offset | INT | Title Text X Offset |
| in_Title_Y_Offset | INT | Title Text Y Offset |
| by_Title_Attr | BYTE | Title text attributes |
| st_Title_String | STRING | st_Title_String |
| in_Cursor_X | INT | current cursor X position |
| in_Cursor_Y | INT | current cursor Y position |
| IN_TYPE | INT | Element Type |
| in_X | INT | Element X position |
| in_Y | INT | Element Y position |
| in_Cursor_Pos | INT | current cursor position |
| by_Attr_mF | BYTE | Attributes for element with focus |
| by_Attr_oF | BYTE | Attributes for element without focus |
| in_selected | INT | Text element is selected |
| st_Input_Mask | STRING | Input mask |
| st_Input_Data | STRING(STRING_LENGTH) | Text input current |
| st_Input_String | STRING | text copy  after entering |
| st_Input_ToolTip | STRING | Text for ToolTip |
| in_Input_Option | INT | Text Options |
| bo_Input_Entered | BOOL | Text RETURN key pass |
| bo_Input_Hidden | BOOL | Text hidden input with '*' |
| bo_Input_Only_Num | BOOL | Text only allow number entry |
| bo_Focus | BOOL | Element has focus |
| bo_Update_Input | BOOL | Element due to input redraw |
| bo_Update_All | BOOL | Element draw from scratch |
