<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Floating point numbers are stored in the format REAL. A common data format according to IEC754 used a 24 bit wide mantissa and an 8-bit exponent. This results in an accuracy of 7-8 digits. Usually this is for applications in control technology more than sufficient, but in certain cases can lead to a problem. A typical case can which be solved with single-precision only inadequate is a consumption meter. If you want to several Mwh (megawatt hours) of total consumption adding up, taking a smallest power of 1 mW (milliwatt) at a distance of 10ms fairs and so you need a resolution of 3.6 * 10^7 (equivalent 10MWs) and it would be a do add up 1* 10^-5 W's. To do this it requires a resolution of 12 digits.

The solution implemented by OSCAT is REAL Double precision and has a resolution of about 15 digits. The implemented data type REAL2 consists of R1 and RX, RX is here the value saved the first 7-8 points as Real and the rest in one real R1. This data type has the advantage that no conversion of REAL2 to REAL is needed, rather, the RX  is rather part of single REAL value.
