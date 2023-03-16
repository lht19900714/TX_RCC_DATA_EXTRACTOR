'''
@File   :  util.py
@Author :  Haitao Lu
@Date   :  16-Mar-2023 3:54 AM
'''

from ebcdic_formats.ebcdic_formats import pic_generic, pic_comp3, pic_decimal


def yield_blocks(file, n):
	block_bytes = file.read(n)
	while block_bytes:
		yield block_bytes
		block_bytes = file.read(n)


def parse_record(record, layout):
	values = {}

	for name, start, size, convert in layout:
		decimal = 0
		##check for additional data for pic_signed and comp 3 methods
		if '_' in str(size):  ##check if size also includes the number of decimals "Size_Decimal"
			size_split = size.split('_')
			size, decimal = int(size_split[0]), int(size_split[1])
		if convert == 'pic_comp':
			values[name] = pic_comp3(record[start:start + size], decimal)
		elif convert == 'pic_decimal':
			values[name] = pic_decimal(record[start:start + size], decimal)
		else:
			values[name] = pic_generic(record[start:start + size])

	return values
