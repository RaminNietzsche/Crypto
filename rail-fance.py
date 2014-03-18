# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
# rail-fance.py
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

#define.railfence_lines

class RailFence(object):
	def Encrypt(self, str):
		# Remove Space and non-alphabetic chars ;)
		tmp = ''
		for item in str:
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				tmp += item.lower()
		str = tmp

		# Make a Array for each line!
		tmp = []
		count = 0
		while count < define.railfence_lines:
			tmp.append([])
			count += 1

		# Encrypt!!!
		count = 0
		for item in str:
			tmp[count%define.railfence_lines].append(item)
			count += 1

		# join all lines (List items :D)
		count = 0
		result =''
		while count < define.railfence_lines:
			result += List2Str(tmp[count])
			count +=1

		return result

	def Decrypt(self, str):
		# Remove Space and non-alphabetic chars ;)
		tmp = ''
		for item in str:
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				tmp += item.lower()
		str = tmp

		# Make a Array for each line!
		tmp = []
		count = 1
		last = 0
		while count <= define.railfence_lines:
			tmp.append(str[last:((len(str)/define.railfence_lines) + 1) * count])
			last = ((len(str)/define.railfence_lines) + 1) * count
			count += 1

		
		arr_count = 0
		i = 0
		result = ''
		
		while i < len(tmp[0]):
			count = 0
			while count < define.railfence_lines:
				try:
					result += tmp[count][i]
				except:
					pass
				count += 1
			i += 1
		
		return result
				

def List2Str(list):
	result = ''
	for item in list:
		result += item
	return result

ram = RailFence()
#a = ram.Encrypt("To be or not to be")
a = ram.Encrypt("meet me at one o clock !")
print (a)
print ram.Decrypt(a)
