# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #
# row-transpose.py
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

class RowTranspose(object):
	def Encrypt(self, str):
		# Remove Space and non-alphabetic chars ;)
		tmp = ''
		for item in str:
			if ord(item.lower()) >= ord('a') and ord(item.lower()) <= ord('z'):
				tmp += item.lower()
		str = tmp

		# Add extra char end of Matrix ;)
		rows = len(str) / define.row_transpose_col + 1
		while len(str) < rows * define.row_transpose_col:
			str += 'x'

		# Make a Array for each line!
		tmp = []
		count = 1
		last = 0

		# define.row_transpose_col
		while count <= rows:
			tmp.append(str[last:define.row_transpose_col * count])
			last = define.row_transpose_col * count
			count += 1

		# Changes cols index :D
		changed_cols = []
		for item in define.row_transpose_key:
			changed_cols.append(())
			
		count = 0
		for item in define.row_transpose_key:
			 changed_cols[int(item)-1] = (zip(*tmp)[count])
			 count += 1

		# Make Result as string!
		result = ''
		for item in changed_cols:
			for item2 in item:
				result += item2

		return result

	#---------------------------------------------------------------------------#
	# str() is python function that convert s.t to str! and in this function	#
	# we need to use it, then we cant named the input paramater as "str" we		#
	# 						changed it to "chiper"!								#
	#---------------------------------------------------------------------------#
	def Decrypt(self, chipher):
		# Add extra char end of Matrix ;)
		rows = len(chipher) / define.row_transpose_col

		# Make a Array for each line!
		tmp = []
		count = 1
		last = 0

		for item in define.row_transpose_key:
			tmp.append(())

		# define.row_transpose_col
		while count <= define.row_transpose_col:
			tmp[list(define.row_transpose_key).index(str(count))]=(chipher[last:rows * count])
			last = rows * count
			count += 1

		print tmp
		result = ''
		for item in zip(*tmp):
			for item2 in item:
				result += item2
		return result

ram = RowTranspose()
#a = ram.Encrypt("To be or not to be")
a = ram.Encrypt("attack post poned until two am")
print (a)
print ram.Decrypt(a)
