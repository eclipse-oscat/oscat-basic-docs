<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## us_TN_MENU_POPUP

A variable of type us_TN_MENU_POPUP can be used to parameterize a POPUP item, to display it and to process element related inputs. us_TN_MENU_POPUP:

| Data field | Data Type | Description |
| --- | --- | --- |
| st_Menu_Text | STRING(STRING_LENGTH) | Menu items |
| in_Menu_E_Count | INT | Number of menu items |
| in_X | INT | Menu X position |
| in_Y | INT | Menu Y position |
| in_Cols | INT | INT |
| INT | INT | Menu, number of lines |
| in_Cur_Item | INT | Current menu item |
| by_Attr_mF | BYTE | Text attributes with focus |
| by_Attr_oF | BYTE | Text attributes without focus |
| by_Input_Exten_Code | BYTE | keycode - special keys |
| Menu, number of lines | BOOL | action: create menu |
| bo_Destroy | BOOL | action: remove menu |
| bo_Update | BOOL | action: refresh menu |
| bo_Activ | BOOL | Menu is active |
