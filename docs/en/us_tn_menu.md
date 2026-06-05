<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## us_TN_MENU

A variable of type us_TN_MENU can be used to parameterize a MENU item, to display it and to process element related inputs. us_TN_MENU:

| Data field | Data Type | Description |
| --- | --- | --- |
| st_Menu_Text | STRING(STRING_LENGTH) | Menu items |
| in_Menu_E_Count | INT | Number of menu items |
| in_Y | INT | Menu Y position |
| in_X | INT | Menu X position |
| by_Attr_mF | BYTE | Text attributes with focus |
| by_Attr_oF | BYTE | Text attributes without focus |
| in_X_SM_new | INT | Sub-menu, new X-position |
| in_Y_SM_new | INT | Sub-menu, new Y-position |
| in_X_SM_old | INT | Sub-menu old X-Position |
| in_Y_SM_old | INT | Sub-menu old Y position |
| in_Cur_Menu_Item | INT | current main menu item |
| in_Cur_Sub_Item | INT | current sub-menu item |
| in_State | INT | menu status |
| in_Menu_Selected | INT | selected menu item |
| Menu, number of lines | BOOL | action: create menu |
| bo_Destroy | BOOL | action: remove menu |
| bo_Update | BOOL | action: refresh menu |
