'''
@File   :  ebcdic_formats.py
@Author :  Haitao Lu
@Date   :  15-Mar-2023 9:07 AM

formats for the ebcdic files

'''

import re
import sys
import unicodedata
import codecs


def build_control_char_regex():
	# create a list of control (unreadable/invisible) characters
	allChars = (chr(i) for i in range(sys.maxunicode))
	controlChars = ''.join(c for c in allChars if unicodedata.category(c) == 'Cc')
	return re.compile('[%s]' % re.escape(controlChars))


def ebc_decode(data):
	ebcdic_decoder = codecs.getdecoder('cp1140')  ## cp1140 is Western European
	decoded = ebcdic_decoder(data)
	value = decoded[0]
	return value


def pic_generic(string):
	string = ebc_decode(string)
	res = str(string).strip()
	res = re.sub(r'[^\x20-\x7E]', '', res).strip()  # remove non-ascii characters
	return res


def pic_comp3(packed, decimal_location=0):
	# Function unpacks a COMP-3 number with number of digits n
	# For more see: http://3480-3590-data-conversion.com/article-packed-fields.html

	n = ['']
	for b in packed[:-1]:
		hi, lo = divmod(b, 16)
		n.append(str(hi))
		n.append(str(lo))
	digit, sign = divmod(packed[-1], 16)
	n.append(str(digit))
	if sign == 13:  # 13 is d in hex.
		n[0] = '-'

	buf = int(''.join(str(x) for x in n))
	if decimal_location:
		decodedValue = buf / (10 ** decimal_location)
	else:
		decodedValue = buf

	return decodedValue


def pic_decimal(data, decimal_location=0):
	data = ebc_decode(data)
	res = str(data).strip()
	res = re.sub(r'[^\x20-\x7E]', '', res).strip()  # remove non-ascii characters
	if decimal_location:
		res = str(int(res) / (10 ** decimal_location))
	return res