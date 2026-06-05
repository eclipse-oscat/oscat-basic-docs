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
| **Input	IN** | BOOL (control input) |
| **REQ** | BOOL (  Request  for automatic mode) |
| **ENQ** | BOOL (  Enable  for output Q) |
| **RST** | BOOL (asynchronous reset input) |
| **Output	Q** | BOOL (switching output for valve) |
| **STATUS** | BYTE (ESR compliant status output) |
| | FLOW_CONTROL switches a valve at the output Q  when the input IN = TRUE. In addition, the valve can also be switched via the input RE. REQ = TRUE turns the valve on for the time T_AUTO and will be locked for the time T_DELAY. after the time T_DELAY the valve can be turned on again on REQ. During this lock period T_DELAY the valve may be controlled by the input IN. An ESR compatible status output STATUS indicates the status of the module. Both the REQ and IN can only switch the output Q when the input ENQ is set to True. |
| **Status = 100** | Ready |
| **Status = 101** | Valve on by a TRUE at IN |
| **Status = 102** | Valve on by a TRUE at REQ |
| **Status = 103** | Reset is executed |
| **The diagram illustrates the structure of inferential FLOW_CONTROL** |  |
| **Setup	T_AUTO** | TIME (valve switch time in automatic mode) |
| **T_DELAY** | TIME(valve disable Time in automatic mode) |

![flow_control](flow_control.gif)

![flow_control_schema](flow_control_schema.gif)
