<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## FLOW_METER

| | |
|:---|:---|
| **Type** | Function module |
| **Input	VX** | REAL (volume per hour) |
| **E** | BOOL (Enable Input) |
| **RST** | BOOL (Reset input) |
| **I / O	X** | REAL  flow rate fractional part) |
| **Y** | UDINT (flow rate integer part) |
| **Output	F** | REAL (actual flow) |
| | The function module FLOW_METER determines the flow rate per unit of time and count quantities. FLOW_METER determines the flow rate from the input VX and E. The module supports two operating modes are determined by the variable setup PULSE_MODE. If PULSE_MODE = TRUE is the volume flow and the amount determined by is added at each rising edge at E, the value of VX upon itself. If the PULSE_MODE = FALSE the input VX is interpreted as flow per unit time and is  added up as long as E = TRUE. Using the input RST, the internal counter can be always set to zero. X and Y are external to be declared variables and  can be declared retentive / permanent to be permanent in case of power failure. The module provides the instantaneous flow value F as the Real in accordance to the unit connected to VX. If a value at VX is applied eg. in liters / hour so is the measured value at the output F in l / h. The output F is set at the constant intervals UPDATE_TIME. The outputs X and Y make up the over time accumulated measure values where X in REAL represent in the decimal point and Y in UDINT the integer part. A count of 234.111234 is represented by 0.111234 at X and a value of 234 at Y. If for count only a REAL is used then the resolution (for Real to IEEE32), is only 7-8 position . The above described method can provide more than 9 digits before the decimal point (2^32-1) and at least 7 digits after the decimal point. Since in this case X is always smaller than 1, Y can be used for output without decimal places. The two variables X and Y must be declared external and can, as the following example, also be secured against power failure. |
| **SETUP	PULSE_MODE** | BOOL (pulse counter when TRUE) |
| **UPDATE_TIME** | TIME (measuring time for F) |

![flow_meter](flow_meter.gif)

**Beispiel:**

Example 1: VX := 4 m³/h; PULSE_MODE := FALSE; UPDATE_TIME := T#100ms; The device measures the flow in m³/h and counts the flow as long as the input E is TRUE. The output F shows (4.0m³/h) as long as E is TRUE, otherwise it shows (0.0). The value of F is re-calculated every 100 milliseconds. Example2: VX := 0,024 l/Puls; PULS_MODE := TRUE; UPDATE_TIME := T#1s; In this example, the flow at the output F is displayed in l/h and with each rising edge at E the counter is increased by 0.024 l.
