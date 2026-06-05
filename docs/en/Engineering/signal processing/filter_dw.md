<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: DWORD

| | |
|:---|:---|
| **Input	X** | DWORD (input) |
| **T** | TIME (time constant of the filter) |
| **Output	Y** | DWORD (filtered value) |
| | FILTER_DW is a filter of the first degree for 32-bit DWORD data. The main application is the filtering of sensor signals for noise reduction. The basic functionality of a filter of the first degree can be found in the module FT_PT1. |

![filter_dw](filter_dw.gif)
