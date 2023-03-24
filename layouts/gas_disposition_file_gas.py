'''
@File   :  gas_disposition_file_gas.py
@Author :  Haitao Lu
@Date   :  25-Mar-2023 2:57 AM

Files for this layout are located in the following sites:
https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/#gas-masters

They are under Production Data section and are named as:
PR(P1/P2) Gas Disposition

Note: The layout may change over time. please confirm the layout with the TXRRC website before using this script.
'''

# GD-PR-CASINGHEAD-DISP-TRANS-RECORD
GAS_DISPOSITION_GAS_LAYOUT = [
	('GD-PR-DISTRICT', 0, 2, 'pic_generic'),
	('GD-PR-GAS-WELL-GAS-RRCID', 2, 6, 'pic_generic'),
	('GD-PR-REPORT-YEAR', 8, 4, 'pic_generic'),
	('GD-PR-REPORT-MONTH', 12, 2, 'pic_generic'),
	('GD-PR-GAS-WELL-GAS-BALANCING-CODE', 14, 1, 'pic_generic'),
	('GD-PR-DISCREPANCY-PRINTED-CODE', 15, 1, 'pic_generic'),
	('GD-PR-INVALID-OR-OMITTED-CODE', 16, 1, 'pic_generic'),
	('GD-PR-EXTRACTION-LOSS-CODE', 17, 1, 'pic_generic'),
	('GD-PR-CODING-MAST-OP-NUMBER', 18, 6, 'pic_generic'),
	('GD-PR-COMPANY-TAPE-OP-NUMBER', 24, 6, 'pic_generic'),
	('GD-PR-FIELD-NUMBER', 30, 8, 'pic_generic'),
	('GD-PR-FIELD-NAME', 38, 32, 'pic_generic'),
	('GD-PR-LEASE-NAME', 70, 32, 'pic_generic'),
	('GD-PR-GAS-WELL-GAS-NUMBER', 102, 6, 'pic_generic'),
	('GD-PR-BATCH-CODE', 108, 1, 'pic_generic'),
	('GD-PR-LEASE-FLD-FUEL-SYSTEMS', 109, 7, 'pic_generic'),
	('GD-PR-TRANSMISSION-LINE', 116, 7, 'pic_generic'),
	('GD-PR-PROCESSING-PLANT', 123, 7, 'pic_generic'),
	('GD-PR-VENTED-OR-FLARED', 130, 7, 'pic_generic'),
	('GD-PR-GAS-WELL-GAS-LIFT', 137, 7, 'pic_generic'),
	('GD-PR-PRESSURE-MAINTENANCE', 144, 7, 'pic_generic'),
	('GD-PR-CARBON-BLACK', 151, 7, 'pic_generic'),
	('GD-PR-UNDERGROUND-STORAGE', 158, 7, 'pic_generic'),
	('GD-PR-EXTRACTION-LOSS', 165, 7, 'pic_generic'),
	('GD-PR-GAS-WELL-GAS-PRODUCTION', 172, 7, 'pic_generic'),
	('GD-PR-GAS-WELL-GAS-LIFT-INJECTED', 179, 7, 'pic_generic'),
	('GD-PR-CONDENSATE-PRODUCTION', 186, 5, 'pic_generic'),
	('FILLER', 191, 9, 'pic_generic'),
]
