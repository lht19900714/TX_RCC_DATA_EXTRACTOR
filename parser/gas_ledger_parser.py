'''
@File   :  gas_ledger_parser.py
@Author :  Haitao Lu
@Date   :  15-Mar-2023 8:53 AM

Extract data from the gas ledger files based on layout in gas_ledger_layout.py

'''

from pathlib import Path
import pandas as pd
from util.util import yield_blocks, parse_record
from layouts.gas_ledger_layout import gas_ledger_layout
from ebcdic_formats.ebcdic_formats import pic_generic


def gas_ledger_parser(source_file_path, dest_folder_path='', block_size=2120, limiting_counter=False, check_stop=100):
	'''
	Extract data from the gas ledger files based on layout in gas_ledger_layout.py
	Saves the data to a csv file

	:param source_file_path: path to the gas ledger file
	:param dest_folder_path: path to save the csv file
	:param block_size: block size for each record in the file
	:param limiting_counter: limit the number of records to be parsed
	:param check_stop: number of records to be parsed
	:return: None
	'''

	print('opening', source_file_path, '...')
	file = open(source_file_path, 'rb')  ##Opens the .ebc file and reads it as bytes

	count = 0  ##counter for number of records
	well_count = 0  ##counter for number of wells
	field_count = 0  ##counter for number of fields

	# Loop section for all records or partial set
	res_gas_field, res_gas_well = [], []
	for block in yield_blocks(file, block_size):  ##for each block in file

		##For testing script
		if limiting_counter == True and well_count > check_stop:  ##Stops the loop once a set number of wells has been complete
			break

		start_value = pic_generic(block[0:1])  ## first two characters of a block

		# Selecting layout based on leading start value and parsing record based on the selected layout

		layout = gas_ledger_layout(start_value)['layout']  # identifies layout based on record start values
		parsed_vals = parse_record(block, layout)  # formats the record and returns a formated {dict}

		temp_df = pd.DataFrame([parsed_vals], columns=parsed_vals.keys())  ##convert {dict} to dataframe

		if start_value == '1':
			field_count += 1
			res_gas_field.append(temp_df)
		elif start_value == '5':
			well_count += 1
			res_gas_well.append(temp_df)
		else:
			print('Error: Unknown record type')
			print('Record start value:', start_value)
			break

		count += 1
	print(f'Number of records: {count}')
	print(f'Number of wells: {well_count}')
	print(f'Number of fields: {field_count}')

	res_gas_field = pd.concat(res_gas_field)
	res_gas_well = pd.concat(res_gas_well)

	if dest_folder_path == '':
		dest_folder_path = f'../out/'
	gas_field_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_gas_field.csv'
	gas_well_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_gas_well.csv'

	res_gas_field.to_csv(gas_field_file_path, index=False)
	res_gas_well.to_csv(gas_well_file_path, index=False)

	print(f'Gas field data saved to {gas_field_file_path}')
	print(f'Gas well data saved to {gas_well_file_path}')

	file.close()


if __name__ == '__main__':
	file_path = r'/Volumes/haitao_folder/rrc/Gas_Ledger_Dist/gsf001l.ebc'
	gas_ledger_parser(file_path)
