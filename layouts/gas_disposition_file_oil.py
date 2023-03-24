'''
@File   :  gas_disposition_file_oil.py
@Author :  Haitao Lu
@Date   :  25-Mar-2023 2:57 AM

Files for this layout are located in the following sites:
https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters

They are under Production Data section and are named as:
PR(P1/P2) Gas Disposition

Note: The layout may change over time. please confirm the layout with the TXRRC website before using this script.
'''

# GD-PR-CASINGHEAD-DISP-TRANS-RECORD
GAS_DISPOSITION_OIL_LAYOUT = [
	('GD-PR-DISTRICT', 0, 2, 'pic_generic'),
	('GD-PR-LEASE-NO', 2, 5, 'pic_generic'),
	('GD-PR-REPORT-CENT', 7, 2, 'pic_generic'),
	('GD-PR-REPORT-YEAR', 9, 2, 'pic_generic'),
	('GD-PR-REPORT-MONTH', 11, 2, 'pic_generic'),
	('GD-PR-CASINGHEAD-BALANCING-CODE', 13, 1, 'pic_generic'),
	('GD-PR-DISCREPANCY-PRINTED-CODE', 14, 1, 'pic_generic'),
	('GD-PR-DISPOSITION-CODE-FLAG', 15, 1, 'pic_generic'),
	('GD-PR-FIELD-NUMBER', 16, 8, 'pic_generic'),
	('GD-PR-CODING-MAST-OP-NUMBER', 24, 6, 'pic_generic'),
	('GD-PR-COMPANY-TAPE-OP-NUMBER', 30, 6, 'pic_generic'),
	('GD-PR-LEASE-NAME', 36, 32, 'pic_generic'),
	('GD-PR-FIELD-NAME', 68, 32, 'pic_generic'),
	('GD-PR-BATCH-CODE', 100, 1, 'pic_generic'),
	('GD-PR-CERT-DATE', 101, 2, 'pic_generic'),
	('GD-PR-LEASE-FLD-FUEL-SYSTEMS', 103, 9, 'pic_generic'),
	('GD-PR-TRANSMISSION-LINE', 112, 9, 'pic_generic'),
	('GD-PR-PROCESSING-PLANT', 121, 9, 'pic_generic'),
	('GD-PR-VENTED-OR-FLARED', 130, 9, 'pic_generic'),
	('GD-PR-CASINGHEAD-LIFT', 139, 9, 'pic_generic'),
	('GD-PR-PRESSURE-MAINTENANCE', 148, 9, 'pic_generic'),
	('GD-PR-CARBON-BLACK', 157, 9, 'pic_generic'),
	('GD-PR-UNDERGROUND-STORAGE', 166, 9, 'pic_generic'),
	('GD-PR-CASINGHEAD-PRODUCTION', 175, 9, 'pic_generic'),
	('GD-PR-CASINGHEAD-LIFT-GAS-INJECTED', 184, 9, 'pic_generic'),
	('FILLER', 193, 7, 'pic_generic')
]
