# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
# -*- coding: utf-8 -*-
# polyalphabetic.py
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

#define.polyalphabetic_key

class Polyalphabetic(object):
	def Encrypt(self, str):
		tmp = ''
		for item in str:
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				tmp += item.lower()
		str = tmp
		tmp = ''
		
		count = 0
		while count < len(str):
			tmp += chr((ord(define.polyalphabetic_key[count % len(define.polyalphabetic_key)]) + (ord(str[count].lower()))) % ord('a') % 26 + ord('a'))
			count += 1
		return tmp
		
	def Decrypt(self, str):
		tmp = ''
		for item in str:
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				tmp += item.lower()
		str = tmp
		tmp = ''
		
		count = 0
		while count < len(str):
			tmp += chr(((ord(str[count].lower())) - ord(define.polyalphabetic_key[count % len(define.polyalphabetic_key)])) %26 + ord('a'))
			count += 1
		return tmp


#ram = Polyalphabetic()
#a = ram.Encrypt("To be or not to be")
#a = ram.Encrypt("Test No:1one :D")
#print (a)
#print ram.Decrypt(a)
