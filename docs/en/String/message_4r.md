<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	M0** | . M3 STRING(string_length) (Information) |
| **MM** | INT (message appears maximum) |
| **ENQ** | BOOL (enable input) |
| **CLK** | BOOL (input to the next turn) |
| **T1** | TIME (time for automatic advance) |
| **Output	MX** | STRING(string_length) (output string) |
| **MN** | INT (currently active message) |
| **TR** | BOOL (  Trigger  Output) |
| | MESSAGE_4R provides at the output MX up to 4 messages. There is only one available of up to 4 entries at MX. The number of messages can be limited to the input of MM. MM is set to 2 then only the messages M0.. M2 passed to output after each other. MM is not set then all messages will be issued M0..M3. With each rising edge of CLK, the next message is written to MX, if CLK remains at TRUE so after the time T1 the next message is passed automatically, until CLK is FALSE again. If the enable-input ENQ is set to FALSE, at the output MX '' is passed and the module  has no function. The output MN indicates what message is just passed at the output MX. The output TR is always for one cycle TRUE if the message at the output MX has changed, it serves to control  given modules to process the messages. |

![message_4r](message_4r.gif)
