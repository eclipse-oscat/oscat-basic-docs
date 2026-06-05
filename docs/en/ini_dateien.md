<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## An initialization file (INI file in short) is a text file, which Windows uses to store program settings (such as location of a program). Re-starting the program, the program settings can be imported to retake the state before the last closing.

Due to the very simple functional structuring and handling, this default standard ist used for program settings and for similar PLC with a file system.. An INI file can be divided into sections, which must be enclosed in square brackets. Information is read out as a key with an associated value. When you create an ini file the following rules apply: Each section must be unique. Each key may appear only once per section. Values are accessed by means of section and key. A section may also contain no key Comments start with a "#" Comments must not be directly behind a key or a section. Comments must always start on a new line Is given no value for a key, an empty string is reported as the value. Each section and each key or the following value must end with a newline. In this case, the type of newline character does not matter since all variants are accepted. Most common variant is <CR><LF> . All control characters (not printable characters) are interpreted as end of line. Space is always considered as part of the elements and is evaluated in the same manner. In principle any number of section and key can be used. Basic structure: #Comment <CR><LF> [Section] <CR><LF> #Comment <CR><LF> Key = value <CR><LF>

**Beispiel:**

Example: [SYSTEM] DEBUG_LEVEL=10 QUIT_TIME=5 #--------------------------- Station 1 Parameter - #--------------------------- [Station_1] NAME=ILC150 ETH IP=192.168.15.100 M2=S2/M3/C1 #--------------------------- # Station 2 parameters - #--------------------------- [Station_2] NAME=ILC350PN IP=192.168.15.108 M1=S1/M1 M2=S3/M2
