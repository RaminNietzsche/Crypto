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

class Playfair(object):
	def Encrypt(self, str):
		tmp = ''
		# Remove extra chars ;)
		for item in str:
			if ord(item.upper()) >= ord('A') and ord(item.upper()) <= ord('Z'):
				tmp += item.upper()
		str = tmp
		tmp = ''

		# Make len(string) == 2n
		if len(str)%2 != 0:
			str += define.playfair_add_char.upper()

		# Replace extra alpabet char ;)
		str = str.replace(define.playfair_ignore_char[0].upper(),define.playfair_ignore_char[1].upper())

		first = []
		second = []
		count = 0

		while count < len(str):
			first = self.FindLoc(str[count])
			second = self.FindLoc(str[count+1])
			if first[0] != second[0] and first[1] != second[1]:
				tmp += define.playfair_dic[first[0]][second[1]] + define.playfair_dic[second[0]][first[1]] + ' '
			elif first[0] == second[0]:
				tmp += define.playfair_dic[first[0]][(first[1] + 1) % len(define.playfair_dic)] + define.playfair_dic[second[0]][(second[1] + 1) % len(define.playfair_dic)] + ' '
			elif first[1] == second[1]:
				tmp += define.playfair_dic[(first[0] + 1) % len(define.playfair_dic)][first[1]] + define.playfair_dic[(second[0] + 1) % len(define.playfair_dic[0])][second[1]] + ' '				
			count += 2
		return tmp
				

				
	def Decrypt(self, str):
		tmp = ''
		# Remove extra chars ;)
		for item in str:
			if ord(item.upper()) >= ord('A') and ord(item.upper()) <= ord('Z'):
				tmp += item.upper()
		str = tmp
		tmp = ''

		# Make len(string) == 2n
		if len(str)%2 != 0:
			str += define.playfair_add_char.uppe

		# Replace extra alpabet char ;)
		str = str.replace(define.playfair_ignore_char[0].upper(),define.playfair_ignore_char[1].upper())
			
		first = []
		second = []
		count = 0

		while count < len(str):
			first = self.FindLoc(str[count])
			second = self.FindLoc(str[count+1])
			if first[0] != second[0] and first[1] != second[1]:
				tmp += define.playfair_dic[first[0]][second[1]] + define.playfair_dic[second[0]][first[1]] + ' '
			elif first[0] == second[0]:
				tmp += define.playfair_dic[first[0]][(first[1] - 1) % len(define.playfair_dic)] + define.playfair_dic[second[0]][(second[1] - 1) % len(define.playfair_dic)] + ' '
			elif first[1] == second[1]:
				tmp += define.playfair_dic[(first[0] - 1) % len(define.playfair_dic)][first[1]] + define.playfair_dic[(second[0] - 1) % len(define.playfair_dic[0])][second[1]] + ' '				
			count += 2
		return tmp.lower()

	def FindLoc(self, chr):
		count = 0
		while count < len(define.playfair_dic):
			if chr in define.playfair_dic[count]:
				return [count, define.playfair_dic[count].index(chr)]
			count += 1

		
#ram = Playfair()
#a = ram.Encrypt("Lord Granvilxles letterz,")
#a = ram.Encrypt("Test No:1one :D")
#print (a)
#print ram.Decrypt(a)
