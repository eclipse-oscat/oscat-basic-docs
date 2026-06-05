<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DLOG_STORE_FILE_HTML

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	X** | DLOG_DATA (DLOG data structure) |
| **INPUT** | ENABLE BOOL (Enable data recording) |
| **TRIG_M** | BOOL (manual trigger) |
| **TRIG_T** | UDINT (automatic trigger over time) |
| **FILE NAME** | STRING (file name) |
| **DTI** | DT (Current DATE-TIME value) |
| **HTML_CAPTION** | STRING (HTML Code for Headline) |
| **HTML_TABLE** | STRING (HTML Code for table) |
| **HTML_TR_HEAD** | STRING (HTML Code for table header) |
| **HTML_TR_EVEN** | STRING (HTML Code for odd lines) |
| **HTML_TR_ODD** | STRING (HTML Code for even lines) |
| **OUTPUT	ERROR_C** | DWORD   (Error code) |
| **ERROR_T** | BYTE   (Problem type) |
| | The module DLOG_STORE_FILE_HTML is for logging (recording) of the process values ​​in an HTML file into which the data are presented as a table. With the HTML_* parameters any HTML code can be inserted at key points. It is mainly about formatting parameters such as font, size and color. |
| | The data can be passed with the modules DLOG_DINT, DLOG_REAL, DLOG_STRING, DLOG_DT. The parameter TRIG_M (positive pulse) is used to manually trigger (start) the storage of process data. With Parameters TRIG_T  an automatic time-controlled release can be realized. If the current date / time value divided by the parameterized TRIG_T value with residual value is 0, then a Save is performed. 
This also ensures that the store is always performed at the same time |

![dlog_store_file_html](dlog_store_file_html.gif)

![dlog_file_html_demo](dlog_file_html_demo.gif)

**Beispiel:**

Examples: TRIG_T = 60 every 60 sec at each new minute in second 0 a store is performed. TRIG_T = 10 In second  0,10,20,30,40,50 a store is performed. TRIG_T = 3600 At after each new hour at minute 0 and second 0 a store is performed. The triggers TRIG_T and TRIG_M can be used in parallel independent of each other. With parameters FILENAME the file name (including path if necessary) is defined. If the filename is changed during the recprding, it will automatically on-the-fly changed to the new record file (with no data loss). This change can also be automated. The parameter FILE NAME supports the use of date / time parameter (see documentation from the module DT_TO_STRF) example: FILENAME = 'Station_01_#R.html' At position of '#R' automatically the current minute number is entered. This means that automatically every minute the file name changes, and therefore the data is written into the file. Thus, within an entire hour 60 files are created and filled with data, and in the ring buffer manner overwritten again and again. A recording can be done automatically and creates every day, week, month, etc. a new file as desired. If a new FILE NAME is detected, a possibly existing file is erased and rewritten. On DTI parameters, the current date / time value has to be transferred. In SEP the ASCII code of the delimiter is given. ERROR_T: HTML-file format: http://de.wikipedia.org/wiki/Html HTML-color codes http://html-color-codes.info/webfarben_hexcodes/ http://www.uni-magdeburg.de/counter/rgb.txt.shtml Example of an HTML file that was created with the demo program DLOG_FILE_HTML_DEMO. As HTML parameters were used following requirements html_caption: STRING := 'Das ist der Titel'; html_tr_even: STRING := 'BGCOLOR=#B3B7FF'; html_tr_odd: STRING := 'BGCOLOR=#E0E0E0'; html_tr_head: STRING := 'BGCOLOR=#FFFF40'; html_table : STRING := 'BORDER="1"'; The generated HTML data looks in the following text editor. <html> <body> <table BORDER="1"> <caption>Das ist der Titel </caption> <TR BGCOLOR=#FFFF40> <TD>Timestamp</TD> <TD>Sinus</TD> <TD>Count</TD> <TD>Count_Bit_2</TD> <TD>Count_Hex</TD> </TR> <TR BGCOLOR=#B3B7FF> <TD>2010-10-22-06:00:00</TD> <TD>50.01</TD> <TD>1</TD> <TD>OFF</TD> <TD>00000000000000000000000000000001</TD> </TR> …...... …....... </table> </body> </html>

| Value | Properties |
| --- | --- |
| 1 | Problem: FILE_SERVERThe exact meaning of ERROR_C can be read at block FILE_SERVER |
