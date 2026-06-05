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
| **Input	KT** | REAL (critical gain) |
| **TT** | REAL ( Period of the critical Vibration ) |
| **PI** | BOOL (TRUE if parameters for PI controller are determined) |
| **PID** | BOOL (TRUE if parameters for PID controller) |
| **Output	KP** | REAL (variable gain KP) |
| **TN** | REAL (past set time of the integrator) |
| **TV** | REAL (retention time of the differentiator) |
| **CI** | REAL (  Gain  of the integrator) |
| **KD** | REAL (  Gain  of  Differentiator  ) |
| | CONTROL_SET1 calculate setting parameters for P, PI and PID controller according to the Ziegler-Nichols method. Here it indicates the critical gain KT, and the period of the critical vibration TT. The parameters are determined by the controller operated as a P-controller    and the gain is ramped up while committed to a continuous oscillation with a constant amplitude. The corresponding values of KT and TT are then determined. Disadvantage of this method is not any real control loop can be moved to the stability limit, and   so the process very long time for slow control loops such as room arrangements. |
| | The default values of the tuning rules are defined in Setup variables and can be changed by the user. The following table shows the default values |
| **Setup	P_K** | REAL:= 0.5 (default value KP for P controller) |
| **PI_K** | REAL:= 0.45 (default value KP for PI controller |
| **PI_TN** | REAL:= 0.83 (default value of TN for PI controller) |
| **PID_K** | REAL:= 0.6 (default value KP for PID controller) |
| **PID_TN** | REAL:= 0.5 (default value of TN for PID controller) |
| **PID_TV** | REAL:= 0.125 (default value TV for PID controller) |

![control_set1](control_set1.gif)

| Controller Type | PI | PID | KP | TN | TV |
| --- | --- | --- | --- | --- | --- |
| P  Controller | 0 | 0 | P_K * KT |  |  |
| PI  Control | 1 | 0 | PI_K * KT | PI_TN * TT |  |
| PID  Controller | 0 | 1 | PID_K * KT | PID_TN * TT | PID_TV * TT |

| Controller Type | PI | PID | KP | TN | TV |
| --- | --- | --- | --- | --- | --- |
| P  Controller | 0 | 0 | P_K = 0.5 |  |  |
| PI  Control | 1 | 0 | PI_K = 0.45 | PI_TN = 0.83 |  |
| PID  Controller | 0 | 1 | PID_K = 0.6 | PID_TN = 0.5 | PID_TV = 0.125 |
