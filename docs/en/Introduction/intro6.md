<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Introduction

The lists described here are stored lists STRING (LIST_LENGTH), the elements of the list begin with the sign SEP followed by the element. The elements can contain all  Strings  allowable characters, and can also be an empty string. An empty list is represented by the string '', the string contains no elements. The length of a list is defined by the is the number of items in the list, an empty list has lengths 0. The functions for processing lists uses I/O variables, so that the long lists must note be copied at every function call into the memory. The separation character SEP of the lists can be freely determined by the user and is passed to the functions at the input SEP. The separation character is always only a single character and can be any valid character in a string. In the following examples  '§' is used as the separation character. Empty list:							'' List with an empty element:			'§' List of 2 items					'§1§NIX' List with 6 elements one of which is empty	'§1§§33§/§1§2'
