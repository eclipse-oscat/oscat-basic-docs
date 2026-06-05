<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## The following modules are designed and harmonized to each other that a modular structure of a shutter controller can be reached. This modular system allows quick and easy setup from simple to complex blind controllers which are aligned to the application. The system can also be expanded at any later time, allowing any expansion of the functions. Applications include all types of blinds, shutters, and all types of shading devices. The modules are designed so they can be easily connected in series and the order of the wiring at the same time determines the priority of the functions. The signals UP and DN for manual operation, and the guidelines for angle and position in the automatic mode (PI and AI) are passed from module to this module, which ensures a simple signal path and a clear structure. A special feature is that the signals UP and DN if both are true simultaneously switch to automatic mode.

All modules have the inputs UP and DN with which the manual upd and down command is received and by QU and QD is passed on to the next module. If both inputs UP and DN set to TRUE then the relevant modules switch to automatic mode and evaluate the inputs PI and AI (position and angle) for input from the blind. If both inputs UP and DN set to TRUE then the relevant modules switch to automatic mode and evaluate the inputs AI and PI (position and angle for input from the blind. By order of the modules also the priority of the individual functions are  determined and can easily changed by  users . Future or custom features can be turned on in this way quickly and easily into the existing modules without having to modify the existing programming. The STATUS output passes ESR compliant messages about the state of the module. When there are no messages available each module passes the input adjacent S_IN status messages on to the STATUS output. Summary of the Blind status messages:

| STATUS | Module | Description |
| --- | --- | --- |
| 111 | SECURITY | Safe position in case of fire |
| 112 | SECURITY | Security position at wind |
| 113 | SECURITY | Safety position at ALARM |
| 114 | SECURITY | Door contact safety position |
| 115 | SECURITY | Security position in the rain |
| 1 | ACTUATOR | Error UP and DOWN simultaneously |
| 120 | ACTUATOR | Up motion |
| 121 | ACTUATOR | down motion |
| 121 | CONTROL | Up moving position |
| 122 | CONTROL | Down moving position |
| 123 | CONTROL | UP moving angle |
| 124 | CONTROL | Down moving angle |
| 121 | CONTROL_S | Up motion |
| 122 | CONTROL_S | down motion |
| 123 | CONTROL_S | Auto positioning |
| 127 | CONTROL_S | Lockout Time |
| 128 | CONTROL_S | Calibration |
| 129 | CONTROL_S | Extend  mode |
| 130 | INPUT | Standby |
| 131 | INPUT | Manual  Timeout |
| 132 | INPUT | Manual Up |
| 133 | INPUT | Manual Down |
| 134 | INPUT | SingleClick up |
| 135 | INPUT | SingleClick Down |
| 136 | INPUT | Forced  position |
| 137 | INPUT | Double click 1 |
| 138 | INPUT | Double click 2 |
| 141 | NIGHT | Night position active |
| Night position active | SHADE | Active shading |
| 160-175 | SCENE | active scene |
| 178 | SET | Set  operation |
| 179 | SET | Restore  operation |
