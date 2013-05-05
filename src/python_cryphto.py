# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #!/usr/bin/python
#
# main.py
# Copyright (C) 2013 Ramin Najjarbashi <Ramin.Najjarbashi@Gmail.com>
# 
# python-Cryphto is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# python-Cryphto is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import ceasar
import monoalphabetic
import playfair
import polyalphabetic

def main(argv):
	if argv[1] == '--ceasar':
		Alg = ceasar.Ceasar()
		try:
			if argv[2] == '--decrypt':
				print Alg.Decrypt(argv[3])
			elif argv[2] == '--encrypt':
				print Alg.Encrypt(argv[3])
		except:
			print "Pleas read Help!!!(Invalid Argumans) "

	elif argv[1] == '--monoalphabetic':
		Alg = monoalphabetic.Monoalphabetic()
		try:
			if argv[2] == '--decrypt':
				print Alg.Decrypt(argv[3])
			elif argv[2] == '--encrypt':
				print Alg.Encrypt(argv[3])
		except:
			print "Pleas read Help!!!(Invalid Argumans) "

	elif argv[1] == '--playfair':
		Alg = playfair.Playfair()
		try:
			if argv[2] == '--decrypt':
				print Alg.Decrypt(argv[3])
			elif argv[2] == '--encrypt':
				print Alg.Encrypt(argv[3])
		except:
			print "Pleas read Help!!!(Invalid Argumans) "

	elif argv[1] == '--polyalphabetic':
		Alg = polyalphabetic.Polyalphabetic()
		try:
			if argv[2] == '--decrypt':
				print Alg.Decrypt(argv[3])
			elif argv[2] == '--encrypt':
				print Alg.Encrypt(argv[3])
		except:
			print "Pleas read Help!!!(Invalid Argumans) "


if __name__ == '__main__':
	import sys
	main(sys.argv)
