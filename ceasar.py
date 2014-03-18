# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
# ceasar.py
# Copyright (C) 2013 Ramin Najjarbashi <Ramin.Najjarbashi@Gmail.com>
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

class Ceasar(object):
	def Decrypt(self, str):
		#Get str as string
		tmp = ''
		for item in str:
			#Get Alpabet
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				#For lowerCase
				if ord(item) >= 97:
					if ((ord(item) + define.ceasar_space) ) > ord('z'):
						tmp += chr((ord(item) + define.ceasar_space - 1) % ord('z') + ord('a'))
					else:
						tmp += chr((ord(item) + define.ceasar_space))
				#For UpperCase
				else:
					if ((ord(item) + define.ceasar_space) ) > ord('Z'):
						tmp += chr((ord(item) + define.ceasar_space - 1) % ord('Z') + ord('A'))
					else:
						tmp += chr((ord(item) + define.ceasar_space))
					
			#For Unalpabet Chars ;)
			else:
				tmp += item
		return tmp

	def Encrypt(self, str):
		tmp = ''
		for item in str:
			#Get Alpabet
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				#For lowerCase
				if ord(item) >= 97:
					#print (ord(item) - define.ceasar_space)  
					if ((ord(item) - define.ceasar_space - 1) ) < ord('a'):
						tmp += chr((ord(item) - define.ceasar_space) + ord('z') % ord('a'))
					else:
						tmp += chr((ord(item) - define.ceasar_space))
				#For UpperCase
				else:
					if ((ord(item) - define.ceasar_space) ) < ord('A'):
						tmp += chr((ord(item) - define.ceasar_space - 1) + ord('Z') % ord('A'))
					else:
						tmp += chr((ord(item) - define.ceasar_space))
					
			#For Unalpabet Chars ;)
			else:
				tmp += item
		return tmp


# ram = Ceasar()
# #a = ram.Encrypt("Test No:1one :D")
# a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# #print (a)
# print ram.Dncrypt(a)
