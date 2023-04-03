'''
@File   :  historical_ledger_statewide_gas.py
@Author :  Haitao Lu
@Date   :  01-Apr-2023 10:01 AM

Files for this layout are located in the following sites:
https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters

They are under Production Data section and is named as:
Historical Ledger – Statewide Gas

Note: The layout may change over time. please confirm the layout with the TXRRC website before using this script.
'''

LDROOT_GAS = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDROOT-OG-CODE', 2, 1, 'pic_generic'),
	('LDROOT-DISTRICT', 3, 2, 'pic_generic'),
	('LDROOT-RRCID-NBR', 5, 6, 'pic_generic'),
	('LD-GAS-OLDEST-EOM-BALANCE', 11, 5, 'pic_comp'),
	('LD-COND-OLDEST-EOM-BALANCE', 17, 5, 'pic_comp'),
	('LD-LIQUID-OLDEST-EOM-BALANCE', 23, 5, 'pic_comp'),
	('FILLER', 29, 6, 'pic_generic'),
	('RRC-TAPE-FILLER', 35, 128, 'pic_generic')
]

LDGSDATA_GAS = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDGSDATA-CYCLE-KEY', 2, 4, 'pic_generic'),
	('LDGSDATA-OPERATOR-NUMBER', 6, 6, 'pic_generic'),
	('LDGSDATA-FL-FIELD-NO', 12, 5, 'pic_generic'),
	('LDGSDATA-FIELD-RESERVOIR-NO', 17, 3, 'pic_generic'),
	('LDGSDATA-FIELD-TYPE', 20, 1, 'pic_generic'),
	('LDGSDATA-TYPE-FIELD-CODE', 21, 2, 'pic_generic'),
	('LDGSDATA-BALANCING-FIELD-FLAG', 23, 1, 'pic_generic'),
	('LDGSDATA-BALANCING-RULE-CODE', 24, 1, 'pic_generic'),
	('LDGSDATA-WELL-NUMBER', 25, 6, 'pic_generic'),
	('LDGSDATA-WLROOT-KEY', 31, 8, 'pic_generic'),
	('LDGSDATA-P2-FILED-FLAG', 39, 1, 'pic_generic'),
	('LDGSDATA-CORRECTED-P2-FLAG', 40, 1, 'pic_generic'),
	('LDGSDATA-WORD-ALLOWABLE', 41, 8, 'pic_generic'),
	('LDGSDATA-ALLOWABLE', 49, 5, 'pic_comp'),
	('LDGSDATA-WELL-TYPE', 54, 2, 'pic_generic'),
	('LDGSDATA-14B2-CODE', 56, 1, 'pic_generic'),
	('FILLER', 57, 2, 'pic_generic'),
	('LDGSDATA-ALLOWABLE-CODE', 59, 2, 'pic_generic'),
	('LDGSDATA-TOP-SCHED-ALLOWABLE', 61, 5, 'pic_comp'),
	('LDGSDATA-REVISED-ALLOW-CODE', 66, 2, 'pic_generic'),
	('LDGSDATA-COMMINGLED-FLAG', 68, 1, 'pic_generic'),
	('LDGSDATA-PRODUCTION', 69, 5, 'pic_comp'),
	('LDGSDATA-INJECTION-CREDIT-CODE', 74, 1, 'pic_generic'),
	('LDGSDATA-G9-INJECTION-AMOUNT', 75, 5, 'pic_comp'),
	('LDGSDATA-LIFT-GAS-INJECTED', 80, 5, 'pic_comp'),
	('LDGSDATA-MONTHLY-STATUS', 85, 5, 'pic_comp'),
	('LDGSDATA-REINSTATED-UNDERAGE', 90, 5, 'pic_comp'),
	('LDGSDATA-REIN-UNDERAGE-YEAR', 95, 4, 'pic_generic'),
	('LDGSDATA-REIN-UNDERAGE-MONTH', 99, 2, 'pic_generic'),
	('LDGSDATA-REIN-UNDERAGE-DAY', 101, 2, 'pic_generic'),
	('LDGSDATA-OVERAGE-TRANSFER', 103, 5, 'pic_comp'),
	('LDGSDATA-CUMU-STATUS', 103, 5, 'pic_comp'),
	('LDGSDATA-COND-LIMIT', 108, 5, 'pic_comp'),
	('LDGSDATA-COND-PLANT-PRODUCTION', 113, 5, 'pic_comp'),
	('LDGSDATA-COND-LEASE-PRODUCTION', 118, 5, 'pic_comp'),
	('LDGSDATA-COND-EOM-BALANCE', 123, 5, 'pic_comp'),
	('LDGSDATA-CANCEL-UNDERAGE-FLAG', 128, 1, 'pic_generic'),
	('LDGSDATA-CUMULATIVE-OVERAGE', 129, 5, 'pic_comp'),
	('LDGSDATA-LIQUID-CUMU-STATUS', 134, 5, 'pic_comp'),
	('FILLER', 139, 8, 'pic_generic'),
	('RRC-TAPE-FILLER', 147, 8, 'pic_generic')
]

LDGASDSP_GAS = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDG-GAS-DISP-CODE', 2, 2, 'pic_generic'),
	('LDG-GAS-DISP-AMT', 4, 5, 'pic_comp'),
	('RRC-TAPE-FILLER', 9, 151, 'pic_generic'),
]

LDGCONDS_GAS = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LDG-CONDS-DISP-CODE', 2, 2, 'pic_generic'),
	('LDG-CONDS-DISP-AMT', 4, 5, 'pic_comp'),
	('RRC-TAPE-FILLER', 9, 151, 'pic_generic'),
]
LDGSTAT_GAS = [
	('RRC-TAPE-RECORD-ID', 0, 2, 'pic_generic'),
	('LD-GAS-BALANCING-PERIOD-STATUS', 2, 5, 'pic_comp'),
	('LD-GAS-CANCELLED-UNDERAGE', 7, 5, 'pic_comp'),
	('LD-GAS-OFF-FILE-BAL-PER-STATUS', 12, 5, 'pic_comp'),
	('LD-GAS-OFF-FILE-CUM-OVERAGE', 17, 5, 'pic_comp'),
	('RRC-TAPE-FILLER', 22, 138, 'pic_generic'),
]


def historical_ledger_statewide_gas_layout(start_value):
	layouts_map = {
		'01': {'name': 'LDROOT_GAS', 'layout': LDROOT_GAS},
		'02': {'name': 'LDGSDATA_GAS', 'layout': LDGSDATA_GAS},
		'03': {'name': 'LDGASDSP_GAS', 'layout': LDGASDSP_GAS},
		'04': {'name': 'LDGCONDS_GAS', 'layout': LDGCONDS_GAS},
		'05': {'name': 'LDGSTAT_GAS', 'layout': LDGSTAT_GAS}
	}
	try:
		return_value = layouts_map[start_value]
	except:
		return_value = None

	return return_value
