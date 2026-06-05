<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## us_TN_SCREEN

A variable of type us_TN_SCREEN can be used to manage display the graphical user interface (GUI). us_TN_SCREEN:

| Data field | Data Type | Description |
| --- | --- | --- |
| bya_CHAR | ARRAY [0..1919] OF BYTE | Screen character |
| bya_COLOR | ARRAY [0..1919] OF BYTE | screen color codes |
| bya_BACKUP | ARRAY [0..1919] OF BYTE | screen backup memory |
| bya_Line_Update | ARRAY [0..23] OF BYTE | screen lines update |
| by_Input_Exten_Code | BYTE | Key code special keys |
| by_Input_ASCII_Code | BYTE | Key Code ASCII |
| bo_Input_ASCII_IsNum | BOOL | Key code is a digit |
| in_Page_Number | INT | current page number |
| in_Cursor_X | INT | Cursor X Position |
| in_Cursor_Y | INT | Cursor Y Position |
| in_EOS_Offset | INT | End of String Offset |
| by_Clear_Screen_Attr | BYTE | screen delete color |
| bo_Clear_Screen_Attr | BOOL | delete screen |
| bo_Modul_Dialog | BOOL | modal dialog active |
| bo_Menu_Bar_Dialog | BOOL | Menu dialog active |
