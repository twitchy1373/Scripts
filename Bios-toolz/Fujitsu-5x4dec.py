#!/usr/bin/python

# Copyright 2009:  dogbert <dogber1@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#
# This script generates master passwords which can be used to unlock
# the BIOS passwords of most Fujitsu Siemens laptops (Lifebook, Amilo etc.).
# You have to install python for running this script.

import os

# someone smacked his head onto the keyboard
XORkey = ":3-v@e4i"

def codeToBytes(code):
	numbers = (int(code[0:5]), int(code[5:10]), int(code[10:15]), int(code[15:20]))
	bytes = []
	for i in numbers:
		bytes.append(i % 256)
		bytes.append(i / 256)
	return bytes 

def byteToChar(byte):
	if byte > 9:
		return chr(ord('a') + byte - 10)
	else:
		return chr(ord('0') + byte)

def decryptCode_old(bytes):
	# apply XOR key
	for i in range(len(bytes)):
		bytes[i] = bytes[i] ^ ord(XORkey[i])

	# swap two bytes
	bytes[2], bytes[6] = bytes[6], bytes[2]
	bytes[3], bytes[7] = bytes[7], bytes[3]

	# interleave the nibbles 
	bytes[0], bytes[1], bytes[2], bytes[3] = ((bytes[0] >> 4) | (bytes[3] << 4) & 0xFF), ((bytes[0] & 0x0F) | (bytes[3] & 0xF0)), ((bytes[1] >> 4) | (bytes[2] << 4) & 0xFF), ((bytes[1] & 0x0F) | (bytes[2] & 0xF0))
	bytes[4], bytes[5], bytes[6], bytes[7] = ((bytes[6] >> 4) | (bytes[5] << 4) & 0xFF), ((bytes[6] & 0x0F) | (bytes[5] & 0xF0)), ((bytes[7] >> 4) | (bytes[4] << 4) & 0xFF), ((bytes[7] & 0x0F) | (bytes[4] & 0xF0))

	# final rotations
	bytes[0] = ((bytes[0] << 3) & 0xFF) | (bytes[0] >> 5)
	bytes[1] = ((bytes[1] << 5) & 0xFF) | (bytes[1] >> 3)
	bytes[2] = ((bytes[2] << 7) & 0xFF) | (bytes[2] >> 1)
	bytes[3] = ((bytes[3] << 4) & 0xFF) | (bytes[3] >> 4)
	bytes[5] = ((bytes[5] << 6) & 0xFF) | (bytes[5] >> 2)
	bytes[6] = ((bytes[6] << 1) & 0xFF) | (bytes[6] >> 7)
	bytes[7] = ((bytes[7] << 2) & 0xFF) | (bytes[7] >> 6)

	# len(solution space) = 10+26
	bytes = [x % 36 for x in bytes]

	masterPwd = ""
	for x in bytes:
		masterPwd += byteToChar(x)
	return masterPwd

# fujitsu's password protection is getting more stupid by the minute
keys = ["4798156302", "7201593846", "5412367098", "6587249310", "9137605284", 
        "3974018625", "8052974163"]
def decryptCode_new(code):
	pwdHash = code[0] + code[2] + code[5] + code[11] + code[13] + code[15] + code[16]
	masterPwd = ""
	i = 0
	for c in pwdHash:
		masterPwd += keys[i][int(c)]
		i += 1
	return masterPwd

print("Master Password Generator for FSI laptops (5x4 digits version)")
print("Copyright (C) 2009-2010 dogbert <dogber1@gmail.com>")
print("")
print("When asked for a password, enter these:")
print("First password:  3hqgo3")
print("Second password: jqw534")
print("Third password:  0qww294e")
print("")
print("You will receive a hash code with five blocks, each with four numbers, ")
print("e.g. 1234-4321-1234-4321-1234")
print("")
print("Please enter the hash: ")
inHash = raw_input().strip().replace('-', '')
password_old = decryptCode_old(codeToBytes(inHash))
password_new = decryptCode_new(inHash)
print("")
print("The master password is: " + password_old + " OR " + password_new)
print("")
print("Please note that the password is encoded for US QWERTY keyboard layouts.")
if (os.name == 'nt'):
	print("Press a key to exit...")
	raw_input()

