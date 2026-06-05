<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## PWM_DC

| | |
|:---|:---|
| **Type** | Function module |
| **Input	F** | REAL (output frequency) |
| **DC** | REAL (duty cycle 0..1) |
| **Output	Q** | BOOL (output) |
| | PWM_DC is a  Duty  -  cycle  modulated frequency generator. The generator generates a fixed frequency F with a duty cycle (TON / TOFF) which can be  modulated (adjusted) by the input DC. A value of 0.5 at the input DC generates a duty cycle of 50%. |
| | The following image shows an output signal with a  duty  -  cycle  2 / 1, which corresponds to a DC (ratio) of 0.67. |

![pwm_dc](pwm_dc.gif)

![pwm_dc_diag](pwm_dc_diag.gif)
