#!/usr/bin/env python

import sys

def convert(char, flag):
	if (char == ' ' and flag):
		return ":space:"
	elif char == ' ':
		return "scrabble-blank"
	elif char.isalpha():
		if (flag and (char != 'a' and char != 'b' and char != 'o' and char != 'x' and char != 's' and char != 'm' and char != 'v')):
			return ":" + char + ":"
		else:
			return ":scrabble-" + char + ":"
	else:
		return char

output = ""
input = sys.argv[1].lower()

if (len(sys.argv) < 3):
	aliasFlag = True
else:
	aliasFlag = (sys.argv[2].lower() != "false")

for ch in input:
	output += convert(ch, aliasFlag)

print(output)
