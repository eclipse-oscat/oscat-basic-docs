<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Global constants

| | |
|:---|:---|
| **SETUP** |  |
| | SETUP defines general basic settings. The settings are defined in the TYPE definition CONSTANTS_SETUP. |
| **LOCATION** |  |
| | LOCATION defines location settings, including but also definitions holiday. The settings are defined in the TYPE definition CONSTANTS_LOCATION. |
| **String_Length** | INT: = 250 |
| | String_Length is by default  250 characters, and is used by STRING function to avoid a range overflow when processing STRINGS. STRING_LENGTH shall also determine within the OSCAT LIB the maximum length, which can lead to high memory consumption when heavily used. If in a Application short STRINGS must be processed, the length may be reduced accordingly on these SETUP constant STRING. We recommend to define STRINGS within the application with the aid of this  constant. STRINGS, if longer than 80 characters, may need to increase this constant at a value to 255. |
| **New_string** | STRING(String_Length). |
| | WIth this definition the newly defined STRING automatically defines the length of STRING_LENGTH and can be changed globally if needed. |
| **LIST_LENGTH** | INT := 250. |
| | LIST_LENGTH is by default 250 characters and sets the size of lists. |

OSCAT The library tries to avoid global variables, an attempt to be easily integrated into other environments. Global variables are not necessary for function and exchange of data between devices. The setup and configuration is fully implemented within the modules to ensure high modularity and portability. For physical and mathematical constants we decided for reasons of clarity to use global constants. MATH  : MATH defined mathematical constants. The constants are defined in the TYPE definition CONSTANTS_MATH. PHYS  : PHYS defines physical constants. The constants are defined in the TYPE definition CONSTANTS_PHYS. LANGUAGE  : LANGUAGE defines language. The settings are defined in the TYPE definition CONSTANTS_LANGUAGE.
