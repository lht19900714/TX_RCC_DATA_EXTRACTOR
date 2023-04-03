'''
@File   :  historical_ledger_statewide_oil.py
@Author :  Haitao Lu
@Date   :  01-Apr-2023 10:01 AM

Files for this layout are located in the following sites:
https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters

They are under Production Data section and is named as:
Historical Ledger – Statewide Oil

Note: The layout may change over time. please confirm the layout with the TXRRC website before using this script.
'''

LDROOT_OIL = [
	('LRRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDROOT-OG-CODE', 2, 1, 'pic_generic'),
	('LLDROOT-DISTRICT', 3, 2, 'pic_generic'),
	('LDROOT-LEASE-NBR ', 5, 6, 'pic_generic'),
	('LD-MOVABLE-BALANCE', 11, 5, 'pic_comp'),
	('LD-BEGINNING-OIL-STATUS', 16, 5, 'pic_comp'),
	('LD-BEGINNING-CSGHD-STATUS', 21, 5, 'pic_comp'),
	('LD-OIL-OLDEST-EOM-BALANCE', 26, 5, 'pic_comp'),
	('FILLER', 31, 1, 'pic_generic'),
	('RRC-TAPE-FILLER', 32, 128, 'pic_generic')
]

LDOLDATA_OIL = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDOLDATA-CYCLE-KEY', 2, 4, 'pic_generic'),
	('LDOLDATA-OPERATOR-NUMBER', 6, 6, 'pic_generic'),
	('LDOLDATA-FL-FIELD-NO', 12, 5, 'pic_generic'),
	('LDOLDATA-FIELD-RESERVOIR-NO', 17, 3, 'pic_generic'),
	('LDOLDATA-OIL-TYPE-FIELD-CODE', 20, 1, 'pic_generic'),
	('LDOLDATA-P1-FILED-FLAG', 21, 1, 'pic_generic'),
	('LDOLDATA-CORRECTED-P1-FLAG', 22, 1, 'pic_generic'),
	('LDOLDATA-FLOW-WELLS', 23, 3, 'pic_generic'),
	('LDOLDATA-OTHER-WELLS', 26, 5, 'pic_generic'),
	('LDOLDATA-COMMINGLED-FLAG', 31, 1, 'pic_generic'),
	('LDOLDATA-ALLOWABLE', 32, 5, 'pic_comp'),
	('LDOLDATA-OIL-PRODUCTION', 37, 5, 'pic_comp'),
	('LDOLDATA-OIL-ENDING-BALANCE', 42, 5, 'pic_comp'),
	('LDOLDATA-OIL-PRESENT-STATUS', 47, 5, 'pic_comp'),
	('LDOLDATA-OIL-MOVABLE-BALANCE', 52, 5, 'pic_comp'),
	('LDOLDATA-CSGHD-LIMIT', 57, 5, 'pic_comp'),
	('LDOLDATA-CSGHD-PRODUCTION', 62, 5, 'pic_comp'),
	('LDOLDATA-CSGHD-LIFT', 67, 5, 'pic_comp'),
	('LDOLDATA-CSGHD-STATUS', 72, 5, 'pic_comp'),
	('FILLER', 77, 17, 'pic_generic'),
	('RRC-TAPE-FILLER', 94, 68, 'pic_generic')
]
LDOILDSP_OIL = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDG-OIL-DISPOSITION-CODE', 2, 2, 'pic_generic'),
	('LDG-OIL-DISPOSITION-AMOUNT', 4, 5, 'pic_comp'),
	('RRC-TAPE-FILLER', 9, 151, 'pic_generic'),
]
LDOCSHDS_OIL = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDG-CSH-DISPOSITION-CODE', 2, 2, 'pic_generic'),
	('LDG-CSH-DISPOSITION-AMOUNT', 4, 5, 'pic_comp'),
	('RRC-TAPE-FILLER', 9, 151, 'pic_generic'),
]


def historical_ledger_statewide_oil_layout(start_value):
	layouts_map = {
		'01': {'name': 'LDROOT_OIL', 'layout': LDROOT_OIL},
		'06': {'name': 'LDOLDATA_OIL', 'layout': LDOLDATA_OIL},
		'07': {'name': 'LDOILDSP_OIL', 'layout': LDOILDSP_OIL},
		'08': {'name': 'LDOCSHDS_OIL', 'layout': LDOCSHDS_OIL}
	}
	try:
		return_value = layouts_map[start_value]
	except:
		return_value = None

	return return_value
