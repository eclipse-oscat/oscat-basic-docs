<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## STACK_16

| | |
|:---|:---|
| **Type** | Function module |
| **Input	DIN** | DWORD (data input) |
| **E** | BOOL (enable input) |
| **RD** | BOOL (read command) |
| **WD** | BOOL (write command) |
| **RST** | BOOL (Reset input) |
| **Output	DOUT** | DWORD (data output) |
| **EMPTY** | BOOL (EMPTY   = TRUE means that memory is empty) |
| **FULL** | BOOL (FULL = TRUE means: memory is full) |
| | STACK_16 is a stack (STACK) with 16 memory locations for DWORD data. The two outputs EMPTY   and FULL indicate when the memory is full or empty. The RST input clears the entire contents of the memory. The FIFO is set with DIN, by setting a TRUE to the input WD, and true to the input E. A read command is executed by TRUE to RD and TRUE to E. Reading and writing can be performed simultaneously in one cycle. The module reads or writes in each cycle as long as the corresponding command (RD, WD) is set to TRUE. |

![stack_16](stack_16.gif)
