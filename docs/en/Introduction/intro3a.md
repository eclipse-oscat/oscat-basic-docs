<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## The time and date functions of the library OSCAT depend on the target system implemented so that they take into account the differences in the implementation of date / time types of the individual systems. For example, on the UNIX systems CoDeSys implements the UNIX TIME DATE, which means that the data type TD is mapped in seconds as of 1.1.1970-00:00 as 32-bit value. In STEP7, however, the data type TD in seconds is shown as 1.1.1990. The range of time / date functions in CoDeSys systems 01.01.1970 - 31.12.2099 and in STEP7 systems 01.01.1990  - 31.12.2099. The limitation of the range on the year 2099 is mainly due to the fact that in 2100 will be not a leap year.

Furthermore, the date and time functions are in accordance with the ISO8601 (international standard for numeric date functions). Here, for example, the implementation of the days with 1 = Monday and 7 = Sunday is prescribed.
