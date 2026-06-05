<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_INPUT_MENU_BAR

| | |
|:---|:---|
| **Type** | Function module |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| **Xus_TN_MENU** | us_TN_MENU |
| | The module TN_INPUT_MENU_BAR is used to manage and view the Menu_Bar. The element is shown in *.in_X and *.in_Y. The menu items are stored as elements within verschachelte *.st_MENU_TEXT. Two different separators are used. A '$' separates the different menu lists, and each menu list is further divided by '#' into individual menu items. The first menu list is the actual menu bar, this implies the number of sub-menus, and the titles of the elements. Then all the sub-menu lists are follow and are separated by '%'. To devide individual sub-menu items from each other or providing them with a cut line, an '-' has to submitted as text menu-element. |
| **By pressing the Escape key, the menu bar activated and the respective sub-menu is displayed using the module TN_INPUT_MENU_POPUP. Within the sub-menu can be navigated with up / down key. Within the sub-menu can be navigated with up / down cursor. If a sub-menu item is confirmed by pressing Enter / Return key, then in *.in_Menu_Selected the number of the selected menu-point is passed. The calculation of the menu item number is as following** | Main menu index * 10 + Submenu-index. The entry in *.in_Menu_Selected needs set again to 0 after acceptance by users. |
| | Thus, a maximum of 9 main menu items and each 9-Submenu items are executable. Means of escape key at any time the menu can be hided again. |
| | Active Menu automatically backs up the background before it is drawn, and restores the background after ending. |
| | As long as a menu is display, the user program may not make graphical changes. This can be checked by TN_SCREEN.bo_Menue_Bar_Dialog = TRUE. |

![tn_input_menu_bar](tn_input_menu_bar.gif)

![tn_input_menu_bar_2](tn_input_menu_bar_2.gif)
![tn_input_menu_bar_3](tn_input_menu_bar_3.gif)

**Beispiel:**

Example: *.in_X := INT#00; *.in_Y := INT#00; *.by_Attr_mF := BYTE#16#33; (* yellow + brown *) *.by_Attr_oF := BYTE#16#0F; (* black + grey *) *.st_MENU_TEXT := 'File#Edit#View#End'; *.st_MENU_TEXT := CONCAT(*.st_MENU_TEXT, '%oeffnen#-#speichern#beenden%loeschen#-#einfuegen#-#kopieren'); *.st_MENU_TEXT := CONCAT(*.st_MENU_TEXT, '%alles#detail#kopieren%Logout'); *.bo_Create := TRUE; The following output:
