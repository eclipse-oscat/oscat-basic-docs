<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Test environment and conditions

Available platforms and related dependencies CoDeSys: Needs the libraries "  SysLibFile.lib " and " SysLibSockets.lib " Runs on WAGO 750-841 CoDeSys SP PLCWinNT V2.4 and compatible platforms PCWORX: No additional library needed Runs on all PLC iwith file system and Ethernet controllers with firmware >= 3.5x BECKHOFF: Requires the installation of "TwinCAT TCP / IP Connection Server"  
 Thus needs the library "TcpIp.Lib  " 
 (Standard.lib; TcBase.Lib; TcSystem.Lib is automatically included) Programming environment:
	NT4, W2K, XP, Xpe;
	TwinCAT system version 2.8 or higher;
	TwinCAT Installation Level: TwinCAT PLC or higher; 
 Target platform:
	TwinCAT PLC runtime system version 2.8 or higher.
	PC or CX (x86)

	TwinCAT TCP/IP Connection Server v1.0.0.0 or higher;
	NT4, W2K, XP, XPe, CE (image v1.75 or higher);
	CX (ARM)

	TwinCAT TCP/IP Connection Server v1.0.0.44 or higher;
	CE (image V2.13 or later);

| Development Environment | Target Platform | PLC libraries to include |
| --- | --- | --- |
| TwinCAT v2.8.0 or higher | PC or CX (x86) | TcSystem.LibTcBase.LibTcSystem.Lib |
| TwinCAT v2.10.0 Build >= 1301 or higher | CX (ARM) | TcSystem.LibTcBase.LibTcSystem.Lib |
