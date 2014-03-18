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

def encodeLetter(inputVal):
	"encode each hex letter to binary and pad appropriately"
	result = None
	limit = 4	
	binresult = bin(int(inputVal, 16))[2:]
	if len(binresult)== limit:
		result = binresult
	else:
		result = '0'*(limit - len(binresult))+ binresult
	return result
		

def encodeData(strInput):
	"Encode the message alphabets to binary representation of their ascii code"
	encodeList = []
	result = None
	nwInput = None

	nwInput = strInput.encode("hex")
	for data in nwInput:
		letter = encodeLetter(data)
		encodeList.append(letter)
	result = ''.join(encodeList)

	limit = 64	
	if not (len(result)== limit):
		result = '0'*(limit - len(result))+ result
	return result


def get_L_and_R(strInput):
	strInput = permMessage(strInput)
	result = encodeData(strInput)
	L,R = result[0:32], result[32:64]
	return L,R

def correctIndex(index):
	'index begins at one and needs some correction'
	index = index - 1
	return index

def processKey(key):
	'encode the key to 64 bits but only 56 of the bits will be used for real encryption'
	hexKey = None
	if len(key) == 8 :
		hexKey = encodeData(key)
	else:
		print 'Key is not 64 bits'
	return hexKey

def getsubKey56Bit(key):
	'56-bit permutation '
	resultList = []	
	permOrderList = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]
	enKey = processKey(key)
	enkeyList = list(enKey)
	for value in permOrderList:
		index = correctIndex(value)
		resultList.append(enkeyList[index])
	output = ''.join(resultList)
	return output
	
def getOriginal_C_D(key):
	'get C0 and D0'
	result = getsubKey56Bit(key)
	C,D = result[0:28], result[28:56]
	return C,D

def shiftPlainText(shiftVal, data):
    #shift the plaintext by the given key
	firstPartNewList = []
	secondPartNewList = []
	data = list(data)
	firstPartNewList = data[0:shiftVal]
	secondPartNewList = data[shiftVal: ]
	secondPartNewList.extend(firstPartNewList)
	output = ''.join(secondPartNewList)
	return output


def getAll_C_D(key):
	outputDict = {}
	result = None
	C,D = getOriginal_C_D(key)
	for num in range(1, 17):
		if (num == 1) or (num == 2) or (num == 9) or (num == 16):
			C = shiftPlainText(1, C)
			D = shiftPlainText(1, D)
			outputDict[num] = (C , D)
		else :
			C = shiftPlainText(2, C)
			D = shiftPlainText(2, D)
			outputDict[num] = (C , D)
	return outputDict

def getAllPermSubKeys(key):
	permOrderList = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,  44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
	C_D_Dict = getAll_C_D(key)
	CD_List = []
	resultList = []
	for C,D in C_D_Dict.values():
		CD ='{0}{1}'.format(C,D)
		CD_List.append(CD)
	for word in CD_List:
		Tmp = []
		for value in permOrderList:
			index = correctIndex(value)
			Tmp.append(word[index])
		resultList.append(''.join(Tmp))
	return resultList
		

def permMessage(strInput):
	'permutate the message with 64-bit block of data'
	resultList = []
	encodMsg = encodeData(strInput)
	permOrderList = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30,  22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9,  1, 59,  51, 43, 35, 27, 19, 11, 3,  61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
	encodMsgList = list(encodMsg)
	for value in permOrderList:
		index = correctIndex(value)
		resultList.append(encodMsgList[index])
	output = ''.join(resultList)
	return output

def get_E_from_R(strInput):
	resultList = []
	L, R = get_L_and_R(strInput)
	permOrderList = [32, 1, 2, 3, 4, 5,  4, 5, 6, 7, 8, 9, 8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
	RList = list(R)
	for value in permOrderList:
		index = correctIndex(value)
		resultList.append(RList[index])
	output = ''.join(resultList)
	return output

def Xor(s1,s2):
	return  (int(str(s1),2) ^ int(str(s2),2))

def ER(R):
    resultList = []
    permOrderList = [32, 1, 2, 3, 4, 5,  4, 5, 6, 7, 8, 9, 8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    Rlist = list(R)
    for value in permOrderList:
        index = correctIndex(value)
        resultList.append(Rlist[index])
    output = ''.join(resultList)
    return output
    
def getFunc_of_K_E (strInput, key):
    listL = []
    listR = []
    result = []
    subKeys = getAllPermSubKeys(key)
    #ER = get_E_from_R(strInput)
    L, R = get_L_and_R(strInput)
    listR.append(R)
    listL.append(L)
    for pos in range(1, 16):
        B = format(Xor( subKeys[pos], ER(listR[(pos - 1)]) ), '048b')
        nL = listR[(pos - 1)]
        listL.append(nL)
        nR = format(Xor( listL[(pos - 1)], permSBox(B)), '032b')
        listR.append(nR)
    result.append(listR)
    result.append(listL)
    return result      
    
    

def get_SBox(B):
    strCntent = []
    length = len(B)
    for start,end in zip(range(0, (length + 1) ,6), range(6, (length + 1),6)):
        strCntent.append(B[ start:end ])

    row1,col1 = process_SBox(strCntent[0])
    row2,col2 = process_SBox(strCntent[1])
    row3,col3 = process_SBox(strCntent[2])
    row4,col4 = process_SBox(strCntent[3])
    row5,col5 = process_SBox(strCntent[4])
    row6,col6 = process_SBox(strCntent[5])
    row7,col7 = process_SBox(strCntent[6])
    row8,col8 = process_SBox(strCntent[7])


    listS1 =[   [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ]

    S1 = listS1[row1][col1]
    S1 = format(S1,'04b')

    listS2 =[   [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13,  4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1,  5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14,  9]
            ]

    S2 = listS2[row2][col2]
    S2 = format(S2,'04b')

    listS3 =[   [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [ 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
            ]

    S3 = listS3[row3][col3]
    S3 = format(S3,'04b')

    listS4 =[   [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [ 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ]

    S4 = listS4[row4][col4]
    S4 = format(S4,'04b')

    listS5 =[   [ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [ 4,  2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11,  8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ]

    S5 = listS5[row5][col5]
    S5 = format(S5,'04b')

    listS6 =[   [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [ 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ]

    S6 = listS6[row6][col6]
    S6 = format(S6,'04b')

    listS7 =[   [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]
            ]

    S7 = listS7[row7][col7]
    S7 = format(S7,'04b')

    listS8 =[   [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ]

    S8 = listS8[row8][col8]
    S8 = format(S8,'04b')

    output = '{0}{1}{2}{3}{4}{5}{6}{7}'.format(S1,S2,S3,S4,S5,S6,S7,S8)
    return output

		
def process_SBox(box):
    rowbit = '{0}{1}'.format(box[0],box[5] )
    row = int(rowbit,2)
    colbit = str(box[1:5])
    col = int(colbit,2)
    return row,col

def permSBox(B):
    R = get_SBox(B)
    resultList = []
    permOrderList = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    Rlist = list(R)
    for value in permOrderList:
        index = correctIndex(value)
        resultList.append(Rlist[index])
    output = ''.join(resultList)
    return output

def encryptData(strInput, key):
    R16 = getFunc_of_K_E (strInput, key)[0][15]
    L16 = getFunc_of_K_E (strInput, key)[1][15]   
    R16_L16 = '{0}{1}'.format(R16, L16)
    resultList = []
    permOrderList = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    Rlist = list(R16_L16)
    for value in permOrderList:
        index = correctIndex(value)
        resultList.append(Rlist[index])
    bitstring = ''.join(resultList)
    return  bitstring

def convertBinToAsciiCharater(bitstring):
    string_blocks = (bitstring[i:i+8] for i in range(0, len(bitstring), 8))
    newstring = ''.join(chr(int(char, 2)) for char in string_blocks)
    return  newstring

def getMessage(B):
    '''
        ECB mode (Electronic codebook).
    '''
    limit = 8
    strCntent = chunks(B, limit)
    strCntent = [format(int(word),'064b') for word in strCntent ]
    return strCntent

def encryptRealMsgr(strInput, key):
    encryptLst = []
    words = getMessage(strInput)
    for word in words:
        encryptWd = encryptData(word, key)
        encryptLst.append( encryptWd )
    output = ''.join(encryptLst)
    output = convertBinToAsciiCharater(output)
    return output

def chunks(l, n):
    '''
        split to n number of elements
    '''
    return [l[i:i+n] for i in range(0, len(l), n)]

     
if __name__ == '__main__':
	print getOriginal_C_D('01234567')
	#print getAllPermSubKeys('01234567')  # returns list
	#print permMessage('01234567')
	#print getFunc_of_K_E ('01234567', '01234567')[1]
    print encryptData('01234567', '01234567')
    #print encryptRealMsgr('01234567934444', '01234567')
	#val = get_E_from_R('01234567')
	#print val[0]
	#print val[1]
	#x,y = get_L_and_R('01234567')
	#print x
	#print y
	#print  get_E_from_R('01234567')



	
		


