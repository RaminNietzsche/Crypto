# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
# -*- coding: utf-8 -*-
# playfair.py
# Copyright (C) 2013 Ramin Najjarbashi <Ramin.Najarbashi@Gmail.com>
#
# crypto is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# crypto is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import define

class DES(object):

	PC_KEY = ""
	L = []
	R = []
	
	def Encrypt(self, str):
		self.MakeRL(self.MakeBin(str))
		print self.MakeBin(str)
		
	def Decrypt(self, str):
		pass

	def MakeRL(self, list):
		while len(list) > 0:
			# Left 32 bit of each block ;)
			self.L.append(List2Str(list[:4]))
			list.pop(3)
			list.pop(2)
			list.pop(1)
			list.pop(0)
			# Right of them :D
			self.R.append(List2Str(list[:4]))
			list.pop(3)
			list.pop(2)
			list.pop(1)
			list.pop(0)
		
	def MakeBin(self, str):
		tmp = []
		for item in str:
			# Convert char to bin and remove '0b'
			tmp_bin = bin(ord(item)).replace('0b','')
			# Make 8 bit for any char!
			while len(tmp_bin) < 8:
				tmp_bin = '0' + tmp_bin
			if len(tmp_bin) > 8:
				#Unormal char! (> 256!)
				return "ERROR!!!"
			tmp.append(tmp_bin)
		# Make it n*64 bit
		while len(tmp) % 8 != 0:
			tmp.append( 8 *'0')
		return tmp

	def PC_1(self):
		# Get binary Key
		key_bin = list(List2Str(self.MakeBin(define.DES_key)))
		key_pc = ''

		# Remove deny bits (n % 8 == 0)
		key_bin.pop(63)
		key_bin.pop(55)
		key_bin.pop(47)
		key_bin.pop(39)
		key_bin.pop(31)
		key_bin.pop(23)
		key_bin.pop(15)
		key_bin.pop(7)
		
		import random
		while len(key_bin) > 0:
			selected_bit = random.randint(0, len(key_bin))
			key_pc += key_bin.pop(selected_bit - 1)
		self.PC_KEY = key_pc

def List2Str(list):
	result = ''
	for item in list:
		result += item
	return result

ram = DES()
ram.PC_1()
a = ram.Encrypt("Test No:1one :D ?dflkeroptn4 m4ko4 نتانت")
print (a)
print ram.Decrypt(a)
