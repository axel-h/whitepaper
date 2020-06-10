#!/usr/bin/env python

# Copyright 2020, Data61, CSIRO (ABN 41 687 119 230)
#
# SPDX-License-Identifier: BSD-2-Clause

import fileinput
import sys

# detex does not consider comment environments

text = ""
for line in fileinput.input():
	text += line

index = 0
while True:
	indexstart = text.find("\\begin{comment}", index)
	if indexstart < 0:
		sys.stdout.write(text[index:])
		break
	sys.stdout.write(text[index:indexstart])
	indexend = text.find("\\end{comment}", indexstart)
	if indexend < 0:
		break
	index = indexend + 13
