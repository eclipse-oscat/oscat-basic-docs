<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## In the field of process control modules for the construction of controllers and controlled systems are provided. Where possible, the modules measures the cycle time and calculate the output change with the current cycle time. This process has and advantage to a process over a fixed cycle time, that control systems of different speeds can be processed within the same task. Another advantage is the fact that at low priority  Tasks  the cycle time can vary and a controller with fixed cycle time inaccurate output values generates. The user should ensure with use of the set, that the cycle time of the task is in accordance with the requirements of the process.

Overview of the control circuit elements: Wind-Up: The wind-  Up  effect effects all controllers with I component. Thus real controller have a restricted control area the  Integrator would always grow, reaching large   control differences and output limits.  If after some time the process value exceeds the nominal value would have to wait until the  Integrator reduces  its high value. This is an undesirable and inappropriate behavior of the controller. The controller would suspend for the time of  Integrator  required to reduce its high value, which would, the longer the longer the controller is in the limitation. Therefore at regulators with I-share anti wind-up  measures are necessary. The simplest measure to prevent the wind  Up  is the integrator to reach a  Limits  to stop and return to work until the area with the last value of the  Integrator  continue working. This method has the disadvantage that changes in the control deviation during the output is limited, continues to perform in unnecessarily high values of the integrator. Modules in the library are working with the procedure marked with a W at the end. A sophisticated anti-  Wind-Up  Measure is a process that the output value of the integrator limits to a value and together with the other control rules exactly leads to the output limit. This method has the advantage that at entering the work area the controller can be operational immediately and can respond without time delay. Modules in the library working with this better method are marked with a WL at the end.

| TYPE | Name | Parameter | Transfer function | Calculation |
| --- | --- | --- | --- | --- |
| P | Proportional element | KP | KP | Y = X * KP |
| I | Integrator | KI |  | Y = Ya + X * KI *  ΔT |
| D | Differentiator | KD |  | Y = KD * ΔX / ΔT |
| PT1 | 1st order low pass | T1 | KP / ( 1 + T1s) |  |
| PT2 | 2nd order low pass | T1, T2 |  |  |
| PI | PI element | KP, KI | KP (1 + 1/TNs) | Y = Ya + KP ((1 + ΔT/TN)X - Xa) |
| PD | PD-element | KP, KD | KP (1 + TDs) |  |
| PDT1 | PD element, delayed | KP, TV, T1 | KP (1 + TVs/(1+T1s)) |  |
| PID | PID-element | KP, TN, TV | KP (1 + 1/TNs + TVs |  |
| PIDT1 | PID element delayed | KP, TN, TV, T1 | KP (1 + 1/TNs + TVs/(1+T1s)) |  |
