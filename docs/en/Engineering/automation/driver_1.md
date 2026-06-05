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
| **Input	SET** | BOOL (asynchronous set input) |
| **IN** | BOOL (switch input) |
| **RST** | BOOL (asynchronous reset input) |
| **Output	Q0** | BOOL (output) |
| | DRIVER_1 a driver module whose output Q can be set by the input IN is when TOGGLE_MODE = FALSE. The output is then held to TRUE until it is either set to FALSE by an asynchronous reset (RST) or until expiry of the maximum switching time (TIMEOUT). Further impulses   at the input IN thereby extend the TRUE period by the output whereas each rising edge at the IN  the Timeout  begins again. If TOGGLE_MODE = TRUE, the output Q switches with each rising edge on the IN state between TRUE and FALSE. Also in TOGGLE_MODE the TIMEOUT limits the maximum TRUE phase at the output Q. TIMEOUT is set to T#0s (  Default  ) Then no  Timeout  active. The asynchronous SET and RST inputs sets the output Q to TRUE or FALSE. The module DRIVER_4 provides the same functionality with 4 switching outputs. |
| **Setup	TOGGLE_MODE** | BOOL (mode of the input IN) |
| **TIMEOUT** | TIME (maximum duty cycle of the outputs) |

![driver_1](driver_1.gif)
