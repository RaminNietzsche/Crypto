#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
#-------------------------------------------------------------------------------#
#                                 define.py					#
#                                                                               #
#  Copyright  04-05-2013  <Ramin.Najarbashi@Gmail.com>				#
#  Last Modified : Sat 18 May 2013 06:09:29 PM IRDT BY: <Ramin.Najarbashi@Gmail.com>	#
#                                                                               #
#  This program is free software; you can redistribute it and/or modify         #
#  it under the terms of the GNU General Public License as published by         #
#  the Free Software Foundation; either version 2 of the License, or            #
#  (at your option) any later version.                                          #
#                                                                               #
#  This program is distributed in the hope that it will be useful,              #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of               #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
#  GNU General Public License for more details.                                 #
#                                                                               #
#  You should have received a copy of the GNU General Public License            #
#  along with this program; if not, write to the Free Software                  #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,                   #
#  MA 02110-1301, USA.                                                          #
#                                                                               #
#--------------------------------------------------------------------------------
 
# if ceasar_space = 2 : A --> C
ceasar_space = 8

# A = monoalphabetic_key[0] ... Z = monoalphabetic_key[25]
monoalphabetic_key = "AQWSDERFGTYHJUIKLOPMNBVCXZ"

# playfair_dic = matrix :D
# matrix = 25 value & len(alpabet) == 26 : need to ignore one char!--> ignore_char
# string must be 2*x! else if len(string) == 2n-1 then : len(string+add_char)==2x :D
playfair_dic = [
	['P','A','L','M','E'],
	['R','S','T','O','N'],
	['B','C','D','F','G'],
	['H','I','K','Q','U'],
	['V','W','X','Y','Z']
]
playfair_ignore_char = ['j','i']
playfair_add_char = 'e'

# polyalphabetic_key ...
polyalphabetic_key="run"

# DES key
#DES_key = [0x13 ,0x34 ,0x57 ,0x79 ,0x9B ,0xBC ,0xDF ,0xF1]
DES_key = "KeyValue"

# 
vigenere_key = "vigenere"
vigenere_table = "abcdefghijklmnopqrstuvwxyz"

# RailFence Line count divs :D
railfence_lines = 3 

# count of RowTranspose Col
row_transpose_col = 7
row_transpose_key = "4312567"
