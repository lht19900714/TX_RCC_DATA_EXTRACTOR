'''
@File   :  gas_ledger_layout.py
@Author :  Haitao Lu
@Date   :  15-Mar-2023 8:20 AM

Files for this layout are located in the following sites:
https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters

They are under Production Data section and are named as:
Gas Ledger Dist 1,2,3
Gas Ledger Dist 4, 5, 6, 6E
Gas Ledger Dist 7B, 7C, 8, 8A, 9, 10

Note: The layout may change over time. please confirm the layout with the TXRRC website before using this script.
'''

GAS_FIELD_01 = [
	('REC-CODE', 0, 1, 'pic_generic'),  ## PIC 9
	('DIST-NO', 1, 2, 'pic_generic'),  ## PIC 99
	('DIST-SFX', 3, 1, 'pic_generic'),  ## PIC X
	('PERM-FLD-ID', 4, 8, 'pic_generic'),  ## PIC 9(8)
	('FILLER', 12, 19, 'pic_generic'),  ## PIC X(19)
	('FLD-NAME', 31, 32, 'pic_generic'),  ## PIC X(32)
	('COUNTY', 63, 18, 'pic_generic'),  ## PIC 9(18)
	('DISC-DATE', 81, 8, 'pic_generic'),  ## PIC 9(8)
	('TYPE-F', 89, 1, 'pic_generic'),  ## PIC X
	('CLASS', 90, 1, 'pic_generic'),  ## PIC X
	('ALLO-CD', 91, 1, 'pic_generic'),  ## PIC X
	('SPOCE', 92, 8, 'pic_generic'),  ## PIC 9(8)
	('NET-ALLO', 100, 1, 'pic_generic'),  ## PIC 9
	('BAL-RULE', 101, 1, 'pic_generic'),  ## PIC 9
	('XMT-FACT', 102, 1, 'pic_generic'),  ## PIC 9
	('PRINT-AS-IS', 103, 1, 'pic_generic'),  ## PIC 9
	('COL-HEAD', 104, 1, 'pic_generic'),  ## PIC X
	('T-CODE', 105, 12, 'pic_generic'),  ## PIC X(12)
	('CUMU-PROD', 117, 12, 'pic_generic'),  ## PIC 9(12)
	('CUMU-COND-PROD', 129, 10, 'pic_generic'),  ## PIC 9(10)
	('UNIT-ACRES', 139, 4, 'pic_generic'),  ## PIC 9(4)
	('UNIT-TOL', 143, 3, 'pic_generic'),  ## PIC 999
	('ALLOCTION', 146, 15, 'pic_generic'),  ## PIC 9(15)
	('CASING', 161, 21, 'pic_generic'),  ## PIC X(21)
	('DIAG-X', 182, 1, 'pic_generic'),  ## PIC X
	('DIAG-INFO', 183, 20, 'pic_generic'),  ## PIC X(20)
	('FG-DEPTH', 203, 5, 'pic_generic'),  ## PIC 9(5)
	('WELLS', 208, 4, 'pic_generic'),  ## PIC 9(4)
	('ALLOW-CALC', 212, 8, 'pic_generic'),  ## PIC 9(8)
	('TOL', 220, 3, 'pic_generic'),  ## PIC 999
	('ALLOW-DESIRED', 223, 8, 'pic_generic'),  ## PIC 9(8)
	('TOTAL-FORECAST', 231, 8, 'pic_generic'),  ## PIC 9(8)
	('OFFSHORE', 239, 1, 'pic_generic'),  ## PIC 9
	('FLD-TRANS', 240, 1, 'pic_generic'),  ## PIC 9
	('EX-BAL', 241, 1, 'pic_generic'),  ## PIC 9
	('EX-GOR', 242, 1, 'pic_generic'),  ## PIC 9
	('PENDING-SPEC-LMT-ALLOW', 243, 1, 'pic_generic'),  ## PIC 9
	('CUMU-PROD-PRIOR-70', 244, 12, 'pic_generic'),  ## PIC 9(12)
	('CUMU-PROD-ERROR-SW', 256, 1, 'pic_generic'),  ## PIC X
	('FILLER1', 257, 45, 'pic_generic'),  ## PIC X(45)
	('LINE-INFO', 302, 264, 'pic_generic'),  ## PIC X(66)
	('FILLER2', 566, 16, 'pic_generic'),  ## PIC X(16)
	('FLD-DATE', 582, 6, 'pic_generic'),  ## PIC 9(6)
	('F-CHANGE', 588, 1, 'pic_generic'),  ## PIC 9
	('PER-WELL-CD', 589, 2, 'pic_generic'),  ## PIC 99
	('PER-WELL', 591, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('AC-CD', 595, 2, 'pic_generic'),  ## PIC 99
	('ACRG-FACT', 597, "8_7", 'pic_comp'),  ## PIC S9(8)V9(7) COMP-3
	('OTHER-CD', 605, 2, 'pic_generic'),  ## PIC 99
	('OTHER-FACT', 607, "6_7", 'pic_comp'),  ## PIC S9(4)V9(7) COMP-3
	('SW-SPLIT', 613, "2_3", 'pic_comp'),  ## PIC SV999 COMP-3
	('SPLIT-DATE', 615, 2, 'pic_generic'),  ## PIC 99
	('SPECIAL-LMT-ALLOW', 617, 1, 'pic_generic'),  ## PIC 9
	('SW-EXC-206-CODE', 618, 1, 'pic_generic'),  ## PIC 9
	('SW-EXC-8609-LIMIT', 619, 2, 'pic_generic'),  ## PIC 99
	('FILLER3', 621, 43, 'pic_generic'),  ## PIC X(43)
	('FILLER4', 1731, 390, 'pic_generic')  ## PIC X(390)
]

GAS_WELL_05 = [
	('W-REC-CODE', 0, 1, 'pic_generic'),  ## PIC 9
	('W-DIST-NO', 1, 2, 'pic_generic'),  ## PIC 99
	('W-DIST-SFX', 3, 1, 'pic_generic'),  ## PIC X
	('W-PERM-FLD-ID', 4, 8, 'pic_generic'),  ## PIC 9(8)
	('OPER-ID', 12, 6, 'pic_generic'),  ## PIC 9(6)
	('WELL-ID', 18, 6, 'pic_generic'),  ## PIC 9(6)
	('FILLER5', 24, 1, 'pic_generic'),  ## PIC 9
	('TRACT-NO', 25, 1, 'pic_generic'),  ## PIC X
	('WELL-NR', 26, 3, 'pic_generic'),  ## PIC XXX
	('SFX-1', 29, 1, 'pic_generic'),  ## PIC X
	('SFX-2', 30, 1, 'pic_generic'),  ## PIC X
	('LSE-NAME', 31, 32, 'pic_generic'),  ## PIC X(32)
	('CO-CODE', 63, 3, 'pic_generic'),  ## PIC 999
	('W-TYPE', 66, 1, 'pic_generic'),  ## PIC X
	('GAS-GATHER-OLD', 67, 5, 'pic_generic'),  ## PIC X(5)
	('G-GATH', 72, 5, 'pic_generic'),  ## PIC X(5)
	('FULL-S', 77, 1, 'pic_generic'),  ## PIC X
	('GAS-SPLIT', 78, 1, 'pic_generic'),  ## PIC X
	('GASGATH2I', 79, 5, 'pic_generic'),  ## PIC X(5)
	('GASGATH3I', 84, 5, 'pic_generic'),  ## PIC X(5)
	('LIQ-GATHER-OLD', 89, 5, 'pic_generic'),  ## PIC X(5)
	('L-GATH', 94, 5, 'pic_generic'),  ## PIC X(5)
	('LIQ-SPLIT', 99, 1, 'pic_generic'),  ## PIC X
	('WELL-INFO', 100, 22, 'pic_generic'),  ## PIC X(22)
	('BATCH-NR', 122, 1, 'pic_generic'),  ## PIC X
	('EXC-14B', 123, 1, 'pic_generic'),  ## PIC X
	('14B-DATE', 124, 8, 'pic_generic'),  ## PIC 9(08)
	('CMP-DATE', 132, 8, 'pic_generic'),  ## PIC 9(8)
	('W-DEPTH', 140, 5, 'pic_generic'),  ## PIC 9(5)
	('UP-PERF', 145, 5, 'pic_generic'),  ## PIC 9(5)
	('LO-PERF', 150, 5, 'pic_generic'),  ## PIC 9(5)
	('COMMCD', 155, 1, 'pic_generic'),  ## PIC 9
	('COMM', 156, 4, 'pic_generic'),  ## PIC 9(4)
	('COMN-DTE', 160, 8, 'pic_generic'),  ## PIC 9(08)
	('DPT-CODE', 168, 1, 'pic_generic'),  ## PIC X
	('BHP-CODE', 169, 1, 'pic_generic'),  ## PIC X
	('SIP-CODE', 170, 1, 'pic_generic'),  ## PIC X
	('G-4-CODE', 171, 1, 'pic_generic'),  ## PIC X
	('WL-TSTX', 172, 1, 'pic_generic'),  ## PIC X
	('G-10-DUE', 173, 2, 'pic_generic'),  ## PIC 99
	('DTE-L-UTL', 175, 8, 'pic_generic'),  ## PIC 9(8)
	('WL-PA-CD', 183, 1, 'pic_generic'),  ## PIC 9
	('P-A-DATE', 184, 8, 'pic_generic'),  ## PIC 9(8)
	('SP-ALLOW', 192, 7, 'pic_generic'),  ## PIC 9(7)
	('SP-AL-CODE', 199, 1, 'pic_generic'),  ## PIC X
	('LIQ-ALLOW', 200, 5, 'pic_generic'),  ## PIC 9(5)
	('LIQ-ALLOW-CODE', 205, 1, 'pic_generic'),  ## PIC 9
	('FORM-LACKING', 206, 1, 'pic_generic'),  ## PIC 9
	('OFF-SHORE', 207, 1, 'pic_generic'),  ## PIC 9
	('WL-TOP-PER', 208, 5, 'pic_generic'),  ## PIC 999V99
	('ROYALTY-CODE', 213, 1, 'pic_generic'),  ## PIC 9
	('PRIOR-RINU', 214, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('PRIOR-RINU-DATE', 219, 6, 'pic_generic'),  ## PIC 9(6)
	('RINU', 225, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('RINU', 225, 5, 'pic_comp_dev'),  ## PIC S9(9) COMP-3
	('RINU-DATE', 230, 6, 'pic_generic'),  ## PIC 9(6)
	('EXC-14B2-TYPE', 236, 1, 'pic_generic'),  ## PIC X(1)
	('FILLER6', 237, 1, 'pic_generic'),  ## PIC X(1)
	('G-1-DATE', 238, 8, 'pic_generic'),  ## PIC 9(8)
	('OPEN-FLO', 246, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('SLOPE', 250, "3_4", 'pic_comp'),  ## PIC S9V9999 COMP-3
	('RATIO', 253, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('G-GRAV', 256, "2_3", 'pic_comp'),  ## PIC SV999 COMP-3
	('O-GRAV', 258, "2_1", 'pic_comp'),  ## PIC S99V9 COMP-3
	('BGS', 260, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('BLS', 265, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('PRIOR-6', 270, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('PCU', 275, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('CURR-BAL', 279, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('CANCEL-G', 284, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('G-STATUS', 288, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('L-STATUS', 293, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('LMT-ALLOW', 297, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('SI-AMT', 301, 5, 'pic_comp'),  ## PIC S9(9) COMP-3
	('SI-CODE', 306, 1, 'pic_generic'),  ## PIC 9
	('EXCEPTION-TO-PROD-LIMIT-CODE', 307, 1, 'pic_generic'),  ## PIC 9
	('EXCEPTION-TO-PROD-LIMIT', 308, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('EXC-14B2-APP-NO', 312, 4, 'pic_comp'),  ## PIC 9(6) COMP-3
	('W-DATE', 316, 6, 'pic_generic'),  ## PIC 9(6)
	('NAME-CHANGE-CODE', 322, 1, 'pic_generic'),  ## PIC 9
	('FORM-REC-CODE', 323, 1, 'pic_generic'),  ## PIC 9
	('BAL-CODE', 324, 1, 'pic_generic'),  ## PIC 9
	('EXC-206-CODE', 325, 1, 'pic_generic'),  ## PIC 9
	('RED-RATE-CODE', 326, 1, 'pic_generic'),  ## PIC 9
	('TSF-CODE', 327, 1, 'pic_generic'),  ## PIC 9
	('NO-SUPP', 328, 1, 'pic_generic'),  ## PIC 9
	('LACK', 329, 1, 'pic_generic'),  ## PIC 9
	('OLD-OP-CODE', 330, 6, 'pic_generic'),  ## PIC 9(6)
	('W-TYPE-MO', 336, 1, 'pic_generic'),  ## PIC X
	('AL-CODE', 337, 1, 'pic_generic'),  ## PIC X
	('WRD-ALLOW', 338, 8, 'pic_generic'),  ## PIC X(8)
	('ON-SHUT-LST', 346, 1, 'pic_generic'),  ## PIC X
	('NO-LMT-ALLOW-SW', 347, 1, 'pic_generic'),  ## PIC 9
	('ALLOW', 348, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('GAS-PRD', 352, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('INJ-CREDIT', 356, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('INJ-CODE', 360, 1, 'pic_generic'),  ## PIC 9
	('W-LIQ-ALLOW', 361, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('LSE-LIQ', 364, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('PLT-LIQ', 367, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('LIQ-DISI', 370, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('LIQ-DISCDI', 373, 1, 'pic_generic'),  ## PIC 9
	('OTH-DISCI', 374, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('OTH-DISCDI', 377, 1, 'pic_generic'),  ## PIC 9
	('MO-G4', 378, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('MO-G2', 382, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('MO-BHP', 385, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('OTHER-PRESI', 388, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('MO-ACRE', 391, "4_3", 'pic_comp'),  ## PIC S9(4)V9(3) COMP-3
	('MO-ACRE-FT', 395, "4_1", 'pic_comp'),  ## PIC S9(4)V9 COMP-3
	('TRAN-ALLOW', 399, 4, 'pic_comp'),  ## PIC S9(7) COMP-3
	('OPEN-COND', 403, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('CLOSE-COND', 406, 3, 'pic_comp'),  ## PIC S9(5) COMP-3
	('MO-LEASE-PERCENT-RESERVE', 409, "4_4", 'pic_comp'),  ## PIC S9(3)V9(4) COMP-3
	('PER-CENT-RED-RATE', 413, 4, 'pic_comp'),  ## PIC S9(07) COMP-3
	('MO-TOP-SCH-ALLOW', 417, 4, 'pic_comp'),  ## PIC S9(07) COMP-3
	('MO-LMT-ALLOW', 421, 4, 'pic_comp'),  ## PIC S9(07) COMP-3
	('MO-HIGHEST-DAILY-PROD-LMT', 425, 4, 'pic_comp'),  ## PIC S9(07) COMP-3
	('EXC-8609-LIMIT', 429, 2, 'pic_generic'),  ## PIC 9(2)
	('SWR38-ACRES-CODE', 431, 1, 'pic_generic'),  ## PIC X
	('FILLER7', 1941, 180, 'pic_generic') ## PIC X(180)
]


def gas_ledger_layout(start_value):
	layouts_map = {
		'1': {'name': 'GAS_FIELD_01', 'layout': GAS_FIELD_01},
		'5': {'name': 'GAS_WELL_05', 'layout': GAS_WELL_05},
	}
	try:
		return_value = layouts_map[start_value]
	except:
		return_value = None

	return return_value
