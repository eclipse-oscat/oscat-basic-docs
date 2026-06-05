<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_INPUT_SELECT_POPUP

| | |
|:---|:---|
| **Type** | Function module |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| **Xus_TN_INPUT_CONTROL** | us_TN_INPUT_CONTROL |
| | The module TN_INPUT_SELECT_POPUP is used to manage a selection of texts, by displaying a pop-up dialogue. This must be set *.IN_TYPE = 3. |
| | The item will be provided as *.in_X and *.in_Y. Every entry line can be provided with a title text. With *.in_Title_Y_Offset and *.in_Title_X_Offset  the position relative to the element coordinates is expressed. The color can be determined with *.by_Title_Attr, and the text by *.st_Title_String. If a tool tip should appear at the element *. st_Input_ToolTip the text hast to be specified. |
| | The selection of texts will be handed over in *.st_Input_Data. The text element should be separated from each other by the character '#'. |
| | If the focus is on an element, using the Enter / Return key selection dialog can be activated. |
| | With the cursor up/down can be changed between the individual elements. If the beginning or the end of the list will be reachted, it continues at the opposite side. |
| | The text-element is connected by means *.st_Input_Mask, meaning that the output text length are affected later. |
| | By pressing the Enter / Return key is the text of the selected element is passed to *. st_Input_String and *. bo_Input_Entered = TRUE. The input flag must be reset after receive by the user. |
| | An active selection (selection dialog) can always be canceled with the Escape key. |

![tn_input_select_popup](tn_input_select_popup.gif)

![tn_input_select_popup_2](tn_input_select_popup_2.gif)

**Beispiel:**

Example: *.in_Type := 03;
*.in_Y := 20;
*.in_X := 18;
*.by_Attr_mF := 16#17;
*.by_Attr_oF := 16#47;
*.st_Input_ToolTip := 
	'Change the current log level   | Press enter to select | '; 
*.in_Input_Option := 00;
*.in_Title_Y_Offset := 00;
*.in_Title_X_Offset := 00;
*.by_Title_Attr := 16#34;
*.st_Title_String := ' LOG-Level ';
*.st_Input_Mask := '  ';
*.st_Input_Data :=	'01#02#03#04#05#06#07#08#09#10#11#12#13#14#15'; The following output:
