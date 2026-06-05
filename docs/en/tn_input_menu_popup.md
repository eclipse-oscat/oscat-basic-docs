<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_INPUT_MENU_POPUP

| | |
|:---|:---|
| **Type** | Function module |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| **Xus_TN_MENU** | us_TN_MENU |
| | The module TN_INPUT_MENU_POPUP is used to manage and display the Menu_Bar Submenu and for the representation of TN_INPUT_SELECT_POPUP elements. The element is shown in *.in_X and *.in_Y. The menu items are stored as elements within  *.st_Menu_Text. The individual element are devided from each other using '#'. To devide individual sub-menu items from each other or providing them with a cut line, an '-' has to submitted as text menu-element. |
| | Within the sub-menu can be navigated with up / down key.  If a sub-menu item is confirmed by pressing Enter / Return key, then in *.in_Menu_Selected the number of the selected menu-point is passed. |
| | An active Menu automatically backs up the background before it is drawn, and restores the background after ending. |
| | As long as a menu is display, the user program may not make graphical changes. This can be checked by TN_SCREEN.bo_Menue_Bar_Dialog = TRUE or TN_SCREEN.bo_Modal_Dialog = TRUE. |
| | The module is primarily from TN_INPUT_MENU_BAR and TN_INPUT_SELECT_POPUP used internally, and need not be executed directly by the user. |

![tn_input_menu_popup](tn_input_menu_popup.gif)
